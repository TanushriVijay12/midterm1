"""
Manages loading of plugins from the plugins folder.
"""
import os
import importlib

class PluginManager:
    def __init__(self, plugin_folder="app/plugins", history_manager=None):
        self.plugin_folder = plugin_folder
        self.history_manager = history_manager
        self.commands = {}

    def load_plugins(self):
        for file in os.listdir(self.plugin_folder):
            if file.endswith(".py") and file != "__init__.py":
                module_name = file[:-3]  # remove .py
                module_path = f"app.plugins.{module_name}"
                module = importlib.import_module(module_path)
                if hasattr(module, "register"):
                    # Pass history_manager if the plugin needs it
                    registered_cmds = module.register(history_manager=self.history_manager)
                    self.commands.update(registered_cmds)

    def get_commands(self):
        return self.commands
