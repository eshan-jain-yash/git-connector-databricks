import pyspark
from pyspark.sql.functions import greatest
from pyspark.sql import SparkSession

#Create SparkSession
customSpark = SparkSession.builder.getOrCreate()



def func(num1,num2):
  df = customSpark.createDataFrame([(num1, num2)],["a","b"])
  df.show()
  df1 =  df.withColumn("max", greatest("a", "b")).select("max")
  return df1.collect()[0][0]


