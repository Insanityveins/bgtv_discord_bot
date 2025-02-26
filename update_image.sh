!#/bin/bash

# script to stop container, update the image, then rerun container

# stop container
docker stop bot_runner

# remove container
docker rm bot_runner

# update image
docker build -t bgtv_bot .

# run image
docker run --name bot_runner --restart always bgtv_bot:latest