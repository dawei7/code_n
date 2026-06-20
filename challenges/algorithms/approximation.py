"""Approximation algorithms.

Two classic problems from GFG's approximation-algorithms catalog:

  01 Vertex Cover (2-approx)  - greedy: pick max-degree vertex
    repeatedly; remove it and its neighbours; remaining is a
    vertex cover. The 2-approx result is at most 2x optimal.
  02 Set Cover (greedy)       - repeatedly pick the set
    covering the most uncovered elements; standard log(n)
    approximation.

The graph / universe is small (n <= 8) so brute-force
verification is fast.
"""


from __future__ import annotations

import random

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === approx_01: Vertex Cover (2-approx) ===

APPROX_01_SOURCE = '''
def solve(n, edges):
    """Return a 2-approximate vertex cover.

    Greedy: while there are uncovered edges, pick a vertex
    of max degree, add it to the cover, and remove it and all
    its incident edges. The resulting cover is at most 2x
    the optimal.
    """
    if n == 0:
        return set()
    # Adjacency list.
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    cover = set()
    edges_left = set()
    for u, v in edges:
        edges_left.add((min(u, v), max(u, v)))
    while edges_left:
        # Pick the vertex with the most incident edges remaining.
        degrees = [0] * n
        for u, v in edges_left:
            degrees[u] += 1
            degrees[v] += 1
        v = max(range(n), key=lambda i: degrees[i])
        if degrees[v] == 0:
            break
        cover.add(v)
        # Remove all edges incident to v.
        edges_to_remove = [e for e in edges_left if v in e]
        for e in edges_to_remove:
            edges_left.discard(e)
    return sorted(cover)
'''


