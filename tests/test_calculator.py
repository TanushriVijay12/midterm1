import pytest
from calculator.calculator import Calculator
from calculator.calculation import Calculation
from calculator.calculations import Calculations

@pytest.fixture
def test_data():
    return {"a": 10, "b": 5, "zero": 0}

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 5, 15),
    (100, 50, 150)
])
def test_static_add(a, b, expected):
    assert Calculator.add(a, b) == expected

def test_instance_subtract(test_data):
    calc = Calculation(test_data["a"], test_data["b"])
    assert calc.subtract() == 5

def test_class_multiply(test_data):
    assert Calculations.multiply(test_data["a"], test_data["b"]) == 50

def test_divide_by_zero_static(test_data):
    with pytest.raises(ValueError):
        Calculator.divide(test_data["a"], test_data["zero"])

def test_divide_by_zero_instance(test_data):
    calc = Calculation(test_data["a"], test_data["zero"])
    with pytest.raises(ValueError):
        calc.divide()

def test_divide_by_zero_class(test_data):
    with pytest.raises(ValueError):
        Calculations.divide(test_data["a"], test_data["zero"])
