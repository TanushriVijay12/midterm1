"""
A plugin that provides a greet command.
"""
import logging

class GreetPluginCommand:
    def execute(self, name="World"):
        greeting = f"Hello from the plugin, {name}!"
        logging.info(f"GreetPluginCommand: {greeting}")
        return greeting

def register(history_manager=None):
    """
    Return a dict of command_name -> command_instance.
    """
    return {
        "greet_plugin": GreetPluginCommand()
    }
