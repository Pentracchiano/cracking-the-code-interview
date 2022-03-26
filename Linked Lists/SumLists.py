# 5 - You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function
# that adds the two numbers and returns the sum as a linked list. You are not allowed to "cheat" and just convert
# the linked list to an integer.

# 7 -> 1 -> 6 + 5 -> 9 -> 2 = 2 -> 1 -> 9

# Follow up: the digits are stored in forward order.

# 6 -> 1 -> 7 + 2 -> 9 -> 5 = 9 -> 1 -> 2
import typing
from numbers import Number

from utils.collections.linkedlist import LinkedListNode


def sum_lists(first: LinkedListNode[Number], second: LinkedListNode[Number]) -> LinkedListNode[Number]:
    current_first = first
    current_second = second

    carry = 0
    result = None
    current_result = None
    while current_first is not None or current_second is not None:
        sum = carry
        if current_first:
            sum += current_first.data
        if current_second:
            sum += current_second.data
        carry = 1 if sum >= 10 else 0

        partial_result = LinkedListNode(data=sum % 10)
        if result is None:
            result = partial_result
        else:
            current_result.next = partial_result

        current_result = partial_result
        current_first = current_first.next if current_first else None
        current_second = current_second.next if current_second else None

    if carry:
        current_result.next = LinkedListNode(data=1)

    return result


def linked_list_length(head: LinkedListNode) -> int:
    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next
    return length


def pad_with_zeroes(head: LinkedListNode, amount: int) -> LinkedListNode:
    for i in range(amount):
        new = LinkedListNode(data=0, next=head)
        head = new
    return head


def sum_lists_forward(addend1: LinkedListNode[Number], addend2: LinkedListNode[Number]) -> LinkedListNode[Number]:
    length_1 = linked_list_length(addend1)
    length_2 = linked_list_length(addend2)

    if length_1 < length_2:
        addend1 = pad_with_zeroes(addend1, length_2 - length_1)
    elif length_2 < length_1:
        addend2 = pad_with_zeroes(addend2, length_1 - length_2)

    result, carry = sum_lists_forward_partial(addend1, addend2, 0, None)
    if carry:
        result = LinkedListNode(data=carry, next=result)

    return result


def sum_lists_forward_partial(addend1: LinkedListNode[Number],
                              addend2: LinkedListNode[Number],
                              carry: Number,
                              partial_result: LinkedListNode[Number] | None) \
        -> typing.Tuple[LinkedListNode[Number], Number]:
    if addend1 is None or addend2 is None:
        return partial_result, 0

    partial_result, carry = sum_lists_forward_partial(addend1.next, addend2.next, carry, partial_result)

    sum = addend1.data + addend2.data + carry
    carry = 1 if sum >= 10 else 0

    return LinkedListNode(next=partial_result, data=sum % 10), carry


def test_sum_lists():
    addend1 = LinkedListNode.create_linked_list_from_iterable([7, 1, 6])
    addend2 = LinkedListNode.create_linked_list_from_iterable([5, 9, 2])
    expected_result = LinkedListNode.create_linked_list_from_iterable([2, 1, 9])

    assert sum_lists(addend1, addend2) == expected_result

    addend1 = LinkedListNode.create_linked_list_from_iterable([1, 6])
    addend2 = LinkedListNode.create_linked_list_from_iterable([5, 9, 9])
    expected_result = LinkedListNode.create_linked_list_from_iterable([6, 5, 0, 1])

    assert sum_lists(addend1, addend2) == expected_result


def test_sum_lists_forward():
    addend1 = LinkedListNode.create_linked_list_from_iterable([6, 1, 7])
    addend2 = LinkedListNode.create_linked_list_from_iterable([2, 9, 5])
    expected_result = LinkedListNode.create_linked_list_from_iterable([9, 1, 2])

    assert sum_lists_forward(addend1, addend2) == expected_result

    addend1 = LinkedListNode.create_linked_list_from_iterable([9, 9, 9])
    addend2 = LinkedListNode.create_linked_list_from_iterable([1, 1, 1, 1])
    expected_result = LinkedListNode.create_linked_list_from_iterable([2, 1, 1, 0])
    result = sum_lists_forward(addend1, addend2)

    assert result == expected_result

    addend1 = LinkedListNode.create_linked_list_from_iterable([9])
    addend2 = LinkedListNode.create_linked_list_from_iterable([1])
    expected_result = LinkedListNode.create_linked_list_from_iterable([1, 0])
    result = sum_lists_forward(addend1, addend2)

    assert result == expected_result