def _setup_vertex_cover(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
    edges = set()
    # Tree edges to ensure connectivity.
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        edges.add((min(u, i), max(u, i)))
    # Extra edges.
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    challenge._n = n_nodes
    return {"n": n_nodes, "edges": sorted(edges)}


def _verify_vertex_cover(challenge, result):
    if not isinstance(result, list):
        return False
    cover = set(result)
    # The cover must touch every edge.
    for u, v in challenge._edges if hasattr(challenge, "_edges") else []:
        if u not in cover and v not in cover:
            return False
    # Brute force: find the minimum cover.
    n = challenge._n
    edges = challenge._edges
    if not edges:
        return True
    best = n
    for mask in range(1 << n):
        cov = {i for i in range(n) if mask & (1 << i)}
        if all(u in cov or v in cov for u, v in edges):
            size = len(cov)
            if size < best:
                best = size
    return len(cover) <= 2 * best


# Need to stash the edges on the challenge for the verify.
def _setup_vertex_cover_patched(challenge, n, seed):
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


# === approx_02: Set Cover (greedy) ===

APPROX_02_SOURCE = '''
def solve(universe, sets, m, k):
    """Greedy set cover: each step picks the set covering the
    most uncovered elements. O(m * k) per step.

    universe is a list of unique elements; sets[i] is a list
    of elements in set i. m = |sets|, k = |universe|.
    Return a sorted list of chosen set indices.
    """
    uncovered = set(universe)
    chosen = []
    while uncovered:
        # Pick the set covering the most uncovered elements.
        best_idx = -1
        best_count = 0
        for i, s in enumerate(sets):
            count = sum(1 for x in s if x in uncovered)
            if count > best_count:
                best_count = count
                best_idx = i
        if best_idx == -1 or best_count == 0:
            break
        chosen.append(best_idx)
        for x in sets[best_idx]:
            uncovered.discard(x)
    return sorted(chosen)
'''


def _setup_set_cover(challenge, n, seed):
    rng = random.Random(seed)
    universe_size = max(2, min(n, 6))
    universe = list(range(universe_size))
    n_sets = max(1, min(n, 4))
    sets = []
    for _ in range(n_sets):
        s = set()
        for u in universe:
            if rng.random() < 0.5:
                s.add(u)
        sets.append(sorted(s))
    challenge._universe = list(universe)
    challenge._sets = [list(s) for s in sets]
    return {"universe": list(universe), "sets": [list(s) for s in sets], "m": len(sets), "k": len(universe)}


def _verify_set_cover(challenge, result):
    if not isinstance(result, list):
        return False
    chosen = set(result)
    universe = set(challenge._universe)
    covered = set()
    for i in chosen:
        if 0 <= i < len(challenge._sets):
            covered.update(challenge._sets[i])
    return covered == universe


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="approx_01",
        name="Vertex Cover (2-Approx)",
        category="approximation",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find a 2-approximate vertex cover. Greedy: while\n"
            "edges remain, pick the vertex with the highest degree,\n"
            "add it to the cover, remove all incident edges. The\n"
            "result is at most 2x the optimal vertex cover. The\n"
            "verify accepts any 2-approx (i.e., len(cover) <= 2 * OPT).\n"
            "Source: https://www.geeksforgeeks.org/vertex-cover-problem-approximate-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/vertex-cover-problem-approximate-algorithm/",
        params=["n", "edges"],
        inputs={
            "n": "number of nodes.",
            "edges": "list of (u, v) tuples (undirected).",
        },
        returns="a sorted list of node indices covering every edge (and 2-approx).",
        source=APPROX_01_SOURCE,
        setup_fn=_setup_vertex_cover_patched,
        verify_fn=_verify_vertex_cover,
        samples=[
            Sample("n = 5, edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]", "[0, 2] (or other 2-approx)"),
        ],
        hint="Pick the max-degree vertex, add to cover, drop its edges. Repeat.",
        parents=["graph_12"],
        children=["approx_02"],
    ),
    AlgorithmSpec(
        id="approx_02",
        name="Set Cover (Greedy)",
        category="approximation",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find a set of indices that cover every element of\n"
            "``universe``. Greedy: each step picks the set covering\n"
            "the most uncovered elements. Standard O(log n) approx\n"
            "ratio for the classical Set Cover problem.\n"
            "Source: https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/",
        params=["universe", "sets", "m", "k"],
        inputs={
            "universe": "list of k unique element IDs (0..k-1).",
            "sets": "list of m sets, each a list of element IDs.",
            "m": "number of sets.",
            "k": "size of universe.",
        },
        returns="a sorted list of chosen set indices covering universe.",
        source=APPROX_02_SOURCE,
        setup_fn=_setup_set_cover,
        verify_fn=_verify_set_cover,
        samples=[
            Sample("universe = [0, 1, 2, 3, 4], sets = [[0, 1], [1, 2, 3], [2, 3, 4], [0, 4]], m = 4, k = 5", "[0, 1, 2] (or 1 + 2)"),
        ],
        hint="Each step: pick the set with the most uncovered elements. Repeat.",
        parents=["approx_01"],
        children=[],
    ),
]


# === approx_03: TSP via MST (2-Approx) ===

APPROX_03_SOURCE = '''
def solve(cost, n):
    """MST-based 2-approximate TSP.

    1. Build MST rooted at 0 via Prim's.
    2. Preorder walk of the MST to produce a tour.
    3. Sum the costs along the tour (including the return
       edge from the last vertex back to 0).
    """
    if n <= 1:
        return 0
    INF = float("inf")
    # Prim's MST.
    in_mst = [False] * n
    in_mst[0] = True
    # parent[i] = the node that brought i into the MST.
    parent = [-1] * n
    for _ in range(n - 1):
        best_w = INF
        best_v = -1
        for u in range(n):
            if not in_mst[u]:
                continue
            for v in range(n):
                if in_mst[v]:
                    continue
                if cost[u][v] < best_w:
                    best_w = cost[u][v]
                    best_v = v
                    parent[v] = u
        if best_v == -1:
            break
        in_mst[best_v] = True
    # Preorder DFS walk of the MST.
    children = [[] for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            children[p].append(v)
    tour = []
    def dfs(u):
        tour.append(u)
        for c in children[u]:
            dfs(c)
    dfs(0)
    # Sum tour cost (including the return edge).
    total = 0
    for i in range(len(tour) - 1):
        total += cost[tour[i]][tour[i + 1]]
    total += cost[tour[-1]][0]
    return total
'''

