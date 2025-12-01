

# ---- Auto-generated tests ----
import unittest
from Number import add_numbers

class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(10, 15), 25)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)
        self.assertEqual(add_numbers(-10, -15), -25)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add_numbers(5, -3), 2)
        self.assertEqual(add_numbers(-7, 4), -3)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(7, 0), 7)

    def test_add_large_numbers(self):
        self.assertEqual(add_numbers(1000000, 2000000), 3000000)
        self.assertEqual(add_numbers(-1000000, -2000000), -3000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_numbers("2", 3)
        with self.assertRaises(TypeError):
            add_numbers(2, "3")
        with self.assertRaises(TypeError):
            add_numbers(None, 3)
        with self.assertRaises(TypeError):
            add_numbers(2, None)

if __name__ == '__main__':
    unittest.main()
