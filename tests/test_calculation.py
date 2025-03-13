import pytest
from app.calculation import Calculation

def test_calculation_add():
    calc = Calculation(3, 2)
    assert calc.add() == 5

def test_calculation_subtract():
    calc = Calculation(10, 4)
    assert calc.subtract() == 6

def test_calculation_multiply():
    calc = Calculation(3, 4)
    assert calc.multiply() == 12

def test_calculation_divide_valid():
    calc = Calculation(10, 2)
    assert calc.divide() == 5

def test_calculation_divide_zero():
    calc = Calculation(10, 0)
    with pytest.raises(ValueError):
        calc.divide()