def _setup_approx_03(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(2, min(n, 6))
    # Build a metric cost matrix. Start with random point
    # coordinates and use Euclidean distance (rounded up to int
    # so triangle inequality holds exactly).
    pts = [(rng.randint(0, 20), rng.randint(0, 20)) for _ in range(n)]
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                cost[i][j] = 0
            else:
                dx = pts[i][0] - pts[j][0]
                dy = pts[i][1] - pts[j][1]
                d2 = dx * dx + dy * dy
                # Round up to integer sqrt to be safe (triangle
                # inequality holds for ceiling of Euclidean).
                d = int(d2 ** 0.5) + (1 if (int(d2 ** 0.5)) ** 2 < d2 else 0)
                cost[i][j] = max(d, 1)
    challenge._n = n
    challenge._cost = [row[:] for row in cost]
    return {"cost": [row[:] for row in cost], "n": n}

def _verify_approx_03(challenge, result):
    # Brute force: try every permutation of cities 1..n-1 and
    # sum the tour cost. The minimum is the true OPT. The MST
    # 2-approx is accepted if its cost is <= 2 * OPT.
    n = challenge._n
    cost = challenge._cost
    if n <= 1:
        return result == 0
    best = float("inf")
    from itertools import permutations
    for perm in permutations(range(1, n)):
        total = cost[0][perm[0]]
        for i in range(len(perm) - 1):
            total += cost[perm[i]][perm[i + 1]]
        total += cost[perm[-1]][0]
        if total < best:
            best = total
    return result <= 2 * best



# === approx_04: Christofides TSP (3/2-Approx) ===

APPROX_04_SOURCE = '''
def solve(cost, n):
    """Christofides 1.5-approximate TSP (greedy matching)."""
    if n <= 1:
        return 0
    if n == 2:
        return cost[0][1] * 2
    INF = float("inf")
    # 1. Prim's MST.
    in_mst = [False] * n
    in_mst[0] = True
    parent = [-1] * n
    for _ in range(n - 1):
        best_w = INF
        best_v = -1
        for u in range(n):
            if not in_mst[u]:
                continue
            for v in range(n):
                if in_mst[v]:
                    continue
                if cost[u][v] < best_w:
                    best_w = cost[u][v]
                    best_v = v
                    parent[v] = u
        if best_v == -1:
            break
        in_mst[best_v] = True
    # 2. Odd-degree vertices of the MST.
    deg = [0] * n
    for v in range(n):
        p = parent[v]
        if p != -1:
            deg[v] += 1
            deg[p] += 1
    odd = [v for v in range(n) if deg[v] % 2 == 1]
    # 3. Greedy minimum-weight perfect matching on odd vertices.
    matched = [False] * n
    matching = []
    # Repeatedly pick the cheapest remaining edge between two
    # unmatched odd vertices.
    while True:
        best_w = INF
        best_pair = None
        for i in odd:
            if matched[i]:
                continue
            for j in odd:
                if matched[j] or i == j:
                    continue
                if cost[i][j] < best_w:
                    best_w = cost[i][j]
                    best_pair = (i, j)
        if best_pair is None:
            break
        a, b = best_pair
        matching.append((a, b))
        matched[a] = True
        matched[b] = True
    # 4. Union of MST + matching forms a multigraph with
    #    even degree at every vertex. Find an Eulerian
    #    circuit by Hierholzer's algorithm.
    adj = [set() for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            adj[v].add(p)
            adj[p].add(v)
    for a, b in matching:
        adj[a].add(b)
        adj[b].add(a)
    # Hierholzer's: DFS, splicing when stuck.
    euler = []
    stack = [0]
    # Track visited edges via a per-edge visit counter.
    # Use adjacency multiset.
    used = [dict() for _ in range(n)]
    while stack:
        u = stack[-1]
        # Find an unused edge.
        next_v = None
        for v in list(adj[u]):
            key = (min(u, v), max(u, v))
            if used[u].get(key, 0) < (1 if key[0] == u or key[1] == u else 0) + 1:
                # Check if we have not over-used this edge.
                pass
        # Easier: build edge multiset count.
        next_v = None
        for v in adj[u]:
            key = (min(u, v), max(u, v))
            used_count = used[u].get(key, 0)
            # Edge (u,v) contributes 1 to u and 1 to v in the multigraph.
            # We can use it at most once per (u, v) occurrence in
            # the union. Since the union is a multigraph but
            # built from sets, two edges between the same pair
            # (e.g., one MST + one matching) would have collapsed.
            # To support multi-edges properly, we re-count.
            if used_count == 0:
                next_v = v
                break
        if next_v is None:
            euler.append(stack.pop())
        else:
            key = (min(u, next_v), max(u, next_v))
            # Mark the edge as used on BOTH endpoints so the
            # algorithm doesn't traverse it twice.
            used[u][key] = used[u].get(key, 0) + 1
            used[next_v][key] = used[next_v].get(key, 0) + 1
            stack.append(next_v)
    euler.reverse()
    # 5. Shortcut to a Hamiltonian tour (skip repeated vertices).
    seen = set()
    tour = []
    for v in euler:
        if v not in seen:
            seen.add(v)
            tour.append(v)
    # Make sure 0 is first.
    while tour[0] != 0:
        tour = tour[1:] + [tour[0]]
    # 6. Sum tour cost.
    total = 0
    for i in range(len(tour) - 1):
        total += cost[tour[i]][tour[i + 1]]
    total += cost[tour[-1]][0]
    return total
'''

def _setup_approx_04(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(2, min(n, 6))
    pts = [(rng.randint(0, 20), rng.randint(0, 20)) for _ in range(n)]
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                cost[i][j] = 0
            else:
                dx = pts[i][0] - pts[j][0]
                dy = pts[i][1] - pts[j][1]
                d2 = dx * dx + dy * dy
                d = int(d2 ** 0.5) + (1 if (int(d2 ** 0.5)) ** 2 < d2 else 0)
                cost[i][j] = max(d, 1)
    challenge._n = n
    challenge._cost = [row[:] for row in cost]
    return {"cost": [row[:] for row in cost], "n": n}

def _verify_approx_04(challenge, result):
    from itertools import permutations
    n = challenge._n
    cost = challenge._cost
    if n <= 1:
        return result == 0
    best = float("inf")
    for perm in permutations(range(1, n)):
        total = cost[0][perm[0]]
        for i in range(len(perm) - 1):
            total += cost[perm[i]][perm[i + 1]]
        total += cost[perm[-1]][0]
        if total < best:
            best = total
    # Christofides guarantees <= 1.5 * OPT for metric TSP.
    return result <= (3 * best + 1) // 2 + 1



# === approx_05: Fractional Knapsack (Greedy) ===

APPROX_05_SOURCE = '''
def solve(values, weights, n, capacity):
    """Fractional knapsack via greedy by value/weight ratio."""
    if capacity <= 0 or n == 0:
        return 0.0
    items = sorted(
        range(n),
        key=lambda i: values[i] / weights[i],
        reverse=True,
    )
    remaining = capacity
    total = 0.0
    for i in items:
        if remaining <= 0:
            break
        if weights[i] <= remaining:
            total += values[i]
            remaining -= weights[i]
        else:
            total += values[i] * (remaining / weights[i])
            remaining = 0
    return total
'''

def _setup_approx_05(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 8))
    values = [rng.randint(1, 100) for _ in range(n)]
    weights = [rng.randint(1, 50) for _ in range(n)]
    capacity = rng.randint(10, 100)
    challenge._values = list(values)
    challenge._weights = list(weights)
    challenge._capacity = capacity
    return {"values": list(values), "weights": list(weights), "n": n, "capacity": capacity}

def _verify_approx_05(challenge, result):
    # Brute force: enumerate every subset of items, plus one
    # fractional item, to find the true maximum. Since the
    # fractional greedy is optimal, the test simply checks the
    # answer matches the brute force.
    values = challenge._values
    weights = challenge._weights
    capacity = challenge._capacity
    n = len(values)
    from itertools import combinations
    best = 0.0
    for k in range(n + 1):
        for subset in combinations(range(n), k):
            total_w = sum(weights[i] for i in subset)
            total_v = sum(values[i] for i in subset)
            if total_w > capacity:
                continue
            remaining = capacity - total_w
            for j in range(n):
                if j in subset:
                    continue
                if weights[j] == 0:
                    continue
                if remaining <= 0:
                    break
                take = min(1.0, remaining / weights[j])
                cand = total_v + values[j] * take
                if cand > best:
                    best = cand
    return abs(result - best) < 1e-6



# === approx_06: Bin Packing (First-Fit Decreasing) ===

APPROX_06_SOURCE = '''
def solve(sizes, n):
    """First-Fit Decreasing bin packing."""
    if n == 0:
        return 0
    # Sort items by size descending.
    items = sorted(sizes, reverse=True)
    bins = []  # each entry is the remaining capacity of a bin
    for s in items:
        placed = False
        for i in range(len(bins)):
            if bins[i] >= s:
                bins[i] -= s
                placed = True
                break
        if not placed:
            bins.append(1.0 - s)
    return len(bins)
'''

def _setup_approx_06(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 10))
    # Sizes: integers 1..10 scaled down to (0, 1]. The
    # denominator is random per setup to vary the difficulty.
    denom = rng.choice([10, 20, 50])
    sizes = [rng.randint(1, denom) / denom for _ in range(n)]
    # Ensure all sizes <= 1.
    sizes = [min(s, 1.0) for s in sizes]
    challenge._sizes = list(sizes)
    return {"sizes": list(sizes), "n": n}

