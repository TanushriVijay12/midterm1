"""
An example module showing a custom greet command.
"""
import logging
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class GreetCommand(Command):
    def execute(self, name):
        message = f"Hello, {name}!"
        logging.info(f"GreetCommand: Greeting {name}")
        return message
