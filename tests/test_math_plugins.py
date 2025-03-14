import math
import pytest
from app.plugins.math_plugins import (
    SquareRootCommand,
    PowerCommand,
    FactorialCommand,
    LogarithmCommand,
    register,
)
# pylint: disable=invalid-name

# ---------------------------
# Tests without a history_manager
# ---------------------------

# --- SquareRootCommand tests without history_manager ---
def test_sqrt_valid():
    cmd = SquareRootCommand()  # without history_manager
    result = cmd.execute(16)
    assert math.isclose(result, 4.0)

def test_sqrt_negative():
    cmd = SquareRootCommand()
    with pytest.raises(ValueError):
        cmd.execute(-9)

# --- PowerCommand tests without history_manager ---
def test_power_valid():
    cmd = PowerCommand()
    result = cmd.execute(2, 3)
    assert result == 8

# --- FactorialCommand tests without history_manager ---
def test_factorial_valid():
    cmd = FactorialCommand()
    result = cmd.execute(5)
    assert result == 120

def test_factorial_negative():
    cmd = FactorialCommand()
    with pytest.raises(ValueError):
        cmd.execute(-3)

# --- LogarithmCommand tests without history_manager ---
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

# ---------------------------
# Tests with a dummy history_manager to cover the history recording branch
# ---------------------------
class DummyHistoryManager:
    def __init__(self):
        self.records = []
    def add_record(self, operation, a, b, result):
        self.records.append((operation, a, b, result))

def test_sqrt_with_history():
    dummy = DummyHistoryManager()
    cmd = SquareRootCommand(dummy)
    result = cmd.execute(25)
    # 25 -> sqrt is 5.0
    assert math.isclose(result, 5.0)
    assert dummy.records == [("sqrt", 25, None, 5.0)]

def test_power_with_history():
    dummy = DummyHistoryManager()
    cmd = PowerCommand(dummy)
    result = cmd.execute(2, 4)
    assert result == 16
    assert dummy.records == [("power", 2, 4, 16)]

def test_factorial_with_history():
    dummy = DummyHistoryManager()
    cmd = FactorialCommand(dummy)
    result = cmd.execute(4)
    expected = math.factorial(4)
    assert result == expected
    assert dummy.records == [("factorial", 4, None, expected)]

def test_log_with_history_default():
    dummy = DummyHistoryManager()
    cmd = LogarithmCommand(dummy)
    result = cmd.execute(math.e)
    # default base is math.e, so log_e(e) should be 1.0
    assert math.isclose(result, 1.0, rel_tol=1e-5)
    # For this command, the record should include (a, base, result)
    assert dummy.records == [("log", math.e, math.e, result)]

def test_log_with_history_custom():
    dummy = DummyHistoryManager()
    cmd = LogarithmCommand(dummy)
    result = cmd.execute(100, base=10)
    assert math.isclose(result, 2.0, rel_tol=1e-5)
    assert dummy.records == [("log", 100, 10, result)]

# ---------------------------
# Test the register() function
# ---------------------------
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
