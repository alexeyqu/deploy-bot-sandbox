#!/bin/bash

docker stop $(docker ps -aq --filter name=deploybot)
docker rm $(docker ps -aq --filter name=deploybot)

docker run --name deploybot -d \
    -v $(pwd)/telegram.token:/app/telegram.token deploybot
