import pytest
import demo

def file_test(num1,num2):
  assert demo.func(num1,num2) == 3

file_test(2,3)