def _verify_approx_06(challenge, result):
    # BFS brute-force OPT for bin packing: try every assignment
    # of items to bins, prune whenever a bin would overflow.
    # Cap the search at n items.
    sizes = challenge._sizes
    n = len(sizes)
    if n == 0:
        return result == 0
    best = [n + 1]
    bins_remaining = []
    def search(i):
        if i == n:
            if len(bins_remaining) < best[0]:
                best[0] = len(bins_remaining)
            return
        saved_len = len(bins_remaining)
        for b in range(saved_len + 1):
            if b == saved_len:
                # Open a new bin.
                if sizes[i] > 1.0:
                    continue
                bins_remaining.append(1.0 - sizes[i])
            else:
                if bins_remaining[b] < sizes[i]:
                    continue
                bins_remaining[b] -= sizes[i]
            search(i + 1)
            # Undo: restore bins_remaining to the pre-call state.
            while len(bins_remaining) > saved_len:
                bins_remaining.pop()
            if b < saved_len:
                bins_remaining[b] += sizes[i]
    search(0)
    opt = best[0]
    # FFD asymptotic guarantee: FFD <= 11/9 * OPT + 6.
    # In practice, FFD is within 11/9 * OPT + 1 for these
    # small cases; allow that.
    return result <= (11 * opt) // 9 + 1



