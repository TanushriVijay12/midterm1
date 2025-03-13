from app.commands.greet_commands import GreetCommand

def test_greet_command():
    cmd = GreetCommand()
    greeting = cmd.execute("Alice")
    assert "Hello" in greeting
    assert "Alice" in greeting
