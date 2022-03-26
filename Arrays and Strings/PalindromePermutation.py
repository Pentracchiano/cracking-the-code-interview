# 4 - Given a string, write a function to check if it is a permutation of a palindrome.
# You can ignore casing and non-letter characters.
# Example: Tact coa -> True
from collections import defaultdict

import pytest

def is_permutation_of_palindrome(string: str) -> bool:
    true_length = 0
    characters_frequency = defaultdict(int)
    for character in string.lower():
        if character.isalpha():
            characters_frequency[character] += 1
            true_length += 1

    # not needed: an even string can't have exactly one odd count of characters
    can_have_extra_character_to_be_palindrome = true_length % 2 != 0

    used_extra = not can_have_extra_character_to_be_palindrome
    for frequency in characters_frequency.values():
        if frequency % 2 != 0:
            if used_extra:
                return False
            used_extra = True

    return True


def test_is_permutation_of_palindrome():
    assert is_permutation_of_palindrome("Tact Coa")
    assert not is_permutation_of_palindrome("cI a o")
    assert is_permutation_of_palindrome("fottof")
    assert is_permutation_of_palindrome("otftof")
