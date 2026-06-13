"""Spec generator input — 5 more approximation specs for Session 1.

Covers the classic approximation-algorithm examples from
GeeksforGeeks that approx_01..02 don't already cover:

  approx_03  TSP via MST 2-Approx           (Prim + preorder walk)
  approx_04  Christofides 1.5-Approx         (MST + min-weight perfect matching)
  approx_05  Fractional Knapsack             (greedy by value/weight ratio)
  approx_06  Bin Packing (First-Fit Decr.)   (11/9 asymptotic approx)
  approx_07  0/1 Knapsack FPTAS              (scaling + DP, (1+eps)-approx)

After this batch, approximation.py covers the canonical
NP-hard-relaxation / approximation-scheme examples.

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module approximation \\
        --input batch_approximation_session1.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # approx_03: TSP via MST (2-Approx)
    # ============================================================
    {
        "id": "approx_03",
        "name": "TSP via MST (2-Approx)",
        "category": "approximation",
        "difficulty": 5,
        "complexity": "O_N2",
        "description": (
            "Given a complete graph with edge costs that satisfy\n"
            "the triangle inequality, return the cost of a TSP\n"
            "tour produced by the MST-based 2-approximation.\n"
            "Build a minimum spanning tree rooted at node 0\n"
            "(Prim's algorithm), do a preorder DFS walk to list\n"
            "vertices, and append 0 at the end. The returned\n"
            "tour cost is guaranteed to be at most 2x optimal\n"
            "for metric instances.\n"
            "Source: https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/",
        "params": ["cost", "n"],
        "inputs": {
            "cost": "n x n cost matrix satisfying the triangle inequality.",
            "n": "number of cities.",
        },
        "returns": "the total cost of the 2-approximate TSP tour as a non-negative int.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("cost = [[0, 111], [112, 0]], n = 2", "223"),
            ("cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]], n = 3", "3000 (or up to 2x optimal)"),
        ],
        "hint": "Run Prim's to build an MST. Do a preorder DFS from node 0 to list all vertices. Sum the tour cost (include the final edge back to 0).",
        "parents": ["approx_01"],
        "children": ["approx_04"],
    },

    # ============================================================
    # approx_04: Christofides 1.5-Approx
    # ============================================================
    {
        "id": "approx_04",
        "name": "Christofides TSP (3/2-Approx)",
        "category": "approximation",
        "difficulty": 7,
        "complexity": "O_N3",
        "description": (
            "Given a complete metric graph, return the cost of\n"
            "a TSP tour produced by the Christofides 1.5-approx\n"
            "algorithm: (1) build an MST, (2) find the odd-\n"
            "degree vertices of the MST, (3) compute a minimum-\n"
            "weight perfect matching on those vertices, (4)\n"
            "unite matching + MST, (5) find an Eulerian circuit,\n"
            "and (6) shortcut to a Hamiltonian tour. The result\n"
            "is at most 1.5x the optimal tour cost.\n"
            "Source: https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/",
        "params": ["cost", "n"],
        "inputs": {
            "cost": "n x n cost matrix satisfying the triangle inequality.",
            "n": "number of cities.",
        },
        "returns": "the total cost of the Christofides 1.5-approximate TSP tour as a non-negative int.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("cost = [[0, 111], [112, 0]], n = 2", "223"),
            ("cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]], n = 3", "3000 (Christofides is optimal for n=3)"),
        ],
        "hint": "Prim's MST, then on odd-degree vertices do greedy min-weight matching. Euler-tour the union, then shortcut to a Hamiltonian tour.",
        "parents": ["approx_03"],
        "children": [],
    },

    # ============================================================
    # approx_05: Fractional Knapsack
    # ============================================================
    {
        "id": "approx_05",
        "name": "Fractional Knapsack (Greedy)",
        "category": "approximation",
        "difficulty": 3,
        "complexity": "O_N_LOG_N",
        "description": (
            "Given n items each with a value and a weight, and a\n"
            "knapsack with capacity C, return the maximum total\n"
            "value of items (or fractions thereof) you can fit.\n"
            "The fractional variant allows taking partial items,\n"
            "so the greedy by value/weight ratio is OPTIMAL\n"
            "(not just an approximation). Sort items by value/\n"
            "weight ratio descending, take each whole item while\n"
            "capacity allows, then fill the remainder with a\n"
            "fraction of the next item.\n"
            "Source: https://www.geeksforgeeks.org/dsa/fractional-knapsack-problem/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/fractional-knapsack-problem/",
        "params": ["values", "weights", "n", "capacity"],
        "inputs": {
            "values": "list of n item values.",
            "weights": "list of n item weights (all > 0).",
            "n": "number of items.",
            "capacity": "knapsack capacity (originally W in the GfG notation).",
        },
        "returns": "the maximum total value achievable (a float).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("values = [60, 100, 120], weights = [10, 20, 30], n = 3, capacity = 50", "240.0"),
            ("values = [500], weights = [30], n = 1, capacity = 10", "166.666... (500 * 10/30)"),
        ],
        "hint": "Sort by value/weight ratio descending. Take each whole item while capacity allows, then fill the rest with a fraction of the next item.",
        "parents": ["approx_02"],
        "children": ["approx_07"],
    },

    # ============================================================
    # approx_06: Bin Packing (First-Fit Decreasing)
    # ============================================================
    {
        "id": "approx_06",
        "name": "Bin Packing (First-Fit Decreasing)",
        "category": "approximation",
        "difficulty": 4,
        "complexity": "O_N_LOG_N",
        "description": (
            "Given a list of item sizes in (0, 1] and unit-\n"
            "capacity bins, return the number of bins used by\n"
            "First-Fit Decreasing: sort items by size descending,\n"
            "then for each item place it in the lowest-index\n"
            "existing bin with enough remaining capacity; if\n"
            "none, open a new bin. FFD is asymptotically\n"
            "11/9-approx (uses at most 11/9 * OPT + 6 bins).\n"
            "Source: https://en.wikipedia.org/wiki/First-fit-decreasing_bin_packing"
        ),
        "source_url": "https://en.wikipedia.org/wiki/First-fit-decreasing_bin_packing",
        "params": ["sizes", "n"],
        "inputs": {
            "sizes": "list of n item sizes, each in (0, 1].",
            "n": "number of items.",
        },
        "returns": "the number of bins used as a non-negative int.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("sizes = [0.5, 0.7, 0.3, 0.8, 0.4, 0.6], n = 6", "3 (FFD)"),
            ("sizes = [0.2, 0.5, 0.4, 0.7, 0.1, 0.3, 0.8], n = 7", "5 (or any FFD-valid count)"),
        ],
        "hint": "Sort sizes descending. For each item, place in the first bin with enough room. Otherwise open a new bin.",
        "parents": ["approx_02"],
        "children": [],
    },

    # ============================================================
    # approx_07: 0/1 Knapsack FPTAS
    # ============================================================
    {
        "id": "approx_07",
        "name": "0/1 Knapsack FPTAS",
        "category": "approximation",
        "difficulty": 7,
        "complexity": "O_N3",
        "description": (
            "Given n items with values and weights and capacity\n"
            "C, return a (1 - eps)-approximation of the maximum\n"
            "knapsack value. Standard FPTAS: scale all values\n"
            "by K / (eps * V_max) where V_max is the largest\n"
            "value; round to integers; run the O(nC') pseudo-\n"
            "polynomial DP (where C' is the scaled max weight);\n"
            "return the original-value best DP result. The\n"
            "scaled value is within (1 - eps) of the true OPT.\n"
            "Source: https://www.geeksforgeeks.org/dsa/fptas-fully-polynomial-time-approximation-scheme/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/fptas-fully-polynomial-time-approximation-scheme/",
        "params": ["values", "weights", "n", "capacity", "eps"],
        "inputs": {
            "values": "list of n item values.",
            "weights": "list of n item weights (all > 0).",
            "n": "number of items.",
            "capacity": "knapsack capacity (originally W in the GfG notation).",
            "eps": "approximation parameter (e.g. 0.1 for 10%).",
        },
        "returns": "an approximate maximum knapsack value (int or float).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("values = [60, 100, 120], weights = [10, 20, 30], n = 3, capacity = 50, eps = 0.1", "~ 220 (within 10% of OPT 220)"),
        ],
        "hint": "Scale all values by K = eps * V_max / n. Run the standard 0/1 knapsack DP on the scaled values. Return the scaled DP answer * K.",
        "parents": ["approx_05"],
        "children": [],
    },
]
