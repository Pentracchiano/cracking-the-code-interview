# 5.7 - Write a program to swap odd and even bits in an integer with as few instructions as possible.


def pairwise_swap(n: int) -> int:
    evens_mask = 0b10101010101010101010101010101010
    odds_mask = ~evens_mask

    return ((n & evens_mask) >> 1) | ((n & odds_mask) << 1)

def test_pairwise_swap():
    pairwise_swap(0b01100110) == 0b10011001