import os
import logging
from calculator.calculator import Calculator
from calculator.history_manager import HistoryManager
from calculator.plugin_manager import PluginManager
from calculator.commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(level=log_level,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting Advanced Python Calculator with REPL...")

    # Initialize core components
    calculator = Calculator()
    history_manager = HistoryManager()
    plugin_manager = PluginManager(history_manager=history_manager)
    plugin_manager.load_plugins()

    # Register built-in commands
    commands = {
        "add": AddCommand(calculator, history_manager),
        "subtract": SubtractCommand(calculator, history_manager),
        "multiply": MultiplyCommand(calculator, history_manager),
        "divide": DivideCommand(calculator, history_manager)
    }
    # Merge plugin commands
    commands.update(plugin_manager.get_commands())

    print("Advanced Python Calculator")
    print("Type 'menu' to see available commands, or 'exit' to quit.")

    while True:
        user_input = input(">> ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if user_input.lower() == "menu":
            print("Available commands:")
            for cmd in sorted(commands.keys()):
                print(" -", cmd)
            continue

        parts = user_input.split()
        cmd_name = parts[0]
        if cmd_name not in commands:
            print("Unknown command:", cmd_name)
            continue

        try:
            # Attempt to convert operands to floats
            operands = [float(x) for x in parts[1:]]
        except ValueError:
            print("Invalid operands. Please enter numbers.")
            continue

        try:
            result = commands[cmd_name].execute(*operands)
            if result is not None:
                print("Result:", result)
        except Exception as e:
            logger.error("Error executing command %s: %s", cmd_name, e, exc_info=True)
            print("Error:", e)

if __name__ == "__main__":
    main()
