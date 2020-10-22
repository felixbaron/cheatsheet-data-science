# DevBox docker

This repository contains the Docker basic commands.

## Build Docker image

```shell
docker build -t myimage:1.0 .
```

## Push Docker image

```shell
docker tag my-image febaron/image
docker push febaron/image
```

## SSH into container

```shell
docker exec -it container # /bin/bash
```

## Run container

```shell
docker container run --name containername -p 5000
```

## Managing volumes

```shell
# Create a volume
docker volume create volumename

# List volumes
docker volume ls

# Delete volumes
docker volume rm mydockervolume

# Create a volume on a network drive
docker volume create --driver local --opt type=cifs --opt device=//192.168.178.1/nas/USB/Volumes/minecraft --opt o=user=admin,password=my-password mydockervolume
```
