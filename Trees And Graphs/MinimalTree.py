# 2 - Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
# a binary search tree with minimal height.
import math
import typing
from abc import abstractmethod
from typing import Sequence, Protocol

import pytest

from utils.collections.tree import BinaryTree


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other) -> bool:
        pass


CT = typing.TypeVar('CT', bound=Comparable)


def minimal_bst_from_sorted_array(array: Sequence[CT]) -> BinaryTree[CT] | None:
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
    return _minimal_bst_from_sorted_array(array, 0, len(array))


def _minimal_bst_from_sorted_array(array: Sequence[CT], start: int, end: int) -> BinaryTree[CT] | None:
    # [1, 2, 3, 4, 5]
    # 0, 5 -> i:2 -> 3
    # 3, 5 -> i:4 -> 5

    # 3, 4 -> i:3 -> 4
    # 3, 3 -> None
    # 4, 4 -> None

    # 0, 2 -> i:1 -> 2
    # 2, 2 -> None

    # 0, 1 -> i:0 -> 1
    # 0, 0 -> None
    # 1, 1 -> None

    """
            3
        2       5
    1         4

    """

    # [1, 2, 3, 4, 5, 6]
    length = end - start
    if length == 0:
        return None

    midpoint_index = length // 2 + start
    root: BinaryTree[CT] = BinaryTree(array[midpoint_index])
    root.left = _minimal_bst_from_sorted_array(array, start, midpoint_index)
    root.right = _minimal_bst_from_sorted_array(array, midpoint_index + 1, end)

    return root


@pytest.mark.parametrize('n_elements', [1, 5, 10, 20, 50])
def test_minimal_bst_from_sorted_array(n_elements):
    array = range(n_elements)

    generated_tree = minimal_bst_from_sorted_array(array)
    print('\n')
    print(generated_tree)
    print('\n')

    assert generated_tree.depth <= math.log2(n_elements) + 1
