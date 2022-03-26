# 9 - Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
# waterbottle is a rotation of erbottlewat

def is_substring(string: str, candidate: str) -> bool:
    if len(candidate) > len(string):
        return False

    string_index = 0
    candidate_index = 0
    while string_index < len(string) and candidate_index < len(candidate):
        if string[string_index] == candidate[candidate_index]:
            string_index += 1
            candidate_index += 1
            continue

        string_index += 1
        candidate_index = 0

    return candidate_index == len(candidate)


def is_string_rotation(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    concatenation = string1 + string1
    return is_substring(concatenation, string2)


def test_is_substring():
    assert is_substring("test", "te")
    assert is_substring("test", "tes")
    assert is_substring("test", "test")
    assert is_substring("test", "st")
    assert is_substring("test", "t")
    assert is_substring("peppe", "pe")
    assert is_substring("peppe", "pep")
    assert is_substring("peppe", "epp")
    assert is_substring("peppe", "peppe")

    assert not is_substring("peppe", "epe")
    assert not is_substring("peppe", "pepe")
    assert not is_substring("test", "tet")
    assert not is_substring("test", "estt")


def test_is_string_rotation():
    string1 = "waterbottle"
    string2 = "erbottlewat"

    assert is_string_rotation(string1, string2)


def test_is_string_rotation_fail_length():
    string1 = "waterbottle"
    string2 = "erbottlewater"

    assert not is_string_rotation(string1, string2)


def test_is_string_rotation_fail():
    string1 = "waterbottle"
    string2 = "wasterbottle"

    assert not is_string_rotation(string1, string2)
