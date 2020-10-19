# Start Thrift server

With the Thrift server one can connect to Spark via ODBC/JDBC. The thrift server should be included in the Spark distribution. However, you need to start it manually, or update [entrypoint.sh](https://github.com/apache/spark/blob/master/resource-managers/kubernetes/docker/src/main/dockerfiles/spark/entrypoint.sh) of the [Dockerfile](https://github.com/apache/spark/blob/master/resource-managers/kubernetes/docker/src/main/dockerfiles/spark/Dockerfile).

```sh
/opt/spark/start-thrift.sh
```
