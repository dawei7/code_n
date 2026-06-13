"""Branch and bound algorithms.

Two problems from GFG's branch-and-bound catalog:

  01 0/1 Knapsack        - max value with weight capacity (decision + value)
  02 Job Assignment      - assign n jobs to n workers, min total cost

Both use exhaustive search with a pruning rule (the "bound"
in branch and bound). Setup keeps n small (4-8) so brute-
force verification is fast.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === bb_01: 0/1 Knapsack ===

BB_01_SOURCE = '''\
"""Optimal solution for bb_01: 0/1 Knapsack.

Each item is either in the knapsack or not. Recursive choice
with a capacity check. The setup keeps n small (n <= 8) so
exhaustive search is feasible; a real solver would use DP or
branch-and-bound with a fractional-relaxation upper bound.
"""


def solve(values, weights, capacity, n):
    best = 0

    def helper(i, value, weight):
        nonlocal best
        if i == n:
            if value > best:
                best = value
            return
        # Skip item i.
        helper(i + 1, value, weight)
        # Take item i (only if it fits).
        if weight + weights[i] <= capacity:
            helper(i + 1, value + values[i], weight + weights[i])

    helper(0, 0, 0)
    return best
'''


def _setup_knapsack(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 8))
    values = [rng.randint(1, 20) for _ in range(n)]
    weights = [rng.randint(1, 10) for _ in range(n)]
    capacity = rng.randint(1, max(2, n) * 5)
    challenge._values = list(values)
    challenge._weights = list(weights)
    challenge._capacity = capacity
    return {
        "values": list(values),
        "weights": list(weights),
        "capacity": capacity,
        "n": n,
    }


def _verify_knapsack(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    # Brute-force: enumerate all subsets.
    values = challenge._values
    weights = challenge._weights
    capacity = challenge._capacity
    expected = 0
    for mask in range(1 << len(values)):
        v = 0
        w = 0
        for i in range(len(values)):
            if mask & (1 << i):
                v += values[i]
                w += weights[i]
        if w <= capacity and v > expected:
            expected = v
    return result == expected


# === bb_02: Job Assignment (assignment problem) ===

BB_02_SOURCE = '''\
"""Optimal solution for bb_02: Job Assignment.

