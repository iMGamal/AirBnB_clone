"""This is a module for our class Digits."""
import unittest


class Digits(unittest.TestCase):
    """This is the base class of project."""

    def setUp(self):
        """TEST parameter."""
        self.digits = 30

    def test_1(self):
        """FIRST test case."""
        self.assertEqual(self.digits, 30)

    def test_2(self):
        """SECOND test case."""
        self.assertIs(self.digits, 30)


if __name__ == '__main__':
    unittest.main()

