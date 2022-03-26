from utils.collections.linkedlist import LinkedListNode


def test_create_linked_list_from_iterable():
    a = LinkedListNode.create_linked_list_from_iterable(range(10))

    b = LinkedListNode(data=0)
    current = b
    for i in range(1, 10):
        current.next = LinkedListNode(data=i)
        current = current.next

    current_a = a
    current_b = b
    while current_a is not None:
        assert current_a.data == current_b.data
        current_a = current_a.next
        current_b = current_b.next

    assert current_b is None


def test_equality():
    a = LinkedListNode.create_linked_list_from_iterable(range(10))
    b = LinkedListNode.create_linked_list_from_iterable(range(10))
    print(a, b)

    assert a == b




