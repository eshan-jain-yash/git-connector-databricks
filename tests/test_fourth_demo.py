import pytest
from demo.fourth_demo import even_or_not

@pytest.mark.parametrize("num1,expected", [(2,True),(3,False),(5,False)])
def test_even_or_not(num1, expected):
    assert even_or_not(num1) == expected
