# Build PySpark Dockerfile

Build Dockerfile for PySpark:

```shell
cd ~/Downloads/spark
./bin/docker-image-tool.sh -t 3.0.1 -p kubernetes/dockerfiles/spark/bindings/python/Dockerfile build
# Optional push to hub.docker
docker tag spark-py:3.0.1 febaron/spark-py
docker push febaron/spark-py
```
