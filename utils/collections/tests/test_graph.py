import pytest
from utils.collections.graph import Graph, AbstractGraph


def test_undirected_graph():
    graph: AbstractGraph[int] = Graph(directed=False)

    graph.add_edge(3, 4)
    graph.add_edge(3, 8)
    graph.add_edge(9, 3)
    graph.add_edge(5, 8)

    assert graph.adjacent(3, 4)
    assert graph.adjacent(4, 3)

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
    assert graph.get_edge_weight(4, 3) == 50

    with pytest.raises(KeyError):
        graph.get_edge_weight(42, 58)

    with pytest.raises(KeyError):
        graph.get_edge_weight(5, 3)

    with pytest.raises(KeyError):
        graph.set_edge_weight(42, 58, 10000)

    with pytest.raises(KeyError):
        graph.get_node_value(42)

    with pytest.raises(KeyError):
        graph.set_node_value(99, 199)

    with pytest.raises(KeyError):
        next(graph.neighbors(32))

    with pytest.raises(KeyError):
        graph.adjacent(98, 3)

    with pytest.raises(KeyError):
        graph.remove_edge(42, 3)

    with pytest.raises(KeyError):
        graph.remove_node(42)

    graph.remove_edge(3, 4)
    assert not graph.adjacent(3, 4)
    assert not graph.adjacent(4, 3)

    graph.remove_node(3)
    assert not graph.adjacent(9, 3)

    with pytest.raises(KeyError):
        graph.adjacent(3, 9)

    with pytest.raises(KeyError):
        graph.get_node_value(3)


def test_directed_graph():
    graph: AbstractGraph[int] = Graph(directed=True)

    graph.add_edge(3, 4)
    graph.add_edge(3, 8)
    graph.add_edge(9, 3)
    graph.add_edge(5, 8)
    graph.add_edge(8, 5)

    assert graph.adjacent(3, 4)
    assert not graph.adjacent(4, 3)

    neighbors = graph.neighbors(3)
    assert next(neighbors) == 4
    assert next(neighbors) == 8
    with pytest.raises(StopIteration):
        next(neighbors)

    edges = graph.edges
    assert next(edges) == (3, 4)
    assert next(edges) == (3, 8)
    assert next(edges) == (9, 3)
    assert next(edges) == (5, 8)
    assert next(edges) == (8, 5)

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

    graph.set_edge_weight(5, 8, 50)
    assert graph.get_edge_weight(5, 8) == 50
    assert graph.get_edge_weight(8, 5) is None

    with pytest.raises(KeyError):
        graph.get_edge_weight(42, 58)

    with pytest.raises(KeyError):
        graph.get_edge_weight(4, 3)

    with pytest.raises(KeyError):
        graph.set_edge_weight(42, 58, 10000)

    with pytest.raises(KeyError):
        graph.get_node_value(42)

    with pytest.raises(KeyError):
        graph.set_node_value(99, 199)

    with pytest.raises(KeyError):
        next(graph.neighbors(32))

    with pytest.raises(KeyError):
        graph.adjacent(98, 3)

    with pytest.raises(KeyError):
        graph.remove_edge(42, 3)

    with pytest.raises(KeyError):
        graph.remove_node(42)

    graph.remove_edge(5, 8)
    assert not graph.adjacent(5, 8)
    assert graph.adjacent(8, 5)

    graph.remove_node(3)
    assert not graph.adjacent(9, 3)

    with pytest.raises(KeyError):
        graph.adjacent(3, 8)

    with pytest.raises(KeyError):
        graph.get_node_value(3)
