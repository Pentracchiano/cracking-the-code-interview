# https://leetcode.com/problems/network-delay-time/

import typing
import collections
import math
import heapq
import numbers

Node = int
Time = numbers.Number


class NodeWithTime(typing.NamedTuple):
    time: Time
    node: Node


class Edge(typing.NamedTuple):
    destination: Node
    time: Time


MAXTIME: typing.Final[Time] = math.inf  # Could be something around 100 * 100 (n * w), but let's not be smart for no reason


class Solution:
    def networkDelayTime(self, times: typing.List[typing.List[int]], n: int, k: int) -> int:
        edges: typing.Dict[Node, typing.List[Edge]] = collections.defaultdict(list)

        for source, destination, time in times:
            edge = Edge(destination=destination, time=time)
            edges[source].append(edge)

        priority_queue = [NodeWithTime(node=k, time=0)]
        timings = collections.defaultdict(lambda: MAXTIME)  # Assuming no node will ever have an edge with MAXTIME.

        timings[k] = 0
        while len(priority_queue) > 0:
            timing_to_current, node = heapq.heappop(priority_queue)

            for neighbor, timing_to_neighbor in edges[node]:
                total_time_to_neighbor = timing_to_current + timing_to_neighbor
                if total_time_to_neighbor < timings[neighbor]:
                    timings[neighbor] = total_time_to_neighbor
                    heapq.heappush(priority_queue, NodeWithTime(node=neighbor, time=total_time_to_neighbor))

        if len(timings) < n:
            return -1

        return max(timings.values())
