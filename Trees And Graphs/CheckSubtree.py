# 4.10 - T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine
# if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

# https://leetcode.com/problems/subtree-of-another-tree/


# COMPLEXITY: O(n + m) to construct the structures + complexity of the `in` python operator which can be O(nm) or O(n+m)
# in good cases it can be sublinear!
# SPACE COMPLEXITY O(n + m)


import typing

from utils.collections.tree import BinaryTree


def _structure(root: typing.Optional[BinaryTree], current_structure: typing.List[str]):
    if root is None:
        current_structure.append('N')
        return

    current_structure.append(str(root.value))
    _structure(root.left, current_structure)
    _structure(root.right, current_structure)


def structure(root: typing.Optional[BinaryTree]) -> str:
    result = []
    _structure(root, result)

    # the initial space serves to differentiate 12 N N from 2 N N such that the second does not end up being
    # a subtree of 12 N N
    return " " + " ".join(result)


def check_subtree(root: typing.Optional[BinaryTree], subroot: typing.Optional[BinaryTree]) -> bool:
    return structure(subroot) in structure(root)
