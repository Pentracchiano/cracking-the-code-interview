# 3 - Implement an algorithm to delete a node in the middle (any node but the first and last node, not necessarily
# the exact middle) of a singly linked list, given only access to that node.
from utils.collections.linkedlist import LinkedListNode


def delete_node(node_to_delete: LinkedListNode) -> bool:
    if node_to_delete is None:
        return True
    if node_to_delete.next is None:
        return False  # other option: mark this as a "dummy" node. Cannot do this without breaking the interface.

    # Make the "to be deleted" the actual next one, deleting the next
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next


def test_delete_node():
    elements = LinkedListNode.create_linked_list_from_iterable(range(5))
    third = elements.next.next

    delete_node(third)
    assert elements == LinkedListNode.create_linked_list_from_iterable([0, 1, 3, 4])

    elements = LinkedListNode.create_linked_list_from_iterable(range(5))
    first = elements

    delete_node(first)
    assert elements == LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4])

    delete_node(elements)
    assert elements == LinkedListNode.create_linked_list_from_iterable([2, 3, 4])

    assert delete_node(elements.next.next) is False
    assert elements == LinkedListNode.create_linked_list_from_iterable([2, 3, 4])



