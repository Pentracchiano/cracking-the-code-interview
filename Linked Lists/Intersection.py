# 7 - Given two singly linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value.
from typing import Optional, Tuple

from utils.collections.linkedlist import LinkedListNode


def intersection_hash(first: LinkedListNode, second: LinkedListNode) -> Optional[LinkedListNode]:
    # To use less memory, one could precompute the length of both lists and then
    # save the node ids of the smallest.
    current_first = first

    first_ids = set()
    while current_first is not None:
        first_ids.add(id(current_first))
        current_first = current_first.next

    current_second = second
    while current_second is not None:
        if id(current_second) in first_ids:
            return current_second

        current_second = current_second.next

    return None


def length_and_tail(head: LinkedListNode) -> Tuple[int, LinkedListNode]:
    size = 0
    current = head
    previous = None
    while current is not None:
        size += 1
        previous = current
        current = current.next
    return size, previous


def get_kth_node(head: LinkedListNode, k: int) -> Optional[LinkedListNode]:
    i = 0
    while head is not None and i < k:
        head = head.next
        i += 1
    return head


"""
a -> b -> c -> d -> None
f -> b -> c -> d -> None

same length = check step by step

a -> t -> b -> c -> d -> None
f -> b -> c -> d -> None

the last is always the same if they intersect 

t -> g ->
           b -> c -> d -> None
f ->

i can make them the same length since the first part is useless
"""


def intersection(first: LinkedListNode, second: LinkedListNode) -> Optional[LinkedListNode]:
    first_length, first_tail = length_and_tail(first)
    second_length, second_tail = length_and_tail(second)

    # Quick get-out
    if id(first_tail) != id(second_tail):
        return None

    longer = first if first_length >= second_length else second
    shorter = second if longer is first else first

    longer = get_kth_node(longer, abs(first_length - second_length))
    while longer is not None and shorter is not None:
        if id(longer) == id(shorter):
            return longer
        longer = longer.next
        shorter = shorter.next

    return None


def test_intersection():
    first = LinkedListNode.create_linked_list_from_iterable(range(10))
    second = LinkedListNode.create_linked_list_from_iterable(range(11, 15))

    assert intersection_hash(first, second) is None
    assert intersection(first, second) is None

    intersection_node, second.next.next.next.next = first.next.next, first.next.next

    assert intersection_hash(first, second) == intersection_node
    assert intersection(first, second) == intersection_node
