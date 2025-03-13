import pytest # pylint: disable=unused-import
from app.plugins.csv_plugin import register as csv_register

def test_csv_plugin_register():
    cmds = csv_register()
    # Assuming csv_plugin registers a command named "export_csv"
    assert "export_csv" in cmds
    # You might want to simulate execution if possible.
