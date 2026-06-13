"""Network Flow algorithms.

Three problems from GFG's flow / matching catalog:

  01 Ford-Fulkerson Max Flow  - DFS-based augmenting path
  02 Edmonds-Karp            - BFS-based, O(V * E^2)
  03 Bipartite Matching       - max matching via max flow

The graph is passed as (n, edges) where edges is a list of
(u, v, capacity) tuples. The flow setup keeps n small
(n <= 6) so the brute-force verify is fast.
"""


from __future__ import annotations

import random
from collections import deque
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === flow_01: Ford-Fulkerson Max Flow ===

FLOW_01_SOURCE = '''
def solve(n, edges):
    """Return the max flow from node 0 to node n-1.

    Standard Ford-Fulkerson with DFS augmenting paths. Build a
    residual graph, repeatedly find an augmenting path, push
    flow along the minimum-capacity edge, and update the
    residual. Stop when no path exists. O(E * max_flow).
    """
    # Build adjacency matrix for the residual graph.
    INF = float("inf")
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c  # in case of parallel edges
    max_flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
        # Find an augmenting path with DFS.
        stack = [0]
        visited = [False] * n
        visited[0] = True
        found = -1
        while stack and found == -1:
            u = stack.pop()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    if v == n - 1:
                        found = v
                        break
                    stack.append(v)
        if found == -1:
            break
        # Find bottleneck.
        path_flow = float("inf")
        v = found
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        # Update residual.
        v = found
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow
'''


def _setup_ford_fulkerson(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 5))
    # Build a connected graph with a guaranteed flow.
    edges = []
    # Tree edges to ensure connectivity.
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        c = rng.randint(1, 10)
        edges.append((u, i, c))
    # Extra edges for variety.
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.append((u, v, rng.randint(1, 10)))
    challenge._n = n_nodes
    challenge._edges = list(edges)
    return {"n": n_nodes, "edges": list(edges)}


def _verify_ford_fulkerson(challenge, result):
    if not isinstance(result, int):
        return False
    # Brute force: try every cut. The min cut = max flow by max-flow min-cut.
    n = challenge._n
    edges = challenge._edges
    # Brute-force max flow: for each subset S containing 0 but not n-1,
    # the cut capacity is the sum of capacities of edges from S to complement.
    # The max flow = min cut.
    full = set(range(n))
    min_cut = float("inf")
    for mask in range(1 << n):
        s = {i for i in range(n) if mask & (1 << i)}
        if 0 not in s or n - 1 in s:
            continue
        t = full - s
        cut = 0
        for u, v, c in edges:
            if u in s and v in t:
                cut += c
        if cut < min_cut:
            min_cut = cut
    return result == min_cut


# === flow_02: Edmonds-Karp ===

FLOW_02_SOURCE = '''
def solve(n, edges):
    """Edmonds-Karp: BFS-based augmenting path, O(V * E^2)."""
    from collections import deque
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
        # BFS from 0 to n-1.
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        while q and parent[n - 1] == -1:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        if parent[n - 1] == -1:
            break
        # Bottleneck.
        path_flow = float("inf")
        v = n - 1
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        # Update.
        v = n - 1
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    return flow
'''


def _setup_edmonds_karp(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 5))
    edges = []
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        c = rng.randint(1, 10)
        edges.append((u, i, c))
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.append((u, v, rng.randint(1, 10)))
    challenge._n = n_nodes
    challenge._edges = list(edges)
    return {"n": n_nodes, "edges": list(edges)}


def _verify_edmonds_karp(challenge, result):
    if not isinstance(result, int):
        return False
    n = challenge._n
    edges = challenge._edges
    full = set(range(n))
    min_cut = float("inf")
    for mask in range(1 << n):
        s = {i for i in range(n) if mask & (1 << i)}
        if 0 not in s or n - 1 in s:
            continue
        t = full - s
        cut = 0
        for u, v, c in edges:
            if u in s and v in t:
                cut += c
        if cut < min_cut:
            min_cut = cut
    return result == min_cut


# === flow_03: Bipartite Matching ===

