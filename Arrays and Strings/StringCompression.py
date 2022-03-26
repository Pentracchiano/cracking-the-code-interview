# 6 - Implement a method to perform basi string compression using the counts of repeated characters.
# Example:
# aabcccccaaa would become a2b1c5a3.
# If the compressed string would not become smaller than the original string, your method should return the original
# string. You can assume the string has only uppercase and lowercase letters (a-z).

import pytest


def compress_string(string: str) -> str:
    if len(string) <= 1:
        return string

    compressed = []
    i = 1
    current_count = 1

    compressed.append(string[0])
    while i < len(string):
        if string[i] != string[i - 1]:
            compressed.append(str(current_count))
            compressed.append(string[i])
            current_count = 1
        else:
            current_count += 1

        i += 1

    compressed.append(str(current_count))
    if len(compressed) <= len(string):
        return "".join(compressed)
    return string


def test_compress_string():
    assert compress_string("aabcccccaaa") == "a2b1c5a3"
    assert compress_string("abcd") == "abcd"
    assert compress_string("a") == "a"
    assert compress_string("aabb") == "a2b2"
