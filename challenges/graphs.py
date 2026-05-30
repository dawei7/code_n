"""Graph algorithm challenges."""

import random
from typing import Any, Optional

from code_n.challenge import Challenge, ChallengeInfo
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList, TrackedGrid, TrackedQueue, TrackedSet


class GraphRepresentationChallenge(Challenge):
    """Build an adjacency list from edge data on a grid."""

    def __init__(self):
        super().__init__()
        self._edges: list[tuple[int, int]] = []
        self._num_nodes: int = 0
        self._expected: dict[int, list[int]] = {}

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="graph_01",
            name="Graph Representation",
            description=(
                "Given a list of edges, build an adjacency list.\n"
                "Return a dict where each key is a node and the value is a sorted list of neighbors.\n"
                "The graph is undirected.\n"
                "Requirement: O(n) where n = number of edges."
            ),
            category="graphs",
            difficulty=2,
            required_complexity=ComplexityClass.O_N,
            hint="For each edge (u, v), add v to u's list and u to v's list.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._num_nodes = max(4, n // 2)
        num_edges = n

        self._edges = []
        for _ in range(num_edges):
            u = rng.randint(0, self._num_nodes - 1)
            v = rng.randint(0, self._num_nodes - 1)
            if u != v:
                self._edges.append((u, v))

        # Build expected
        self._expected = {i: set() for i in range(self._num_nodes)}
        for u, v in self._edges:
            self._expected[u].add(v)
            self._expected[v].add(u)
        self._expected = {k: sorted(v) for k, v in self._expected.items()}

        # Visualize as grid
        size = self._num_nodes
        self.grid = Grid(size, size)
        for u, v in self._edges:
            self.grid.set(v, u, CellType.PATH, "1")
            self.grid.set(u, v, CellType.PATH, "1")

        return {
            "num_nodes": self._num_nodes,
            "edges": TrackedList(self._edges),
        }

    def verify(self, result: Any) -> bool:
        if not isinstance(result, dict):
            return False
        for k, v in self._expected.items():
            if k not in result:
                return False
            if sorted(result[k]) != v:
                return False
        return True


class DijkstraChallenge(Challenge):
    """Find shortest paths in a weighted graph."""

    def __init__(self):
        super().__init__()
        self._num_nodes: int = 0
        self._edges: list[tuple[int, int, int]] = []
        self._start: int = 0
        self._expected_dist: dict[int, int] = {}

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="graph_04",
            name="Dijkstra",
            description=(
                "Find the shortest distance from the start node to all other nodes.\n"
                "The graph has weighted edges (all positive weights).\n"
                "Return a dict mapping each node to its shortest distance from start.\n"
                "Unreachable nodes should have distance -1.\n"
                "Requirement: O(n²) where n = number of nodes (simple version)."
            ),
            category="graphs",
            difficulty=6,
            required_complexity=ComplexityClass.O_N2,
            hint="Maintain distances. Repeatedly pick the unvisited node with smallest distance, update neighbors.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._num_nodes = max(5, n // 2)
        self._start = 0

        # Generate a connected weighted graph
        self._edges = []
        # Ensure connectivity with a spanning tree
        for i in range(1, self._num_nodes):
            parent = rng.randint(0, i - 1)
            weight = rng.randint(1, 20)
            self._edges.append((parent, i, weight))
            self._edges.append((i, parent, weight))

        # Add extra edges
        for _ in range(n):
            u = rng.randint(0, self._num_nodes - 1)
            v = rng.randint(0, self._num_nodes - 1)
            if u != v:
                w = rng.randint(1, 20)
                self._edges.append((u, v, w))

        # Compute expected distances
        self._expected_dist = self._dijkstra()

        # Visualize as distance grid
        size = self._num_nodes
        self.grid = Grid(size, size)
        adj = [[0] * size for _ in range(size)]
        for u, v, w in self._edges:
            if u < size and v < size:
                adj[u][v] = w
        for y in range(min(size, self.grid.height)):
            for x in range(min(size, self.grid.width)):
                if adj[y][x] > 0:
                    self.grid.set(x, y, CellType.VALUE, adj[y][x])

        return {
            "num_nodes": self._num_nodes,
            "edges": self._edges,
            "start": self._start,
        }

    def _dijkstra(self) -> dict[int, int]:
        import heapq
        dist = {i: float("inf") for i in range(self._num_nodes)}
        dist[self._start] = 0
        pq = [(0, self._start)]
        visited = set()

        adj = {i: [] for i in range(self._num_nodes)}
        for u, v, w in self._edges:
            adj[u].append((v, w))

        while pq:
            d, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            for v, w in adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        return {k: (v if v != float("inf") else -1) for k, v in dist.items()}

    def verify(self, result: Any) -> bool:
        if not isinstance(result, dict):
            return False
        for k, v in self._expected_dist.items():
            if result.get(k) != v:
                return False
        return True
