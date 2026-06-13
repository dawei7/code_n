"""Spec generator input - 5 more randomized specs for Session 1.

Covers the GfG randomized-algorithms topic list that
randomized_01..02 (Quicksort + Reservoir Sampling) don't
already cover:

  randomized_03  Fisher-Yates Shuffle         (Las Vegas, O(n))
  randomized_04  Randomized Binary Search     (Las Vegas, O(log n) expected)
  randomized_05  Karger's Min-Cut            (Monte Carlo, O(E))
  randomized_06  Estimating Pi via Monte Carlo (Monte Carlo, O(k))
  randomized_07  Freivald's Matrix-Product Check (Monte Carlo, O(kn^2))

After this batch, randomized.py covers the canonical
Las Vegas + Monte Carlo algorithm examples from GfG.

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module randomized \\
        --input batch_randomized_session1.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # randomized_03: Fisher-Yates Shuffle
    # ============================================================
    {
        "id": "randomized_03",
        "name": "Fisher-Yates Shuffle",
        "category": "randomized",
        "difficulty": 3,
        "complexity": "O_N",
        "description": (
            "Given an array of n elements, return a uniformly\n"
            "random permutation of the array using the\n"
            "Fisher-Yates shuffle (a.k.a. Knuth shuffle): for i\n"
            "from n-1 down to 1, pick a random j in [0, i] and\n"
            "swap a[i] with a[j]. O(n) time, O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/dsa/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/",
        "params": ["arr", "n"],
        "inputs": {
            "arr": "list of n elements to shuffle.",
            "n": "length of arr.",
        },
        "returns": "a new list of n elements which is a random permutation of arr.",
        "solve": '''
def solve(arr, n):
    """Fisher-Yates shuffle. Returns a new list."""
    import random
    work = list(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        work[i], work[j] = work[j], work[i]
    return work
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 12))
arr = [rng.randint(0, 99) for _ in range(n)]
challenge._arr = list(arr)
return {"arr": list(arr), "n": n}
''',
        "verify": '''
# Verify the result is a permutation of the input.
arr = challenge._arr
if not isinstance(result, list) or len(result) != len(arr):
    return False
return sorted(result) == sorted(arr)
''',
        "samples": [
            ("arr = [1, 2, 3, 4, 5, 6, 7, 8], n = 8", "a random permutation of [1..8]"),
            ("arr = [42], n = 1", "[42]"),
        ],
        "hint": "For i from n-1 down to 1: pick random j in [0, i], swap a[i] and a[j].",
        "parents": ["randomized_01"],
        "children": ["randomized_04"],
    },

    # ============================================================
    # randomized_04: Randomized Binary Search
    # ============================================================
    {
        "id": "randomized_04",
        "name": "Randomized Binary Search",
        "category": "randomized",
        "difficulty": 4,
        "complexity": "O_LOG_N",
        "description": (
            "Given a sorted list of n distinct integers and a\n"
            "query value, return the index of the query in the\n"
            "list (0-indexed) or -1 if not found. Instead of\n"
            "the standard deterministic binary search that\n"
            "always picks the middle, the randomized variant\n"
            "picks a uniformly random index in the current\n"
            "search range [lo, hi] as the pivot each step.\n"
            "Expected O(log n) time; O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/dsa/randomized-binary-search-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/randomized-binary-search-algorithm/",
        "params": ["arr", "n", "target"],
        "inputs": {
            "arr": "list of n distinct integers, sorted ascending.",
            "n": "length of arr.",
            "target": "value to search for.",
        },
        "returns": "the index of target in arr (0-indexed), or -1 if not present.",
        "solve": '''
def solve(arr, n, target):
    """Randomized binary search.

    Pick a uniformly random pivot in [lo, hi], then narrow
    the range based on whether arr[pivot] is less than,
    greater than, or equal to target. Expected O(log n).
    """
    import random
    if n == 0:
        return -1
    lo, hi = 0, n - 1
    while lo <= hi:
        pivot = random.randint(lo, hi)
        if arr[pivot] == target:
            return pivot
        if arr[pivot] < target:
            lo = pivot + 1
        else:
            hi = pivot - 1
    return -1
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(2, min(n, 16))
# Build a strictly sorted, distinct array.
arr = sorted(set(rng.randint(0, 99) for _ in range(n * 2)))[:n]
# Pick a target: 50% present, 50% absent.
if rng.random() < 0.5 and arr:
    target = rng.choice(arr)
else:
    # Pick something NOT in arr.
    target = -1
    while target in arr:
        target = rng.randint(-100, 100)
challenge._arr = list(arr)
challenge._target = target
return {"arr": list(arr), "n": n, "target": target}
''',
        "verify": '''
arr = challenge._arr
target = challenge._target
if target in arr:
    return result == arr.index(target)
else:
    return result == -1
''',
        "samples": [
            ("arr = [1, 2, 3, 4, 5, 6, 7, 8], n = 8, target = 5", "4"),
            ("arr = [1, 3, 5, 7, 9], n = 5, target = 100", "-1"),
        ],
        "hint": "Pick a random pivot in [lo, hi]. If arr[pivot] == target, return pivot. Else narrow [lo, hi] based on comparison.",
        "parents": ["randomized_03"],
        "children": [],
    },

    # ============================================================
    # randomized_05: Karger's Min-Cut (Monte Carlo)
    # ============================================================
    {
        "id": "randomized_05",
        "name": "Karger's Min-Cut (Monte Carlo)",
        "category": "randomized",
        "difficulty": 6,
        "complexity": "O_N2",
        "description": (
            "Given an undirected unweighted graph (with\n"
            "potential parallel edges) as a list of (u, v)\n"
            "edges, find a minimum cut (the smallest set of\n"
            "edges whose removal disconnects the graph).\n"
            "Karger's randomized algorithm: contract a random\n"
            "edge until 2 vertices remain; the remaining\n"
            "edges form the cut. The cut produced may NOT be\n"
            "minimum, but the algorithm is run trials times\n"
            "and the minimum cut across all trials is\n"
            "returned. O(E * V * trials) total.\n"
            "Source: https://www.geeksforgeeks.org/dsa/introduction-and-implementation-of-kargers-algorithm-for-minimum-cut/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/introduction-and-implementation-of-kargers-algorithm-for-minimum-cut/",
        "params": ["edges", "n", "trials"],
        "inputs": {
            "edges": "list of (u, v) tuples (0-indexed vertices).",
            "n": "number of vertices in the graph.",
            "trials": "number of independent trials to run.",
        },
        "returns": "the size of the smallest cut found across all trials (int).",
        "solve": '''
def solve(edges, n, trials):
    """Karger's min-cut algorithm with multiple trials.

    Each trial: randomly contract edges until 2 vertices
    remain. The number of remaining edges is the cut size
    for that trial. Return the minimum cut across all
    trials.
    """
    import random
    if n <= 1:
        return 0
    if n == 2:
        return len(edges)
    best = float("inf")
    for _ in range(max(1, trials)):
        # Union-Find: each vertex has a parent representative.
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            r = x
            while parent[r] != r:
                r = parent[r]
            # Path compression.
            while parent[x] != r:
                parent[x], x = r, parent[x]
            return r
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        # Run one trial: shuffle edges and contract until
        # 2 components remain. The contracted multigraph
        # has parallel edges; we model it by keeping all
        # edges and counting "alive" ones.
        live_edges = list(edges)
        random.shuffle(live_edges)
        # Number of components = number of distinct roots.
        num_components = n
        for u, v in live_edges:
            if num_components <= 2:
                break
            ru, rv = find(u), find(v)
            if ru == rv:
                # Self-loop in the contracted graph; ignore.
                continue
            union(ru, rv)
            num_components -= 1
        # Count cut edges: edges (u, v) with find(u) != find(v).
        cut = 0
        for u, v in edges:
            if find(u) != find(v):
                cut += 1
        if cut < best:
            best = cut
    return best
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(2, min(n, 6))
# Build a connected graph by first creating a spanning tree,
# then adding a few extra edges.
# Generate a random tree: parent[i] = rand(0, i-1) for i in 1..n.
parent = [-1] * n
parent[0] = 0
edges = []
for i in range(1, n):
    p = rng.randint(0, i - 1)
    parent[i] = p
    edges.append((p, i))
# Add a few extra edges (still small graph, n <= 6).
for _ in range(n):
    u = rng.randint(0, n - 1)
    v = rng.randint(0, n - 1)
    if u != v:
        edges.append((u, v))
# Number of trials: enough to get a good chance of the
# minimum cut, but small enough to be fast.
trials = max(20, n * 10)
challenge._edges = list(edges)
challenge._n = n
return {"edges": list(edges), "n": n, "trials": trials}
''',
        "verify": '''
# Brute-force: enumerate all subsets of vertices (S, V\\S)
# and find the cut with the smallest number of crossing
# edges. O(2^n) for the partition, O(E) per check.
from itertools import combinations
edges = challenge._edges
n = challenge._n
best = float("inf")
for mask in range(1 << n):
    s = {i for i in range(n) if mask & (1 << i)}
    if not s or len(s) == n:
        continue
    cut = 0
    for u, v in edges:
        if (u in s) != (v in s):
            cut += 1
    if cut < best:
        best = cut
return result == best
''',
        "samples": [
            ("edges = [(0,1),(0,2),(0,3),(1,2),(2,3)], n = 4, trials = 50", "2 (the 4-cycle with the 2 cross-edges)"),
        ],
        "hint": "Each trial: shuffle the edges, then contract one-by-one until 2 components remain. The number of remaining cross-edges is the cut. Run many trials and return the minimum cut found.",
        "parents": ["randomized_04"],
        "children": ["randomized_06"],
    },

    # ============================================================
    # randomized_06: Estimating Pi via Monte Carlo
    # ============================================================
    {
        "id": "randomized_06",
        "name": "Estimating Pi via Monte Carlo",
        "category": "randomized",
        "difficulty": 2,
        "complexity": "O_N",
        "description": (
            "Estimate the value of pi using the Monte Carlo\n"
            "method: sample n uniformly random points in the\n"
            "unit square [0, 1] x [0, 1] and count how many fall\n"
            "inside the quarter unit circle (x^2 + y^2 <= 1).\n"
            "The fraction of points inside, multiplied by 4,\n"
            "estimates pi. As n grows, the estimate converges\n"
            "to pi. O(n) time. The result is a float.\n"
            "Source: https://en.wikipedia.org/wiki/Monte_Carlo_method (referenced in GfG DSA Random)"
        ),
        "source_url": "https://en.wikipedia.org/wiki/Monte_Carlo_method",
        "params": ["n", "seed_value"],
        "inputs": {
            "n": "number of random points to sample.",
            "seed_value": "an integer seed for reproducibility.",
        },
        "returns": "a float estimate of pi (the absolute error vs true pi should be small for large n).",
        "solve": '''
def solve(n, seed_value):
    """Estimate pi via Monte Carlo: count points (x, y) in
    [0, 1]^2 with x^2 + y^2 <= 1, return 4 * (count / n)."""
    import random
    rng = random.Random(seed_value)
    inside = 0
    for _ in range(n):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / n
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(100, min(n, 5000))
seed_value = rng.randint(0, 1000000)
challenge._n = n
challenge._seed_value = seed_value
return {"n": n, "seed_value": seed_value}
''',
        "verify": '''
# Verify the estimate is within a reasonable tolerance of
# the true value of pi. For n >= 100 samples, we expect the
# error to be < 0.5 with very high probability. We use a
# generous tolerance to keep the test robust.
import math
return abs(result - math.pi) < 0.5
''',
        "samples": [
            ("n = 10000, seed_value = 42", "~3.14 (very close to true pi)"),
        ],
        "hint": "Sample (x, y) uniformly in [0, 1]^2. Count how many have x^2 + y^2 <= 1. Return 4 * (count / n).",
        "parents": ["randomized_05"],
        "children": ["randomized_07"],
    },

    # ============================================================
    # randomized_07: Freivald's Matrix Product Verification
    # ============================================================
    {
        "id": "randomized_07",
        "name": "Freivald's Algorithm (Matrix Product Check)",
        "category": "randomized",
        "difficulty": 6,
        "complexity": "O_N2",
        "description": (
            "Given three square n x n matrices A, B, C,\n"
            "determine if C = A * B. Freivald's Monte Carlo\n"
            "algorithm: generate a random n x 1 vector r with\n"
            "entries 0 or 1. Compute p = A * (B * r) - C * r.\n"
            "If p is the zero vector, return True (but this may\n"
            "be a false positive with low probability). Otherwise\n"
            "return False. Repeat trials times and accept if\n"
            "ALL iterations return True (or accept if ANY\n"
            "iteration returns False). O(n^2) per iteration.\n"
            "Source: https://www.geeksforgeeks.org/dsa/freivalds-algorithm/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/freivalds-algorithm/",
        "params": ["mat_a", "mat_b", "mat_c", "size", "trials", "seed_value"],
        "inputs": {
            "mat_a": "n x n matrix of integers (originally 'A' in the GfG notation).",
            "mat_b": "n x n matrix of integers (originally 'B').",
            "mat_c": "n x n matrix of integers (originally 'C').",
            "size": "size of the matrices (originally 'n').",
            "trials": "number of Freivald iterations to run.",
            "seed_value": "an integer seed for reproducibility.",
        },
        "returns": "True if the algorithm believes mat_c = mat_a * mat_b, False otherwise. (False positives are possible but unlikely.)",
        "solve": '''
def solve(mat_a, mat_b, mat_c, size, trials, seed_value):
    """Freivald's algorithm: k iterations of random
    vector r in {0, 1}^n; check if A*(B*r) == C*r.
    """
    import random
    rng = random.Random(seed_value)
    n = size
    A = mat_a
    B = mat_b
    C = mat_c
    for _ in range(max(1, trials)):
        r = [rng.randint(0, 1) for _ in range(n)]
        # Compute B * r.
        Br = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += B[i][j] * r[j]
            Br[i] = s
        # Compute C * r.
        Cr = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += C[i][j] * r[j]
            Cr[i] = s
        # Compute A * (B * r).
        ABr = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += A[i][j] * Br[j]
            ABr[i] = s
        # Check A * (B * r) == C * r componentwise.
        if ABr != Cr:
            return False
    return True
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(2, min(n, 4))
# Generate A, B randomly.
A = [[rng.randint(-3, 3) for _ in range(n)] for _ in range(n)]
B = [[rng.randint(-3, 3) for _ in range(n)] for _ in range(n)]
# With probability 0.5, set C = A*B (correct); otherwise
# C = A*B with one random cell changed (incorrect).
def matmul(X, Y, n):
    return [[sum(X[i][k] * Y[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]
C = matmul(A, B, n)
if rng.random() < 0.5:
    # Make C incorrect by perturbing a cell.
    i = rng.randint(0, n - 1)
    j = rng.randint(0, n - 1)
    C[i][j] += rng.randint(1, 5)
trials = 20
seed_value = rng.randint(0, 1000000)
challenge._A = [row[:] for row in A]
challenge._B = [row[:] for row in B]
challenge._C = [row[:] for row in C]
challenge._n = n
challenge._correct = (A, B, C, n)
# Pre-compute the ground truth.
def _matmul(X, Y, n):
    return [[sum(X[i][k] * Y[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]
truth = (_matmul(A, B, n) == C)
challenge._truth = truth
return {
    "mat_a": [row[:] for row in A],
    "mat_b": [row[:] for row in B],
    "mat_c": [row[:] for row in C],
    "size": n,
    "trials": trials,
    "seed_value": seed_value,
}
''',
        "verify": '''
# Reference: compute the true product and compare to C.
A = challenge._A
B = challenge._B
C = challenge._C
n = challenge._n
def _matmul(X, Y, n):
    return [[sum(X[i][k] * Y[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]
truth = (_matmul(A, B, n) == C)
# Freivald can produce false positives (returning True for a
# non-equal C), but for our small test sizes and 5 trials,
# this is extremely unlikely. We accept Freivald's answer
# if it matches the truth, OR if it returns False (which
# can never be a false positive).
if result is True:
    return truth  # True must mean the truth is True
else:
    return not truth  # False must mean the truth is False
''',
        "samples": [
            ("A = [[1,1],[1,1]], B = [[1,1],[1,1]], C = [[2,2],[2,2]], n = 2, trials = 5, seed_value = 42", "True"),
            ("A = [[1,1],[1,1]], B = [[1,1],[1,1]], C = [[2,2],[2,3]], n = 2, trials = 5, seed_value = 42", "False (C is not A*B)"),
        ],
        "hint": "For each trial: pick a random 0/1 vector r. Compute B*r, then C*r, then A*(B*r). If A*(B*r) != C*r, return False immediately. After all trials, return True.",
        "parents": ["randomized_06"],
        "children": [],
    },
]
