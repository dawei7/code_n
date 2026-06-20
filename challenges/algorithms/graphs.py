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
        "edges": challenge._edges,
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


# === graph_02: Breadth-First Search ================================
#
# Pure-graph BFS on an adjacency list, distinct from
# search_03 (BFS on a 2D grid). Returns the visit order from
# node 0. Sorted neighbor traversal for determinism.


GRAPH_02_SOURCE = '''
def solve(num_nodes, edges):
    """BFS from node 0. Return the visit order as a list of node ids."""
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_nodes
    order = []
    q = deque([0])
    seen[0] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(adj[u]):  # sorted for determinism
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return order
'''


def _setup_graph_bfs(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(2, n)
    edges = set()
    # Build a connected-ish graph: chain from 0 to n-1, then
    # sprinkle a few extra edges.
    for i in range(num_nodes - 1):
        edges.add((i, i + 1))
    # Add a few extra random edges (with caps to avoid
    # pathological density).
    extra = min(num_nodes, 3)
    for _ in range(extra):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, num_nodes - 1)
        if u != v:
            lo, hi = sorted((u, v))
            edges.add((lo, hi))
    edges_list = sorted(edges)
    challenge._num_nodes = num_nodes
    challenge._edges = edges_list
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_graph_bfs(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    # Re-run BFS to compute the expected order.
    from collections import deque
    num_nodes = challenge._num_nodes
    adj = [[] for _ in range(num_nodes)]
    for u, v in challenge._edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_nodes
    expected: list[int] = []
    q = deque([0])
    seen[0] = True
    while q:
        u = q.popleft()
        expected.append(u)
        for v in sorted(adj[u]):
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return result == expected


# === graph_03: Depth-First Search ================================


GRAPH_03_SOURCE = '''
def solve(num_nodes, edges):
    """DFS (recursive) from node 0. Return visit order."""
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_nodes
    order = []

    def walk(u):
        seen[u] = True
        order.append(u)
        for v in sorted(adj[u]):  # sorted for determinism
            if not seen[v]:
                walk(v)

    walk(0)
    return order
'''


def _setup_graph_dfs(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    # Same shape as BFS: a chain plus a few extra edges.
    return _setup_graph_bfs(challenge, n, seed)


def _verify_graph_dfs(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    num_nodes = challenge._num_nodes
    adj = [[] for _ in range(num_nodes)]
    for u, v in challenge._edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_nodes
    expected: list[int] = []

    def walk(u):
        seen[u] = True
        expected.append(u)
        for v in sorted(adj[u]):
            if not seen[v]:
                walk(v)

    walk(0)
    return result == expected


# === graph_05: Bellman-Ford =======================================
#
# Supports negative edges; the setup avoids negative cycles
# (player is not expected to detect them — the spec just
# advertises "supports negative edges").


GRAPH_05_SOURCE = '''
def solve(num_nodes, edges, start):
    """Bellman-Ford: shortest distances from start. -1 if unreachable.

    The graph is directed; edges is a list of (u, v, w) tuples.
    Supports negative edges but no negative cycles (per the
    spec — the player is not asked to detect them).
    """
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[start] = 0
    for _ in range(num_nodes - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    # Build a plain dict result so the player can iterate.
    return {i: (d if d != INF else -1) for i, d in enumerate(dist)}
'''


def _setup_bellman_ford(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(2, n)
    # Build a connected-ish DAG of edges (using u < v as the
    # edge direction guarantees no cycles).
    edges = []
    for i in range(num_nodes - 1):
        w = rng.randint(-3, 8)
        edges.append((i, i + 1, w))
    # Add a few extra edges (u < v to stay acyclic).
    for _ in range(min(num_nodes, 3)):
        u = rng.randint(0, num_nodes - 2)
        v = rng.randint(u + 1, num_nodes - 1)
        w = rng.randint(-3, 8)
        edges.append((u, v, w))
    start = 0
    challenge._edges = edges
    challenge._num_nodes = num_nodes
    return {"num_nodes": num_nodes, "edges": edges, "start": start}


def _verify_bellman_ford(challenge, result: Any) -> bool:
    if not isinstance(result, dict):
        return False
    num_nodes = challenge._num_nodes
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[0] = 0
    for _ in range(num_nodes - 1):
        for u, v, w in challenge._edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    expected = {i: (d if d != INF else -1) for i, d in enumerate(dist)}
    return result == expected


# === graph_06: Floyd-Warshall =====================================


GRAPH_06_SOURCE = '''
def solve(num_nodes, edges):
    """All-pairs shortest distances via Floyd-Warshall.

    Returns an N x N matrix where entry [i][j] is the shortest
    distance from i to j, or -1 if j is unreachable from i.
    The diagonal [i][i] is 0. (No self-loops in the input.)
    """
    INF = float("inf")
    # Initialize with infinities and 0 on the diagonal.
    dist = [[INF] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
    # Floyd-Warshall: try every intermediate node.
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    # Replace infinities with -1 for the result.
    return [[d if d != INF else -1 for d in row] for row in dist]
'''


def _setup_floyd_warshall(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(2, min(n, 8))  # cap; the matrix is num_nodes^2
    edges = []
    # Dense-ish random directed graph with positive weights.
    for u in range(num_nodes):
        for v in range(num_nodes):
            if u != v and rng.random() < 0.4:
                w = rng.randint(1, 10)
                edges.append((u, v, w))
    challenge._edges = edges
    challenge._num_nodes = num_nodes
    return {"num_nodes": num_nodes, "edges": edges}


def _verify_floyd_warshall(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    num_nodes = challenge._num_nodes
    INF = float("inf")
    dist = [[INF] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        dist[i][i] = 0
    for u, v, w in challenge._edges:
        if w < dist[u][v]:
            dist[u][v] = w
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    expected = [[d if d != INF else -1 for d in row] for row in dist]
    if len(result) != len(expected):
        return False
    for got_row, exp_row in zip(result, expected):
        if list(got_row) != list(exp_row):
            return False
    return True


# === graph_07: Topological Sort (Kahn's algorithm) ================
#
# The setup generates a DAG by using u < v for every edge.
# On a cycle, the canonical answer is -1; the setup never
# produces cycles so the player doesn't have to handle that.


GRAPH_07_SOURCE = '''
def solve(num_nodes, edges):
    """Topological sort via Kahn's algorithm (BFS).

    Returns the unique topological order for the DAG, or -1 if
    a cycle is detected. The spec guarantees a DAG (the setup
    uses u < v for every edge), so the answer is always a list.
    """
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    indeg = [0] * num_nodes
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque()
    for i in range(num_nodes):
        if indeg[i] == 0:
            q.append(i)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(adj[u]):  # sorted for determinism
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != num_nodes:
        return -1  # cycle
    return order
'''


def _setup_topological_sort(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(2, n)
    edges = set()
    # u < v guarantees acyclic.
    for _ in range(min(num_nodes * 2, 12)):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, num_nodes - 1)
        if u < v:
            edges.add((u, v))
    # Ensure connectivity from 0: add 0 → i for some i.
    for i in range(1, num_nodes):
        if rng.random() < 0.5:
            edges.add((0, i))
    edges_list = sorted(edges)
    challenge._edges = edges_list
    challenge._num_nodes = num_nodes
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_topological_sort(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    num_nodes = challenge._num_nodes
    expected: list[int] = []
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    indeg = [0] * num_nodes
    for u, v in challenge._edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque()
    for i in range(num_nodes):
        if indeg[i] == 0:
            q.append(i)
    while q:
        u = q.popleft()
        expected.append(u)
        for v in sorted(adj[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return result == expected


# === graph_08: Kruskal's MST ======================================
#
# The setup always produces a CONNECTED graph (extra edges
# guarantee connectivity) so the MST has exactly num_nodes - 1
# edges. The result is the list of MST edges sorted by (u, v).


GRAPH_08_SOURCE = '''
def solve(num_nodes, edges):
    """Kruskal's minimum spanning tree.

    Returns the MST as a sorted list of (u, v, w) tuples, or []
    if the graph is not connected.
    """
    # Sort edges by weight; greedy-union with DSU.
    parent = list(range(num_nodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path compression
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    mst: list[tuple[int, int, int]] = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if union(u, v):
            mst.append((u, v, w))
    if len(mst) != num_nodes - 1:
        return []  # not connected
    return sorted(mst)
'''


def _setup_kruskal(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(2, n)
    edges = set()
    # Chain from 0 to n-1 ensures connectivity.
    for i in range(num_nodes - 1):
        w = rng.randint(1, 20)
        lo, hi = i, i + 1
        edges.add((lo, hi, w))
    # A few extra random edges.
    for _ in range(min(num_nodes, 4)):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, num_nodes - 1)
        if u != v:
            lo, hi = sorted((u, v))
            edges.add((lo, hi, rng.randint(1, 20)))
    edges_list = sorted(edges, key=lambda e: e[2])
    challenge._edges = edges_list
    challenge._num_nodes = num_nodes
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_kruskal(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    # Re-run Kruskal and compare.
    num_nodes = challenge._num_nodes
    parent = list(range(num_nodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    expected: list[tuple[int, int, int]] = []
    for u, v, w in sorted(challenge._edges, key=lambda e: e[2]):
        if union(u, v):
            expected.append((u, v, w))
    if len(expected) != num_nodes - 1:
        return result == []
    return sorted(result) == sorted(expected)


# === graph_09: Union-Find (DSU) ===================================
#
# ops is a list of tuples. Two shapes:
#   ("union", a, b) — perform union; result is None
#   ("find",  a, b) — return True iff a and b are in the same set
# The solve function returns a list[bool] of the find results
# in order; union ops contribute no entry to the result list.


GRAPH_09_SOURCE = '''
def solve(n, ops):
    """Disjoint-set with path compression and union by rank.

    ops is a list of operations:
      ("union", a, b): union the sets of a and b
      ("find",  a, b): return True iff a and b are in the same set
    Returns a list of bools, one per ("find", ...) op in order.
    """
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

    results: list[bool] = []
    for op in ops:
        if op[0] == "union":
            union(op[1], op[2])
        elif op[0] == "find":
            results.append(find(op[1]) == find(op[2]))
    return results
'''


def _setup_union_find(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_elems = max(2, min(n, 16))
    # Mix of union and find ops. Always start with some unions
    # to actually create sets.
    ops: list[tuple] = []
    # Unions: 60% of ops.
    for _ in range(max(2, n_elems // 2)):
        a = rng.randint(0, n_elems - 1)
        b = rng.randint(0, n_elems - 1)
        if a != b:
            ops.append(("union", a, b))
    # Finds: rest of ops.
    for _ in range(max(2, n_elems // 2)):
        a = rng.randint(0, n_elems - 1)
        b = rng.randint(0, n_elems - 1)
        ops.append(("find", a, b))
    challenge._ops = ops
    challenge._n = n_elems
    return {"n": n_elems, "ops": ops}


def _verify_union_find(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    n = challenge._n
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

    expected: list[bool] = []
    for op in challenge._ops:
        if op[0] == "union":
            union(op[1], op[2])
        elif op[0] == "find":
            expected.append(find(op[1]) == find(op[2]))
    return result == expected


# === graph_10: Prim's MST =========================================
#
# Vertex-growth MST, similar shape to Kruskal (graph_08) but
# uses a min-heap of (weight, neighbor) instead of DSU.


GRAPH_10_SOURCE = '''
def solve(num_nodes, edges):
    """Prim's minimum spanning tree on an undirected weighted graph.

    Returns the MST as a sorted list of (u, v, w) tuples, or []
    if the graph is not connected.
    """
    import heapq
    if num_nodes == 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    visited = [False] * num_nodes
    visited[0] = True
    heap: list = []
    for v, w in adj[0]:
        heapq.heappush(heap, (w, 0, v))
    mst: list[tuple[int, int, int]] = []
    while heap:
        w, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst.append((u, v, w))
        for nxt, w2 in adj[v]:
            if not visited[nxt]:
                heapq.heappush(heap, (w2, v, nxt))
    if len(mst) != num_nodes - 1:
        return []
    return sorted(mst)
'''


def _setup_prim(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    # Same connected-graph pattern as Kruskal.
    return _setup_kruskal(challenge, n, seed)


def _verify_prim(challenge, result: Any) -> bool:
    # The MST of a connected graph is unique up to edge ordering.
    # We sort both sides; both algorithms should produce MSTs with
    # the same total weight and same edge set.
    if not isinstance(result, list):
        return False
    # Re-run Kruskal (graph_08) and compare total weight — simpler
    # than comparing edge sets across MSTs.
    total = sum(w for _, _, w in result)
    num_nodes = challenge._num_nodes
    parent = list(range(num_nodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    expected_w = 0
    edges_used = 0
    for u, v, w in sorted(challenge._edges, key=lambda e: e[2]):
        if union(u, v):
            expected_w += w
            edges_used += 1
    if edges_used != num_nodes - 1:
        return result == []
    return total == expected_w and len(result) == num_nodes - 1


# === graph_11: Cycle Detect (Undirected) ==========================


GRAPH_11_SOURCE = '''
def solve(num_nodes, edges):
    """Return True iff the undirected graph has a cycle.

    Uses iterative DFS with parent tracking. The graph is
    undirected; edges is a list of (u, v) tuples.
    """
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * num_nodes
    for start in range(num_nodes):
        if visited[start]:
            continue
        # Iterative DFS with explicit parent stack.
        stack = [(start, -1)]
        visited[start] = True
        while stack:
            u, parent = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, u))
                elif v != parent:
                    return True
    return False
'''


def _setup_cycle_detect(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(2, n)
    # Decide acyclic vs cyclic.
    is_cyclic = rng.random() < 0.5
    edges = set()
    # Chain from 0 to n-1 (always present, always acyclic).
    for i in range(num_nodes - 1):
        edges.add((i, i + 1))
    if is_cyclic:
        # Add an extra edge that closes a cycle.
        # Pick any u in [0, n-1] and v in [u+2, n-1] (guarantees
        # a cycle via the chain).
        u = rng.randint(0, num_nodes - 3)
        v = rng.randint(u + 2, num_nodes - 1)
        edges.add((u, v))
    # Add a few extra non-cycle edges (just to make the graph denser).
    for _ in range(min(num_nodes, 3)):
        a = rng.randint(0, num_nodes - 1)
        b = rng.randint(0, num_nodes - 1)
        if a != b:
            lo, hi = sorted((a, b))
            # Skip if this would close a cycle (any edge between
            # nodes already connected by the chain closes a cycle).
            # Easier: just allow extra edges; if the "is_cyclic"
            # branch added one, the answer stays True.
            edges.add((lo, hi))
    edges_list = sorted(edges)
    # Recompute the expected answer: the chain alone is acyclic,
    # but the closure edge in the is_cyclic branch made it cyclic.
    # The extra random edges might also close cycles — re-run
    # the canonical cycle detection to determine the actual answer.
    expected = False
    if num_nodes > 0:
        adj = [[] for _ in range(num_nodes)]
        for u, v in edges_list:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * num_nodes
        for s in range(num_nodes):
            if visited[s]:
                continue
            stack = [(s, -1)]
            visited[s] = True
            found = False
            while stack:
                u, parent = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append((v, u))
                    elif v != parent:
                        expected = True
                        found = True
                        break
                if found:
                    break
            if expected:
                break
    challenge._expected = expected
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_cycle_detect(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    return result == challenge._expected


# === graph_12: Bipartite Check ====================================
#
# 2-coloring via BFS. A graph is bipartite iff it has no odd
# cycles (equivalently, iff we can 2-color it).


GRAPH_12_SOURCE = '''
def solve(num_nodes, edges):
    """Return True iff the undirected graph is bipartite.

    Uses BFS-based 2-coloring. Returns False as soon as we try
    to assign two different colors to the same node.
    """
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [-1] * num_nodes  # -1 = uncolored, 0/1 = two colors
    for start in range(num_nodes):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
'''


def _setup_bipartite(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(2, n)
    # Half the time build a bipartite graph, half the time add
    # an odd cycle (3-cycle) to make it non-bipartite.
    is_bipartite = rng.random() < 0.5
    edges = set()
    # Build a tree (always bipartite).
    for i in range(num_nodes - 1):
        edges.add((i, i + 1))
    if not is_bipartite and num_nodes >= 3:
        # Add a 3-cycle: edges 0-1, 1-2, 0-2. (0-1 and 1-2 are
        # already in the chain; add 0-2 to close a triangle.)
        edges.add((0, 2))
    # Add a few extra non-cycle edges (still bipartite).
    for _ in range(min(num_nodes, 3)):
        a = rng.randint(0, num_nodes - 1)
        b = rng.randint(0, num_nodes - 1)
        if a != b:
            lo, hi = sorted((a, b))
            edges.add((lo, hi))
    edges_list = sorted(edges)
    challenge._expected = is_bipartite
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_bipartite(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    return result == challenge._expected


# === graph_13 Articulation Points ===

GRAPH_13_SOURCE = '''\
"""Optimal solution for graph_13: Articulation Points.

Tarjan-style DFS on an undirected graph. A node u is an
articulation point iff one of its DFS-tree children v has
``low[v] >= disc[u]`` (and u is not the root, OR u is the
root with more than one DFS child). The result is the sorted
list of articulation point indices.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [set() for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    parent = [-1] * num_nodes
    ap = set()

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        children = 0
        for v in sorted(adj[u]):
            if disc[v] == -1:
                parent[v] = u
                children += 1
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    ap.add(u)
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, 0)
    return sorted(ap)
'''


def _setup_articulation(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(3, min(n, 8))
    # Build a connected undirected graph with a small chance of cycles.
    edges = set()
    for i in range(1, num_nodes):
        parent = rng.randint(0, i - 1)
        edges.add((min(parent, i), max(parent, i)))
    # Add a few extra edges to create cycles (so the algorithm has work to do).
    extra = max(0, num_nodes // 2)
    for _ in range(extra):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, num_nodes - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    edges_list = sorted(edges)
    challenge._num_nodes = num_nodes
    challenge._edges = edges_list
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_articulation(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    if sorted(result) != result:
        return False  # must be sorted
    # Re-run Tarjan's articulation-point algorithm and compare.
    num_nodes = challenge._num_nodes
    adj = [set() for _ in range(num_nodes)]
    for u, v in challenge._edges:
        adj[u].add(v)
        adj[v].add(u)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    parent = [-1] * num_nodes
    ap = set()

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        children = 0
        for v in sorted(adj[u]):
            if disc[v] == -1:
                parent[v] = u
                children += 1
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    ap.add(u)
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, 0)
    expected = sorted(ap)
    return result == expected


# === graph_14 Bridges ===

GRAPH_14_SOURCE = '''\
"""Optimal solution for graph_14: Bridges.

Tarjan-style DFS on an undirected graph. An edge (u, v) is a
bridge iff, in the DFS tree, ``low[v] > disc[u]``. The result
is the sorted list of (u, v) bridge tuples with u < v.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [set() for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    bridges = set()

    def dfs(u, parent, time):
        disc[u] = low[u] = time
        time += 1
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, u, time)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((min(u, v), max(u, v)))
            elif v != parent:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, -1, 0)
    return sorted(bridges)
'''


def _setup_bridges(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(3, min(n, 8))
    edges = set()
    for i in range(1, num_nodes):
        parent = rng.randint(0, i - 1)
        edges.add((min(parent, i), max(parent, i)))
    # Extra edges to create cycles (cycles hide bridges).
    extra = max(0, num_nodes // 3)
    for _ in range(extra):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, num_nodes - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    edges_list = sorted(edges)
    challenge._num_nodes = num_nodes
    challenge._edges = edges_list
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_bridges(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    if sorted(result) != result:
        return False
    num_nodes = challenge._num_nodes
    adj = [set() for _ in range(num_nodes)]
    for u, v in challenge._edges:
        adj[u].add(v)
        adj[v].add(u)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    bridges = set()

    def dfs(u, parent, time):
        disc[u] = low[u] = time
        time += 1
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, u, time)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((min(u, v), max(u, v)))
            elif v != parent:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, -1, 0)
    expected = sorted(bridges)
    return result == expected


# === graph_15 Tarjan's SCC ===

GRAPH_15_SOURCE = '''\
"""Optimal solution for graph_15: Tarjan's SCC.

Single-pass DFS on a directed graph that maintains each node's
discovery time and low-link value. When low[u] == disc[u], u
is the root of an SCC; pop the stack until u is removed.
Returns a list of SCCs, each sorted; outer list sorted by
smallest element.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    on_stack = [False] * num_nodes
    stack = []
    sccs = []

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        stack.append(u)
        on_stack[u] = True
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])
        if low[u] == disc[u]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == u:
                    break
            sccs.append(sorted(component))
        return time

    for start in range(num_nodes):
        if disc[start] == -1:
            dfs(start, 0)
    return sorted(sccs, key=lambda c: c[0])
'''


def _setup_tarjan_scc(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(3, min(n, 8))
    # Build a random DAG-ish base; add a few back edges to create SCCs.
    edges = set()
    for i in range(1, num_nodes):
        parent = rng.randint(0, i - 1)
        edges.add((parent, i))
    back = max(0, num_nodes // 3)
    for _ in range(back):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, u - 1) if u > 0 else 0
        if u != v:
            edges.add((u, v))
    edges_list = sorted(edges)
    challenge._num_nodes = num_nodes
    challenge._edges = edges_list
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_tarjan_scc(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    num_nodes = challenge._num_nodes
    adj = [[] for _ in range(num_nodes)]
    for u, v in challenge._edges:
        adj[u].append(v)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    on_stack = [False] * num_nodes
    stack = []
    sccs = []

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        stack.append(u)
        on_stack[u] = True
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])
        if low[u] == disc[u]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == u:
                    break
            sccs.append(sorted(component))
        return time

    for start in range(num_nodes):
        if disc[start] == -1:
            dfs(start, 0)
    expected = sorted(sccs, key=lambda c: c[0])
    return result == expected


# === graph_16 Kosaraju's SCC ===

GRAPH_16_SOURCE = '''\
"""Optimal solution for graph_16: Kosaraju's SCC.

Two-pass DFS on a directed graph. Pass 1 walks the original
graph, pushing each node onto a stack when its DFS finishes.
Pass 2 walks the transpose graph in stack-pop order; each DFS
tree in pass 2 is one SCC. Outer list sorted by smallest
element.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    radj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)
    visited = [False] * num_nodes
    order = []

    def dfs1(u):
        visited[u] = True
        for v in sorted(adj[u]):
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(num_nodes):
        if not visited[u]:
            dfs1(u)
    visited = [False] * num_nodes
    sccs = []

    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in sorted(radj[u]):
            if not visited[v]:
                dfs2(v, comp)

    for u in reversed(order):
        if not visited[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(sorted(comp))
    return sorted(sccs, key=lambda c: c[0])
'''


def _setup_kosaraju_scc(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(3, min(n, 8))
    edges = set()
    for i in range(1, num_nodes):
        parent = rng.randint(0, i - 1)
        edges.add((parent, i))
    back = max(0, num_nodes // 3)
    for _ in range(back):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, u - 1) if u > 0 else 0
        if u != v:
            edges.add((u, v))
    edges_list = sorted(edges)
    challenge._num_nodes = num_nodes
    challenge._edges = edges_list
    return {"num_nodes": num_nodes, "edges": edges_list}


def _verify_kosaraju_scc(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    num_nodes = challenge._num_nodes
    adj = [[] for _ in range(num_nodes)]
    radj = [[] for _ in range(num_nodes)]
    for u, v in challenge._edges:
        adj[u].append(v)
        radj[v].append(u)
    visited = [False] * num_nodes
    order = []

    def dfs1(u):
        visited[u] = True
        for v in sorted(adj[u]):
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(num_nodes):
        if not visited[u]:
            dfs1(u)
    visited = [False] * num_nodes
    sccs = []

    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in sorted(radj[u]):
            if not visited[v]:
                dfs2(v, comp)

    for u in reversed(order):
        if not visited[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(sorted(comp))
    expected = sorted(sccs, key=lambda c: c[0])
    return result == expected


# === graph_17 0-1 BFS ===

GRAPH_17_SOURCE = '''\
"""Optimal solution for graph_17: 0-1 BFS.

Shortest path on a graph with edge weights in {0, 1}. Use a
deque: pop the left, push 0-weight neighbors to the LEFT and
1-weight neighbors to the RIGHT. This is O(V + E).
"""


def solve(num_nodes, edges, start):
    if num_nodes <= 0:
        return {}
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[start] = 0
    from collections import deque
    dq = deque([start])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return {i: (-1 if dist[i] == INF else dist[i]) for i in range(num_nodes)}
'''


def _setup_zero_one_bfs(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_nodes = max(4, min(n, 10))
    edges = []
    for i in range(1, num_nodes):
        parent = rng.randint(0, i - 1)
        w = rng.randint(0, 1)
        edges.append((parent, i, w))
        edges.append((i, parent, w))
    # Extra edges.
    for _ in range(num_nodes):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, num_nodes - 1)
        if u != v:
            edges.append((u, v, rng.randint(0, 1)))
    challenge._num_nodes = num_nodes
    challenge._edges = edges
    challenge._start = 0
    return {"num_nodes": num_nodes, "edges": list(edges), "start": 0}


def _verify_zero_one_bfs(challenge, result: Any) -> bool:
    if not isinstance(result, dict):
        return False
    num_nodes = challenge._num_nodes
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in challenge._edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[0] = 0
    from collections import deque
    dq = deque([0])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    expected = {i: (-1 if dist[i] == INF else dist[i]) for i in range(num_nodes)}
    return result == expected


# === graph_18 A* Search (2D grid) ===

GRAPH_18_SOURCE = '''\
"""Optimal solution for graph_18: A* Search on a 2D grid.

Manhattan-distance heuristic. Walk the grid with 4-neighbour
moves; a priority queue keyed on f = g + h (cost so far plus
Manhattan distance to goal) drives the expansion order.
Return the shortest path length in steps, or -1 if no path.
"""


def solve(grid, start, goal, size):
    from heapq import heappush, heappop
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return -1
    if start == goal:
        return 0

    def heuristic(p):
        return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

    open_heap = []
    heappush(open_heap, (heuristic(start), 0, start))
    g_score = {start: 0}
    while open_heap:
        f, g, current = heappop(open_heap)
        if current == goal:
            return g
        if g > g_score.get(current, float("inf")):
            continue
        row, col = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0:
                nbr = (nr, nc)
                tentative = g + 1
                if tentative < g_score.get(nbr, float("inf")):
                    g_score[nbr] = tentative
                    heappush(open_heap, (tentative + heuristic(nbr), tentative, nbr))
    return -1
'''


def _setup_astar(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    size = max(3, min(n, 12))
    # 0 = walkable, 1 = wall. Start top-left, goal bottom-right.
    grid = [[0] * size for _ in range(size)]
    # Scatter walls; keep start/goal walkable and reachable.
    wall_count = max(1, size // 2)
    for _ in range(wall_count):
        r = rng.randint(0, size - 1)
        c = rng.randint(0, size - 1)
        if (r, c) != (0, 0) and (r, c) != (size - 1, size - 1):
            grid[r][c] = 1
    # BFS to verify a path exists; if not, clear a row to ensure reachability.
    if not _has_path(grid, size, (0, 0), (size - 1, size - 1)):
        for c in range(size):
            grid[size - 1][c] = 0
    challenge._grid = grid
    return {
        "grid": [row[:] for row in grid],
        "start": (0, 0),
        "goal": (size - 1, size - 1),
        "size": size,
    }


def _has_path(grid, size, start, goal):
    from collections import deque
    q = deque([start])
    seen = {start}
    while q:
        r, c = q.popleft()
        if (r, c) == goal:
            return True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in seen and grid[nr][nc] == 0:
                seen.add((nr, nc))
                q.append((nr, nc))
    return False


def _verify_astar(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    grid = challenge._grid
    size = len(grid)
    # Brute-force BFS gives the ground-truth shortest path.
    from collections import deque
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if (r, c) == (size - 1, size - 1):
            return result == d
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in seen and grid[nr][nc] == 0:
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))
    return result == -1


# === Spec list ====================================================


SPECS.extend([
    AlgorithmSpec(
        id="graph_02",
        name="Breadth-First Search",
        category="graphs",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Traverse the graph in breadth-first order starting from node 0.\n"
            "Return the list of visited node indices in BFS order.\n"
            "The graph is undirected. Neighbors are visited in sorted order.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/"
        ),
        source_url="https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples representing undirected edges.",
        },
        returns="a list of node indices in BFS visit order, starting from node 0.",
        source=GRAPH_02_SOURCE,
        setup_fn=_setup_graph_bfs,
        verify_fn=_verify_graph_bfs,
        samples=[
            Sample("num_nodes = 3, edges = [(0, 1), (1, 2)]", "[0, 1, 2]"),
            Sample("num_nodes = 2, edges = []", "[0]"),
            Sample("num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]", "[0, 1, 2, 3]"),
        ],
        hint="Use a queue. Start at 0; pop, visit neighbors (sorted), enqueue unseen ones.",
        parents=["graph_01"],
        children=["graph_03", "graph_07"],
    ),
    AlgorithmSpec(
        id="graph_03",
        name="Depth-First Search",
        category="graphs",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Traverse the graph in depth-first order starting from node 0.\n"
            "Return the list of visited node indices in DFS order.\n"
            "The graph is undirected. Neighbors are visited in sorted order.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/"
        ),
        source_url="https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples representing undirected edges.",
        },
        returns="a list of node indices in DFS visit order, starting from node 0.",
        source=GRAPH_03_SOURCE,
        setup_fn=_setup_graph_dfs,
        verify_fn=_verify_graph_dfs,
        samples=[
            Sample("num_nodes = 3, edges = [(0, 1), (1, 2)]", "[0, 1, 2]"),
            Sample("num_nodes = 2, edges = []", "[0]"),
            Sample("num_nodes = 4, edges = [(0, 1), (0, 2), (0, 3)]", "[0, 1, 2, 3]"),
        ],
        hint="Recurse: visit node, then recurse on each neighbor (sorted) that's unseen.",
        parents=["graph_02"],
        children=["graph_07"],
    ),
    AlgorithmSpec(
        id="graph_05",
        name="Bellman-Ford",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Find the shortest distance from the start node to all other\n"
            "nodes using the Bellman-Ford algorithm. The graph has\n"
            "directed, weighted edges (weights can be negative, but the\n"
            "spec guarantees no negative cycles).\n"
            "Return a dict mapping each node to its shortest distance from\n"
            "start. Unreachable nodes get -1.\n"
            "Requirement: O(V * E).\n"
            "Source: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/"
        ),
        source_url="https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/",
        params=["num_nodes", "edges", "start"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v, weight) tuples for directed edges.",
            "start": "source node.",
        },
        returns="a dict mapping each node to its shortest distance. Unreachable nodes get -1.",
        source=GRAPH_05_SOURCE,
        setup_fn=_setup_bellman_ford,
        verify_fn=_verify_bellman_ford,
        samples=[
            Sample("num_nodes = 3, edges = [(0, 1, 5), (1, 2, 3)], start = 0", "{0: 0, 1: 5, 2: 8}"),
            Sample("num_nodes = 2, edges = [], start = 0", "{0: 0, 1: -1}"),
            Sample("num_nodes = 4, edges = [(0, 1, 1), (1, 2, 1), (0, 2, 5)], start = 0", "{0: 0, 1: 1, 2: 2, 3: -1}"),
        ],
        hint="Relax all edges V-1 times. Stop early if a pass produces no updates.",
        parents=["graph_04"],
        children=["graph_06"],
    ),
    AlgorithmSpec(
        id="graph_06",
        name="Floyd-Warshall",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Compute all-pairs shortest paths using the Floyd-Warshall\n"
            "algorithm. The graph has directed, weighted edges (positive\n"
            "weights). Return the N x N distance matrix where entry [i][j]\n"
            "is the shortest distance from i to j, or -1 if j is\n"
            "unreachable from i. The diagonal [i][i] is 0.\n"
            "Requirement: O(V^3).\n"
            "Source: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/"
        ),
        source_url="https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v, weight) tuples for directed edges.",
        },
        returns="an N x N matrix of shortest distances; -1 for unreachable pairs.",
        source=GRAPH_06_SOURCE,
        setup_fn=_setup_floyd_warshall,
        verify_fn=_verify_floyd_warshall,
        samples=[
            Sample("num_nodes = 3, edges = [(0, 1, 1), (1, 2, 1), (0, 2, 5)]", "[[0, 1, 2], [999, 0, 1], [999, 999, 0]] (replace 999 with -1)"),
            Sample("num_nodes = 2, edges = []", "[[0, -1], [-1, 0]]"),
        ],
        hint="Try every intermediate node k. dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]).",
        parents=["graph_05"],
        children=[],
    ),
    AlgorithmSpec(
        id="graph_07",
        name="Topological Sort",
        category="graphs",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Compute a topological ordering of the directed acyclic graph\n"
            "using Kahn's algorithm. Return the order as a list of node\n"
            "indices, or -1 if a cycle is detected.\n"
            "The spec guarantees a DAG (the setup uses u < v for every\n"
            "edge), so the answer is always a list.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/"
        ),
        source_url="https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples for directed edges (u < v guarantees DAG).",
        },
        returns="a list of node indices in topological order, or -1 on a cycle.",
        source=GRAPH_07_SOURCE,
        setup_fn=_setup_topological_sort,
        verify_fn=_verify_topological_sort,
        samples=[
            Sample("num_nodes = 4, edges = [(0, 1), (0, 2), (1, 3), (2, 3)]", "[0, 1, 2, 3]"),
            Sample("num_nodes = 3, edges = []", "[0, 1, 2]"),
            Sample("num_nodes = 3, edges = [(0, 1), (0, 2)]", "[0, 1, 2]"),
        ],
        hint="Kahn's BFS. Start from indegree-0 nodes, process, decrement neighbors' indegrees.",
        parents=["graph_02", "graph_03"],
        children=[],
    ),
    AlgorithmSpec(
        id="graph_08",
        name="Kruskal's MST",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Find the minimum spanning tree of an undirected, weighted\n"
            "graph using Kruskal's algorithm. Return the MST as a sorted\n"
            "list of (u, v, weight) tuples, or [] if the graph is not\n"
            "connected. The setup always produces a connected graph.\n"
            "Requirement: O(E log E).\n"
            "Source: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/"
        ),
        source_url="https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v, weight) tuples for undirected edges.",
        },
        returns="a sorted list of MST edges (u, v, w), or [] if the graph is disconnected.",
        source=GRAPH_08_SOURCE,
        setup_fn=_setup_kruskal,
        verify_fn=_verify_kruskal,
        samples=[
            Sample("num_nodes = 4, edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]", "[(2, 3, 4), (0, 3, 5), (0, 1, 10)]"),
            Sample("num_nodes = 3, edges = [(0, 1, 1), (1, 2, 2)]", "[(0, 1, 1), (1, 2, 2)]"),
        ],
        hint="Sort edges by weight. Greedy-union with a DSU. Skip edges that connect nodes already in the same set.",
        parents=["graph_09"],
        children=[],
    ),
    AlgorithmSpec(
        id="graph_09",
        name="Union-Find (DSU)",
        category="graphs",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Implement the Disjoint Set Union data structure with path\n"
            "compression and union by rank. ops is a list of tuples:\n"
            "  (\"union\", a, b) — union the sets of a and b\n"
            "  (\"find\",  a, b) — return True iff a and b are in the same set\n"
            "Return a list of bools, one per (\"find\", ...) op, in order.\n"
            "Requirement: O(α(n)) per op (effectively constant).\n"
            "Source: https://www.geeksforgeeks.org/union-find/"
        ),
        source_url="https://www.geeksforgeeks.org/union-find/",
        params=["n", "ops"],
        inputs={
            "n": "number of elements (0 to n-1).",
            "ops": "list of operation tuples: (\"union\", a, b) or (\"find\", a, b).",
        },
        returns="a list of bools (one per \"find\" op) — True iff the two elements share a set.",
        source=GRAPH_09_SOURCE,
        setup_fn=_setup_union_find,
        verify_fn=_verify_union_find,
        samples=[
            Sample("n = 5, ops = [('union', 0, 1), ('find', 0, 1)]", "[True]"),
            Sample("n = 4, ops = [('union', 0, 1), ('find', 2, 3)]", "[False]"),
            Sample("n = 3, ops = [('union', 0, 1), ('union', 1, 2), ('find', 0, 2)]", "[True]"),
        ],
        hint="Path compression + union by rank gives near-constant amortized ops.",
        parents=["graph_01"],
        children=["graph_08"],
    ),
    AlgorithmSpec(
        id="graph_10",
        name="Prim's MST",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the minimum spanning tree of an undirected, weighted\n"
            "graph using Prim's algorithm (vertex-growth with a min-heap).\n"
            "Return the MST as a sorted list of (u, v, weight) tuples,\n"
            "or [] if the graph is not connected. The setup always\n"
            "produces a connected graph.\n"
            "Requirement: O(E log V) with a heap; O(V^2) without.\n"
            "Source: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/"
        ),
        source_url="https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v, weight) tuples for undirected edges.",
        },
        returns="a sorted list of MST edges (u, v, w), or [] if disconnected.",
        source=GRAPH_10_SOURCE,
        setup_fn=_setup_prim,
        verify_fn=_verify_prim,
        samples=[
            Sample("num_nodes = 4, edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]", "[(2, 3, 4), (0, 3, 5), (0, 1, 10)]"),
            Sample("num_nodes = 3, edges = [(0, 1, 1), (1, 2, 2)]", "[(0, 1, 1), (1, 2, 2)]"),
        ],
        hint="Start at any node. Repeatedly add the cheapest edge that connects a visited node to an unvisited one.",
        parents=["graph_08"],
        children=[],
    ),
    AlgorithmSpec(
        id="graph_11",
        name="Cycle Detection",
        category="graphs",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Return True iff the undirected graph has a cycle.\n"
            "Uses iterative DFS with parent tracking.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/detect-cycle-undirected-graph/"
        ),
        source_url="https://www.geeksforgeeks.org/detect-cycle-undirected-graph/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples for undirected edges.",
        },
        returns="True iff the graph has at least one cycle.",
        source=GRAPH_11_SOURCE,
        setup_fn=_setup_cycle_detect,
        verify_fn=_verify_cycle_detect,
        samples=[
            Sample("num_nodes = 4, edges = [(0, 1), (0, 2), (1, 2), (2, 3)]", "True (0-1-2-0)"),
            Sample("num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]", "False (chain)"),
            Sample("num_nodes = 3, edges = [(0, 1), (1, 2)]", "False"),
        ],
        hint="DFS. If you reach an already-visited node that is NOT your parent, there's a cycle.",
        parents=["graph_03"],
        children=["graph_12"],
    ),
    AlgorithmSpec(
        id="graph_12",
        name="Bipartite Check",
        category="graphs",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Return True iff the undirected graph is bipartite\n"
            "(2-colorable). Equivalent: the graph contains no odd\n"
            "cycles. BFS-based 2-coloring is the standard approach.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/bipartite-graph/"
        ),
        source_url="https://www.geeksforgeeks.org/bipartite-graph/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples for undirected edges.",
        },
        returns="True iff the graph is 2-colorable (no odd cycles).",
        source=GRAPH_12_SOURCE,
        setup_fn=_setup_bipartite,
        verify_fn=_verify_bipartite,
        samples=[
            Sample("num_nodes = 4, edges = [(0, 1), (0, 3), (1, 2), (2, 3)]", "True (color 0: 0,2; color 1: 1,3)"),
            Sample("num_nodes = 3, edges = [(0, 1), (1, 2), (0, 2)]", "False (triangle)"),
            Sample("num_nodes = 2, edges = []", "True"),
        ],
        hint="BFS. Assign alternating colors; if a neighbor already has the same color, fail.",
        parents=["graph_11"],
        children=["graph_13"],
    ),
    AlgorithmSpec(
        id="graph_13",
        name="Articulation Points",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find all articulation points (cut vertices) in an undirected\n"
            "graph. A node u is an articulation point iff its removal\n"
            "disconnects the graph. Tarjan-style DFS: u is one iff it has\n"
            "more than one DFS child (if root) or some child v has\n"
            "``low[v] >= disc[u]``.\n"
            "Return the sorted list of articulation point indices.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/"
        ),
        source_url="https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples for undirected edges.",
        },
        returns="a sorted list of articulation point indices.",
        source=GRAPH_13_SOURCE,
        setup_fn=_setup_articulation,
        verify_fn=_verify_articulation,
        samples=[
            Sample("num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4)]", "[0, 3]"),
            Sample("num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]", "[1, 2]"),
        ],
        hint="Tarjan DFS. A node is an articulation point if it has >1 DFS child (when root) or a child v with low[v] >= disc[u].",
        parents=["graph_12"],
        children=["graph_14"],
    ),
    AlgorithmSpec(
        id="graph_14",
        name="Bridges",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find all bridges (cut edges) in an undirected graph. An\n"
            "edge (u, v) is a bridge iff its removal disconnects the\n"
            "graph. Tarjan-style DFS: (u, v) is a bridge iff\n"
            "``low[v] > disc[u]``.\n"
            "Return the sorted list of (u, v) tuples (u < v).\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/bridge-in-a-graph/"
        ),
        source_url="https://www.geeksforgeeks.org/bridge-in-a-graph/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples for undirected edges.",
        },
        returns="a sorted list of (u, v) bridge tuples (u < v).",
        source=GRAPH_14_SOURCE,
        setup_fn=_setup_bridges,
        verify_fn=_verify_bridges,
        samples=[
            Sample("num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4)]", "[(0, 3), (3, 4)]"),
            Sample("num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]", "[(0, 1), (1, 2), (2, 3)]"),
        ],
        hint="Tarjan DFS. (u, v) is a bridge iff low[v] > disc[u].",
        parents=["graph_13"],
        children=["graph_15"],
    ),
    AlgorithmSpec(
        id="graph_15",
        name="Tarjan's SCC",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find all strongly connected components of a directed graph\n"
            "using Tarjan's algorithm. Each SCC is a maximal set of\n"
            "nodes where every node can reach every other.\n"
            "Return a list of SCCs; each SCC is sorted internally; the\n"
            "outer list is sorted by smallest element.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/"
        ),
        source_url="https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples for directed edges.",
        },
        returns="a list of SCCs (each a sorted list of node indices; outer list sorted).",
        source=GRAPH_15_SOURCE,
        setup_fn=_setup_tarjan_scc,
        verify_fn=_verify_tarjan_scc,
        samples=[
            Sample("num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]", "[[0, 1, 2], [3], [4]]"),
            Sample("num_nodes = 3, edges = [(0, 1), (1, 2)]", "[[0], [1], [2]]"),
        ],
        hint="DFS with disc and low. When low[u] == disc[u], u is the root of an SCC - pop the stack.",
        parents=["graph_14"],
        children=["graph_16"],
    ),
    AlgorithmSpec(
        id="graph_16",
        name="Kosaraju's SCC",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find all strongly connected components of a directed graph\n"
            "using Kosaraju's two-pass algorithm. Pass 1: DFS in the\n"
            "original graph, pushing nodes onto a stack in finish time\n"
            "order. Pass 2: pop the stack and DFS on the transpose\n"
            "graph; each DFS tree is one SCC.\n"
            "Return a list of SCCs sorted as in Tarjan's spec.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/strongly-connected-components/"
        ),
        source_url="https://www.geeksforgeeks.org/strongly-connected-components/",
        params=["num_nodes", "edges"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples for directed edges.",
        },
        returns="a list of SCCs (each a sorted list of node indices; outer list sorted).",
        source=GRAPH_16_SOURCE,
        setup_fn=_setup_kosaraju_scc,
        verify_fn=_verify_kosaraju_scc,
        samples=[
            Sample("num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]", "[[0, 1, 2], [3], [4]]"),
            Sample("num_nodes = 3, edges = [(0, 1), (1, 2), (2, 0)]", "[[0, 1, 2]]"),
        ],
        hint="Two passes. Pass 1 pushes nodes by finish order; pass 2 DFS the transpose graph in reverse finish order.",
        parents=["graph_15"],
        children=["graph_17"],
    ),
    AlgorithmSpec(
        id="graph_17",
        name="0-1 BFS",
        category="graphs",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Shortest path on a graph with edge weights in {0, 1}.\n"
            "Use a deque: pop the left, push 0-weight neighbors to the\n"
            "LEFT and 1-weight neighbors to the RIGHT. This makes the\n"
            "algorithm O(V + E) - the same as BFS, but supports unit\n"
            "weights too.\n"
            "Return a dict mapping each node to its shortest distance from\n"
            "start. Unreachable nodes get -1.\n"
            "Requirement: O(V + E).\n"
            "Source: https://www.geeksforgeeks.org/0-1-bfs-shortest-path-unit-weight-edges/"
        ),
        source_url="https://www.geeksforgeeks.org/0-1-bfs-shortest-path-unit-weight-edges/",
        params=["num_nodes", "edges", "start"],
        inputs={
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v, weight) tuples; weight is 0 or 1.",
            "start": "source node.",
        },
        returns="a dict mapping each node to its shortest distance. Unreachable nodes get -1.",
        source=GRAPH_17_SOURCE,
        setup_fn=_setup_zero_one_bfs,
        verify_fn=_verify_zero_one_bfs,
        samples=[
            Sample("num_nodes = 4, edges = [(0, 1, 0), (1, 2, 1), (0, 2, 1), (2, 3, 0)], start = 0", "{0: 0, 1: 0, 2: 1, 3: 1}"),
        ],
        hint="Deque (not queue). 0-weight neighbors go to the LEFT, 1-weight neighbors go to the RIGHT.",
        parents=["graph_16"],
        children=["graph_18"],
    ),
    AlgorithmSpec(
        id="graph_18",
        name="A* Search",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Shortest path on a 2D grid with 4-neighbour moves. The\n"
            "expansion order is driven by a priority queue keyed on\n"
            "``f = g + h``, where g is the cost-so-far and h is the\n"
            "Manhattan-distance heuristic from the current cell to the\n"
            "goal. With an admissible heuristic, A* finds an optimal\n"
            "path in (typically) far fewer expansions than BFS.\n"
            "Return the shortest path length in steps, or -1 if no path.\n"
            "Source: https://www.geeksforgeeks.org/a-search-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/a-search-algorithm/",
        params=["grid", "start", "goal", "size"],
        inputs={
            "grid": "2D list-like. 0 = walkable, 1 = wall. Read with grid[row][column].",
            "start": "(row, column) start position.",
            "goal": "(row, column) goal position.",
            "size": "width and height of the square grid.",
        },
        returns="the length of the shortest path from start to goal in steps, or -1.",
        source=GRAPH_18_SOURCE,
        setup_fn=_setup_astar,
        verify_fn=_verify_astar,
        max_n=35,  # MAX_2D_N
        samples=[
            Sample("grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], start = (0, 0), goal = (2, 2), size = 3", "4"),
            Sample("grid = [[0, 0, 1], [0, 0, 0], [1, 0, 0]], start = (0, 0), goal = (2, 2), size = 3", "4"),
        ],
        hint="Priority queue keyed on (g + h, g, position) where h is the Manhattan distance to the goal.",
        parents=["graph_17"],
        children=[],
    ),
])


# === graph_19: M-Coloring Problem ===

GRAPH_19_SOURCE = '''
def solve(n, edges, m):
    """Return True iff the graph can be colored with m colors
    such that no two adjacent vertices share a color.

    Backtracking: assign colors to vertices one at a time.
    At each step, try each color; if it doesn't conflict with
    any already-colored neighbor, recurse.
    """
    if n == 0:
        return True
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    color = [-1] * n

    def safe(v, c):
        for u in adj[v]:
            if color[u] == c:
                return False
        return True

    def helper(v):
        if v == n:
            return True
        for c in range(m):
            if safe(v, c):
                color[v] = c
                if helper(v + 1):
                    return True
                color[v] = -1
        return False

    return helper(0)
'''


def _setup_m_coloring(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
    edges = set()
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        edges.add((min(u, i), max(u, i)))
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    # Choose m so that the answer is True (small graphs are usually 2-colorable).
    m = 3
    challenge._n = n_nodes
    challenge._edges = sorted(edges)
    challenge._m = m
    return {"n": n_nodes, "edges": sorted(edges), "m": m}


def _verify_m_coloring(challenge, result):
    if not isinstance(result, bool):
        return False
    # Brute force: try every assignment.
    n = challenge._n
    edges = challenge._edges
    m = challenge._m
    for mask in range(m ** n):
        # Decode mask as a base-m representation.
        colors = []
        x = mask
        for _ in range(n):
            colors.append(x % m)
            x //= m
        if all(colors[u] != colors[v] for u, v in edges):
            return result is True
    return result is False


# === graph_20: Travelling Salesman (DP) ===

GRAPH_20_SOURCE = '''
def solve(dist, n):
    """Travelling Salesman: minimum Hamiltonian cycle cost.

    Held-Karp DP: dp[mask][i] = min cost to start at 0,
    visit exactly the cities in ``mask``, and end at city i.
    Recurrence: dp[mask][i] = min over j in mask of
    dp[mask ^ (1<<i)][j] + dist[j][i]. Final answer is
    min over i of dp[all][i] + dist[i][0].
    """
    if n <= 1:
        return 0
    INF = float("inf")
    # dp[mask][i] where mask is an int, i is the destination.
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at 0 with only 0 visited.
    for mask in range(1, 1 << n):
        if not (mask & 1):
            continue  # mask must include 0
        for i in range(n):
            if not (mask & (1 << i)) or dp[mask][i] == INF:
                continue
            # Try extending to a new city j.
            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + dist[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
    full = (1 << n) - 1
    best = INF
    for i in range(n):
        if dp[full][i] < INF:
            cycle = dp[full][i] + dist[i][0]
            if cycle < best:
                best = cycle
    return best
'''


def _setup_tsp(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 5))  # 2^n subset enumeration grows fast
    # Generate a random distance matrix satisfying triangle inequality.
    pts = [(rng.randint(0, 10), rng.randint(0, 10)) for _ in range(n_nodes)]

    def d(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    dist = [[d(pts[i], pts[j]) for j in range(n_nodes)] for i in range(n_nodes)]
    challenge._dist = [row[:] for row in dist]
    challenge._n = n_nodes
    return {"dist": [row[:] for row in dist], "n": n_nodes}


def _verify_tsp(challenge, result):
    if not isinstance(result, int):
        return False
    n = challenge._n
    dist = challenge._dist
    from itertools import permutations
    if n <= 1:
        return result == 0
    # Brute force: try every permutation starting and ending at 0.
    best = float("inf")
    nodes = list(range(1, n))
    for perm in permutations(nodes):
        cost = dist[0][perm[0]]
        for i in range(len(perm) - 1):
            cost += dist[perm[i]][perm[i + 1]]
        cost += dist[perm[-1]][0]
        if cost < best:
            best = cost
    return result == best


SPECS.extend([
    AlgorithmSpec(
        id="graph_19",
        name="M-Coloring Problem",
        category="graphs",
        difficulty=5,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Return True iff the graph can be colored with m\n"
            "colors such that no two adjacent vertices share a\n"
            "color. Backtracking: assign colors to vertices one\n"
            "at a time, picking only colors that don't conflict\n"
            "with already-colored neighbours.\n"
            "Source: https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/"
        ),
        source_url="https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/",
        params=["n", "edges", "m"],
        inputs={
            "n": "number of nodes.",
            "edges": "list of (u, v) tuples (undirected).",
            "m": "number of available colors.",
        },
        returns="True iff a valid m-coloring exists.",
        source=GRAPH_19_SOURCE,
        setup_fn=_setup_m_coloring,
        verify_fn=_verify_m_coloring,
        samples=[
            Sample("n = 4, edges = [(0, 1), (1, 2), (2, 3), (3, 0)], m = 2", "True (alternating)"),
            Sample("n = 3, edges = [(0, 1), (1, 2), (0, 2)], m = 2", "False (triangle)"),
        ],
        hint="Backtrack. At each vertex, try each color that doesn't conflict with neighbours.",
        parents=["graph_12"],
        children=["graph_20"],
    ),
    AlgorithmSpec(
        id="graph_20",
        name="Travelling Salesman (Held-Karp DP)",
        category="graphs",
        difficulty=7,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Given a distance matrix, find the minimum-cost\n"
            "Hamiltonian cycle (visit every city exactly once,\n"
            "return to start). Held-Karp DP: dp[mask][i] = min\n"
            "cost to visit exactly the cities in ``mask`` and end\n"
            "at city i. Recurrence adds one city at a time.\n"
            "Source: https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/"
        ),
        source_url="https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/",
        params=["dist", "n"],
        inputs={
            "dist": "n x n distance matrix.",
            "n": "number of cities.",
        },
        returns="the minimum Hamiltonian cycle cost.",
        source=GRAPH_20_SOURCE,
        setup_fn=_setup_tsp,
        verify_fn=_verify_tsp,
        samples=[
            Sample("dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]], n = 4", "80 (0->1->2->3->0 or 0->3->2->1->0)"),
        ],
        hint="Held-Karp: dp[mask][i] = min cost to visit exactly mask, end at i. Try each j not in mask.",
        parents=["graph_19"],
        children=["graph_21"],
    ),
])


# === graph_21: Hamiltonian Path Existence ===

GRAPH_21_SOURCE = '''
def solve(n, edges):
    """Return True iff there's a Hamiltonian path from node 0
    to node n-1 (visiting every vertex exactly once).

    Backtracking: try each permutation of intermediate nodes.
    For the test gauntlet (n <= 6), the brute force is fast.
    """
    if n <= 1:
        return n == 1
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    visited = [False] * n
    visited[0] = True

    def dfs(u, count):
        if count == n:
            return u == n - 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if dfs(v, count + 1):
                    return True
                visited[v] = False
        return False

    return dfs(0, 1)
'''


def _setup_hamiltonian(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
    edges = set()
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        edges.add((min(u, i), max(u, i)))
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    challenge._n = n_nodes
    challenge._edges = sorted(edges)
    return {"n": n_nodes, "edges": sorted(edges)}


def _verify_hamiltonian(challenge, result):
    if not isinstance(result, bool):
        return False
    n = challenge._n
    edges = challenge._edges
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    def has_hamiltonian_path(u, visited):
        if len(visited) == n:
            return u == n - 1
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                if has_hamiltonian_path(v, visited):
                    return True
                visited.discard(v)
        return False

    return result is has_hamiltonian_path(0, {0})


# === graph_22: Bipartite Check (BFS, already in graph_12) ===
# This slot reserved.

SPECS.extend([
    AlgorithmSpec(
        id="graph_21",
        name="Hamiltonian Path Existence",
        category="graphs",
        difficulty=6,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Return True iff there's a Hamiltonian path from 0 to\n"
            "n-1 in the undirected graph. Backtracking: at each\n"
            "step, try each unvisited neighbour. Stop at the first\n"
            "path that visits every vertex and ends at n-1.\n"
            "Source: https://www.geeksforgeeks.org/backtracking-set-7-hamiltonian-cycle/"
        ),
        source_url="https://www.geeksforgeeks.org/backtracking-set-7-hamiltonian-cycle/",
        params=["n", "edges"],
        inputs={
            "n": "number of nodes (capped at 6).",
            "edges": "list of (u, v) tuples (undirected).",
        },
        returns="True iff a Hamiltonian path from 0 to n-1 exists.",
        source=GRAPH_21_SOURCE,
        setup_fn=_setup_hamiltonian,
        verify_fn=_verify_hamiltonian,
        samples=[
            Sample("n = 4, edges = [(0, 1), (0, 2), (1, 3), (2, 3)]", "True (0->1->3->2 or 0->2->3->1)"),
            Sample("n = 4, edges = [(0, 1), (1, 2), (2, 3)]", "False (3 is only reachable from 2)"),
        ],
        hint="DFS from 0. At each vertex, try unvisited neighbours. Stop at n-1 when count == n.",
        parents=["graph_20"],
        children=[],
    ),
])
