"""
A sample plugin that provides a CSVExportCommand.
"""
import logging
import pandas as pd
from pathlib import Path

class CSVExportCommand:
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, filepath="export.csv"):
        # Export the current history DataFrame to a CSV file
        df = self.history_manager.history
        df.to_csv(filepath, index=False)
        logging.info(f"CSVExportCommand: Exported history to {filepath}")
        return f"History exported to {filepath}"

def register(history_manager=None):
    """
    Return a dict of command_name -> command_instance.

    history_manager is an optional dependency you can pass from your main application.
    """
    return {
        "export_csv": CSVExportCommand(history_manager)
    }
