# 4 - Implement a function to check if a balanced tree is balanced. For the purposes of the question, balanced
# tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
import typing

import pytest

from utils.collections.tree import BinaryTree
from MinimalTree import minimal_bst_from_sorted_array


def is_balanced(tree: BinaryTree) -> bool:
    return _is_balanced_recursive(tree)[0]


def _is_balanced_recursive(tree: BinaryTree) -> typing.Tuple[bool, int]:
    if tree is None:
        return True, 0

    is_balanced_left, height_left = _is_balanced_recursive(tree.left)
    if not is_balanced_left:
        return False, 0
    is_balanced_right, height_right = _is_balanced_recursive(tree.right)
    if not is_balanced_right:
        return False, 0

    return abs(height_right - height_left) <= 1, max(height_right, height_left) + 1


@pytest.mark.parametrize('size', [1, 10, 20, 50, 100])
def test_is_balanced_true(size):
    tree = minimal_bst_from_sorted_array(list(range(size)))

    assert is_balanced(tree) is True


def test_is_balanced_false():
    tree = BinaryTree(10)
    tree.left = BinaryTree(10)
    tree.left.left = BinaryTree(100)

    assert is_balanced(tree) is False
