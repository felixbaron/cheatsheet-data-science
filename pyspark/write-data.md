# Read and write data

## Write any data to Hadoop

```python

```

## Write Pandas data to Hadoop

```python

```

## Read data with Hive SQL

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName('appName') \
    .config('spark.driver.port', 8080) \
    .config('spark.driver.host', '127.0.0.1') \
    .getOrCreate()
rddFromFile = spark.sparkContext.textFile("hdfs://127.0.0.1/text01.txt")

```

Resources:
- [Official examples](https://github.com/apache/spark/blob/master/examples/src/main/python/sql/arrow.py)
- [Parquet data](https://sparkbyexamples.com/spark/spark-read-write-files-from-hdfs-txt-csv-avro-parquet-json/)
- [Write Parquet data](https://kontext.tech/column/spark/257/write-and-read-parquet-files-in-hdfs-through-sparkscala)
- [Write to HDFS](https://saagie.zendesk.com/hc/en-us/articles/360029759552-PySpark-Read-and-Write-Files-from-HDFS)
- [Write to HDFS II](https://saagie.zendesk.com/hc/en-us/articles/360030094231-Spark-Scala-Read-Write-files-from-HDFS)
