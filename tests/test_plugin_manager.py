"""
Tests for the PluginManager functionality.
"""
from app.plugin_manager import PluginManager

def test_load_plugins():
    """
        Test that PluginManager correctly loads plugins and registers their commands.
        """
    pm = PluginManager(plugin_folder="app/plugins")
    pm.load_plugins()
    commands = pm.get_commands()

    # Expected plugin commands as registered by your plugin file (e.g., math_plugins.py)
    expected_commands = {"sqrt", "power"}  # Add more keys here if your plugin registers additional commands (e.g., "factorial", "log")

    # Check that each expected command is present in the loaded commands
    for cmd in expected_commands:
        assert cmd in commands, f"Plugin command '{cmd}' not loaded"

    # Optionally, test that the command objects have an execute() method
    for cmd_name, command in commands.items():
        assert hasattr(command, "execute") and callable(command.execute), f"Command '{cmd_name}' does not have a callable execute() method"
