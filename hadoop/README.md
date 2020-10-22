# Install Hadoop on Docker

Build image

```shell
docker build -t hadoop:latest .
docker container run hadoop -p 8088 5070
docker run -it hadoop
```

## SSH into Hadoop

You can ssh into the machine as follows:

```shell
docker exec -it hadoop /bin/bash
```
