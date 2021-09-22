import pyspark
import pyspark.sql.functions as F
from test_conf import spark
#from pyspark.sql import SparkSession

#Create SparkSession
#customSpark = SparkSession.builder.getOrCreate()



#def func(df):
 # df1 =  df.withColumn("max", greatest("a", "b")).select("max")
  #return df1.collect()[0][0]

def remove_non_word_characters(spark, col):
    df = spark.createDataFrame([(2, 3)],["a","b"])
    return F.regexp_replace(col, "[^\\w\\s]+", "")

