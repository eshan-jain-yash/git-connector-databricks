import pytest
from demo/first_demo import remove_non_word_characters
import pyspark.sql.functions as F
from pytest_pyspark_conf import spark

def test_remove_non_word_characters(spark):
    data = [
        ("jo&&se", "jose"),
        ("**li**", "li"),
        ("#::luisa", "luisa"),
        (None, None)
    ]
    df = spark.createDataFrame(data, ["name", "expected_name"])\
        .withColumn("clean_name", remove_non_word_characters(spark, F.col("name")))
    a = df.select("clean_name").collect()
    b = df.select("expected_name").collect()
    assert a == b
