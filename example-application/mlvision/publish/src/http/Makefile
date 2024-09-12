#
# Makefile : http : A flask based local http server for UI
#

export ARCH ?= ${shell uname -p}

IMAGE_NAME = rg.example.http_${ARCH}:1.0.0

# all: build push
test:
	@echo ${ARCH}
# Build the docker container
build:
	docker build -t ${CR_USERNAME}/${IMAGE_NAME} -f ./Dockerfile.${ARCH} .

# Push the docker container to the DockerHub registry
push:
	docker login -u ${CR_USERNAME} -p ${CR_DOCKER_APIKEY}
	docker push ${CR_USERNAME}/${IMAGE_NAME}

run:
	docker run -d -p 5000:5000 -e APP_VIEW_COLUMNS="1" ${CR_USERNAME}/${IMAGE_NAME}

