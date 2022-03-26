# 2 - Given two strings, write a method to decide if one is a permutation of the other.
from collections import defaultdict

import pytest
import typing


def _character_frequency(string: str) -> typing.Dict[str, int]:
    frequency_map = defaultdict(int)
    for char in string:
        frequency_map[char] += 1

    return frequency_map


def check_permutation(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False

    first_word_characters = _character_frequency(first)
    second_word_characters = _character_frequency(second)

    return first_word_characters == second_word_characters


@pytest.mark.parametrize("string1,string2,expected", [
    ("car", "rac", True),
    ("wreck", "ckewr", True),
    ("nope", "yess", False),
    ("absolutelynot", "yay!", False),
    ("wreck", "wrakc", False)
])
def test_check_permutation(string1, string2, expected):
    assert check_permutation(string1, string2) == expected

