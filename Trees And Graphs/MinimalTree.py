# 2 - Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
# a binary search tree with minimal height.
import math
import typing
from abc import abstractmethod
from typing import List, Protocol

import pytest

from utils.collections.tree import BinaryTree


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other) -> bool:
        pass


CT = typing.TypeVar('CT', bound=Comparable)


def minimal_bst_from_sorted_array(array: List[CT]) -> BinaryTree[CT] | None:
    # [0 1 2 3 4 5 6 7 8]
    """
                4
           1            6
        0    2       5     7
                3             8


                4
           2        6
        1    3
      0

    """
    # The trick is to put the middle element of the array as the current root.
    # I think it's a problem that is solved naturally recursively.
    # Let's approach it recursively first.
    return _helper(array, 0, len(array))


def _helper(array: List[CT], start: int, end: int) -> BinaryTree[CT] | None:
    length = end - start
    if length == 0:
        return None

    midpoint_index = length // 2 + start
    root: BinaryTree[CT] = BinaryTree(array[midpoint_index])
    root.left = _helper(array, start, midpoint_index)
    root.right = _helper(array, midpoint_index + 1, end)

    return root


@pytest.mark.parametrize('n_elements', [1, 5, 10, 20, 50])
def test_minimal_tree(n_elements):
    array = list(range(n_elements))

    generated_tree = minimal_bst_from_sorted_array(array)
    print('\n')
    print(generated_tree)
    print('\n')

    assert generated_tree.depth <= math.log2(n_elements) + 1

#
