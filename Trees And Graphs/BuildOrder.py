# 7 - You are given a list of projects and a list of dependencies
# (which is a list of pairs of projects, where the second project is dependent on the first project)
# All of a project's dependencies must be built before the project is. Find a build order that will allow the projects
# to be built. If there is no valid build order, return an error.
import typing
import collections
from utils.collections.graph import Graph, AbstractGraph


class Project(typing.NamedTuple):
    id: int
    name: str


class Dependency(typing.NamedTuple):
    father: Project
    child: Project


def projects_build(projects: typing.Sequence[Project], dependencies: typing.Sequence[Dependency]) -> typing.Sequence[Project] | None:
    dependency_graph: AbstractGraph[Project] = Graph(directed=True)

    for project in projects:
        dependency_graph.add_node(project)
    for dependency in dependencies:
        dependency_graph.add_edge(dependency.father, dependency.child)

    queue: typing.Deque[Project] = collections.deque()

    # can't remove edges during iterations!
    in_degrees: typing.Dict[Project, int] = {}
    for project in dependency_graph.nodes:
        current_in_degree = dependency_graph.in_degree(project)
        if current_in_degree == 0:
            queue.append(project)
        else:
            in_degrees[project] = current_in_degree

    build: typing.List[Project] = []
    while len(queue) > 0:
        project = queue.popleft()

        build.append(project)
        for child in dependency_graph.neighbors(project):
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                queue.append(child)
                del in_degrees[child]

    if len(build) != len(projects):
        return None

    return build


