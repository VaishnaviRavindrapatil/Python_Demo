

# ---- Auto-generated tests ----
import unittest
from Strings import remove_capital_characters

class TestRemoveCapitalCharacters(unittest.TestCase):

    def test_remove_capital_characters_all_caps(self):
        input_str = "HELLO"
        expected_output = ""
        self.assertEqual(remove_capital_characters(input_str), expected_output)

    def test_remove_capital_characters_no_caps(self):
        input_str = "hello"
        expected_output = "hello"
        self.assertEqual(remove_capital_characters(input_str), expected_output)

    def test_remove_capital_characters_mixed_case(self):
        input_str = "HeLLoWoRLd"
        expected_output = "eoood"
        self.assertEqual(remove_capital_characters(input_str), expected_output)

    def test_remove_capital_characters_with_numbers(self):
        input_str = "HeLLo123WoRLd"
        expected_output = "eoood123"
        self.assertEqual(remove_capital_characters(input_str), expected_output)

    def test_remove_capital_characters_with_special_characters(self):
        input_str = "HeLLo!@#WoRLd$%^"
        expected_output = "eoood!@#$%^"
        self.assertEqual(remove_capital_characters(input_str), expected_output)

    def test_remove_capital_characters_empty_string(self):
        input_str = ""
        expected_output = ""
        self.assertEqual(remove_capital_characters(input_str), expected_output)

    def test_remove_capital_characters_only_special_characters(self):
        input_str = "!@#$%^&*()"
        expected_output = "!@#$%^&*()"
        self.assertEqual(remove_capital_characters(input_str), expected_output)

    def test_remove_capital_characters_only_numbers(self):
        input_str = "1234567890"
        expected_output = "1234567890"
        self.assertEqual(remove_capital_characters(input_str), expected_output)

    def test_remove_capital_characters_invalid_input_integer(self):
        with self.assertRaises(TypeError):
            remove_capital_characters(12345)

    def test_remove_capital_characters_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_capital_characters(None)

if __name__ == "__main__":
    unittest.main()