FLOW_03_SOURCE = '''
def solve(left_n, right_n, edges):
    """Find the maximum matching in a bipartite graph.

    Build a flow network: source -> left nodes -> right nodes ->
    sink, with all edge capacities = 1. Run Edmonds-Karp; the
    max flow equals the max matching size. Return the matching
    size.
    """
    from collections import deque
    n = left_n + right_n + 2
    source = 0
    sink = n - 1
    cap = [[0] * n for _ in range(n)]
    for u, v in edges:
        # u is a left node, v is a right node.
        cap[1 + u][1 + left_n + v] += 1
    for u in range(left_n):
        cap[source][1 + u] += 1
    for v in range(right_n):
        cap[1 + left_n + v][sink] += 1
    # Edmonds-Karp.
    flow = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        q = deque([source])
        visited = [False] * n
        visited[source] = True
        while q and parent[sink] == -1:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        if parent[sink] == -1:
            break
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = sink
        while v != source:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    return flow
'''


def _setup_bipartite_match(challenge, n, seed):
    rng = random.Random(seed)
    left_n = max(1, min(n, 4))
    right_n = max(1, min(n, 4))
    edges = []
    for u in range(left_n):
        for v in range(right_n):
            if rng.random() < 0.6:
                edges.append((u, v))
    challenge._left_n = left_n
    challenge._right_n = right_n
    return {"left_n": left_n, "right_n": right_n, "edges": list(edges)}


def _verify_bipartite_match(challenge, result):
    if not isinstance(result, int):
        return False
    edges = challenge._edges if hasattr(challenge, "_edges") else []
    # Brute force: try every subset of edges and find a max matching
    # via augmenting paths.
    left_n = challenge._left_n
    right_n = challenge._right_n
    edges = []
    for u in range(left_n):
        for v in range(right_n):
            pass  # need to retrieve from setup
    # Simpler: enumerate all matchings.
    # Max matching in bipartite graph: try every subset of left
    # side and see if it pairs with disjoint right.
    # We do brute force by trying all subsets of left->right.
    best = 0
    # Build edge list from challenge state - but we don't have access
    # to the original edges here. Recover from the flow's setup.
    edges = list(getattr(challenge, "_edges", []))
    if not edges and hasattr(challenge, "_left_n"):
        # Re-derive edges is impossible; instead, brute force via
        # trying every assignment of left->right.
        # Use a Hungarian-style approach via backtracking.
        matched_right = [False] * right_n

        def backtrack(i, count):
            nonlocal best
            if i == left_n:
                if count > best:
                    best = count
                return
            for v in range(right_n):
                if not matched_right[v] and (i, v) in [(u, vv) for u, vv in getattr(challenge, "_orig_edges", edges)]:
                    matched_right[v] = True
                    backtrack(i + 1, count + 1)
                    matched_right[v] = False
            # Skip left node i.
            backtrack(i + 1, count)

        # We need the actual edges. Store them in challenge when set.
        backtrack(0, 0)
    return result == best


# Actually, the bipartite matching verify is too complex with the
# recovered-edges hack. Let me re-define it to use the original
# setup's edges via a different mechanism. The setup returns edges
# in the dict, and we stash them in challenge via a closure.
def _verify_bipartite_match(challenge, result):
    if not isinstance(result, int):
        return False
    left_n = challenge._left_n
    right_n = challenge._right_n
    edges = challenge._bipartite_edges
    best = 0

    def backtrack(left_i, count, used_right):
        nonlocal best
        if count > best:
            best = count
        if left_i == left_n:
            return
        # Skip this left node.
        backtrack(left_i + 1, count, used_right)
        # Try matching it to each free right.
        for r in range(right_n):
            if (left_i, r) in edge_set and not used_right[r]:
                used_right[r] = True
                backtrack(left_i + 1, count + 1, used_right)
                used_right[r] = False

    edge_set = set(edges)
    used = [False] * right_n
    backtrack(0, 0, used)
    return result == best


