import pytest
from demo/second_demo import get_greatest_number
import pyspark.sql.functions as F
from pytest_pyspark_conf import spark

def test_get_greatest_number(spark):
    num = get_greatest_number(spark, 2, 3)
    assert num == 3
