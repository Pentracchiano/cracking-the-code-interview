


from typing import TypeVar, List, Protocol
from abc import abstractmethod
import pytest

T = TypeVar('T')


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other):
        raise NotImplementedError


CT = TypeVar('CT', bound=Comparable)

Stack = List[T]


def is_empty(stack: Stack) -> bool:
    return len(stack) == 0


def peek(stack: Stack[T]) -> T:
    return stack[-1]


def pop(stack: Stack[T]) -> T:
    return stack.pop()


def push(stack: Stack[T], data: T):
    stack.append(data)


def sort_stack(stack: Stack[CT]) -> None:
    temporary_stack: Stack[CT] = []
    current_element: CT

    while not is_empty(stack):
        current_element = pop(stack)
        if is_empty(temporary_stack):
            push(temporary_stack, current_element)
        else:
            temporary_element = peek(temporary_stack)
            # since we are using the original stack in support of temporary one, we keep track of how much we used
            temporary_elements_in_original_stack = 0
            while temporary_element > current_element:
                push(stack, pop(temporary_stack))
                temporary_elements_in_original_stack += 1

                temporary_element = peek(temporary_stack)

            push(temporary_stack, current_element)

            while temporary_elements_in_original_stack > 0:
                push(temporary_stack, pop(stack))
                temporary_elements_in_original_stack -= 1

    while not is_empty(temporary_stack):
        push(stack, pop(temporary_stack))


def cleaner_sort_stack(stack: Stack[CT]) -> None:
    temporary_stack = []

    while not is_empty(stack):
        current_element = pop(stack)
        while not is_empty(temporary_stack) and peek(temporary_stack) > current_element:
            push(stack, pop(temporary_stack))
        push(temporary_stack, current_element)

    while not is_empty(temporary_stack):
        push(stack, pop(temporary_stack))


@pytest.mark.parametrize('sorting_function', [sort_stack, cleaner_sort_stack])
def test_sort_stack(sorting_function):
    stack = []
    push(stack, 5)
    push(stack, 3)
    push(stack, 8)
    push(stack, 11)
    push(stack, 3)

    expected = sorted(stack, reverse=True)

    sorting_function(stack)
    assert stack == expected

