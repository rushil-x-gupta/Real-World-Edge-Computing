#
# Makefile : infer : machine inferencing
#

export ARCH ?= ${shell uname -p}

IMAGE_NAME = rg.example.infer.${APP_MODEL_FMWK}_${ARCH}:1.0.0

# all: build push

# Build the docker container
build-tflite-cpu:
	docker build -t ${CR_USERNAME}/${IMAGE_NAME} -f ./Dockerfile.${APP_MODEL_FMWK}.cpu.${ARCH} .

build-pth-cpu:
	docker build -t ${CR_USERNAME}/${IMAGE_NAME} -f ./Dockerfile.${APP_MODEL_FMWK}.cpu.${ARCH} .

# Push the docker container to the DockerHub registry
push:
	docker login -u ${CR_USERNAME} -p ${CR_DOCKER_RW_APIKEY}
	docker push ${CR_USERNAME}/${IMAGE_NAME}

run:
	docker login -u ${CR_USERNAME} -p ${CR_DOCKER_RW_APIKEY}
	docker run \
	-e APP_MODEL_FMWK="${APP_MODEL_FMWK}" \
	-e APP_MODEL_DIR="${APP_MODEL_DIR}" \
	-e APP_ML_MODEL="${APP_ML_MODEL}" \
	-e APP_VIDEO_FILES="${APP_VIDEO_FILES}" \
	-e APP_BIND_HORIZON_DIR="${APP_BIND_HORIZON_DIR}" \
	-e APP_CAMERAS="${APP_CAMERAS}" \
	-e APP_RTSPS="${APP_RTSPS}" \
	-e APP_VIEW_COLUMNS="${APP_VIEW_COLUMNS}" \
	-e DEVICE_ID="${DEVICE_ID}" \
	-e DEVICE_NAME="${DEVICE_NAME}" \
	-e DEVICE_IP_ADDRESS="${DEVICE_IP_ADDRESS}" \
	-e SHOW_OVERLAY="${SHOW_OVERLAY}" \
	-e PUBLISH_STREAM="${PUBLISH_STREAM}" \
	-e MIN_CONFIDENCE_THRESHOLD="${MIN_CONFIDENCE_THRESHOLD}" \
	-e HTTP_PUBLISH_STREAM_URL="${HTTP_PUBLISH_STREAM_URL}" \
	-v "${APP_BIND_HORIZON_DIR}":"${APP_BIND_HORIZON_DIR}" ${CR_USERNAME}/${IMAGE_NAME}





