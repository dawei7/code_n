"""Spec generator input — 3 more flow specs for Session 1.

Covers the remaining GfG "Network Flow" topic list pages that
flow_01..03 don't already cover:

  flow_04  Dinic's Algorithm            (BFS level graph + DFS)
  flow_05  Minimum s-t Cut              (reachable-set cut)
  flow_06  Push-Relabel Max Flow        (Goldberg-Tarjan)

After this batch, flow.py covers the full GfG max-flow topic
list (see https://www.geeksforgeeks.org/dsa/max-flow-problem-introduction/).

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module flow \\
        --input batch_flow_session1.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # flow_04: Dinic's Algorithm
    # ============================================================
    {
        "id": "flow_04",
        "name": "Dinic's Max Flow",
        "category": "flow",
        "difficulty": 6,
        "complexity": "O_N2",
        "description": (
            "Compute the max s-t flow in a directed capacitated\n"
            "graph. Dinic's algorithm: BFS from s builds a level\n"
            "graph (distance in edges, ignoring saturated\n"
            "edges); then DFS sends blocking flows along\n"
            "level-monotone paths; when BFS can't reach t, stop.\n"
            "O(E * sqrt(V)) for unit capacities, O(V^2 * E) worst\n"
            "case. Source = node 0, sink = node n-1.\n"
            "Source: https://www.geeksforgeeks.org/dsa/dinics-algorithm-maximum-flow/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/dinics-algorithm-maximum-flow/",
        "params": ["n", "edges"],
        "inputs": {
            "n": "number of nodes (small in tests, n <= 6).",
            "edges": "list of (u, v, capacity) tuples; u, v in [0, n).",
        },
        "returns": "the max s-t flow as a non-negative int (s=0, t=n-1).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("n = 2, edges = [(0,1,5)]", "5"),
            ("n = 4, edges = [(0,1,10),(0,2,8),(1,3,10),(2,3,8)]", "18"),
            ("n = 4, edges = [(0,1,10),(1,2,5),(2,3,8),(0,3,7)]", "15"),
        ],
        "hint": "BFS from s to assign levels. Then DFS pushes blocking flow along edges where level[v] = level[u] + 1 and cap[u][v] > 0. Repeat until BFS can't reach t.",
        "parents": ["flow_02"],
        "children": ["flow_05"],
    },

    # ============================================================
    # flow_05: Minimum s-t Cut
    # ============================================================
    {
        "id": "flow_05",
        "name": "Minimum s-t Cut",
        "category": "flow",
        "difficulty": 5,
        "complexity": "O_N2",
        "description": (
            "Find the minimum s-t cut in a directed flow network.\n"
            "Run any max-flow algorithm, then in the final residual\n"
            "graph do DFS/BFS from s; the set of reachable nodes\n"
            "is S, and every edge (u, v) in the ORIGINAL graph\n"
            "with u in S and v not in S is a min-cut edge. By the\n"
            "max-flow min-cut theorem, the min cut's capacity\n"
            "equals the max flow. Return the list of min-cut\n"
            "edges as a sorted list of (u, v) tuples.\n"
            "Source: https://www.geeksforgeeks.org/dsa/minimum-cut-in-a-directed-graph/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/minimum-cut-in-a-directed-graph/",
        "params": ["n", "edges"],
        "inputs": {
            "n": "number of nodes (small in tests, n <= 6).",
            "edges": "list of (u, v, capacity) tuples; u, v in [0, n).",
        },
        "returns": "a sorted list of (u, v) tuples that form a minimum s-t cut (s=0, t=n-1).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("n = 4, edges = [(0,1,16),(0,2,13),(1,2,10),(1,3,12),(2,1,4),(2,4,14),(3,2,9),(3,5,20),(4,3,7),(4,5,4)]", "edges of the min cut (e.g. [(1,3),(4,3),(4,5)] with capacity 23)"),
        ],
        "hint": "Run max flow first, then in the residual graph BFS/DFS from s to find reachable nodes. The cut is all original-graph edges going from a reachable node to a non-reachable node.",
        "parents": ["flow_04"],
        "children": [],
    },

    # ============================================================
    # flow_06: Push-Relabel Max Flow
    # ============================================================
    {
        "id": "flow_06",
        "name": "Push-Relabel Max Flow",
        "category": "flow",
        "difficulty": 7,
        "complexity": "O_N3",
        "description": (
            "Compute the max s-t flow using the Goldberg-Tarjan\n"
            "push-relabel algorithm. Maintain per-vertex 'height'\n"
            "labels and 'excess' flow. Initialize: height of s =\n"
            "n, others = 0, push full capacity from s to its\n"
            "neighbors. Then repeatedly: pick an overflowing\n"
            "vertex u; if any neighbor v with residual capacity\n"
            "has height[u] = height[v] + 1, push (relabel-to-fit).\n"
            "Otherwise relabel u to 1 + min height of neighbors\n"
            "with residual. When no vertex (except s, t) is\n"
            "overflowing, the excess at t is the max flow.\n"
            "O(V^3) generic, O(V^2 * sqrt(E)) with highest-label\n"
            "selection. Source = node 0, sink = node n-1.\n"
            "Source: https://www.geeksforgeeks.org/dsa/push-relabel-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/push-relabel-algorithm/",
        "params": ["n", "edges"],
        "inputs": {
            "n": "number of nodes (small in tests, n <= 6).",
            "edges": "list of (u, v, capacity) tuples; u, v in [0, n).",
        },
        "returns": "the max s-t flow as a non-negative int (s=0, t=n-1).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("n = 4, edges = [(0,1,16),(0,2,13),(1,2,10),(1,3,12),(2,1,4),(2,4,14),(3,2,9),(3,5,20),(4,3,7),(4,5,4)]", "23"),
        ],
        "hint": "Initialize source height to n, push to all neighbors. Repeatedly pick an overflowing vertex, push along admissible edges (height[u] = height[v] + 1) or relabel if no such edge. Excess at t is the max flow.",
        "parents": ["flow_02"],
        "children": [],
    },
]
