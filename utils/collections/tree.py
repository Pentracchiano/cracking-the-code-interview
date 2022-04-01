import collections
import dataclasses
import typing


T = typing.TypeVar('T')


@dataclasses.dataclass(repr=False, eq=False)
class BinaryTree(typing.Generic[T]):
    value: T
    left: 'BinaryTree[T]' = None
    right: 'BinaryTree[T]' = None
    parent: 'BinaryTree[T]' = None

    def __repr__(self) -> str:
        depth = self.depth
        # BFS
        queue: typing.Deque[typing.Tuple[BinaryTree[T], int]] = collections.deque()

        queue.append((self, depth))
        result = []
        previous_depth = depth
        while len(queue) > 0:
            current, current_depth = queue.popleft()

            if previous_depth > current_depth:
                result.append('\n')
            result.append("    " * current_depth)

            if current is not None:
                result.append(repr(current.value))

                queue.append((current.left, current_depth - 1))
                queue.append((current.right, current_depth - 1))

            previous_depth = current_depth

        return "".join(result)

    @property
    def depth(self) -> int:
        return 1 + max(self.left.depth if self.left else 0, self.right.depth if self.right else 0)

    def insert(self, value: T):
        current = self
        while True:  # self can't be None
            if value < current.value:
                if current.left is None:
                    current.left = BinaryTree(value, parent=current)
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BinaryTree(value, parent=current)
                    return
                else:
                    current = current.right

    def insert_recursive(self, value: T):
        self._insert_recursive(value)

    def _insert_recursive(self, value: T) -> "BinaryTree[T]":
        if self is None:
            return BinaryTree(value)

        child = self.left if value < self.value else self.right

        child = BinaryTree._insert_recursive(child, value)
        child.parent = self
        return self
