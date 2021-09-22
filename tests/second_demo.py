import pyspark
from pyspark.sql.functions import greatest

def func(spark, num1, num2):
  df = spark.createDataFrame([(num1, num2)],["a","b"])  
  df1 =  df.withColumn("max", greatest("a", "b")).select("max")
  return df1.collect()[0][0]

