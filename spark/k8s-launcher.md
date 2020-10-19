# Kubernetes Launcher

To launch Spark with Kubernetes you need a K8s configuration. A wonderful example lives in the [Kubernetes respository](https://github.com/kubernetes/examples/tree/master/staging/spark) itself.

## Launch K8s cluster

Under [./resource-manager](./resource-manager) you find an adapted version that launches the Thrift server automatically. To launch the K8s cluster:

```shell
kubectl create -f ./resource-manager -n spark-cluster
```

## Delete Spark cluster

```shell
kubectl delete namespace spark-cluster
```

## Inspect running cluster

```shell
kubectl get pods -n spark-cluster
kubectl get svc -o wide -n spark-cluster
```

## Run Thrift server (ODBC)

```shell
kubectl get pods -n spark-cluster
# Change pod name
kubectl exec --stdin --tty -n spark-cluster spark-master-controller-rbldp -- /opt/spark/sbin/start-thriftserver.sh
kubectl port-forward spark-master-controller-rbldp 10000:10000 -n spark-cluster #&
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

## Get latest configuration

```shell
cd ~/Downloads
pwd
git clone --depth=1 https://github.com/kubernetes/examples
kubectl create -f examples/staging/spark -n spark-cluster
```
