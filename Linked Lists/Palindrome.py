# 6 - Write a function that checks if a linked list is a palindrome.
from abc import abstractmethod
from typing import Protocol, TypeVar

from utils.collections.linkedlist import LinkedListNode


class SupportsEqual(Protocol):
    @abstractmethod
    def __eq__(self, other):
        pass


ET = TypeVar('ET', bound=SupportsEqual)


def middle(head: LinkedListNode) -> LinkedListNode:
    current = head
    runner = head

    while runner is not None and runner.next is not None:
        current = current.next
        runner = runner.next.next

    return current


def is_palindrome(head: LinkedListNode[ET]) -> bool:
    middle_element = middle(head)
    # Invert the second part of the list using a stack
    second_part_stack = []
    current_second = middle_element
    while current_second is not None:
        second_part_stack.append(current_second)
        current_second = current_second.next

    current_first = head
    while current_first is not middle_element and len(second_part_stack) > 0:
        current_second = second_part_stack.pop()

        if current_first.data != current_second.data:
            return False

        current_first = current_first.next

    return True


def test_is_palindrome():
    palindrome = LinkedListNode.create_linked_list_from_iterable([1, 2, 1])
    assert is_palindrome(palindrome)

    palindrome = LinkedListNode.create_linked_list_from_iterable([1, 2, 2, 1])
    assert is_palindrome(palindrome)

    palindrome = LinkedListNode.create_linked_list_from_iterable([8, 'a', 'a', 8])
    assert is_palindrome(palindrome)

    not_palindrome = LinkedListNode.create_linked_list_from_iterable([1, 2, 3, 1])
    assert not is_palindrome(not_palindrome)
