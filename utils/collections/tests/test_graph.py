import pytest

from utils.collections.graph import Graph, AbstractGraph


def test_undirected_graph():
    graph: AbstractGraph[int] = Graph(directed=False)

    graph.add_edge(3, 4)
    graph.add_edge(3, 8)
    graph.add_edge(9, 3)
    graph.add_edge(5, 8)

    neighbors = graph.neighbors(3)
    assert next(neighbors) == 4
    assert next(neighbors) == 8
    assert next(neighbors) == 9
    with pytest.raises(StopIteration):
        next(neighbors)

    edges = graph.edges
    assert next(edges) == (3, 4)
    assert next(edges) == (3, 8)
    assert next(edges) == (3, 9)
    assert next(edges) == (4, 3)
    assert next(edges) == (8, 3)
    assert next(edges) == (8, 5)
    assert next(edges) == (9, 3)
    assert next(edges) == (5, 8)
    with pytest.raises(StopIteration):
        next(edges)

    nodes = graph.nodes
    assert next(nodes) == 3
    assert next(nodes) == 4
    assert next(nodes) == 8
    assert next(nodes) == 9
    assert next(nodes) == 5
    with pytest.raises(StopIteration):
        next(nodes)

    assert graph.get_edge_weight(3, 4) is None
    assert graph.get_node_value(8) is None

    graph.set_node_value(3, 50)
    assert graph.get_node_value(3) == 50

    graph.set_edge_weight(3, 4, 50)
    assert graph.get_edge_weight(3, 4) == 50


def test_directed_graph():
    graph: AbstractGraph[int] = Graph(directed=True)
