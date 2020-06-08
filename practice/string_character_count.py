"""
get count of character in a string
"""


def count_char(string: str, char: str):
    return string.lower().count(char.lower())


print(count_char('aabcdddddd', 'd'))
