# 2 - Implement a method to return the kth to last element in a linked list.
import typing

from utils.collections.linkedlist import LinkedListNode


def kth_to_last(head: LinkedListNode, k: int) -> typing.Optional[LinkedListNode]:
    # k = 0 -> Return last node

    current = head

    element_at_k_from_current = head
    i = 0
    while element_at_k_from_current is not None and i < k:
        element_at_k_from_current = element_at_k_from_current.next
        i += 1

    if element_at_k_from_current is None:
        return None

    while element_at_k_from_current.next is not None:
        current = current.next
        element_at_k_from_current = element_at_k_from_current.next

    return current


def test_kth_to_last():
    elements = LinkedListNode.create_linked_list_from_iterable(range(10))

    assert kth_to_last(elements, 0).data == 9
    assert kth_to_last(elements, 1).data == 8
    assert kth_to_last(elements, 10) is None
    assert kth_to_last(elements, 9).data == 0
