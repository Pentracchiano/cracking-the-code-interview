# 3 - Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space
# at the end to hold the additional characters, and that you are given the "true" length of the string.
from typing import List

import pytest


def _shift_characters_right(string: List[str], start: int, size: int, n_characters_to_shift: int):
    # Assumes there's space in the original string
    for i in range(size, start - 1, -1):
        string[i + n_characters_to_shift] = string[i]


def urlify_squared(string: List[str], true_size: int) -> List[str]:
    SPACE = " "
    SUBSTITUTION = list("%20")

    total_size = true_size
    for i in range(true_size - 1, -1, -1):
        character = string[i]
        if character == SPACE:
            _shift_characters_right(string, i, total_size - 1, len(SUBSTITUTION) - 1)
            string[i:i + len(SUBSTITUTION)] = SUBSTITUTION[:]
            total_size += len(SUBSTITUTION) - 1

    return string


def urlify(string: List[str], true_size: int) -> List[str]:
    SPACE = " "
    SUBSTITUTION = list("%20")

    number_of_spaces = 0
    for char in string[:true_size]:
        if char == SPACE:
            number_of_spaces += 1
    # or, maybe, a little cheat could be to read the actual length of the string. Not doing that since it's not
    # possible to do in any language (could be a char pointer in C with uninitialized values)
    current_shift = (len(SUBSTITUTION) - 1) * number_of_spaces
    for i in range(true_size - 1, -1, -1):
        current_character = string[i]
        if current_character == SPACE:
            current_shift -= len(SUBSTITUTION) - 1
            string[i + current_shift:i + current_shift + len(SUBSTITUTION)] = SUBSTITUTION[:]
        else:
            string[i + current_shift] = string[i]
    return string


@pytest.mark.parametrize("string,true_size,expected", [
    (list("A cute test with more spaces          "), 28, list("A%20cute%20test%20with%20more%20spaces")),
    (list("Mr John Smith    "), 13, list("Mr%20John%20Smith")),
])
def test_urlify_squared(string, true_size, expected):
    assert urlify_squared(string, true_size) == expected


@pytest.mark.parametrize("string,true_size,expected", [
    (list("A cute test with more spaces          "), 28, list("A%20cute%20test%20with%20more%20spaces")),
    (list("Mr John Smith    "), 13, list("Mr%20John%20Smith")),
])
def test_urlify(string, true_size, expected):
    assert urlify(string, true_size) == expected
