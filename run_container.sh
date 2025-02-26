#!bin/bash

# run image and keep running using policy to ensure up time
docker run --name bot_runner --restart always bgtv_bot:latest