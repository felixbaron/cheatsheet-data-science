# Connect to Spark

## Build session ...

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('appName') \
    .config('spark.driver.port', 8080) \
    .config('spark.driver.host', '127.0.0.1') \
    .config('spark.sql.hive.thriftServer.singleSession', True) \
    .enableHiveSupport() \
    .getOrCreate()
spark
```

## ... or create SparkContext

```python
from pyspark import SparkConf, SparkContext
conf = SparkConf()\
  .setAppName('appName')\
  .set('spark.driver.port', 8080)\
  .set('spark.driver.host', '127.0.0.1')
sc = SparkContext(conf=conf)
```

### Write data

```python
from tempfile import NamedTemporaryFile
tempFile = NamedTemporaryFile(delete=True)
tempFile.close()
sc.parallelize(range(10)).saveAsTextFile(tempFile.name)
```

### Create global temp view

See examples:
[1](https://www.adaltas.com/en/2019/03/25/spark-sql-dataframe-thrift-server/)
[2](https://interworks.com/blog/alentz/2016/01/19/spark-sql-and-tableau-spin-cluster-your-own/)
[3](https://spark.apache.org/docs/latest/sql-getting-started.html)

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.random(10))
sdf = spark.createDataFrame(df)
df = spark.read.option("header","true").csv("data.csv").cache()
sdf.createOrReplaceTempView("taxi_rides")
spark.sql("create table mytable as select * from taxi_rides");
sc = spark.sparkContext
# sdf.createGlobalTempView('people')
```

See [example](http://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html)
or [2](https://stackoverflow.com/questions/27108863/accessing-spark-sql-rdd-tables-through-the-thrift-server)

```python
df = spark.read.load("data.csv", format="csv")
df.select('VendorID').write.save('vendorId.csv', format='csv')
```

Use [SQL runner](http://www.sqledit.com/odbc/runner.html) on Windows if beeline is not working.

## Write data to Hive

```python
from os.path import join, abspath
from pyspark.sql import Row

warehouse_location = abspath('saprk-warehouse')
spark.sql('CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive')
spark.sql("LOAD DATA LOCAL INPATH 'example.txt' INTO TABLE src")
```

This

## Write data

```python
import pandas as pd
df = pd.DataFrame(np.random.random(10))
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
sdf = spark.createDataFrame(df)
mySele = sdf.select("*").toPandas()
mySele
spark.version
```



In this example we use [PyArrow](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html) for efficient conversion.

```python
import numpy as np
import pandas as pd

# Enable Arrow-based columnar data transfers
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

# Generate a Pandas DataFrame
pdf = pd.DataFrame(np.random.rand(100, 3))

# Create a Spark DataFrame from a Pandas DataFrame using Arrow
df = spark.createDataFrame(pdf)

# Convert the Spark DataFrame back to a Pandas DataFrame using Arrow
result_pdf = df.select("*").toPandas()
df.saveAsNewAPIHadoopFile('file://my-file')
print(result_pdf)
```

### Load file

TODO: repair this section

```python
df = spark.read.load('./fixtures/sample.json', format='json')
df.select("fruit", "size").write.save("namesAndAges.parquet", format="parquet")
spark
```

### Handle pandas data

Resources:

-   [PySpark Usage Guide](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html)

### Connect to Spark SQL via ODBC

Resources:

-   [Running a Thrift JDBC/ODBC server](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#running-the-thrift-jdbcodbc-server)
-   [Stack Overflow](https://stackoverflow.com/questions/25730438/connect-to-spark-sql-via-odbc)

## Resources

[Pyspark introduction](https://bit.ly/3nOACgU)
![How to interact with Spark](https://bit.ly/2IzYYuD)
