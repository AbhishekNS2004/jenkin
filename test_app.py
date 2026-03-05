import unittest
from app import reverse_string


class TestReverseString(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_numbers(self):
        self.assertEqual(reverse_string("12345"), "54321")


if __name__ == "__main__":
    unittest.main()