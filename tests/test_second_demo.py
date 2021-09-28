import pytest
import demo
import pyspark.sql.functions as F
from pytest_pyspark_conf import spark

@pytest.mark.parametrize("num1,num2,expected", [(2,3,3),(5,3,5)])
def test_get_greatest_number(spark,num1,num2,expected):
    num = demo.get_greatest_number(spark, num1, num2)
    assert num == expected
