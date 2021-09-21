import pyspark
from pyspark.sql import SparkSession
#Create SparkSession
customSpark = SparkSession.builder.getOrCreate()

# COMMAND ----------

import pytest
from pyspark.sql.functions import greatest

# COMMAND ----------

def func():
  df = customSpark.createDataFrame([(2, 3)],["a","b"])
  df.show()
  df1 =  df.withColumn("max", greatest("a", "b")).select("max")
#   print(df1.collect()[0][0])
  return df1.collect()[0][0]


