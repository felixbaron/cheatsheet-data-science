# Hive on Docker

Build Hive Docker image:

```shell
docker build -t hive:latest .
## SSH into machine
docker run -d -p 10002:10002 -p 10000:10000 -p 9083:9083 hive:latest
```
