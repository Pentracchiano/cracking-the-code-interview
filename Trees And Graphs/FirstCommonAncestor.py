# 8 - Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
# Avoid storing additional nodes in a data structure.
from utils.collections.tree import BinaryTree
import typing


T = typing.TypeVar('T')


def find_one_of_nodes(root: BinaryTree[T] | None, nodes: typing.Sequence[BinaryTree[T]]) -> BinaryTree[T] | None:
    if root is None:
        return None
    if any((root is node for node in nodes)):
        return root

    value = find_one_of_nodes(root.left, nodes)
    if value is not None:
        return value
    return find_one_of_nodes(root.right, nodes)


def common_ancestor_with_parent_link(root: BinaryTree[T], node1: BinaryTree[T], node2: BinaryTree[T]) -> BinaryTree[T] | None:
    # O(n). This can actually be done in O(d) where d is the depth of the deepest node.
    candidate_ancestor = find_one_of_nodes(root, (node1, node2))
    to_find = node1 if candidate_ancestor is node2 else node2

    found = find_one_of_nodes(candidate_ancestor, (to_find,))
    if found is not None:
        return candidate_ancestor

    # if we get here, we have to go upwards
    current = candidate_ancestor.parent  # must exist because i am assuming node1 and node2 are in the subtree
    previous = candidate_ancestor
    while True:
        if current.parent is None:
            return current

        if current.left is previous and find_one_of_nodes(current.right, (to_find,) is not None):
            return current

        current = current.parent
        previous = current


def common_ancestor(root: BinaryTree[T], node1: BinaryTree[T], node2: BinaryTree[T]) -> BinaryTree[T] | None:
    ancestor, is_ancestor = _common_ancestor(root, node1, node2)
    if is_ancestor:
        return ancestor
    return None


def _common_ancestor(root: BinaryTree[T], node1: BinaryTree[T], node2: BinaryTree[T]) -> typing.Tuple[BinaryTree[T] | None, bool]:
    # the second value aims at solving the problem of only one node of the two being in the tree
    if root is None:
        return None, False

    if root is node1 and root is node2:
        return root, True

    left_ancestor, left_is_ancestor = common_ancestor(root.left, node1, node2)
    if left_is_ancestor:
        return left_ancestor, True
    right_ancestor, right_is_ancestor = common_ancestor(root.right, node1, node2)
    if right_is_ancestor:
        return right_ancestor, True

    if (left_ancestor is node1 or left_ancestor is node2) and (right_ancestor is node1 or right_ancestor is node2):
        return root, True

    if root is node1 or root is node2:
        if left_ancestor is not None or right_ancestor is not None:
            return root, True
        return root, False

    if left_ancestor is not None:
        return left_ancestor, False

    return right_ancestor, False

