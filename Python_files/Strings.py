
def length_of_string(s):
    return len(s)


def remove_capital_characters(s: str) -> str:
    return ''.join(c for c in s if not c.isupper())


def is_palindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]


def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)
