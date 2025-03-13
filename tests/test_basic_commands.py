import pytest
from app.calculator import Calculator
from app.history_manager import HistoryManager
from app.commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.fixture
def history_manager(tmp_path):
    csv_file = tmp_path / "test_history.csv"
    return HistoryManager(csv_file=str(csv_file))

@pytest.fixture
def calculator():
    return Calculator()

def test_add_command(calculator, history_manager):
    cmd = AddCommand(calculator, history_manager)
    result = cmd.execute(5, 3)
    assert result == 8

def test_subtract_command(calculator, history_manager):
    cmd = SubtractCommand(calculator, history_manager)
    result = cmd.execute(10, 4)
    assert result == 6

def test_multiply_command(calculator, history_manager):
    cmd = MultiplyCommand(calculator, history_manager)
    result = cmd.execute(3, 4)
    assert result == 12

def test_divide_command_valid(calculator, history_manager):
    cmd = DivideCommand(calculator, history_manager)
    result = cmd.execute(10, 2)
    assert result == 5

def test_divide_command_zero(calculator, history_manager):
    cmd = DivideCommand(calculator, history_manager)
    with pytest.raises(ValueError):
        cmd.execute(10, 0)
