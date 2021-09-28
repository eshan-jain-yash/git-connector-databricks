import pytest
import demo

@pytest.mark.parametrize("num1,expected", [(2,True),(3,False),(5,False)])
def test_even_or_not(num1, expected):
    assert demo.even_or_not(num1) == expected
