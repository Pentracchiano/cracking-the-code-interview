# 2 - How would you design a stack which, in addition to push and pop, would also have a function that returns
# the minimum element? All of these 3 functions should operate in O(1) time.
from typing import Generic, TypeVar, Protocol, List

import pytest


class Comparable(Protocol):
    def __lt__(self, other) -> bool:
        pass


CT = TypeVar('CT', bound=Comparable)


class StackElement(Generic[CT]):
    def __init__(self, data: CT):
        self.data: CT = data
        self.min_of_substack: CT = data


class EmptyStack(IndexError):
    pass


class StackMin(Generic[CT]):
    def __init__(self):
        self._elements: List[StackElement[CT]] = []

    @property
    def _last_stack_element(self) -> StackElement[CT]:
        # Internally throws if not checked
        return self._elements[-1]

    def push(self, data: CT) -> None:
        new_element = StackElement(data)
        if len(self) > 0:
            last_min = self._last_stack_element.min_of_substack
            if last_min < new_element.min_of_substack:
                new_element.min_of_substack = last_min
        self._elements.append(new_element)

    def pop(self) -> CT:
        if len(self) == 0:
            raise EmptyStack
        return self._elements.pop().data

    def peek(self) -> CT:
        if len(self) == 0:
            raise EmptyStack
        return self._last_stack_element.data

    def min(self) -> CT:
        if len(self) == 0:
            raise EmptyStack
        return self._last_stack_element.min_of_substack

    def __len__(self) -> int:
        return len(self._elements)


class StackMinEfficient(Generic[CT]):
    def __init__(self):
        self._stack: List[CT] = []
        self._min_stack: List[CT] = []

    def push(self, data: CT) -> None:
        self._stack.append(data)
        if len(self._min_stack) == 0 or data < self._min_stack[-1]:
            self._min_stack.append(data)

    def pop(self) -> CT:
        if len(self) == 0:
            raise EmptyStack
        value = self._stack.pop()
        if value == self._min_stack[-1]:
            self._min_stack.pop()
        return value

    def peek(self) -> CT:
        if len(self) == 0:
            raise EmptyStack
        return self._stack[-1]

    def min(self) -> CT:
        if len(self) == 0:
            raise EmptyStack
        return self._min_stack[-1]

    def __len__(self) -> int:
        return len(self._stack)


@pytest.mark.parametrize('StackClass', [StackMin[int], StackMinEfficient[int]])
def test_stack(StackClass):
    stack = StackClass()

    stack.push(5)
    stack.push(1)
    stack.push(3)

    assert len(stack) == 3
    assert stack.peek() == 3
    assert stack.min() == 1

    assert stack.pop() == 3
    assert len(stack) == 2
    assert stack.peek() == 1
    assert stack.min() == 1

    assert stack.pop() == 1
    assert len(stack) == 1
    assert stack.min() == 5
    assert stack.peek() == 5

    assert stack.pop() == 5

    assert len(stack) == 0
    with pytest.raises(EmptyStack):
        stack.pop()
    with pytest.raises(EmptyStack):
        stack.peek()
    with pytest.raises(EmptyStack):
        stack.min()

