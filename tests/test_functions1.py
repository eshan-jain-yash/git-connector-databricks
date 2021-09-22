import pytest
from demo1 import func
import pyspark.sql.functions as F
from test_conf import spark

def test_func(spark):
    num = func(spark, 2, 3)
    assert num == 3
