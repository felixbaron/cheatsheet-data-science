# Spark

## Download Spark

Download and unzip [latest Spark release](https://spark.apache.org/downloads.html):

```shell
cd ~/Downloads
curl -L -o spark.tgz https://mirror.netcologne.de/apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
```

## Build PySpark Dockerfile

Build Dockerfile for PySpark:

```shell
cd ~/spark
./bin/docker-image-tool.sh -t 3.0.1 -p kubernetes/dockerfiles/spark/bindings/python/Dockerfile build
# Optional push to hub.docker
docker tag spark-py:3.0.1 febaron/spark-py
docker push febaron/spark-py
```

## Install Spark on Kubernetes

```shell
cd ~/Downloads
pwd
git clone --depth=1 https://github.com/kubernetes/examples
kubectl create -f examples/staging/spark -n spark-cluster
```

## Inspect running cluster

```shell
kubectl get pods -n spark-cluster
kubectl get svc -o wide -n spark-cluster
```

## Open Spark UI

```shell
kubectl proxy --port=8001 -n spark-cluster
```

Then visit [http://localhost:8001/api/v1/proxy/namespaces/spark-cluster/services/spark-ui-proxy/](http://localhost:8001/api/v1/proxy/namespaces/spark-cluster/services/spark-ui-proxy/)

## Run Zeppelin

```shell
kubectl port-forward zeppelin-controller-dlwml 8080:8080 -n spark-cluster #&
```

## Run Thrift server (ODBC)

```shell
kubectl port-forward spark-master-controller-wgx6h 1000:1000 -n spark-cluster #&
```

## Delete Spark cluster

```shell
kubectl delete namespace spark-cluster
```
