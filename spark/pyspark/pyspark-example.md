# PySpark example

Create a simple Spark application ([source](https://spark.apache.org/docs/latest/quick-start.html#self-contained-applications)):

```python
"""SimpleApp.py"""
from pyspark.sql import SparkSession

logFile = "README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
```
