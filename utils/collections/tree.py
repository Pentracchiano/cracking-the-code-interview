import collections
import dataclasses
import typing


T = typing.TypeVar('T')


@dataclasses.dataclass(repr=False)
class BinaryTree(typing.Generic[T]):
    value: T
    left: 'BinaryTree[T]' = None
    right: 'BinaryTree[T]' = None

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



