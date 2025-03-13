import os
import inspect
import logging
from app.calculator import Calculator
from app.history_manager import HistoryManager
from app.plugin_manager import PluginManager
from app.commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

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

        # Check if command exists
        cmd_name = parts[0].lower()
        if cmd_name not in commands:
            print("Unknown command:", cmd_name)
            continue

        # Ensure there are operands provided
        #if len(parts) < 3:
         #   print("Invalid input. Format: command operand1 operand2")
          #  continue

        # Use inspect to determine the number of operands required (excluding 'self')
        sig = inspect.signature(commands[cmd_name].execute)
        expected_operands = len(sig.parameters)

        if len(parts[1:]) < expected_operands:
            print(f"Invalid input. {cmd_name} expects {expected_operands} operand(s).")
            continue

        try:
            # Only take the number of operands expected.
            operands = [float(x) for x in parts[1:expected_operands+1]]
        except ValueError:
            print("Invalid operands. Please enter numbers.")
            continue

        #try:
            # Convert all operands (everything after the command) to floats
         #   operands = [float(x) for x in parts[1:]]
        #except ValueError:
         #   print("Invalid operands. Please enter numbers.")
          #  continue

        try:
            result = commands[cmd_name].execute(*operands)
            if result is not None:
                print("Result:", result)
        except Exception as e:
            logger.error("Error executing command %s: %s", cmd_name, e, exc_info=True)
            print("Error:", e)

if __name__ == "__main__":
    main()
