import pytest
from demo import remove_non_word_characters
import pyspark.sql.functions as F
from test_conf import spark

#def test_func(spark):
 #   df = spark.createDataFrame([(2,3)],["a","b"])
  #  df1 = df.withColumn("greater", func(df))
   # assert_column_equality(df1, "greater", "b")
#from chispa.column_comparer import assert_column_equality
import pytest
import pyspark.sql.functions as F
def test_remove_non_word_characters(spark):
    data = [
        ("jo&&se", "jose"),
        ("**li**", "li"),
        ("#::luisa", "luisa"),
        (None, None)
    ]
    df = spark.createDataFrame(data, ["name", "expected_name"])\
        .withColumn("clean_name", remove_non_word_characters(spark, F.col("name")))
    #assert_column_equality(df, "clean_name", "expected_name")
    a = df.select("clean_name").collect()
    b = df.select("expected_name").collect()
    print(a)
    print(b)
    assert a == b
