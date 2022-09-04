#!/bin/bash

docker stop lk_ping_tool
docker rm lk_ping_tool
docker rmi lk_ping_tool
docker build . -t lk_ping_tool