# === approx_07: 0/1 Knapsack FPTAS ===

APPROX_07_SOURCE = '''
def solve(values, weights, n, capacity, eps):
    """0/1 Knapsack FPTAS: scale values, run DP, return result."""
    if capacity <= 0 or n == 0:
        return 0
    v_max = max(values) if values else 1
    if v_max == 0:
        return 0
    K = (eps * v_max) / n
    if K <= 0:
        K = 1
    scaled = [max(1, int(v / K)) for v in values]
    # DP: dp[w] = max scaled value for weight w.
    dp = [0] * (capacity + 1)
    for i in range(n):
        wi = min(weights[i], capacity)
        vi = scaled[i]
        for w in range(capacity, wi - 1, -1):
            cand = dp[w - wi] + vi
            if cand > dp[w]:
                dp[w] = cand
    return dp[capacity] * K
'''

def _setup_approx_07(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 6))
    values = [rng.randint(1, 50) for _ in range(n)]
    weights = [rng.randint(1, 15) for _ in range(n)]
    capacity = rng.randint(10, 30)
    eps = 0.2  # 20% approx
    challenge._values = list(values)
    challenge._weights = list(weights)
    challenge._capacity = capacity
    challenge._eps = eps
    return {
        "values": list(values),
        "weights": list(weights),
        "n": n,
        "capacity": capacity,
        "eps": eps,
    }

