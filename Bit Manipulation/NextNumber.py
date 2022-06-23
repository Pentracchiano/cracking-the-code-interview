# 5.4 - Given a positive integer, print the next smallest and the next largest number that have the same number of
# 1 bits in their binary representation.


# for the biggest: you swap the rightmost 1 that has a 0 to its left with the zero.
# also, you shift right the remaining 1s for the amount of 0s that are to their right.

# for the smallest: you swap the rightmost 1 that has a 0 to its right with the zero.
# also, you shift left the 1s that are remaining for the amount of 0s that are to their left.
