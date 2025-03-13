import pytest # pylint: disable=unused-import
from app.main import main

def test_repl_exit(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert "Goodbye!" in captured

def test_repl_menu(monkeypatch, capsys):
    # Simulate user typing 'menu' then 'exit'
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert "Available commands:" in captured

def test_repl_unknown(monkeypatch, capsys):
    # Test unknown command handling then exit
    inputs = iter(["unknown", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert "Unknown command" in captured
