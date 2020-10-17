# PySpark Basics
## Installation

For Windows only: install [winutils](https://github.com/cdarlint/winutils).

Clone and launch docker-spark:

``` shell
git clone https://github.com/big-data-europe/docker-spark
cd docker-spark
docker-compose up -d
```

## Getting started
### Connect with Spark cluster

```python
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession

pd.DataFrame(np.random.random(10))
spark = SparkSession.builder \
    .appName('appName') \
    .config('spark.driver.port', 8080) \
    .config('spark.driver.host', '127.0.0.1') \
    .getOrCreate()
spark
```

### Load file

```python
df = spark.read.load('./fixtures/sample.json', format='json')
df.select("fruit", "size").write.save("namesAndAges.parquet", format="parquet")
spark
```

### Handle pandas data

Resources:
- [PySpark Usage Guide](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html)

### Connect to Spark SQL via ODBC

Resources:
- [Running a Thrift JDBC/ODBC server](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#running-the-thrift-jdbcodbc-server)
- [Stack Overflow](https://stackoverflow.com/questions/25730438/connect-to-spark-sql-via-odbc)

## Resources
[Pyspark introduction](https://bit.ly/3nOACgU)
![How to interact with Spark](https://bit.ly/2IzYYuD)
