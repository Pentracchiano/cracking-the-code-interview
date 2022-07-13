# 8.4 - Write a method to return all subsets of a set.

# if i have a set which is {1, 3} all subsets are the set itself, the empty set, 1, and 3.

# basically we have to select all possible variants of the set!
# the algorithm can at best be 2^n since this is the amount of subsets a set has -- the conclusion is that
# you can pick any element and either choose it or not to be in the subset. and then you pick all possible choices.
# everytime we are therefore making a choice between 2 actions, putting or not putting the element in the new subset.
# in the end, we will make this choice n times, therefore 2^n.

# a first algorithm that comes to my mind is to emulate this behavior by creating a binary string long n:
# for instance, for the subset of 2 elements, we create the string 00 and then create the set that is corresponding to
# that set of choices -> the empty set. then we increment the string until we go through all possibilities.
# i increment the string 2^n times and go through all of the values possible -- the point is that in order to read the
# string we are going through n operations -- which is n times 2^n. the algorithm is therefore O(n2^n).

# Can we do better?

# Maybe we can avoid using a binary string, because in order to read it we need to do n operations.
# Probably recursion can help.

# we use a recursive function that calls itself while building a subset solution both with and without the current element.
# This should be 2^n and according to the previous considerations, it's the best we can do.