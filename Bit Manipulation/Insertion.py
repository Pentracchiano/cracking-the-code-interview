# 5.1 - You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N
# such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to fit
# all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i. You would not,
# for example, have j = 3 and i = 2. because M would not fully fit.

def insert(n: int, m: int, i: int, j: int) -> int:
    # create a mask from i to j to apply to n, to apply to m (inversed)
    # add n and m bits
    length = j - i + 1
    ones = (1 << 32) - 1  # tutti 1
    ones >>= 32 - length  # metto 32 - length zeri a sinistra
    ones <<= i            # metto i 0 a destra e sposto gli 1 dove devono stare

    # OPPURE MOLTO MEGLIO:
    # ones = ((1 << length) - 1) << i
    # praticamente creo il numero di 1 che mi serve e poi lo sposto dove deve essere

    n &= ~ones
    m <<= i
    m &= ones
    return n | m


def test_insert():
    n = 0b10000000000
    m = 0b10011
    i = 2
    j = 6

    result = insert(n, m, i, j)
    expected = 0b10001001100

    assert result == expected
