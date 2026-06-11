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
])
