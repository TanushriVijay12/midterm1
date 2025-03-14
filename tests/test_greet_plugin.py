import pytest # pylint: disable=unused-import
from app.plugins.greet_plugin import GreetPluginCommand, register

def test_greet_plugin_default():
    # When no name is provided, the default "World" should be used.
    cmd = GreetPluginCommand()
    result = cmd.execute()
    # Update the expected string to match the plugin output
    assert result == "Hello World, Greetings from the greet plugin!"


def test_greet_plugin_custom_name():
    # When a custom name is provided, it should appear in the greeting.
    cmd = GreetPluginCommand()
    result = cmd.execute("Alice")
    assert result == "Hello Alice, Greetings from the greet plugin!"

def test_register_function():
    # The register() function should return a dict with "greet_plugin" as a key.
    cmds = register()
    assert "greet_plugin" in cmds
    # Test that the returned command behaves as expected.
    cmd = cmds["greet_plugin"]
    result = cmd.execute("Bob")
    assert result == "Hello Bob, Greetings from the greet plugin!"
