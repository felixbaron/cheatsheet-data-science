# Spark on Kubernetes

Launch K8s cluster:

```shell
kubectl apply -f https://raw.githubusercontent.com/big-data-europe/docker-spark/master/k8s-spark-cluster.yaml -n spark-cluster
```

Forward ports:

```shell
kubectl proxy --port=8080 -n spark-cluster
```
