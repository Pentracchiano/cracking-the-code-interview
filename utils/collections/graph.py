import typing
from abc import ABC, abstractmethod
from collections import defaultdict

T = typing.TypeVar('T', bound=typing.Hashable)  # node type
V = typing.TypeVar('V')  # node value type
W = typing.TypeVar('W')  # edge weight type


def Graph(directed: bool = False) -> 'AbstractGraph[T, V, W]':
    return AdjacencyListGraph(directed)


class AbstractGraph(ABC, typing.Generic[T, V, W]):
    directed: typing.Final[bool]

    def __init__(self, directed: bool):
        self.directed = directed

    @abstractmethod
    def adjacent(self, x: T, y: T) -> bool:
        pass

    @abstractmethod
    def neighbors(self, x: T) -> typing.Sequence[T]:
        pass

    @abstractmethod
    def add_node(self, x: T, value: V = None) -> typing.NoReturn:
        pass

    @abstractmethod
    def add_edge(self, x: T, y: T, weight: W = None) -> typing.NoReturn:
        pass

    @abstractmethod
    def remove_node(self, x: T) -> typing.NoReturn:
        pass

    @abstractmethod
    def remove_edge(self, x: T, y: T) -> typing.NoReturn:
        pass

    @abstractmethod
    def get_node_value(self, x: T) -> V:
        pass

    @abstractmethod
    def get_edge_weight(self, x: T, y: T) -> W:
        pass

    @abstractmethod
    def set_node_value(self, x: T, value: V) -> typing.NoReturn:
        pass

    @abstractmethod
    def set_edge_weight(self, x: T, y: T, weight: W) -> typing.NoReturn:
        pass
    @property
    @abstractmethod
    def nodes(self) -> typing.Iterator[T]:
        pass

    @property
    @abstractmethod
    def edges(self) -> typing.Iterator[typing.Tuple[T, T]]:
        pass


class AdjacencyListGraph(AbstractGraph[T, V, W]):
    _node_to_inbound: typing.Dict[T, typing.Dict[T, W]]
    _node_to_outbound: typing.Dict[T, typing.Dict[T, W]]
    _node_values: typing.Dict[T, V]

    def __init__(self, directed: bool):
        super().__init__(directed)

        self._node_values = {}
        self._node_to_outbound = defaultdict(dict)
        if not directed:
            self._node_to_inbound = self._node_to_outbound
        else:
            self._node_to_inbound = defaultdict(dict)

    def adjacent(self, x: T, y: T) -> bool:
        # The check avoids the inadvertent creation of a node entry
        if x not in self._node_values:
            raise KeyError

        return y in self._node_to_outbound[x]

    def neighbors(self, x: T) -> typing.Iterator[T]:
        # The check avoids the inadvertent creation of a node entry
        if x not in self._node_values:
            raise KeyError
        yield from self._node_to_outbound[x].keys()

    def add_node(self, x: T, value: V = None) -> typing.NoReturn:
        self._node_values[x] = value

    def add_edge(self, x: T, y: T, weight: W = None) -> typing.NoReturn:
        self._node_to_outbound[x][y] = weight
        self._node_to_inbound[y][x] = weight

        # This creates the entries if it's the first time the nodes are inserted in the graph
        # otherwise, the value of the node is left unchanged
        self._node_values.setdefault(x, None)
        self._node_values.setdefault(y, None)

    def remove_node(self, x: T) -> typing.NoReturn:
        outbound = self._node_to_outbound.pop(x, {})
        inbound = self._node_to_inbound.pop(x, {})

        for out_neighbor in outbound.keys():
            self._node_to_inbound[out_neighbor].pop(x)

        # if the graph is not directed, this for will not be executed because inbound = outbound.
        # therefore, the removal of outbound already removed inbound too. No special cases necessary.
        for in_neighbor in inbound.keys():
            self._node_to_outbound[in_neighbor].pop(x)

        del self._node_values[x]

    def remove_edge(self, x: T, y: T) -> typing.NoReturn:
        del self._node_to_outbound[x][y]
        del self._node_to_inbound[y][x]

    def get_node_value(self, x: T) -> V:
        return self._node_values[x]

    def get_edge_weight(self, x: T, y: T) -> W:
        return self._node_to_outbound[x][y]

    def set_edge_weight(self, x: T, y: T, weight: W) -> typing.NoReturn:
        # since this should not create nodes or edges, a check is executed
        if y not in self._node_to_outbound[x] or x not in self._node_to_inbound[y]:
            raise KeyError
        self._node_to_outbound[x][y] = weight
        self._node_to_inbound[y][x] = weight

    def set_node_value(self, x: T, value: V) -> typing.NoReturn:
        # since this should not create nodes, the existence of node is checked for
        if x not in self._node_values:
            raise KeyError
        self._node_values[x] = value

    @property
    def nodes(self) -> typing.Iterator[T]:
        yield from self._node_values.keys()

    @property
    def edges(self) -> typing.Iterator[typing.Tuple[T, T]]:
        for x, neighbors in self._node_to_outbound.items():
            for y in neighbors.keys():
                yield x, y
