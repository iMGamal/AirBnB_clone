"""Module to display current date and time."""
from datetime import datetime


class Fun:
    """Class for practice."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Hey, {self.a}. {self.b} is coming"

mod = Fun(7, 3)
print(mod)
current = datetime.now()
now = current.isoformat()
print(current)
print(now)

