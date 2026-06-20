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


# === flow_04: Dinic's Max Flow ===

FLOW_04_SOURCE = '''
def solve(n, edges):
    """Dinic's max flow on an adjacency-matrix residual graph.

    Returns the max flow from 0 to n-1.
    """
    from collections import deque
    INF = float("inf")
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    flow = 0
    while True:
        # BFS builds the level graph.
        level = [-1] * n
        level[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in range(n):
                if level[v] < 0 and cap[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        if level[n - 1] < 0:
            break
        # DFS sends blocking flow along level-monotone paths.
        it = [0] * n
        def dfs(u, f):
            if u == n - 1:
                return f
            for i in range(it[u], n):
                v = i
                it[u] = i
                if level[v] == level[u] + 1 and cap[u][v] > 0:
                    pushed = dfs(v, min(f, cap[u][v]))
                    if pushed:
                        cap[u][v] -= pushed
                        cap[v][u] += pushed
                        return pushed
            return 0
        while True:
            pushed = dfs(0, INF)
            if not pushed:
                break
            flow += pushed
    return flow
'''

def _setup_flow_04(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
    edges = []
    # Tree edges to ensure connectivity.
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        c = rng.randint(1, 10)
        edges.append((u, i, c))
    # Extra edges.
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.append((u, v, rng.randint(1, 10)))
    challenge._n = n_nodes
    challenge._edges = list(edges)
    return {"n": n_nodes, "edges": list(edges)}

def _verify_flow_04(challenge, result):
    # Brute force: max flow = min cut (exhaustive over S subsets).
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



# === flow_05: Minimum s-t Cut ===

FLOW_05_SOURCE = '''
def solve(n, edges):
    """Min s-t cut via max-flow then residual reachability.

    Returns a sorted list of (u, v) tuples for the cut.
    """
    from collections import deque
    INF = float("inf")
    # Build a fresh capacity matrix.
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    # Ford-Fulkerson with BFS (Edmonds-Karp) on the residual.
    flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
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
        path_flow = INF
        v = n - 1
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = n - 1
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    # Now DFS from s in the residual to find reachable set.
    reachable = [False] * n
    reachable[0] = True
    stack = [0]
    while stack:
        u = stack.pop()
        for v in range(n):
            if not reachable[v] and cap[u][v] > 0:
                reachable[v] = True
                stack.append(v)
    # Cut edges: original edges from reachable to non-reachable.
    cut = []
    for u, v, c in edges:
        if reachable[u] and not reachable[v]:
            cut.append((u, v))
    cut.sort()
    return cut
'''

def _setup_flow_05(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
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

def _verify_flow_05(challenge, result):
    # Brute force: try every S subset, find the min cut capacity.
    # The min cut returned by our solve may differ from any specific
    # brute-force min cut if there are ties, so we accept any cut
    # whose capacity equals the true min cut.
    from collections import Counter
    n = challenge._n
    edges = challenge._edges
    full = set(range(n))
    best_capacity = float("inf")
    for mask in range(1 << n):
        s = {i for i in range(n) if mask & (1 << i)}
        if 0 not in s or n - 1 in s:
            continue
        t = full - s
        cut = 0
        for u, v, c in edges:
            if u in s and v in t:
                cut += c
        if cut < best_capacity:
            best_capacity = cut
    # Compute the capacity of the returned cut. The cut is a list
    # of (u, v) edge references (possibly with duplicates for
    # parallel edges). Pair each entry to a distinct original
    # edge with the same (u, v).
    remaining = Counter(edges)
    got = list(result)
    got_capacity = 0
    for entry in got:
        # Try the natural form first.
        key = (entry[0], entry[1], None)
        # Find any unused original edge with the same (u, v).
        found = None
        for c in list(remaining):
            if c[0] == entry[0] and c[1] == entry[1] and remaining[c] > 0:
                found = c
                break
        if found is None:
            return False
        remaining[found] -= 1
        got_capacity += found[2]
    return got_capacity == best_capacity



# === flow_06: Push-Relabel Max Flow ===

FLOW_06_SOURCE = '''
def solve(n, edges):
    """Goldberg-Tarjan push-relabel max flow.

    Generic O(V^3) variant. The residual capacity of an edge
    (u, v) is maintained as a direct value (not cap-flow),
    so a push that decreases residual[u][v] increases
    residual[v][u] by the same amount.
    """
    # residual[u][v] = remaining forward capacity from u to v.
    residual = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        residual[u][v] += c
    height = [0] * n
    excess = [0] * n
    height[0] = n
    # Initial push from source: saturate every outgoing edge.
    for v in range(n):
        if residual[0][v] > 0:
            pushed = residual[0][v]
            residual[0][v] -= pushed
            residual[v][0] += pushed
            excess[v] += pushed

    def push(u, v):
        d = min(excess[u], residual[u][v])
        if d <= 0:
            return False
        residual[u][v] -= d
        residual[v][u] += d
        excess[u] -= d
        excess[v] += d
        return True

    def relabel(u):
        best = float("inf")
        for v in range(n):
            if residual[u][v] > 0 and height[v] < best:
                best = height[v]
        if best < float("inf"):
            height[u] = best + 1

    # Main loop: discharge active vertices (those with positive
    # excess that are not s or t). When a push creates new
    # excess at an inner vertex, add it to the active list.
    active = set()
    for i in range(1, n - 1):
        if excess[i] > 0:
            active.add(i)
    while active:
        # Highest-label selection.
        u = max(active, key=lambda x: height[x])
        old_h = height[u]
        # Discharge: try to push, or relabel.
        while excess[u] > 0:
            pushed = False
            for v in range(n):
                if residual[u][v] > 0 and height[u] == height[v] + 1:
                    if push(u, v):
                        pushed = True
                        if v != 0 and v != n - 1 and excess[v] > 0:
                            active.add(v)
                        break
            if not pushed:
                relabel(u)
        if excess[u] == 0:
            active.discard(u)
    return excess[n - 1]
'''

def _setup_flow_06(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
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

def _verify_flow_06(challenge, result):
    # Brute force: min cut.
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


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="flow_04",
        name="Dinic's Max Flow",
        category="flow",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Compute the max s-t flow in a directed capacitated
            graph. Dinic's algorithm: BFS from s builds a level
            graph (distance in edges, ignoring saturated
            edges); then DFS sends blocking flows along
            level-monotone paths; when BFS can't reach t, stop.
            O(E * sqrt(V)) for unit capacities, O(V^2 * E) worst
            case. Source = node 0, sink = node n-1.
            Source: https://www.geeksforgeeks.org/dsa/dinics-algorithm-maximum-flow/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/dinics-algorithm-maximum-flow/",
        params=["n", "edges"],
        inputs={
            "n": "number of nodes (small in tests, n <= 6).",
            "edges": "list of (u, v, capacity) tuples; u, v in [0, n).",
        },
        returns="the max s-t flow as a non-negative int (s=0, t=n-1).",
        source=FLOW_04_SOURCE,
        setup_fn=_setup_flow_04,
        verify_fn=_verify_flow_04,
        samples=[
            Sample("n = 2, edges = [(0,1,5)]", "5"),
            Sample("n = 4, edges = [(0,1,10),(0,2,8),(1,3,10),(2,3,8)]", "18"),
            Sample("n = 4, edges = [(0,1,10),(1,2,5),(2,3,8),(0,3,7)]", "15"),
        ],
        hint="BFS from s to assign levels. Then DFS pushes blocking flow along edges where level[v] = level[u] + 1 and cap[u][v] > 0. Repeat until BFS can't reach t.",
        parents=["flow_02"],
        children=["flow_05"],
    ),
    AlgorithmSpec(
        id="flow_05",
        name="Minimum s-t Cut",
        category="flow",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Find the minimum s-t cut in a directed flow network.
            Run any max-flow algorithm, then in the final residual
            graph do DFS/BFS from s; the set of reachable nodes
            is S, and every edge (u, v) in the ORIGINAL graph
            with u in S and v not in S is a min-cut edge. By the
            max-flow min-cut theorem, the min cut's capacity
            equals the max flow. Return the list of min-cut
            edges as a sorted list of (u, v) tuples.
            Source: https://www.geeksforgeeks.org/dsa/minimum-cut-in-a-directed-graph/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/minimum-cut-in-a-directed-graph/",
        params=["n", "edges"],
        inputs={
            "n": "number of nodes (small in tests, n <= 6).",
            "edges": "list of (u, v, capacity) tuples; u, v in [0, n).",
        },
        returns="a sorted list of (u, v) tuples that form a minimum s-t cut (s=0, t=n-1).",
        source=FLOW_05_SOURCE,
        setup_fn=_setup_flow_05,
        verify_fn=_verify_flow_05,
        samples=[
            Sample("n = 4, edges = [(0,1,16),(0,2,13),(1,2,10),(1,3,12),(2,1,4),(2,4,14),(3,2,9),(3,5,20),(4,3,7),(4,5,4)]", "edges of the min cut (e.g. [(1,3),(4,3),(4,5)] with capacity 23)"),
        ],
        hint="Run max flow first, then in the residual graph BFS/DFS from s to find reachable nodes. The cut is all original-graph edges going from a reachable node to a non-reachable node.",
        parents=["flow_04"],
        children=[],
    ),
    AlgorithmSpec(
        id="flow_06",
        name="Push-Relabel Max Flow",
        category="flow",
        difficulty=7,
        required_complexity=ComplexityClass.O_N3,
        description=("""
            Compute the max s-t flow using the Goldberg-Tarjan
            push-relabel algorithm. Maintain per-vertex 'height'
            labels and 'excess' flow. Initialize: height of s =
            n, others = 0, push full capacity from s to its
            neighbors. Then repeatedly: pick an overflowing
            vertex u; if any neighbor v with residual capacity
            has height[u] = height[v] + 1, push (relabel-to-fit).
            Otherwise relabel u to 1 + min height of neighbors
            with residual. When no vertex (except s, t) is
            overflowing, the excess at t is the max flow.
            O(V^3) generic, O(V^2 * sqrt(E)) with highest-label
            selection. Source = node 0, sink = node n-1.
            Source: https://www.geeksforgeeks.org/dsa/push-relabel-algorithm/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/push-relabel-algorithm/",
        params=["n", "edges"],
        inputs={
            "n": "number of nodes (small in tests, n <= 6).",
            "edges": "list of (u, v, capacity) tuples; u, v in [0, n).",
        },
        returns="the max s-t flow as a non-negative int (s=0, t=n-1).",
        source=FLOW_06_SOURCE,
        setup_fn=_setup_flow_06,
        verify_fn=_verify_flow_06,
        samples=[
            Sample("n = 4, edges = [(0,1,16),(0,2,13),(1,2,10),(1,3,12),(2,1,4),(2,4,14),(3,2,9),(3,5,20),(4,3,7),(4,5,4)]", "23"),
        ],
        hint="Initialize source height to n, push to all neighbors. Repeatedly pick an overflowing vertex, push along admissible edges (height[u] = height[v] + 1) or relabel if no such edge. Excess at t is the max flow.",
        parents=["flow_02"],
        children=[],
    ),
])
