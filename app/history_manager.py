"""
Facade for managing the calculation history with Pandas.
"""
import os
import pandas as pd

class HistoryManager:
    def __init__(self, csv_file="history.csv"):
        self.csv_file = csv_file
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        if os.path.exists(csv_file):
            self.load_history()

    def add_record(self, operation, a, b, result):
        # Convert values to string so that text-based commands (like greet_plugin) are recorded correctly.
        new_row = {
            "operation": operation,
            "operand1": str(a) if a is not None else "",
            "operand2": str(b) if b is not None else "",
            "result": str(result)
        }
        self.history = pd.concat([self.history, pd.DataFrame([new_row])], ignore_index=True)
        self.save_history()

    def load_history(self):
        self.history = pd.read_csv(self.csv_file)

    def save_history(self):
        self.history.to_csv(self.csv_file, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        self.save_history()

    def delete_history_file(self):
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