Given an n x n cost matrix cost[i][j] = cost to assign job j
to worker i, find the minimum-cost assignment. Brute-force
enumerate all n! permutations of jobs. Setup keeps n small
(n <= 6) so this is tractable.
"""


def solve(cost, n):
    if n == 0:
        return 0
    jobs = list(range(n))
    best = float("inf")

    def helper(worker, used, current):
        nonlocal best
        if worker == n:
            if current < best:
                best = current
            return
        for job in jobs:
            if not used[job]:
                used[job] = True
                helper(worker + 1, used, current + cost[worker][job])
                used[job] = False

    helper(0, [False] * n, 0)
    return best
'''


def _setup_job_assignment(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 6))
    cost = [[rng.randint(1, 20) for _ in range(n)] for _ in range(n)]
    challenge._cost = [row[:] for row in cost]
    return {"cost": [row[:] for row in cost], "n": n}


def _verify_job_assignment(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    cost = challenge._cost
    n = len(cost)
    # Brute-force: try every permutation of jobs.
    from itertools import permutations
    expected = min(
        sum(cost[i][perm[i]] for i in range(n))
        for perm in permutations(range(n))
    )
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="bb_01",
        name="0/1 Knapsack",
        category="branch_and_bound",
        difficulty=5,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Given a list of items (each with a value and a weight) and\n"
            "a knapsack with a weight capacity, return the maximum total\n"
            "value of items you can fit. Each item is either in the\n"
            "knapsack or not. Exhaustive recursive search (a real solver\n"
            "would use DP or branch-and-bound with a fractional relaxation).\n"
            "Source: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/"
        ),
        source_url="https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/",
        params=["values", "weights", "capacity", "n"],
        inputs={
            "values": "list of n values.",
            "weights": "list of n weights (parallel to values).",
            "capacity": "maximum total weight.",
            "n": "number of items.",
        },
        returns="the maximum total value of items that fit in the knapsack.",
        source=BB_01_SOURCE,
        setup_fn=_setup_knapsack,
        verify_fn=_verify_knapsack,
        samples=[
            Sample("values = [60, 100, 120], weights = [10, 20, 30], capacity = 50, n = 3", "220 (items 1+2)"),
            Sample("values = [10, 20, 30], weights = [1, 1, 1], capacity = 2, n = 3", "50 (items 1+2)"),
        ],
        hint="Recurse: skip or take. Only take if weight fits in the remaining capacity.",
        parents=["backtrack_03"],
        children=["bb_02"],
    ),
    AlgorithmSpec(
        id="bb_02",
        name="Job Assignment (Hungarian)",
        category="branch_and_bound",
        difficulty=6,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Given an n x n cost matrix cost[i][j] = cost to assign job j\n"
            "to worker i, find the minimum total cost over all n!\n"
            "permutations of jobs. Brute-force enumeration (real solver:\n"
            "Hungarian algorithm, O(n^3)).\n"
            "Source: https://www.geeksforgeeks.org/job-assignment-problem-set-1/"
        ),
        source_url="https://www.geeksforgeeks.org/job-assignment-problem-set-1/",
        params=["cost", "n"],
        inputs={
            "cost": "n x n cost matrix.",
            "n": "number of workers (= number of jobs).",
        },
        returns="the minimum total assignment cost.",
        source=BB_02_SOURCE,
        setup_fn=_setup_job_assignment,
        verify_fn=_verify_job_assignment,
        samples=[
            Sample("cost = [[9, 2, 7], [6, 4, 3], [5, 8, 1]], n = 3", "10 (workers 0,1,2 -> jobs 1,2,2 sum 2+3+1 = 6, or 0,1,2: 9+4+1=14, best is 0->1, 1->2, 2->0: 2+3+5=10)"),
        ],
        hint="Try every permutation of jobs. Track the minimum total cost seen.",
        parents=["bb_01"],
        children=[],
    ),
]


# === bb_03: 0/1 Knapsack (Least-Cost B&B) ===

BB_03_SOURCE = '''
def solve(values, weights, capacity, n):
    """0/1 Knapsack via Least-Cost Branch and Bound.

    Sort items by value/weight ratio descending. Build a
    priority queue (min-heap by lower bound) of live nodes.
    Each node has level, accumulated value, accumulated weight,
    and an upper bound (fractional knapsack from this level).
    Pop the node with the smallest lower bound; if it is at
    leaf level, update the best. Generate both children
    (exclude and include the next item), compute their bounds,
    and enqueue if they are still promising (UB <= best).
    """
    if n == 0 or capacity <= 0:
        return 0
    # Sort items by value/weight ratio descending.
    order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    v_sorted = [values[i] for i in order]
    w_sorted = [weights[i] for i in order]
    # Precompute suffix sums for the fractional upper bound.
    import heapq
    INF = float("inf")
    best = 0

    def upper_bound(level, cur_value, cur_weight):
        """Fractional knapsack UB from `level` onwards."""
        if cur_weight > capacity:
            return -INF
        value = cur_value
        weight = cur_weight
        for i in range(level, n):
            if weight + w_sorted[i] <= capacity:
                weight += w_sorted[i]
                value += v_sorted[i]
            else:
                # Take a fraction of item i.
                frac = (capacity - weight) / w_sorted[i]
                value += v_sorted[i] * frac
                break
        return value

    def lower_bound(level, cur_value, cur_weight):
        """LB: same as UB but break instead of taking fraction."""
        if cur_weight > capacity:
            return -INF
        value = cur_value
        weight = cur_weight
        for i in range(level, n):
            if weight + w_sorted[i] <= capacity:
                weight += w_sorted[i]
                value += v_sorted[i]
            else:
                break
        return value

    # For MAXIMIZATION, the correct LC search is "best-first by
    # upper bound": pop the node with the highest UB. Early-exit
    # when the head's UB is no greater than the current best.
    # We use a max-heap by negating the UB.
    # Each queue entry: (neg_ub, counter, level, cur_value, cur_weight)
    counter = 0
    pq = []
    initial_ub = upper_bound(0, 0, 0)
    heapq.heappush(pq, (-initial_ub, 0, 0, 0, 0, 0))
    while pq:
        neg_ub, _, level, cur_value, cur_weight, _ = heapq.heappop(pq)
        ub = -neg_ub
        # Early-exit: if the highest UB in the queue is no
        # better than our best-known solution, no future node
        # can improve on `best`.
        if ub <= best:
            break
        if level == n:
            # Leaf.
            if cur_value > best:
                best = cur_value
            continue
        # Right child: exclude item at this level.
        right_value = cur_value
        right_weight = cur_weight
        right_ub = upper_bound(level + 1, right_value, right_weight)
        if right_ub > best:
            right_lb = lower_bound(level + 1, right_value, right_weight)
            if right_lb < INF:
                counter += 1
                heapq.heappush(pq, (-right_ub, counter, level + 1,
                                    int(right_value),
                                    int(right_weight), 0))
        # Left child: include item at this level (if it fits).
        if cur_weight + w_sorted[level] <= capacity:
            left_value = cur_value + v_sorted[level]
            left_weight = cur_weight + w_sorted[level]
            left_ub = upper_bound(level + 1, left_value, left_weight)
            if left_ub > best:
                left_lb = lower_bound(level + 1, left_value, left_weight)
                if left_lb < INF:
                    counter += 1
                    heapq.heappush(pq, (-left_ub, counter, level + 1,
                                        int(left_value),
                                        int(left_weight), 0))
    return best
'''

def _setup_bb_03(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 8))
    values = [rng.randint(1, 20) for _ in range(n)]
    weights = [rng.randint(1, 10) for _ in range(n)]
    capacity = rng.randint(1, max(2, n) * 5)
    challenge._values = list(values)
    challenge._weights = list(weights)
    challenge._capacity = capacity
    return {
        "values": list(values),
        "weights": list(weights),
        "capacity": capacity,
        "n": n,
    }

def _verify_bb_03(challenge, result):
    # Brute-force knapsack (same as bb_01).
    from itertools import combinations
    values = challenge._values
    weights = challenge._weights
    capacity = challenge._capacity
    n = len(values)
    expected = 0
    for k in range(n + 1):
        for subset in combinations(range(n), k):
            if sum(weights[i] for i in subset) > capacity:
                continue
            v = sum(values[i] for i in subset)
            if v > expected:
                expected = v
    return result == expected



# === bb_04: 8-Puzzle (Branch and Bound) ===

BB_04_SOURCE = '''
def solve(start, goal):
    """8-puzzle via B&B with misplaced-tiles heuristic.

    Return the minimum number of moves (depth) of the goal
    node, or -1 if no solution is found within the search
    budget.
    """
    import heapq
    N = 3
    # Flatten the goal to a tuple for O(1) hashing.
    goal_flat = tuple(sum(goal, []))

    def misplaced(board_flat):
        return sum(1 for i, v in enumerate(board_flat) if v != 0 and v != goal_flat[i])

    def neighbors(board, zr, zc, parent_z):
        """Yield (new_board, new_zr, new_zc, move_id) for the four
        possible moves of the blank, skipping the parent
        direction (encoded as the previous (zr, zc))."""
        out = []
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = zr + dr, zc + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) != parent_z:
                # Move blank from (zr, zc) to (nr, nc).
                new = list(board)
                bi = zr * N + zc
                ni = nr * N + nc
                new[bi], new[ni] = new[ni], new[bi]
                out.append((tuple(new), nr, nc))
        return out

    # Find the blank in start.
    start_flat = tuple(sum(start, []))
    try:
        z0 = start_flat.index(0)
    except ValueError:
        return -1
    zr0, zc0 = z0 // N, z0 % N

    # Each entry: (cost, counter, board_flat, zr, zc, depth, parent_z)
    # cost = depth + misplaced(board). We use a counter to break
    # ties so equal-cost nodes are processed FIFO.
    counter = 0
    pq = [(misplaced(start_flat), 0, start_flat, zr0, zc0, 0, None)]
    seen = {start_flat: 0}  # board_flat -> best depth seen
    while pq:
        cost, _, board, zr, zc, depth, parent_z = heapq.heappop(pq)
        if board == goal_flat:
            return depth
        if seen.get(board, float("inf")) < depth:
            continue
        for new_board, nr, nc in neighbors(board, zr, zc, parent_z):
            new_depth = depth + 1
            if seen.get(new_board, float("inf")) <= new_depth:
                continue
            seen[new_board] = new_depth
            counter += 1
            new_cost = new_depth + misplaced(new_board)
            heapq.heappush(pq, (new_cost, counter, new_board, nr, nc,
                                new_depth, (zr, zc)))
    return -1
'''

def _setup_bb_04(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Start from a goal state of 1..8 + 0 in row-major order, then
    # shuffle with a few random moves so the start is solvable.
    N = 3
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    # Simulate 6 random moves from the goal to make the start.
    cur = [row[:] for row in goal]
    zr, zc = 2, 2
    prev = None
    for _ in range(6):
        moves = []
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = zr + dr, zc + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) != prev:
                moves.append((nr, nc, dr, dc))
        if not moves:
            break
        nr, nc, dr, dc = rng.choice(moves)
        # Swap blank with (nr, nc).
        cur[zr][zc], cur[nr][nc] = cur[nr][nc], cur[zr][zc]
        prev = (zr, zc)
        zr, zc = nr, nc
    start = [row[:] for row in cur]
    challenge._start = [row[:] for row in start]
    challenge._goal = [row[:] for row in goal]
    return {"start": [row[:] for row in start], "goal": [row[:] for row in goal]}

def _verify_bb_04(challenge, result):
    # Brute force: BFS over the state space, return shortest path
    # length (capped to 20 to keep the test fast).
    from collections import deque
    start = challenge._start
    goal = challenge._goal
    N = 3
    start_flat = tuple(sum(start, []))
    goal_flat = tuple(sum(goal, []))
    if start_flat == goal_flat:
        expected = 0
    else:
        # BFS.
        q = deque([(start_flat, 0)])
        visited = {start_flat: 0}
        expected = -1
        while q:
            b, d = q.popleft()
            if b == goal_flat:
                expected = d
                break
            if d > 20:
                break
            # Find blank.
            z = b.index(0)
            zr, zc = z // N, z % N
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = zr + dr, zc + dc
                if 0 <= nr < N and 0 <= nc < N:
                    zi = zr * N + zc
                    ni = nr * N + nc
                    new = list(b)
                    new[zi], new[ni] = new[ni], new[zi]
                    new = tuple(new)
                    if new not in visited:
                        visited[new] = d + 1
                        q.append((new, d + 1))
    # solve() may also return -1 if it can't find a solution;
    # accept that.
    if expected == -1:
        return result == -1
    return result == expected



# === bb_05: N-Queen (Branch and Bound) ===

BB_05_SOURCE = '''
def solve(n):
    """N-queen via branch and bound (column-by-column with
    O(1) row/diagonal lookups)."""
    if n <= 0:
        return []
    row_used = [False] * n
    # / diagonal: r + c. backslash diagonal: c - r + (n - 1).
    slash = [False] * (2 * n - 1)
    backslash = [False] * (2 * n - 1)
    placement = []                        # list of (row, col)
    found = []

    def dfs(col):
        if col == n:
            found.extend(placement)
            return True
        for r in range(n):
            si = r + col
            bi = col - r + (n - 1)
            if row_used[r] or slash[si] or backslash[bi]:
                continue
            row_used[r] = True
            slash[si] = True
            backslash[bi] = True
            placement.append((r, col))
            if dfs(col + 1):
                return True
            placement.pop()
            row_used[r] = False
            slash[si] = False
            backslash[bi] = False
        return False

    dfs(0)
    return sorted(found)
'''

def _setup_bb_05(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Always solvable: pick n in {1, 4, 5, 6, 7, 8}. (Skip n=2
    # and n=3 which have no solution.)
    n = rng.choice([1, 4, 5, 6, 7, 8])
    challenge._n = n
    return {"n": n}

def _verify_bb_05(challenge, result):
    # Verify the placement is a valid N-queen solution.
    n = challenge._n
    placement = list(result)
    if not placement:
        # For our chosen n (1, 4, 5, 6, 7, 8) a solution exists.
        return False
    # Check exactly n queens.
    if len(placement) != n:
        return False
    # All unique cols (and rows) and not on the same diagonal.
    rows = set()
    cols = set()
    diags1 = set()
    diags2 = set()
    for r, c in placement:
        if r in rows or c in cols or (r + c) in diags1 or (r - c) in diags2:
            return False
        rows.add(r)
        cols.add(c)
        diags1.add(r + c)
        diags2.add(r - c)
    return True



# === bb_06: TSP via Reduced Matrix (B&B) ===

BB_06_SOURCE = '''
def solve(cost, n):
    """TSP via reduced-matrix LC branch and bound.

    Each live node has: (lb, path, matrix, cost_so_far).
    Lower bound = path cost + row/column reduction cost.
    Branching: include or exclude the next edge from the
    current node to an unvisited city.
    """
    INF = float("inf")
    N_MAX = 12
    if n <= 1:
        return 0
    if n == 2:
        return cost[0][1] + cost[1][0]

    def reduce(mat):
        """Return (reduced_matrix, reduction_cost)."""
        red = [row[:] for row in mat]
        reduction = 0
        # Row reduction.
        for i in range(n):
            finite = [v for v in red[i] if v < INF]
            if not finite:
                continue
            min_val = min(finite)
            if min_val == 0:
                continue
            reduction += min_val
            for j in range(n):
                if red[i][j] < INF:
                    red[i][j] -= min_val
        # Column reduction.
        for j in range(n):
            col_vals = [red[i][j] for i in range(n) if red[i][j] < INF]
            if not col_vals:
                continue
            min_val = min(col_vals)
            if min_val == 0:
                continue
            reduction += min_val
            for i in range(n):
                if red[i][j] < INF:
                    red[i][j] -= min_val
        return red, reduction

    # Each priority queue entry:
    # (lb, path_tuple, matrix, cost_so_far, parent_reduction)
    # lb = cost_so_far + (current reduction). The reduction at
    # this node has been accounted for in `lb`; for the child,
    # we use: new_lb = lb + edge_cost + (new_reduction - old_reduction).
    import heapq
    root_red, root_red_cost = reduce(cost)
    pq = [(root_red_cost, (0,), tuple(tuple(row) for row in root_red), 0, root_red_cost)]
    best = INF
    while pq:
        lb, path, mat_t, cost_so_far, parent_red = heapq.heappop(pq)
        if lb >= best:
            continue
        if len(path) == n:
            # Complete tour: return to start.
            total = cost_so_far + cost[path[-1]][0]
            if total < best:
                best = total
            continue
        # Branch: try each unvisited city from path[-1].
        cur = path[-1]
        for nxt in range(n):
            if nxt in path:
                continue
            edge_cost = cost[cur][nxt]
            if edge_cost >= INF:
                continue
            new_mat = [list(row) for row in mat_t]
            for j in range(n):
                new_mat[cur][j] = INF
            for i in range(n):
                new_mat[i][nxt] = INF
            new_mat[nxt][0] = INF
            new_red, new_red_cost = reduce(new_mat)
            new_lb = lb + edge_cost + (new_red_cost - parent_red)
            if new_lb < best:
                new_path = path + (nxt,)
                heapq.heappush(pq, (new_lb, new_path,
                                    tuple(tuple(row) for row in new_red),
                                    cost_so_far + edge_cost,
                                    new_red_cost))
    return best if best < INF else -1
'''

def _setup_bb_06(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(2, min(n, 5))
    # Symmetric metric cost matrix.
    pts = [(rng.randint(0, 15), rng.randint(0, 15)) for _ in range(n)]
    cost = [[0] * n for _ in range(n)]
    INF = float("inf")
    for i in range(n):
        for j in range(n):
            if i == j:
                cost[i][j] = INF
            else:
                dx = pts[i][0] - pts[j][0]
                dy = pts[i][1] - pts[j][1]
                d2 = dx * dx + dy * dy
                d = int(d2 ** 0.5) + (1 if (int(d2 ** 0.5)) ** 2 < d2 else 0)
                cost[i][j] = max(d, 1)
    challenge._n = n
    challenge._cost = [row[:] for row in cost]
    return {"cost": [row[:] for row in cost], "n": n}

def _verify_bb_06(challenge, result):
    # Brute force: try every permutation of cities 1..n-1 and
    # sum the tour cost including the return to 0.
    import math
    from itertools import permutations
    n = challenge._n
    cost = challenge._cost
    INF = float("inf")
    best = INF
    for perm in permutations(range(1, n)):
        ok = True
        total = 0
        last = 0
        for c in perm:
            if cost[last][c] >= INF:
                ok = False
                break
            total += cost[last][c]
            last = c
        if not ok:
            continue
        if cost[last][0] >= INF:
            continue
        total += cost[last][0]
        if total < best:
            best = total
    return result == best


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="bb_03",
        name="0/1 Knapsack (Least-Cost B&B)",
        category="branch_and_bound",
        difficulty=6,
        required_complexity=ComplexityClass.O_2N,
        description=("""
            Solve 0/1 knapsack via Least-Cost (LC) branch and
            bound. Sort items by value/weight ratio descending.
            Maintain a priority queue of live nodes ordered by
            their lower bound (LC = min cost). For each node
            popped, compute a fractional-knapsack upper bound
            for both children (include / exclude the current
            item); discard any child whose UB exceeds the
            current best lower bound. Stop when the priority
            queue is empty. The setup keeps n small (n <= 8)
            so brute-force verification is fast.
            Source: https://www.geeksforgeeks.org/dsa/0-1-knapsack-using-least-count-branch-and-bound/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/0-1-knapsack-using-least-count-branch-and-bound/",
        params=["values", "weights", "capacity", "n"],
        inputs={
            "values": "list of n item values.",
            "weights": "list of n item weights (all > 0).",
            "capacity": "knapsack capacity.",
            "n": "number of items.",
        },
        returns="the maximum total value of items fitting in the knapsack (int).",
        source=BB_03_SOURCE,
        setup_fn=_setup_bb_03,
        verify_fn=_verify_bb_03,
        samples=[
            Sample("values = [10, 10, 12, 18], weights = [2, 4, 6, 9], capacity = 15, n = 4", "38"),
            Sample("values = [18, 20, 14, 18], weights = [6, 3, 5, 9], capacity = 21, n = 4", "56"),
        ],
        hint="Sort by value/weight ratio. Priority queue of live nodes keyed by lower bound. For each popped node, build exclude and include children, compute their bounds, enqueue only if their UB is still above the current best.",
        parents=["bb_01"],
        children=["bb_04"],
    ),
    AlgorithmSpec(
        id="bb_04",
        name="8-Puzzle (Branch and Bound)",
        category="branch_and_bound",
        difficulty=6,
        required_complexity=ComplexityClass.O_2N,
        description=("""
            Solve the 8-puzzle (3x3 sliding-tile puzzle with
            one empty cell) using branch and bound with the
            misplaced-tiles heuristic. Cost of a node = depth
            so far + number of tiles not in their goal position.
            Use a priority queue of live nodes; expand the
            node with the smallest cost; move the empty cell
            in the four cardinal directions to generate
            children, skipping the previous position. Stop
            when a goal state is reached. Return the number of
            moves in the shortest solution (depth of the goal
            node).
            Source: https://www.geeksforgeeks.org/dsa/8-puzzle-problem-using-branch-and-bound/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/8-puzzle-problem-using-branch-and-bound/",
        params=["start", "goal"],
        inputs={
            "start": "3x3 list of lists representing the initial board (0 = blank).",
            "goal": "3x3 list of lists representing the target board.",
        },
        returns="the minimum number of moves to reach the goal from start, or -1 if unsolvable (heuristic-search bound).",
        source=BB_04_SOURCE,
        setup_fn=_setup_bb_04,
        verify_fn=_verify_bb_04,
        samples=[
            Sample("start = [[1,2,3],[4,5,6],[7,8,0]], goal = [[1,2,3],[4,5,6],[7,8,0]]", "0"),
            Sample("start = [[1,2,3],[4,0,6],[7,5,8]], goal = [[1,2,3],[4,5,6],[7,8,0]]", "2 (or whatever BFS finds)"),
        ],
        hint="Cost = depth + (number of tiles not in goal position). Use a priority queue; expand lowest cost; generate 4 neighbors (skip the parent); stop at goal.",
        parents=["bb_03"],
        children=["bb_05"],
    ),
    AlgorithmSpec(
        id="bb_05",
        name="N-Queen (Branch and Bound)",
        category="branch_and_bound",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Place N queens on an N x N board so that no two
            queens attack each other. Use branch and bound:
            place queens column by column, and for each column
            prune any row that is already attacked (by row,
            or by either of the two diagonal directions). Use
            three boolean arrays for O(1) safety checks:
            row[r], slash[r + c] (for / diagonals), and
            backslash[c - r + (N-1)] (for backslash diagonals).
            Return a sorted list of (row, col) tuples for one
            valid placement, or an empty list if none exists
            for this N.
            Source: https://www.geeksforgeeks.org/dsa/n-queen-problem-using-branch-and-bound/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/n-queen-problem-using-branch-and-bound/",
        params=["n"],
        inputs={
            "n": "board size (small in tests, 1 <= n <= 8).",
        },
        returns="a list of (row, col) tuples for one valid N-queen placement, sorted by col; empty list if no solution exists.",
        source=BB_05_SOURCE,
        setup_fn=_setup_bb_05,
        verify_fn=_verify_bb_05,
        samples=[
            Sample("n = 1", "[(0, 0)]"),
            Sample("n = 4", "[(1, 0), (3, 1), (0, 2), (2, 3)] (one valid placement)"),
            Sample("n = 8", "a valid 8-queen placement, e.g. [(0,0),(4,1),(7,2),(5,3),(2,4),(6,5),(1,6),(3,7)]"),
        ],
        hint="Place queens column by column. For each column, try every row, skipping any row that is already attacked. Use row_used, slash[r+c], backslash[c-r+(n-1)] for O(1) safety checks.",
        parents=["bb_04"],
        children=["bb_06"],
    ),
    AlgorithmSpec(
        id="bb_06",
        name="TSP via Reduced Matrix (B&B)",
        category="branch_and_bound",
        difficulty=7,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Solve the traveling salesman problem using the
            reduced-matrix branch-and-bound method. Each node
            in the search tree is a state (current path, cost
            so far, the reduced cost matrix). Branching:
            include or exclude the next unvisited city's edge.
            Bounding: subtract the row and column minimums to
            produce a 'reduced' matrix; the cost of the
            reduction is the lower bound. The algorithm uses
            a priority queue (min-heap) of live nodes keyed by
            their lower bound; the goal is to find a complete
            tour with the minimum total cost. Return the
            minimum tour cost.
            Source: https://www.geeksforgeeks.org/dsa/travelling-salesman-problem-tsp-using-reduced-matrix-method/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/travelling-salesman-problem-tsp-using-reduced-matrix-method/",
        params=["cost", "n"],
        inputs={
            "cost": "n x n cost matrix (cost[i][j] is the cost from i to j).",
            "n": "number of cities.",
        },
        returns="the minimum TSP tour cost (int).",
        source=BB_06_SOURCE,
        setup_fn=_setup_bb_06,
        verify_fn=_verify_bb_06,
        samples=[
            Sample("cost = [[INF, 10, 15, 20], [10, INF, 35, 25], [15, 35, INF, 30], [20, 25, 30, INF]], n = 4", "80 (the optimal tour)"),
        ],
        hint="Reduce the cost matrix (subtract row/column minimums). The reduction amount is the lower bound. Branch on include/exclude the next edge; recurse. Prune nodes whose lower bound exceeds the best tour found.",
        parents=["bb_05"],
        children=[],
    ),
])
