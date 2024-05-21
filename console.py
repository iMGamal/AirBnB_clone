#!/usr/bin/python3
"""This is a module for our class Step."""


class Step:
    """This is our main class."""

    def __init__(self, height, weight):
        """CLASS constructor."""
        self.height = height
        self.weight = weight

    def area(self):
        """RETURN string."""
        return f"area = {self.height} * {self.weight}"

