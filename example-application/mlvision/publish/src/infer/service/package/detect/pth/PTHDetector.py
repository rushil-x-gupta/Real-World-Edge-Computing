#
# pthDetector.py
#
# Sanjeev Gupta, Mar 21, 2021
#

import time

import torch
import torchvision
from torchvision import transforms
from torchvision.models import ResNet50_Weights

from package.util import util

class PTHDetector:
    def __init__(self, config, classes=[]):

        self.config = config

        # weights = ResNet50_Weights.DEFAULT
        # self.classes = weights.meta["categories"]
        self.classes = ['__background__'] + classes
        # self.classes = ['__background__']

        # self.classes = classes

        self.device = self.getTorchDevice()
        print(self.device)
        print("cuda=" + str(torch.cuda.is_available()))

        
        self.model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

        print(len(self.classes))
        print(self.classes)
        in_features = self.model.roi_heads.box_predictor.cls_score.in_features
        self.model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, len(self.classes))
        # self.model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, len(self.classes))

        #self.model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, 1)

        
        
        
        
        self.model.to(self.device)
        print ("{:.7f}V self.config.getModelPathPTH()=".format(time.time()), config.getModelPathPTH(), end="\n", flush=True)
        self.model.load_state_dict(torch.load(config.getModelPathPTH(), map_location=self.device))
        # self.model.get_internal_model().load_state_dict(torch.load(config.getModelPathPTH(), map_location=self.device))
        
        self.model.eval()
        self.modelPath = config.getModelPathPTH()

    def getModelPath(self):
        return self.modelPath

    def getInferResults(self, frame_normalized):
        t1 = time.time()
        predictions = self.predict(frame_normalized)
        classes, boxes, scores = predictions
        self.inference_interval = time.time() - t1
        return self.inference_interval, boxes, classes, scores

    def predict(self, images):
        # Create a list of images if a single image
        is_single_image = not util.isIterable(images)
        images = [images] if is_single_image else images
        print("before pred loop:", len(images))
        print(images[0])
        results = []
        with torch.no_grad():
            tensors = self.transformTensor()
            images = [tensors(image) for image in images]
            print("within pred loop:", len(images))
            # Position on CPU/GPU
            images = [image.to(self.device) for image in images]
            print("on device:", len(images))
            preds = self.model(images)
            print("pred length:", len(preds))
            print(preds)
            # Tensor to CPU as  needed
            preds = [{key: value.to(torch.device('cpu')) for key, value in pred.items()} for pred in preds]
            print("pred length on CPU:", len(preds))
            for pred in preds:
                # Predicted index to string classes
                result = ([self.classes[value] for value in pred['labels']], pred['boxes'], pred['scores'])
                results.append(result)
            print("results:", results)

        return results[0] if is_single_image else results

    def getHeight(self):
        return 480

    def getWidth(self):
        return 640

    def getFloatingModel(self):
        return False

    def getTorchDevice(self):
        # return torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        return torch.device('cpu')

    def transformNormalize(self):
        return transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    def transformTensor(self):
        return transforms.Compose([transforms.ToTensor(), self.transformNormalize()])