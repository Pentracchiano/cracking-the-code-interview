# 5.3 - You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the
# longest sequence of 1s that you can create.

def longest_ones_with_one_flip(n: int) -> int:
    current_mask = 1 << 31

    longest_streak = 0
    current_streak = 0
    last_flip = None
    for i in range(32):
        if n & current_mask:
            current_streak += 1
        elif last_flip is None:
            current_streak += 1
            last_flip = i
        else:
            current_streak = i - last_flip
            last_flip = i

        longest_streak = max(longest_streak, current_streak)
        current_mask >>= 1

    return longest_streak

def test_longest_ones_with_one_flip():
    assert longest_ones_with_one_flip(1775) == 8
    assert longest_ones_with_one_flip(0b00001000001101) == 4
    assert longest_ones_with_one_flip(0) == 1


