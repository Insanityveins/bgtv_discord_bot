#!/bin/bash

# build image
docker build -t bgtv_bot .

# run image and delete when not running to preserve name
docker run --rm --name bot_runner bgtv_bot:latest
