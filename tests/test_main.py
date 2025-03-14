import pytest # pylint: disable=unused-import
from app.main import main

def test_repl_exit(monkeypatch, capsys):
    # Simulate entering "exit" immediately.
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Goodbye!" in output

def test_repl_menu(monkeypatch, capsys):
    # Simulate "menu" then "exit" to check that available commands are listed.
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Available commands:" in output

def test_repl_add(monkeypatch, capsys):
    # Simulate a valid "add" command: "add 1 2" should result in "Result: 3.0"
    inputs = iter(["add 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Result:" in output and "3.0" in output

def test_repl_invalid_operands(monkeypatch, capsys):
    # Simulate entering non-numeric operands for "add", which should prompt an invalid message.
    inputs = iter(["add x y", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Invalid operands. Please enter numbers." in output

def test_repl_unknown_command(monkeypatch, capsys):
    # Simulate entering an unknown command
    inputs = iter(["foobar", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Unknown command:" in output

def test_repl_insufficient_operands(monkeypatch, capsys):
    # Simulate a command with insufficient operands (e.g., "add" with no numbers)
    inputs = iter(["add", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    # Expect an error message about insufficient operands.
    assert "expects" in output

def test_repl_invalid_numeric(monkeypatch, capsys):
    # Simulate a command with non-numeric operands for a numeric command.
    inputs = iter(["multiply a b", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Invalid operands. Please enter numbers." in output

def test_repl_divide_by_zero(monkeypatch, capsys):
    # Simulate a divide command that should raise an error (division by zero)
    inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    # Check that an error is printed (the specific message may vary)
    assert "Error:" in output and "zero" in output.lower()

def test_repl_greet_plugin(monkeypatch, capsys):
    # Simulate a greet_plugin command with a custom name.
    # This assumes greet_plugin is registered by your plugin manager.
    inputs = iter(["greet_plugin Tanu", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    # Expected output: "Result: Hello Tanu, Greetings from the greet plugin!"
    assert "Hello Tanu, Greetings from the greet plugin!" in output

def test_repl_export_csv(monkeypatch, capsys):
    # Simulate the export_csv command.
    # This assumes export_csv is registered by your plugin manager.
    inputs = iter(["export_csv export_test.csv", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    # Expected output should include the export message.
    assert "History exported to export_test.csv" in output
