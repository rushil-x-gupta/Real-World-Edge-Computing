# Setting up Sauron

## Setting Environment Variables

1. Create a file called `ENV_MLVISION` with the following content. Replace the content within `<>` with values applicable as per your environment. Following setup assumes that you are using Docker Hub.

```
export CR_USERNAME="<your-docker-namespace>"
export CR_DOCKER_RW_APIKEY="<docker-read-write-api-key>"
export CR_DOCKER_RO_APIKEY="<docker-read-only-api-key>"
export APP_BIND_HORIZON_DIR=/var/local/horizon
export APP_HOST_IP_ADDRESS="<edge-node-ip-address>"
export APP_HOST_PORT="5000"
export APP_MODEL_FMWK="tflite"
export APP_MODEL_DIR="${APP_BIND_HORIZON_DIR}/ml/model/tflite"
export APP_ML_MODEL="tflite-model-1.0.0-mms.zip"
export APP_VIDEO_FILES="${APP_BIND_HORIZON_DIR}/sample/video/sample-video.mp4"
export APP_CAMERAS="-"
export APP_RTSPS="-"
export APP_VIEW_COLUMNS="1"
export DEVICE_ID="<edge-node-device-id>"
export DEVICE_NAME="<edge-node-device-name>"
export DEVICE_IP_ADDRESS="${APP_HOST_IP_ADDRESS}"
export SHOW_OVERLAY="true"
export PUBLISH_STREAM="true"
export MIN_CONFIDENCE_THRESHOLD="0.6"
export HTTP_PUBLISH_STREAM_URL="http://${APP_HOST_IP_ADDRESS}:${APP_HOST_PORT}/publish/stream"
```

2. Source the environment variables that were just created.
```
source ENV_MLVISION
```
## Build and Publish the Application

3. Change to the `http` directory.
```
cd publish/src/http
```

4. Build and publish the HTTP service.

```
make
make run
```

5. Change to the `infer` directory.
```
cd ../infer
```

6. Build and publish the video inferencing service.

```
make
make run
```