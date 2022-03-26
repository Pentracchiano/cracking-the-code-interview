# 1 - Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: How would you solve the problem if a temporary buffer is not allowed?
from utils.collections.linkedlist import LinkedListNode


def remove_duplicates(head: LinkedListNode):
    unique_data = set()

    current = head
    previous = None
    while current is not None:
        if current.data in unique_data:
            previous.next = current.next
        else:
            unique_data.add(current.data)
            previous = current
        current = current.next


def remove_duplicates_no_buffer(head: LinkedListNode):
    current = head
    while current is not None:
        # I have to check forwards for duplicates
        previous = current
        candidate_duplicate = current.next
        while candidate_duplicate is not None:
            if candidate_duplicate.data == current.data:
                previous.next = candidate_duplicate.next
            else:
                previous = candidate_duplicate
            candidate_duplicate = candidate_duplicate.next

        current = current.next


def test_remove_duplicates():
    elements = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4, 4, 2, 1, 9])
    expected = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4, 9])

    remove_duplicates(elements)

    assert elements == expected

    elements = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4, 9])
    expected = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4, 9])

    remove_duplicates(elements)

    assert elements == expected


def test_remove_duplicates_no_buffer():
    elements = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4, 4, 2, 1, 9])
    expected = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4, 9])

    remove_duplicates_no_buffer(elements)
    assert elements == expected

    elements = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4, 9])
    expected = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 4, 9])

    remove_duplicates_no_buffer(elements)
    assert elements == expected
