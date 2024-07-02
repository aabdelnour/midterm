import os
import sys
import pytest

from app.calculator import Calculator
def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtract():
    calc = Calculator()
    assert calc.subtract(2, 1) == 1

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(1, 0)
