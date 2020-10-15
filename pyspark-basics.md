# PySpark Basics
## Installation
``` shell
git clone https://github.com/big-data-europe/docker-spark
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
    .config('spark.driver.port', 9000) \
    .config('spark.driver.host', '127.0.0.1') \
    .getOrCreate()
spark
```

## Resources
[Pyspark introduction](https://bit.ly/3nOACgU)
![How to interact with Spark](https://bit.ly/2IzYYuD)
