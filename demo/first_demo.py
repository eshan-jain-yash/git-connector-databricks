   
import pyspark
import pyspark.sql.functions as F

def remove_non_word_characters(spark, col):
    df = spark.createDataFrame([(2, 3)],["a","b"])
    return F.regexp_replace(col, "[^\\w\\s]+", "")
