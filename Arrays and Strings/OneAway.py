# There are three types of edits that can be performed on strings: insert a character, remove a character,
# or replace a character. Given two strings, write a function to check if they are one or zero edits away.

def is_edit_distance_one_away(first: str, second: str) -> bool:
    size_difference = abs(len(first) - len(second))
    if size_difference > 1:
        return False

    first_index = 0
    second_index = 0
    bigger_string = None

    if size_difference == 1:
        if len(first) > len(second):
            bigger_string = 0
        else:
            bigger_string = 1

    used_edit = False
    while first_index < len(first) and second_index < len(second):
        if first[first_index] != second[second_index]:
            if used_edit:
                return False
            used_edit = True

            if bigger_string is not None:
                if bigger_string == 0:
                    first_index += 1
                else:
                    second_index += 1
                continue

        first_index += 1
        second_index += 1

    return True


def test_is_edit_distance_one_away():
    assert is_edit_distance_one_away("pale", "ple")
    assert is_edit_distance_one_away("pales", "pale")
    assert is_edit_distance_one_away("pale", "bale")
    assert not is_edit_distance_one_away("pale", "bake")