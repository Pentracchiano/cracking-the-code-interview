import typing
from abc import ABC, abstractmethod
from collections import defaultdict

T = typing.TypeVar('T', bound=typing.Hashable)  # node type
V = typing.TypeVar('V')  # value type


def Graph(directed: bool = False) -> 'AbstractGraph[T]':
    if directed:
        raise NotImplementedError
    return AdjacencyListUndirectedGraph()


class AbstractGraph(ABC, typing.Generic[T, V]):
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
    def add_edge(self, x: T, y: T, value: V = None) -> typing.NoReturn:
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
    def get_edge_value(self, x: T, y: T) -> V:
        pass

    @property
    @abstractmethod
    def nodes(self) -> typing.Iterator[T]:
        pass

    @property
    @abstractmethod
    def edges(self) -> typing.Iterator[typing.Tuple[T, T]]:
        pass


class AdjacencyListUndirectedGraph(AbstractGraph[T, V]):
    _node_to_neighbors: typing.Dict[T, typing.Dict[T, V]] = defaultdict(dict)
    _node_values: typing.Dict[T, V]

    def adjacent(self, x: T, y: T) -> bool:
        return y in self._node_to_neighbors[x]

    def neighbors(self, x: T) -> typing.Iterator[T]:
        yield from self._node_to_neighbors[x].keys()

    def add_node(self, x: T, value: V = None) -> typing.NoReturn:
        self._node_to_neighbors[x] = {}
        self._node_values[x] = value

    def add_edge(self, x: T, y: T, value: V = None) -> typing.NoReturn:
        self._node_to_neighbors[x][y] = value
        self._node_to_neighbors[y][x] = value

    def remove_node(self, x: T) -> typing.NoReturn:
        for neighbors in self._node_to_neighbors:
            if x in neighbors:
                del neighbors[x]

        del self._node_to_neighbors[x]
        del self._node_values[x]

    def remove_edge(self, x: T, y: T) -> typing.NoReturn:
        del self._node_to_neighbors[x][y]
        del self._node_to_neighbors[y][x]

    def get_node_value(self, x: T) -> V:
        return self._node_values[x]

    def get_edge_value(self, x: T, y: T) -> V:
        return self._node_to_neighbors[x][y]

    @property
    def nodes(self) -> typing.Iterator[T]:
        yield from self._node_to_neighbors.keys()

    @property
    def edges(self) -> typing.Iterator[typing.Tuple[T, T]]:
        # it returns both (x, y) and (y, x)
        for x, x_neighbors in self._node_to_neighbors.items():
            for y in x_neighbors.keys():
                yield x, y

