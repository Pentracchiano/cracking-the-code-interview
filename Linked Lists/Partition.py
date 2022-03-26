# 4 - Write code to partition a linked list around a value x, such that all nodes less than x
# come before all nodes greater than or equal to x.
from abc import abstractmethod
from typing import Protocol, Any, TypeVar

from utils.collections.linkedlist import LinkedListNode


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar('CT', bound=Comparable)


def move_node_to_head(new_head: LinkedListNode, previous: LinkedListNode | None, old_head: LinkedListNode) -> LinkedListNode:
    assert previous.next is new_head
    previous.next = new_head.next
    new_head.next = old_head
    return new_head


def partition(head: LinkedListNode[CT], middle: CT) -> LinkedListNode[CT]:
    # I never move the right elements.
    # I don't move the left elements if no right element has been encountered yet.
    # If at least one has, then I always move the left to the head.
    current = head
    previous = head

    found_a_right_element = False
    while current is not None:
        next_node = current.next
        if current.data < middle and found_a_right_element:
            head = move_node_to_head(current, previous, head)
        elif current.data >= middle:
            found_a_right_element = True
            previous = current
        else:
            previous = current

        current = next_node

    return head


def test_partition():
    elements = LinkedListNode.create_linked_list_from_iterable([4, 7, 8, 2, 15, 3, 89, 5])
    partitioning = 12

    print()
    print(elements)
    print()
    elements = partition(elements, partitioning)

    print(elements)
    print()
    elements = LinkedListNode.create_linked_list_from_iterable([4, 7, 8, 2, 15, 3, 89, 5])
    partitioning = 8

    elements = partition(elements, partitioning)
    print(elements)

    print()
    elements = LinkedListNode.create_linked_list_from_iterable([4, 7, 8, 2, 15, 3, 89, 5])
    partitioning = 12

    elements = partition(elements, partitioning)
    print(elements)
