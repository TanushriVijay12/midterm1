import pytest
from app.calculations import Calculations

def test_calculations_add():
    assert Calculations.add(3, 2) == 5

def test_calculations_subtract():
    assert Calculations.subtract(10, 4) == 6

def test_calculations_multiply():
    assert Calculations.multiply(3, 4) == 12

def test_calculations_divide_valid():
    assert Calculations.divide(10, 2) == 5

def test_calculations_divide_zero():
    with pytest.raises(ValueError):
        Calculations.divide(10, 0)
