#
# pthDetector.py
#
# Sanjeev Gupta, Mar 21, 2021
#

import os
import time

import torch
import torchvision
from torchvision import transforms
from torchvision.models.detection import FasterRCNN_ResNet50_FPN_Weights, FasterRCNN_ResNet50_FPN_V2_Weights
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor, fasterrcnn_resnet50_fpn_v2
from torchvision.transforms import transforms as T
import torchvision.transforms.functional as TF

from package.util import util

class PTHDetector:
    def __init__(self, config, classes=[]):

        self.config = config

        self.classes = ['__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table', 'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
        
        self.device = self.getTorchDevice()
        print(self.device)
        # Test: To load directly at runtime. 
        #self.model = torchvision.models.detection.fasterrcnn_resnet50_fpn_v2(weights=torchvision.models.detection.FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT)
        # App uses model from the docker image fetched during docker build time
        self.model = torchvision.models.detection.fasterrcnn_resnet50_fpn_v2()
        print ("{:.7f} ##App## config.getModelPathPTH=".format(time.time()), config.getModelPathPTH(), end="\n", flush=True)
        self.model.load_state_dict(torch.load(os.path.join(config.getModelPathPTH())))
        
        
        self.model.to(self.device)
        print ("{:.7f} ##App## self.model=".format(time.time()), "loaded on " + str(self.device), end="\n", flush=True)
        self.model.eval()
        print ("{:.7f} ##App## self.model=".format(time.time()), "eval done", end="\n", flush=True)
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
        results = []
        for image in images:
            image_tensor = torchvision.transforms.functional.to_tensor(image).to(self.device)
            with torch.no_grad():
                preds = self.model([image_tensor])
                preds = [{key: value.to(torch.device('cpu')) for key, value in pred.items()} for pred in preds]
                for pred in preds:
                    # Predicted index to string classes
                    result = ([self.classes[value] for value in pred['labels']], pred['boxes'], pred['scores'])
                results.append(result)
        return results[0] if is_single_image else results

    def getHeight(self):
        return 480

    def getWidth(self):
        return 640

    def getFloatingModel(self):
        return False

    def getTorchDevice(self):
        return torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        # return torch.device('cpu')

    def transformNormalize(self):
        return transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    def transformTensor(self):
        return transforms.Compose([transforms.ToTensor(), self.transformNormalize()])