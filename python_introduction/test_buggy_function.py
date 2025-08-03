# test_buggy_function.py

import unittest
from buggy_function import square_number

class TestSquareNumber(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(square_number(3), 9, "Should return 9 when input is 3")
        self.assertEqual(square_number(5), 25, "Should return 25 when input is 5")

    def test_zero_input(self):
        self.assertEqual(square_number(0), 0, "Should return 0 when input is 0")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            square_number("a")  # Should raise TypeError because multiplying string by int is invalid here

if __name__ == '__main__':
    unittest.main()