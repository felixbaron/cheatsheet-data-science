# Kubernetes Launcher

To launch Spark with Kubernetes you need a K8s configuration. A wonderful example lives in the [Kubernetes respository](https://github.com/kubernetes/examples/tree/master/staging/spark) itself. For the quick start jump to [tl;dr](#tldr)

## <a name="tldr"></a> tl;dr

Under [./resource-manager](./resource-manager) you find an adapted version that launches the Thrift server automatically. To launch the K8s cluster:

```shell
kubectl create -f ./ -n spark-cluster
```

## Optional

### Delete Spark cluster

```shell
kubectl delete namespace spark-cluster
```

### Inspect running cluster

```shell
kubectl get pods -n spark-cluster
kubectl get svc -o wide -n spark-cluster
```

### Run Thrift server (ODBC)

```shell
kubectl get pods -n spark-cluster
# Change pod name
kubectl exec --stdin --tty -n spark-cluster spark-master-controller-rbldp -- /opt/spark/sbin/start-thriftserver.sh
kubectl port-forward spark-master-controller-rbldp 10000:10000 -n spark-cluster #&
```

### Open Spark UI

```shell
kubectl proxy --port=8001 -n spark-cluster
```
Then visit [http://127.0.0.1:8001/api/v1/namespaces/spark-cluster/services/http:spark-master:8080/proxy/](http://127.0.0.1:8001/api/v1/namespaces/spark-cluster/services/http:spark-master:8080/proxy/)

### Run Zeppelin

```shell
kubectl port-forward zeppelin-controller-r6bz8 8080:8080 -n spark-cluster #&
```
