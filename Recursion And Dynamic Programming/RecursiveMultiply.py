# 8.5 - Write a recursive function to multiply two positive integers without using
# the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
# minimize the number of those operations.
import pytest


def recursive_multiply(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)

    if b == 0:
        return 0
    if b == 1:
        return a
    if b % 2 == 0:
        return recursive_multiply(a << 1, b >> 1)

    # 7 * 3 = (7 * 2) + (7 * 1) =

    return recursive_multiply(a , b - 1) + a


@pytest.mark.parametrize("a,b", [
    [1, 5],
    [0, 5],
    [7, 5],
    [144, 99],
    [8, 2]
])
def test_recursive_multiply(a, b):
    assert a * b == recursive_multiply(a, b)

