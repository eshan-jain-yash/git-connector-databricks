import pytest
from demo.third_demo import get_sum
from pytest_pyspark_conf import spark

@pytest.mark.parametrize("num1,num2,expected", [(3,5,8),(6,1,7)])
def test_eval(num1,num2, expected):
    assert get_sum(num1,num2) == expected
