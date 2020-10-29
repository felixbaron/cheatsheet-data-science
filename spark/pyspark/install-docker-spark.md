# Spark on Docker
## Installation

``` shell
git clone https://github.com/big-data-europe/docker-spark
cd docker-spark
docker-compose up -d
```

## Connect to Spark

For Windows only: install [winutils](https://github.com/cdarlint/winutils)

Set `$HADDOP_HOME`, `$JAVA_HOME` as environment variables. Also add `$HADOOP_HOME/bin` to path.

See [connect-to-spark.md](connect-to-spark.md).