# Patch the setup to stash the edge set for the verify.
def _setup_bipartite_match_patched(challenge, n, seed):
    rng = random.Random(seed)
    left_n = max(1, min(n, 4))
    right_n = max(1, min(n, 4))
    edges = []
    for u in range(left_n):
        for v in range(right_n):
            if rng.random() < 0.6:
                edges.append((u, v))
    challenge._left_n = left_n
    challenge._right_n = right_n
    challenge._bipartite_edges = list(edges)
    return {"left_n": left_n, "right_n": right_n, "edges": list(edges)}


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="flow_01",
        name="Ford-Fulkerson Max Flow",
        category="flow",
        difficulty=6,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Find the maximum flow from node 0 to node n-1 in a\n"
            "directed, weighted graph. Ford-Fulkerson with DFS\n"
            "augmenting paths: repeatedly find an augmenting path,\n"
            "push the minimum-capacity edge's flow along it, and\n"
            "update the residual graph. Stop when no path exists.\n"
            "O(E * max_flow).\n"
            "Source: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/"
        ),
        source_url="https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/",
        params=["n", "edges"],
        inputs={
            "n": "number of nodes (capped at 5 in the setup).",
            "edges": "list of (u, v, capacity) tuples for directed edges.",
        },
        returns="the maximum flow value from node 0 to node n-1.",
        source=FLOW_01_SOURCE,
        setup_fn=_setup_ford_fulkerson,
        verify_fn=_verify_ford_fulkerson,
        samples=[
            Sample("n = 4, edges = [(0, 1, 10), (0, 2, 5), (1, 2, 15), (1, 3, 10), (2, 3, 10)]", "15 (0->1->3 and 0->2->3)"),
        ],
        hint="DFS to find an augmenting path. Push bottleneck. Update residual. Repeat.",
        parents=["graph_18"],
        children=["flow_02"],
    ),
    AlgorithmSpec(
        id="flow_02",
        name="Edmonds-Karp",
        category="flow",
        difficulty=6,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Max flow via Edmonds-Karp: BFS-based augmenting path\n"
            "that finds the shortest (in edges) augmenting path. The\n"
            "BFS guarantees O(V * E) augmentations, giving O(V * E^2)\n"
            "total. Edge capacities are integers.\n"
            "Source: https://www.geeksforgeeks.org/edmonds-karp-algorithm-for-max-flow-set-2-implementation/"
        ),
        source_url="https://www.geeksforgeeks.org/edmonds-karp-algorithm-for-max-flow-set-2-implementation/",
        params=["n", "edges"],
        inputs={
            "n": "number of nodes.",
            "edges": "list of (u, v, capacity) tuples.",
        },
        returns="the maximum flow value from 0 to n-1.",
        source=FLOW_02_SOURCE,
        setup_fn=_setup_edmonds_karp,
        verify_fn=_verify_edmonds_karp,
        samples=[
            Sample("n = 4, edges = [(0, 1, 10), (0, 2, 5), (1, 2, 15), (1, 3, 10), (2, 3, 10)]", "15"),
        ],
        hint="BFS for the shortest augmenting path (in edges). Push bottleneck. Update residual.",
        parents=["flow_01"],
        children=["flow_03"],
    ),
    AlgorithmSpec(
        id="flow_03",
        name="Bipartite Matching",
        category="flow",
        difficulty=6,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Given a bipartite graph (left_n left nodes, right_n\n"
            "right nodes, edges connecting them), find the maximum\n"
            "matching. Reduce to max flow: source->left (cap 1),\n"
            "left->right (cap 1), right->sink (cap 1). The max flow\n"
            "equals the max matching size. Run Edmonds-Karp.\n"
            "Source: https://www.geeksforgeeks.org/maximum-bipartite-matching/"
        ),
        source_url="https://www.geeksforgeeks.org/maximum-bipartite-matching/",
        params=["left_n", "right_n", "edges"],
        inputs={
            "left_n": "number of left-side nodes.",
            "right_n": "number of right-side nodes.",
            "edges": "list of (left_idx, right_idx) tuples.",
        },
        returns="the size of the maximum matching.",
        source=FLOW_03_SOURCE,
        setup_fn=_setup_bipartite_match_patched,
        verify_fn=_verify_bipartite_match,
        samples=[
            Sample("left_n = 3, right_n = 3, edges = [(0, 0), (0, 1), (1, 0), (2, 1), (2, 2)]", "3 (perfect matching)"),
        ],
        hint="Reduce to max flow: source->left (1), left->right (1), right->sink (1). Max flow = max matching.",
        parents=["flow_02"],
        children=[],
    ),
]
