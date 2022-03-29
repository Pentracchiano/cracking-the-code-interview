# 3 - Given a binary tree, design an algorithm that creates a linked list of all the nodes at each depth
# (if you have a tree with depth D, you'll have D linked lists).
import math
import typing
from collections import deque
from typing import List, TypeVar

from utils.collections.linkedlist import LinkedListNode
from utils.collections.tree import BinaryTree

from MinimalTree import minimal_bst_from_sorted_array


T = TypeVar('T')


class NodeWithLevel(typing.NamedTuple):
    node: BinaryTree[T]
    level: int


def nodes_per_level(root: BinaryTree[T]) -> List[LinkedListNode]:
    level_list: List[LinkedListNode] = []
    if root is None:
        return level_list

    queue: typing.Deque[NodeWithLevel] = deque()
    queue.append(NodeWithLevel(root, 0))

    previous_level = -1
    while len(queue) > 0:
        current, level = queue.popleft()

        new_node = LinkedListNode(data=current.value)
        if previous_level < level:
            level_list.append(new_node)
        else:
            new_node.next = level_list[-1]
            level_list[-1] = new_node

        if current.left is not None:
            queue.append(NodeWithLevel(current.left, level + 1))
        if current.right is not None:
            queue.append(NodeWithLevel(current.right, level + 1))
        previous_level = level

    return level_list


def test_nodes_per_level():
    n = 10
    tree = minimal_bst_from_sorted_array(list(range(n)))

    assert len(nodes_per_level(tree)) == math.ceil(math.log2(n))
