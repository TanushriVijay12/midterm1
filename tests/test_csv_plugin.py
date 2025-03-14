import logging
import pandas as pd
import pytest # pylint: disable=unused-import
from app.plugins.csv_plugin import CSVExportCommand, register

# A dummy history manager that simulates a real one by providing a sample DataFrame.
class DummyHistoryManager:
    def __init__(self):
        self.history = pd.DataFrame({
            "operation": ["add", "subtract"],
            "operand1": [1, 5],
            "operand2": [2, 3],
            "result": [3, 2]
        })

def test_csv_plugin_register():
    dummy_history = DummyHistoryManager()
    cmds = register(history_manager=dummy_history)
    # Check that the command "export_csv" is registered.
    assert "export_csv" in cmds
    # Verify that it is an instance of CSVExportCommand.
    assert isinstance(cmds["export_csv"], CSVExportCommand)

def test_csv_export(tmp_path, caplog):
    dummy_history = DummyHistoryManager()
    cmd = CSVExportCommand(dummy_history)
    # Create a temporary file path for exporting.
    file_path = tmp_path / "export_test.csv"
    with caplog.at_level(logging.INFO):
        result = cmd.execute(str(file_path))
    # Check that the returned result string is as expected.
    expected_result = f"History exported to {file_path}"
    assert result == expected_result
    # Verify that the CSV file is created.
    assert file_path.exists()
    # Read the CSV file and compare its contents with the dummy history DataFrame.
    exported_df = pd.read_csv(file_path)
    pd.testing.assert_frame_equal(dummy_history.history, exported_df)
    # Optionally, verify that the logging message was generated.
    log_found = any("Exported history" in record.message for record in caplog.records)
    assert log_found
