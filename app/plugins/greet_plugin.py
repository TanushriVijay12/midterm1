"""
A plugin that provides a greet command.
"""
import logging

class GreetPluginCommand:
    def __init__(self, history_manager=None):
        self.history_manager = history_manager

    def execute(self, name="World"):
        greeting = f"Hello {name}, Greetings from the greet plugin!"
        logging.info(f"GreetPluginCommand: {greeting}")
        if self.history_manager:
            self.history_manager.add_record("greet_plugin", name, None, greeting)
        return greeting

def register(history_manager=None):
    """
    Return a dict of command_name -> command_instance.
    """
    return {
        "greet_plugin": GreetPluginCommand(history_manager)
    }
