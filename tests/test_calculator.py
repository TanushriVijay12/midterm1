""" Unit tests for the calculator module. """

from calculator import add, subt

def test_add():
    """Tests the add function."""
    assert add(2, 2) == 4

def test_subt():
    """Tests the subtract function."""
    assert subt(2,2) == 0
