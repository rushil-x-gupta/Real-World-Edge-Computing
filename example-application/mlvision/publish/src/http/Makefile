#
# Makefile : http : A flask based local http server for UI
#

export ARCH ?= ${shell uname -p}

IMAGE_NAME = rg.example.http_${ARCH}:1.0.0

all: build push

# Build the docker container
build:
	docker build -t ${CR_USERNAME}/${IMAGE_NAME} -f ./Dockerfile.${ARCH} .

# Push the docker container to the DockerHub registry
push:
	docker login -u ${CR_USERNAME} -p ${CR_DOCKER_RW_APIKEY}
	docker push ${CR_USERNAME}/${IMAGE_NAME}

run:
	docker login -u ${CR_USERNAME} -p ${CR_DOCKER_RO_APIKEY}
	docker run -d -p ${APP_HOST_PORT}:${APP_HOST_PORT} -e APP_VIEW_COLUMNS=${APP_VIEW_COLUMNS} ${CR_USERNAME}/${IMAGE_NAME}

