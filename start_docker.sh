#!/usr/bin/env bash

# github自动部署文件重启脚本

PORT="3278"
NAME="web-1"

result=$(echo $(docker ps -a) | grep "$PORT")

if [[ "$result" != "" ]];
then
    echo "in"
    docker start $NAME
    docker exec -id $NAME bash /root/project/docker_web/start.sh
else
    echo "not in"
    docker run -id --name=$NAME --volumes-from web-base -p $PORT:$PORT web-py3:1.0 /bin/bash
    docker exec -id $NAME bash /root/project/docker_web/start.sh
fi