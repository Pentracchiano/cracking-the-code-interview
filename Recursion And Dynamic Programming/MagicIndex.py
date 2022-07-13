# 8.3 - A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# FOLLOW UP: what if the values are not distinct?


# first solution, easy O(n) brute force.

# second solution, let's use the fact that the array is sorted.
# a binary search could work, so maybe we go in the middle looking for n // 2.


# [1 4 5 9 10 11 12 13 14 ]

# if it's not there and the element is bigger, we have to go to the left. since it's all distinct elements,
# the index will never catch up with the elements, therefore it's going to be on the left.
# if it's there, we're done.
# if it's not there and the element is smaller than the index we're looking for, it means that there are negative
# integers at the beginning of the array. The element must be on the right.

# [-4 -2 -1 0 4]

# This has a O(log n) complexity and exploits the sorted structure + the distinct elements.
# What if the elements are not distinct?

# At that point, it's not true anymore that the indices cannot catch up!

# [1 4 5 9 10 11 11 11 11 11 11 11]
