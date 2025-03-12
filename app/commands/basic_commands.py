"""
Defines basic arithmetic commands using the Command Pattern.
"""
import logging
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class AddCommand(Command):
    def __init__(self, calculator, history_manager):
        self.calculator = calculator
        self.history_manager = history_manager

    def execute(self, a, b):
        result = self.calculator.add(a, b)
        self.history_manager.add_record('add', a, b, result)
        logging.info(f"AddCommand: {a} + {b} = {result}")
        return result

class SubtractCommand(Command):
    def __init__(self, calculator, history_manager):
        self.calculator = calculator
        self.history_manager = history_manager

    def execute(self, a, b):
        result = self.calculator.subtract(a, b)
        self.history_manager.add_record('subtract', a, b, result)
        logging.info(f"SubtractCommand: {a} - {b} = {result}")
        return result

class MultiplyCommand(Command):
    def __init__(self, calculator, history_manager):
        self.calculator = calculator
        self.history_manager = history_manager

    def execute(self, a, b):
        result = self.calculator.multiply(a, b)
        self.history_manager.add_record('multiply', a, b, result)
        logging.info(f"MultiplyCommand: {a} * {b} = {result}")
        return result

class DivideCommand(Command):
    def __init__(self, calculator, history_manager):
        self.calculator = calculator
        self.history_manager = history_manager

    def execute(self, a, b):
        result = self.calculator.divide(a, b)
        self.history_manager.add_record('divide', a, b, result)
        logging.info(f"DivideCommand: {a} / {b} = {result}")
        return result
