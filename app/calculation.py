# app/calculation.py
# pylint: disable=unnecessary-dunder-call, invalid-name
class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ValueError("Division by zero!")
        return self.a / self.b
