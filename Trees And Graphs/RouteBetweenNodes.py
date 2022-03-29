# 1 - Given a directed graph and two nodes, design an algorithm to find out whether there is a route from the first to
# the second.
import collections

from utils.collections.graph import AbstractGraph, Graph
from typing import TypeVar, Protocol, Any
from abc import abstractmethod


class SupportsEqual(Protocol):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass


T = TypeVar('T', bound=SupportsEqual)


def route(graph: AbstractGraph[T, Any, Any], source: T, destination: T) -> bool:
    # Simple BFS
    queue = collections.deque()

    visited = set()
    queue.append(source)
    while len(queue) > 0:
        current = queue.popleft()
        if current == destination:
            return True
        visited.add(current)
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.append(neighbor)

    return False


def test_route():
    graph: AbstractGraph[int] = Graph(directed=True)

    source = 1
    destination = 8

    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)
    graph.add_edge(7, 8)

    assert route(graph, source, destination) is True

    graph.remove_edge(7, 8)
    assert route(graph, source, destination) is False



