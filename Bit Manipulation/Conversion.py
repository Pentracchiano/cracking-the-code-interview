# 5.6 - Write a function to determine the number of bits you would need to flip to convert integer A to integer B.


def number_of_flips(a: int, b: int) -> int:
    mask = 1

    flips = 0
    while mask < 1 << 32:
        a_bit = a & mask
        b_bit = b & mask

        if a_bit != b_bit:
            flips += 1

        mask <<= 1
    return flips


def number_of_flips_xor(a: int, b: int) -> int:
    return ones(a ^ b)

def ones(n: int) -> int:
    mask = 1

    ones = 0
    while mask < 1 << 32:
        if n & mask:
            ones += 1
        mask <<= 1
    return ones

def test_number_of_flips():
    assert number_of_flips(29, 15) == 2
    assert number_of_flips_xor(29, 15) == 2
