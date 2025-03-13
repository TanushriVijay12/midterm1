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
    assert "Invalid input." in output

def test_repl_invalid_numeric(monkeypatch, capsys):
    # Simulate a command with non-numeric operands
    inputs = iter(["multiply a b", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Invalid operands. Please enter numbers." in output
