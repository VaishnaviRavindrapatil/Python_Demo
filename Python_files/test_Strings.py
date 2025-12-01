

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


# ---- Auto-generated tests ----
import unittest
from Strings import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_valid_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome(""))

    def test_invalid_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("unittest"))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Level"))

    def test_with_spaces_and_special_characters(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertFalse(is_palindrome("This is not a palindrome!"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_numeric_palindromes(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1221"))
        self.assertFalse(is_palindrome("12345"))
        self.assertFalse(is_palindrome("123456"))

if __name__ == "__main__":
    unittest.main()
