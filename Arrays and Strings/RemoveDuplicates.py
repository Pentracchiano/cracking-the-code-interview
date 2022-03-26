# NotBook - In a sorted array, remove duplicates.


def remove_duplicates(array):
    if len(array) < 2:
        return array

    current_shift = 0

    i = 1
    while i < len(array):
        if array[i] == array[i - 1]:
            current_shift += 1
        else:
            array[i - current_shift] = array[i]
        i += 1

    return array[:len(array) - current_shift]


def test_remove_duplicates():
    assert remove_duplicates(list("aaabccddefg")) == list("abcdefg")
    assert remove_duplicates(list("a")) == list("a")
    assert remove_duplicates(list("aa")) == list("a")
    assert remove_duplicates(list("ab")) == list("ab")

