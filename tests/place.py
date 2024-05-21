"""This is a module for our class Place."""
import unittest


class Place(unittest.TestCase):
    """This is a test class."""

    def setUp(self):
        """TEST parameter."""
        self.place = 50

    def test_place(self):
        self.assertEqual(self.place, 50)

