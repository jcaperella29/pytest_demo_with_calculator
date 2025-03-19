# test_calculator.py

# Unit tests for calculator.py using pytest.

import pytest
from calculator import add, subtract, multiply, divide, power, round_to_places

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 7) == 21
    assert multiply(-2, 4) == -8

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 1) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_round_to_places():
    assert round_to_places(3.14159, 2) == 3.14
    assert round_to_places(2.71828, 3) == 2.718
