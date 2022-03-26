# 8 - Given a linked list that might contain a loop, implement an algorithm that returns the node at the beginning of
# the loop, if one exists.
from utils.collections.linkedlist import LinkedListNode
from typing import Optional


def detect_loop(head: LinkedListNode) -> Optional[LinkedListNode]:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break

    if fast is None or fast.next is None:
        return None

    first = head
    second = fast

    while first is not second:
        first = first.next
        second = second.next

    return first


def test_detect_loop():
    no_loop = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4])
    assert detect_loop(no_loop) is None

    looping_node = no_loop.next.next
    no_loop.next.next.next.next = looping_node

    loop = no_loop
    assert detect_loop(loop) is looping_node
