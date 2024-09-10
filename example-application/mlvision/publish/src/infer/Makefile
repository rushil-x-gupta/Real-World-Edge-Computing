#
# Makefile : infer : machine inferencing
#

IMAGE_NAME = rg.example.infer_amd64:1.0.0

export ARCH ?= amd64

# all: build push

# Build the docker container
build:
	docker build -t ${CR_USERNAME}/${IMAGE_NAME} -f ./Dockerfile.${ARCH} .

# Push the docker container to the DockerHub registry
push:
	docker login -u ${CR_USERNAME} -p ${CR_DOCKER_APIKEY} ${CR_HOST}
	docker push ${CR_USERNAME}/${IMAGE_NAME}

run:
	docker run \
	-e APP_MODEL_FMWK="tflite" \
	-e APP_MODEL_DIR="/var/local/horizon/ml/model/tflite" \
	-e APP_ML_MODEL="tflite-model-1.0.0-mms.zip" \
	-e APP_VIDEO_FILES="/var/local/horizon/sample/video/sample-video.mp4" \
	-e APP_BIND_HORIZON_DIR=/var/local/horizon \
	-e APP_CAMERAS="-" \
	-e APP_RTSPS="-" \
	-e APP_VIEW_COLUMNS="1" \
	-e DEVICE_ID="wsl2" \
	-e DEVICE_NAME="WSL2" \
	-e DEVICE_IP_ADDRESS="localhost" \
	-e SHOW_OVERLAY="true" \
	-e PUBLISH_STREAM="true" \
	-e MIN_CONFIDENCE_THRESHOLD="0.6" \
	-v "/var/local/horizon/ml/model/tflite":"/var/local/horizon/ml/model/tflite" \
	${CR_USERNAME}/${IMAGE_NAME}





