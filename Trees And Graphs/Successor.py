# 6 - Write an algorithm to find the "next" node , (in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to its parent.
import typing
from utils.collections.tree import BinaryTree

T = typing.TypeVar('T')


def tree_min(node: BinaryTree[T]) -> T:
    current = node
    while current.left is not None:
        current = current.left
    return current.value


def successor(node: BinaryTree[T] | None) -> T | None:
    if node is None:
        return None

    if node.right is not None:
        return tree_min(node.right)

    current = node.parent
    previous = node
    while current is not None:
        if current.left is previous:
            return current.value

        previous = current
        current = current.parent

    return None


def test_successor():
    bst: BinaryTree[int] = BinaryTree(50)
    bst.insert(25)
    bst.insert(75)
    bst.insert(12)
    bst.insert(30)
    bst.insert(26)
    bst.insert(75)
    bst.insert(60)

    assert successor(bst) == 60
    assert successor(bst.left.left) == 25
    assert successor(bst.left) == 26
    assert successor(bst.left.right) == 50


