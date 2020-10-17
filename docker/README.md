# DevBox docker

This repository contains the Docker basic commands.

## Push docker container

```Shell
docker tag my-image febaron/image
docker push image
```

## Managing volumes

```Shell
# Create a volume
docker volume create volumename

# List volumes
docker volume ls

# Delete volumes
docker volume rm mydockervolume

# Create a volume on a network drive
docker volume create --driver local --opt type=cifs --opt device=//192.168.178.1/nas/USB/Volumes/minecraft --opt o=user=admin,password=my-password mydockervolume
```
