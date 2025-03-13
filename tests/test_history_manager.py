import os
import pandas as pd
import pytest
from app.history_manager import HistoryManager

@pytest.fixture
def history_manager(tmp_path):
    # Use a temporary CSV file to ensure tests don't interfere with your real history.csv
    csv_file = tmp_path / "test_history.csv"
    return HistoryManager(csv_file=str(csv_file))

def test_add_record(history_manager):
    # Add a record and check that it appears in the history DataFrame
    history_manager.add_record("add", 2, 3, 5)
    assert len(history_manager.history) == 1
    row = history_manager.history.iloc[0]
    assert row["operation"] == "add"
    assert row["operand1"] == 2
    assert row["operand2"] == 3
    assert row["result"] == 5

def test_save_and_load_history(history_manager):
    # Add a record, then create a new HistoryManager that loads from the CSV file
    history_manager.add_record("subtract", 10, 4, 6)
    new_manager = HistoryManager(csv_file=history_manager.csv_file)
    # Verify that the new instance loaded the record correctly
    assert len(new_manager.history) == 1
    row = new_manager.history.iloc[0]
    assert row["operation"] == "subtract"
    assert row["operand1"] == 10
    assert row["operand2"] == 4
    assert row["result"] == 6

def test_clear_history(history_manager):
    # Add a record and then clear the history
    history_manager.add_record("multiply", 3, 4, 12)
    history_manager.clear_history()
    # The DataFrame should be empty after clearing history
    assert history_manager.history.empty
    # If the CSV file exists, reading it should result in an empty DataFrame
    if os.path.exists(history_manager.csv_file):
        df = pd.read_csv(history_manager.csv_file)
        assert df.empty

def test_delete_history_file(history_manager):
    # Add a record and then delete the history file
    history_manager.add_record("divide", 8, 2, 4)
    history_manager.delete_history_file()
    # The file should no longer exist
    assert not os.path.exists(history_manager.csv_file)
    # The in-memory DataFrame should be empty
    assert history_manager.history.empty