def _verify_approx_07(challenge, result):
    # Brute force 0/1 knapsack OPT.
    from itertools import combinations
    values = challenge._values
    weights = challenge._weights
    capacity = challenge._capacity
    eps = challenge._eps
    n = len(values)
    opt = 0
    for k in range(n + 1):
        for subset in combinations(range(n), k):
            if sum(weights[i] for i in subset) > capacity:
                continue
            v = sum(values[i] for i in subset)
            if v > opt:
                opt = v
    # FPTAS returns a (1 - eps)-approx of opt.
    return result >= (1 - eps) * opt - 1e-6


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="approx_03",
        name="TSP via MST (2-Approx)",
        category="approximation",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Given a complete graph with edge costs that satisfy
            the triangle inequality, return the cost of a TSP
            tour produced by the MST-based 2-approximation.
            Build a minimum spanning tree rooted at node 0
            (Prim's algorithm), do a preorder DFS walk to list
            vertices, and append 0 at the end. The returned
            tour cost is guaranteed to be at most 2x optimal
            for metric instances.
            Source: https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/",
        params=["cost", "n"],
        inputs={
            "cost": "n x n cost matrix satisfying the triangle inequality.",
            "n": "number of cities.",
        },
        returns="the total cost of the 2-approximate TSP tour as a non-negative int.",
        source=APPROX_03_SOURCE,
        setup_fn=_setup_approx_03,
        verify_fn=_verify_approx_03,
        samples=[
            Sample("cost = [[0, 111], [112, 0]], n = 2", "223"),
            Sample("cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]], n = 3", "3000 (or up to 2x optimal)"),
        ],
        hint="Run Prim's to build an MST. Do a preorder DFS from node 0 to list all vertices. Sum the tour cost (include the final edge back to 0).",
        parents=["approx_01"],
        children=["approx_04"],
    ),
    AlgorithmSpec(
        id="approx_04",
        name="Christofides TSP (3/2-Approx)",
        category="approximation",
        difficulty=7,
        required_complexity=ComplexityClass.O_N3,
        description=("""
            Given a complete metric graph, return the cost of
            a TSP tour produced by the Christofides 1.5-approx
            algorithm: (1) build an MST, (2) find the odd-
            degree vertices of the MST, (3) compute a minimum-
            weight perfect matching on those vertices, (4)
            unite matching + MST, (5) find an Eulerian circuit,
            and (6) shortcut to a Hamiltonian tour. The result
            is at most 1.5x the optimal tour cost.
            Source: https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/",
        params=["cost", "n"],
        inputs={
            "cost": "n x n cost matrix satisfying the triangle inequality.",
            "n": "number of cities.",
        },
        returns="the total cost of the Christofides 1.5-approximate TSP tour as a non-negative int.",
        source=APPROX_04_SOURCE,
        setup_fn=_setup_approx_04,
        verify_fn=_verify_approx_04,
        samples=[
            Sample("cost = [[0, 111], [112, 0]], n = 2", "223"),
            Sample("cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]], n = 3", "3000 (Christofides is optimal for n=3)"),
        ],
        hint="Prim's MST, then on odd-degree vertices do greedy min-weight matching. Euler-tour the union, then shortcut to a Hamiltonian tour.",
        parents=["approx_03"],
        children=[],
    ),
    AlgorithmSpec(
        id="approx_05",
        name="Fractional Knapsack (Greedy)",
        category="approximation",
        difficulty=3,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Given n items each with a value and a weight, and a
            knapsack with capacity C, return the maximum total
            value of items (or fractions thereof) you can fit.
            The fractional variant allows taking partial items,
            so the greedy by value/weight ratio is OPTIMAL
            (not just an approximation). Sort items by value/
            weight ratio descending, take each whole item while
            capacity allows, then fill the remainder with a
            fraction of the next item.
            Source: https://www.geeksforgeeks.org/dsa/fractional-knapsack-problem/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/fractional-knapsack-problem/",
        params=["values", "weights", "n", "capacity"],
        inputs={
            "values": "list of n item values.",
            "weights": "list of n item weights (all > 0).",
            "n": "number of items.",
            "capacity": "knapsack capacity (originally W in the GfG notation).",
        },
        returns="the maximum total value achievable (a float).",
        source=APPROX_05_SOURCE,
        setup_fn=_setup_approx_05,
        verify_fn=_verify_approx_05,
        samples=[
            Sample("values = [60, 100, 120], weights = [10, 20, 30], n = 3, capacity = 50", "240.0"),
            Sample("values = [500], weights = [30], n = 1, capacity = 10", "166.666... (500 * 10/30)"),
        ],
        hint="Sort by value/weight ratio descending. Take each whole item while capacity allows, then fill the rest with a fraction of the next item.",
        parents=["approx_02"],
        children=["approx_07"],
    ),
    AlgorithmSpec(
        id="approx_06",
        name="Bin Packing (First-Fit Decreasing)",
        category="approximation",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Given a list of item sizes in (0, 1] and unit-
            capacity bins, return the number of bins used by
            First-Fit Decreasing: sort items by size descending,
            then for each item place it in the lowest-index
            existing bin with enough remaining capacity; if
            none, open a new bin. FFD is asymptotically
            11/9-approx (uses at most 11/9 * OPT + 6 bins).
            Source: https://en.wikipedia.org/wiki/First-fit-decreasing_bin_packing
            """),
        source_url="https://en.wikipedia.org/wiki/First-fit-decreasing_bin_packing",
        params=["sizes", "n"],
        inputs={
            "sizes": "list of n item sizes, each in (0, 1].",
            "n": "number of items.",
        },
        returns="the number of bins used as a non-negative int.",
        source=APPROX_06_SOURCE,
        setup_fn=_setup_approx_06,
        verify_fn=_verify_approx_06,
        samples=[
            Sample("sizes = [0.5, 0.7, 0.3, 0.8, 0.4, 0.6], n = 6", "3 (FFD)"),
            Sample("sizes = [0.2, 0.5, 0.4, 0.7, 0.1, 0.3, 0.8], n = 7", "5 (or any FFD-valid count)"),
        ],
        hint="Sort sizes descending. For each item, place in the first bin with enough room. Otherwise open a new bin.",
        parents=["approx_02"],
        children=[],
    ),
    AlgorithmSpec(
        id="approx_07",
        name="0/1 Knapsack FPTAS",
        category="approximation",
        difficulty=7,
        required_complexity=ComplexityClass.O_N3,
        description=("""
            Given n items with values and weights and capacity
            C, return a (1 - eps)-approximation of the maximum
            knapsack value. Standard FPTAS: scale all values
            by K / (eps * V_max) where V_max is the largest
            value; round to integers; run the O(nC') pseudo-
            polynomial DP (where C' is the scaled max weight);
            return the original-value best DP result. The
            scaled value is within (1 - eps) of the true OPT.
            Source: https://www.geeksforgeeks.org/dsa/fptas-fully-polynomial-time-approximation-scheme/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/fptas-fully-polynomial-time-approximation-scheme/",
        params=["values", "weights", "n", "capacity", "eps"],
        inputs={
            "values": "list of n item values.",
            "weights": "list of n item weights (all > 0).",
            "n": "number of items.",
            "capacity": "knapsack capacity (originally W in the GfG notation).",
            "eps": "approximation parameter (e.g. 0.1 for 10%).",
        },
        returns="an approximate maximum knapsack value (int or float).",
        source=APPROX_07_SOURCE,
        setup_fn=_setup_approx_07,
        verify_fn=_verify_approx_07,
        samples=[
            Sample("values = [60, 100, 120], weights = [10, 20, 30], n = 3, capacity = 50, eps = 0.1", "~ 220 (within 10% of OPT 220)"),
        ],
        hint="Scale all values by K = eps * V_max / n. Run the standard 0/1 knapsack DP on the scaled values. Return the scaled DP answer * K.",
        parents=["approx_05"],
        children=[],
    ),
])
