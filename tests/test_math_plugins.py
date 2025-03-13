import math
import pytest
from app.plugins import math_plugins  # pylint: disable=unused-import
from app.plugins.math_plugins import (
    SquareRootCommand,
    PowerCommand,
    FactorialCommand,
    LogarithmCommand,
    register,
)

# --- SquareRootCommand tests ---
def test_sqrt_valid():
    cmd = SquareRootCommand()  # without history_manager
    result = cmd.execute(16)
    assert math.isclose(result, 4.0)

def test_sqrt_negative():
    cmd = SquareRootCommand()
    with pytest.raises(ValueError):
        cmd.execute(-9)

# --- PowerCommand tests ---
def test_power_valid():
    cmd = PowerCommand()
    result = cmd.execute(2, 3)
    assert result == 8

# --- FactorialCommand tests ---
def test_factorial_valid():
    cmd = FactorialCommand()
    result = cmd.execute(5)
    assert result == 120

def test_factorial_negative():
    cmd = FactorialCommand()
    with pytest.raises(ValueError):
        cmd.execute(-3)

# --- LogarithmCommand tests ---
def test_logarithm_default():
    cmd = LogarithmCommand()
    result = cmd.execute(math.e)
    assert math.isclose(result, 1.0, rel_tol=1e-5)

def test_logarithm_custom_base():
    cmd = LogarithmCommand()
    result = cmd.execute(100, base=10)
    # log10(100) should be 2.0
    assert math.isclose(result, 2.0, rel_tol=1e-5)

def test_logarithm_invalid():
    cmd = LogarithmCommand()
    with pytest.raises(ValueError):
        cmd.execute(0)

# --- Test the register() function ---
def test_register_function():
    cmds = register()
    # Verify all expected keys exist
    expected_keys = {"sqrt", "power", "factorial", "log"}
    assert expected_keys.issubset(cmds.keys())
    # Verify that each command is an instance of its respective class.
    assert isinstance(cmds["sqrt"], SquareRootCommand)
    assert isinstance(cmds["power"], PowerCommand)
    assert isinstance(cmds["factorial"], FactorialCommand)
    assert isinstance(cmds["log"], LogarithmCommand)
