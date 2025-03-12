import pytest
from app.calculator import Calculator

def test_add():
    """Test that Calculator.add returns the correct sum."""
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    """Test that Calculator.subtract returns the correct difference."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    """Test that Calculator.multiply returns the correct product."""
    calc = Calculator()
    assert calc.multiply(4, 3) == 12

def test_divide():
    """Test that Calculator.divide returns the correct quotient."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    """Test that Calculator.divide raises a ValueError when dividing by zero."""
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)
