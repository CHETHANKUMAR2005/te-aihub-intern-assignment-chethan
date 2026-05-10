# Docker Commands for Label Studio

docker --version

docker pull heartexlabs/label-studio:latest

docker run -it -p 8080:8080 -v ${PWD}/mydata:/label-studio/data heartexlabs/label-studio:latest

docker ps

docker logs <container_id_or_name>

docker stop <container_id_or_name>

docker start <container_id_or_name>

docker exec -it <container_id_or_name> bash

docker rm <container_id_or_name>

docker images
