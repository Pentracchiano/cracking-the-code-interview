# 4.11 You are implementing a binary search tree from scratch which, in addition to insert, find, and delete, has
# a method get_random_node() which returns a random node from the tree. All nodes should be equally likely to be chosen.
# Design and implement an algorithm for get_random_node, and explain how you would implement the rest of the methods.
import typing
import random
import pytest

T = typing.TypeVar('T')


class RandomTree(typing.Generic[T]):
    value: T
    size: int = 1
    left: "RandomTree[T]" = None
    right: "RandomTree[T]" = None

    def __init__(self, value: T):
        self.value = value

    def insert(self, value: T):
        self.size += 1
        if value < self.value:
            if self.left is None:
                self.left = RandomTree(value)
                return
            self.left.insert(value)
            return

        if self.right is None:
            self.right = RandomTree(value)
            return

        self.right.insert(value)

    def find(self, value: T) -> "RandomTree[T] | None":
        if value == self.value:
            return self
        if value < self.value:
            if self.left is not None:
                return self.left.find(value)
            return None
        if self.right is not None:
            return self.right.find(value)
        return None

    def delete(self, value: T) -> "RandomTree[T] | None":
        # Precondition: the value must be in the tree
        self.size -= 1
        if value == self.value:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            substitute = self.left.max()
            self.delete(substitute.value)  # SELF and not substitute because i have to update the sizes!
            self.value = substitute.value
            return self

        if value < self.value:
            self.left = self.left.delete(value)
            return self
        self.right = self.right.delete(value)
        return self

    def max(self) -> "RandomTree[T]":
        current = self
        while current.right is not None:
            current = current.right
        return current

    def get_random_node(self) -> "RandomTree[T]":
        index_of_node_to_return = random.randint(0, self.size - 1)
        return self.get_node_by_index(index_of_node_to_return)

    def get_node_by_index(self, index) -> "RandomTree[T]":
        left_size = 0 if self.left is None else self.left.size

        if index == left_size:
            return self
        if index < left_size:
            return self.left.get_node_by_index(index)
        return self.right.get_node_by_index(index - left_size - 1)


def test_random_node():
    root = RandomTree(7)
    root.insert(5)
    root.insert(10)
    root.insert(20)
    root.insert(9)
    root.insert(1)
    root.insert(6)

    # sizes
    assert root.size == 7
    assert root.left.size == 3
    assert root.right.size == 3

    # inserts
    assert root.left.value == 5
    assert root.left.left.value == 1
    assert root.left.right.value == 6

    # finds
    assert root.find(9) is root.right.left
    assert root.find(7) is root
    assert root.find(100) is None

    # index
    assert root.get_node_by_index(0) is root.left.left
    assert root.get_node_by_index(1) is root.left
    assert root.get_node_by_index(6) is root.right.right

    # delete
    root = root.delete(7)
    assert root.value == 6
    assert root.right.delete(20) is root.right

    assert root.size == 5


