# 5 - Implement a function to check if a binary tree is a binary search tree.

# A tree is balanced if its left subtree does not contain any element that is larger or equal than the root,
# its right subtree does not contain any element that is lower than the root, and this is valid for all of its subtrees.

from utils.collections.tree import BinaryTree
from MinimalTree import minimal_bst_from_sorted_array
from typing import TypeVar, Protocol, Any
from abc import abstractmethod


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar('CT', bound=Comparable)


def validate_bst(root: BinaryTree[CT] | None) -> bool:
    return _validate_bst(root, None, None)


def _validate_bst(root: BinaryTree[CT] | None, min_value: CT | None, max_value: CT | None) -> bool:
    if root is None:
        return True

    if min_value is not None and root.value < min_value:
        return False

    if max_value is not None and root.value > max_value:
        return False

    is_left_bst = _validate_bst(root.left, min_value, root.value)
    is_right_bst = _validate_bst(root.right, root.value, max_value)

    return is_left_bst and is_right_bst


def test_validate_bst():
    bst: BinaryTree[int] = minimal_bst_from_sorted_array(range(10))
    assert validate_bst(bst) is True


def test_validate_bst_false():
    """
    10 -> go to left -> check 5 < 10 and 5 > min

    5 -> go to right
    min = 5
    max = 10
    11 > min and 11 < max

    5 -> go to left
    min = None
    max = 5
    3 < max and 3 > min



            10
        5        12
    3     11   11
      4

   go to left -> max
   go to right -> min

   check range

   None

    """
    not_a_bst: BinaryTree[int] = BinaryTree(10)

    not_a_bst.left = BinaryTree(5)
    not_a_bst.right = BinaryTree(12)

    not_a_bst.left.right = BinaryTree(11)

    assert validate_bst(not_a_bst) is False

