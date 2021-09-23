   
import pyspark
import pyspark.sql.functions as F

def remove_non_word_characters(spark, col):
    return F.regexp_replace(col, "[^\\w\\s]+", "")
