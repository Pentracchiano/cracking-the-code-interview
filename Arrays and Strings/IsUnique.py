#  1 - Implement an algorithm to determine if a string has all unique characters.
#  What if you cannot use additional data structures?


# Time O(n), Memory O(possible_characters) ~ O(1)
def is_unique_with_data_structures(string: str) -> bool:
    characters = set()
    for char in string:
        if char in characters:
            return False
        characters.add(char)

    return True


def is_unique(string: str) -> bool:
    sorted_string = sorted(string)

    for current_character, next_character in zip(sorted_string, sorted_string[1:]):
        if current_character == next_character:
            return False

    return True


if __name__ == "__main__":
    test = [
        "abcde", "asdfjhkfd", "asd4fg7hjklq"
    ]

    for test_string in test:
        print(test_string, is_unique_with_data_structures(test_string))
        print(test_string, is_unique(test_string))
        print()
