import dataclasses
import typing


T = typing.TypeVar('T')


@dataclasses.dataclass
class LinkedListNode(typing.Generic[T]):
    next: "LinkedListNode" = None
    data: T = None

    @staticmethod
    def create_linked_list_from_iterable(elements: typing.Iterable) -> "LinkedListNode":
        elements = iter(elements)
        head = LinkedListNode(data=next(elements))

        previous_node = head
        for element in elements:
            node = LinkedListNode(data=element)

            previous_node.next = node
            previous_node = node

        return head

    def __repr__(self):
        if self.next:
            return f"{self.data} -> {self.next}"  # O(n^2) string concatenation, care. OK for my purposes.
        return f"{self.data}"


