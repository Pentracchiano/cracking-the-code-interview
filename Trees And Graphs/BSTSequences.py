# 9 - A binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

"""
Input:
        2
    1       3

Output:
{2, 1, 3}, {2, 3, 1}
"""

import typing
from utils.collections.tree import BinaryTree
from collections import deque


T = typing.TypeVar('T')

PossibleSequence = typing.Deque[T]
Solution = typing.List[PossibleSequence[T]]


def merge_sequences(start_value: T, sequences1: Solution[T], sequences2: Solution[T]) -> Solution[T]:
    if len(sequences1) == 0 and len(sequences2) == 0:
        return [deque((start_value,))]
    if len(sequences1) == 0 or len(sequences2) == 0:
        non_empty_sequence = sequences1 if len(sequences2) == 0 else sequences2
        for sequence in non_empty_sequence:
            sequence.appendleft(start_value)
        return non_empty_sequence

    solution = []
    for sequence1 in sequences1:
        for sequence2 in sequences2:
            partial_solution = merge_two_sequences(sequence1, sequence2)
            solution.extend(partial_solution)

    for sequence in solution:
        sequence.appendleft(start_value)

    return solution


def merge_two_sequences(sequence1: PossibleSequence[T], sequence2: PossibleSequence[T], current_sequence: PossibleSequence[T] = None) -> Solution[T]:
    if len(sequence1) == 0 and len(sequence2) == 0:
        return []

    if current_sequence is None:
        current_sequence = deque()

    if len(sequence1) == 0 or len(sequence2) == 0:
        result = current_sequence.copy()
        result.extend(sequence1)
        result.extend(sequence2)

        return [result]

    # prepare new combination
    first = sequence1.popleft()
    current_sequence.append(first)

    # combine
    partial_solution = merge_two_sequences(sequence1, sequence2, current_sequence)
    # restore
    sequence1.appendleft(current_sequence.pop())

    # prepare new combination
    first = sequence2.popleft()
    current_sequence.append(first)

    # combine
    partial_solution.extend(merge_two_sequences(sequence1, sequence2, current_sequence))
    # restore
    sequence2.appendleft(current_sequence.pop())

    return partial_solution


def bst_sequences(root: BinaryTree[T]) -> Solution[T]:
    if root is None:
        return []

    solutions_left = bst_sequences(root.left)
    solutions_right = bst_sequences(root.right)

    return merge_sequences(root.value, solutions_left, solutions_right)


def test_bst_sequences():
    bst = BinaryTree(2)
    bst.insert(1)
    bst.insert(3)

    assert bst_sequences(bst) == [deque((2, 1, 3)), deque((2, 3, 1))]


def test_bst_sequences_print():
    bst = BinaryTree(75)
    bst.insert(70)
    bst.insert(80)
    bst.insert(30)
    bst.insert(15)
    bst.insert(90)

    print(bst_sequences(bst))
