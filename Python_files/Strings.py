
def length_of_string(s):
    return len(s)


def remove_capital_characters(s: str) -> str:
    return ''.join(c for c in s if not c.isupper())
