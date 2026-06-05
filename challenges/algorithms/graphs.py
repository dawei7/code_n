"""Graph algorithms.

The current catalog has two: Graph Representation (turning an edge
list into an adjacency list) and Dijkstra (shortest paths with
positive weights). Future sessions will add BFS, DFS, Bellman-Ford,
Floyd-Warshall, Topological sort, Kruskal, Prim, Tarjan, etc.
"""

from __future__ import annotations

import heapq
import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList


# --- Graph Representation ---


def _setup_graph_representation(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._num_nodes = max(4, n // 2)
    num_edges = n
    challenge._edges = []
    for _ in range(num_edges):
        u = rng.randint(0, challenge._num_nodes - 1)
        v = rng.randint(0, challenge._num_nodes - 1)
        if u != v:
            challenge._edges.append((u, v))

    expected: dict[int, set[int]] = {i: set() for i in range(challenge._num_nodes)}
    for u, v in challenge._edges:
        expected[u].add(v)
        expected[v].add(u)
    challenge._expected = {k: sorted(v) for k, v in expected.items()}

    size = challenge._num_nodes
    challenge.grid = Grid(size, size)
    for u, v in challenge._edges:
        challenge.grid.set(v, u, CellType.PATH, "1")
        challenge.grid.set(u, v, CellType.PATH, "1")

    return {
        "num_nodes": challenge._num_nodes,
        "edges": TrackedList(challenge._edges),
    }


def _verify_graph_representation(challenge, result: Any) -> bool:
    if not isinstance(result, dict):
        return False
    for k, v in challenge._expected.items():
        if k not in result:
            return False
        if sorted(result[k]) != v:
            return False
    return True


GRAPH_01_SOURCE = '''\
"""Optimal solution for graph_01: Graph Representation.

Build an adjacency list from a list of edges. The graph is
undirected, so each edge (u, v) adds v to u's list and u to v's.
The input may contain duplicate edges; using a per-node set
deduplicates them in O(1) each. O(n) where n is the number of
edges.
"""


def solve(num_nodes, edges):
    graph = {i: set() for i in range(num_nodes)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return {node: sorted(neighbors) for node, neighbors in graph.items()}
'''


# --- Dijkstra ---


def _setup_dijkstra(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._num_nodes = max(5, n // 2)
    challenge._start = 0
    challenge._edges = []
    # Spanning tree to guarantee connectivity.
    for i in range(1, challenge._num_nodes):
        parent = rng.randint(0, i - 1)
        weight = rng.randint(1, 20)
        challenge._edges.append((parent, i, weight))
        challenge._edges.append((i, parent, weight))
    # Extra edges for variety.
    for _ in range(n):
        u = rng.randint(0, challenge._num_nodes - 1)
        v = rng.randint(0, challenge._num_nodes - 1)
        if u != v:
            w = rng.randint(1, 20)
            challenge._edges.append((u, v, w))

    challenge._expected_dist = _dijkstra(challenge._num_nodes, challenge._edges, challenge._start)

    size = challenge._num_nodes
    challenge.grid = Grid(size, size)
    adj = [[0] * size for _ in range(size)]
    for u, v, w in challenge._edges:
        if u < size and v < size:
            adj[u][v] = w
    for y in range(min(size, challenge.grid.height)):
        for x in range(min(size, challenge.grid.width)):
            if adj[y][x] > 0:
                challenge.grid.set(x, y, CellType.VALUE, adj[y][x])

    return {
        "num_nodes": challenge._num_nodes,
        "edges": challenge._edges,
        "start": challenge._start,
    }


def _verify_dijkstra(challenge, result: Any) -> bool:
    if not isinstance(result, dict):
        return False
    for k, v in challenge._expected_dist.items():
        if result.get(k) != v:
            return False
    return True


def _dijkstra(num_nodes: int, edges: list[tuple[int, int, int]], start: int) -> dict[int, int]:
    dist: dict[int, float] = {i: float("inf") for i in range(num_nodes)}
    dist[start] = 0
    pq: list[tuple[int, int]] = [(0, start)]
    visited: set[int] = set()
    adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(num_nodes)}
    for u, v, w in edges:
        adj[u].append((v, w))
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return {k: (v if v != float("inf") else -1) for k, v in dist.items()}


GRAPH_04_SOURCE = '''\
"""Optimal solution for graph_04: Dijkstra.

Find shortest paths from `start` to all other nodes using a
min-heap. All edge weights are positive. O((V + E) log V) with
heapq; the simple O(V^2) version also fits the challenge budget
since the V^2 limit is generous enough.
"""


def solve(num_nodes, edges, start):
    import heapq

    # Build adjacency list (one direction; the input is "directed"
    # for the challenge's purposes, even though edges look symmetric).
    adj = {i: [] for i in range(num_nodes)}
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = {i: float("inf") for i in range(num_nodes)}
    dist[start] = 0
    pq = [(0, start)]
    visited = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return {node: (d if d != float("inf") else -1) for node, d in dist.items()}
'''


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="graph_01",
        name="Graph Representation",
        category="graphs",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Given a list of edges, build an adjacency list.\n"
            "Return a dict where each key is a node and the value is a sorted list of neighbors.\n"
            "The graph is undirected.\n"
            "Requirement: O(n) where n = number of edges.\n"
            "Source: https://www.geeksforgeeks.org/graph-and-its-representations/"
        ),
        source_url="https://www.geeksforgeeks.org/graph-and-its-representations/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples representing undirected edges.",
        },
        returns="a dict mapping each node to a sorted list of its neighbors.",
        source=GRAPH_01_SOURCE,
        setup_fn=_setup_graph_representation,
        verify_fn=_verify_graph_representation,
        samples=[
            Sample("num_nodes = 3, edges = [(0, 1), (1, 2)]", "{0: [1], 1: [0, 2], 2: [1]}"),
            Sample("num_nodes = 2, edges = []", "{0: [], 1: []}"),
            Sample("num_nodes = 3, edges = [(0, 2)]", "{0: [2], 1: [], 2: [0]}"),
        ],
        hint="For each edge (u, v), add v to u's list and u to v's list.",
        parents=["intro_01"],
        children=[],
    ),
    AlgorithmSpec(
        id="graph_04",
        name="Dijkstra",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the shortest distance from the start node to all other nodes.\n"
            "The graph has weighted edges (all positive weights).\n"
            "Return a dict mapping each node to its shortest distance from start.\n"
            "Unreachable nodes should have distance -1.\n"
            "Requirement: O(n^2) where n = number of nodes (simple version).\n"
            "Source: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/"
        ),
        source_url="https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/",
        params=["num_nodes", "edges", "start"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v, weight) tuples for directed edges.",
            "start": "source node.",
        },
        returns="a dict mapping each node to its shortest distance from start. Unreachable nodes get -1.",
        source=GRAPH_04_SOURCE,
        setup_fn=_setup_dijkstra,
        verify_fn=_verify_dijkstra,
        samples=[
            Sample("num_nodes = 3, edges = [(0, 1, 5), (1, 2, 3)], start = 0", "{0: 0, 1: 5, 2: 8}"),
            Sample("num_nodes = 2, edges = [], start = 0", "{0: 0, 1: -1}"),
            Sample("num_nodes = 4, edges = [(0, 1, 1), (1, 2, 1), (0, 2, 5)], start = 0", "{0: 0, 1: 1, 2: 2, 3: -1}"),
        ],
        hint="Maintain distances. Repeatedly pick the unvisited node with smallest distance, update neighbors.",
        parents=[],
        children=[],
    ),
]
