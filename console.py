#!/usr/bin/python3
"""This is a module for our class Step."""
import cmd, json, models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place

class Step:
    """This is our main class."""

    def __init__(self, height, weight):
        """CLASS constructor."""
        self.height = height
        self.weight = weight

    def area(self):
        """RETURN string."""
        return f"area = {self.height} * {self.weight}"

