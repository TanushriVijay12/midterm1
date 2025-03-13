import math
import logging

# Square Root Command
class SquareRootCommand:
    def __init__(self, history_manager=None):
        self.history_manager = history_manager
    def execute(self, a):
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        result = math.sqrt(a)
        logging.info(f"SquareRootCommand: sqrt({a}) = {result}")
         # Record the calculation if history_manager is available.
        if self.history_manager:
            # Since square root only uses one operand, we can store None for a second operand.
            self.history_manager.add_record("sqrt", a, None, result)
        return result

# Power Command
class PowerCommand:
    def __init__(self, history_manager=None):
        self.history_manager = history_manager
    def execute(self, a, b):
        result = a ** b
        logging.info(f"PowerCommand: {a} raised to the power {b} = {result}")
        if self.history_manager:
            self.history_manager.add_record("power", a, b, result)
        return result

# Factorial Command (Additional Example)
class FactorialCommand:
    def execute(self, a):
        if a < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = math.factorial(int(a))
        logging.info(f"FactorialCommand: factorial({a}) = {result}")
        return result

# Logarithm Command (Additional Example)
class LogarithmCommand:
    def execute(self, a, base=math.e):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        result = math.log(a, base)
        logging.info(f"LogarithmCommand: log_{base}({a}) = {result}")
        return result

def register(history_manager=None):
    """
    Register multiple math commands.
    The history_manager parameter is available if the commands need to interact with it.
    """
    return {
        "sqrt": SquareRootCommand(history_manager),
        "power": PowerCommand(history_manager),
        "factorial": FactorialCommand(),
        "log": LogarithmCommand(),
    }
