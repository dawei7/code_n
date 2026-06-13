"""Spec generator input — 4 more branch-and-bound specs for Session 1.

Covers the remaining GfG branch-and-bound standard-problem list
(see https://www.geeksforgeeks.org/branch-and-bound-algorithm/):

  bb_03  0/1 Knapsack (Least-Cost B&B)    (priority queue + fractional UB)
  bb_04  8-Puzzle                         (LC search with misplaced-tiles heuristic)
  bb_05  N-Queen                          (B&B with row/diagonal lookup arrays)
  bb_06  TSP via Reduced-Matrix Method    (row/column reduction + LC)

After this batch, branch_and_bound.py covers the full GfG B&B
problem catalog (bb_01, bb_02 were added in an earlier round).

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module branch_and_bound \\
        --input batch_bb_session1.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # bb_03: 0/1 Knapsack (Least-Cost Branch and Bound)
    # ============================================================
    {
        "id": "bb_03",
        "name": "0/1 Knapsack (Least-Cost B&B)",
        "category": "branch_and_bound",
        "difficulty": 6,
        "complexity": "O_2N",
        "description": (
            "Solve 0/1 knapsack via Least-Cost (LC) branch and\n"
            "bound. Sort items by value/weight ratio descending.\n"
            "Maintain a priority queue of live nodes ordered by\n"
            "their lower bound (LC = min cost). For each node\n"
            "popped, compute a fractional-knapsack upper bound\n"
            "for both children (include / exclude the current\n"
            "item); discard any child whose UB exceeds the\n"
            "current best lower bound. Stop when the priority\n"
            "queue is empty. The setup keeps n small (n <= 8)\n"
            "so brute-force verification is fast.\n"
            "Source: https://www.geeksforgeeks.org/dsa/0-1-knapsack-using-least-count-branch-and-bound/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/0-1-knapsack-using-least-count-branch-and-bound/",
        "params": ["values", "weights", "capacity", "n"],
        "inputs": {
            "values": "list of n item values.",
            "weights": "list of n item weights (all > 0).",
            "capacity": "knapsack capacity.",
            "n": "number of items.",
        },
        "returns": "the maximum total value of items fitting in the knapsack (int).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("values = [10, 10, 12, 18], weights = [2, 4, 6, 9], capacity = 15, n = 4", "38"),
            ("values = [18, 20, 14, 18], weights = [6, 3, 5, 9], capacity = 21, n = 4", "56"),
        ],
        "hint": "Sort by value/weight ratio. Priority queue of live nodes keyed by lower bound. For each popped node, build exclude and include children, compute their bounds, enqueue only if their UB is still above the current best.",
        "parents": ["bb_01"],
        "children": ["bb_04"],
    },

    # ============================================================
    # bb_04: 8-Puzzle (LC search with misplaced-tiles heuristic)
    # ============================================================
    {
        "id": "bb_04",
        "name": "8-Puzzle (Branch and Bound)",
        "category": "branch_and_bound",
        "difficulty": 6,
        "complexity": "O_2N",
        "description": (
            "Solve the 8-puzzle (3x3 sliding-tile puzzle with\n"
            "one empty cell) using branch and bound with the\n"
            "misplaced-tiles heuristic. Cost of a node = depth\n"
            "so far + number of tiles not in their goal position.\n"
            "Use a priority queue of live nodes; expand the\n"
            "node with the smallest cost; move the empty cell\n"
            "in the four cardinal directions to generate\n"
            "children, skipping the previous position. Stop\n"
            "when a goal state is reached. Return the number of\n"
            "moves in the shortest solution (depth of the goal\n"
            "node).\n"
            "Source: https://www.geeksforgeeks.org/dsa/8-puzzle-problem-using-branch-and-bound/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/8-puzzle-problem-using-branch-and-bound/",
        "params": ["start", "goal"],
        "inputs": {
            "start": "3x3 list of lists representing the initial board (0 = blank).",
            "goal": "3x3 list of lists representing the target board.",
        },
        "returns": "the minimum number of moves to reach the goal from start, or -1 if unsolvable (heuristic-search bound).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("start = [[1,2,3],[4,5,6],[7,8,0]], goal = [[1,2,3],[4,5,6],[7,8,0]]", "0"),
            ("start = [[1,2,3],[4,0,6],[7,5,8]], goal = [[1,2,3],[4,5,6],[7,8,0]]", "2 (or whatever BFS finds)"),
        ],
        "hint": "Cost = depth + (number of tiles not in goal position). Use a priority queue; expand lowest cost; generate 4 neighbors (skip the parent); stop at goal.",
        "parents": ["bb_03"],
        "children": ["bb_05"],
    },

    # ============================================================
    # bb_05: N-Queen (Branch and Bound with row/diagonal lookups)
    # ============================================================
    {
        "id": "bb_05",
        "name": "N-Queen (Branch and Bound)",
        "category": "branch_and_bound",
        "difficulty": 5,
        "complexity": "O_N2",
        "description": (
            "Place N queens on an N x N board so that no two\n"
            "queens attack each other. Use branch and bound:\n"
            "place queens column by column, and for each column\n"
            "prune any row that is already attacked (by row,\n"
            "or by either of the two diagonal directions). Use\n"
            "three boolean arrays for O(1) safety checks:\n"
            "row[r], slash[r + c] (for / diagonals), and\n"
            "backslash[c - r + (N-1)] (for backslash diagonals).\n"
            "Return a sorted list of (row, col) tuples for one\n"
            "valid placement, or an empty list if none exists\n"
            "for this N.\n"
            "Source: https://www.geeksforgeeks.org/dsa/n-queen-problem-using-branch-and-bound/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/n-queen-problem-using-branch-and-bound/",
        "params": ["n"],
        "inputs": {
            "n": "board size (small in tests, 1 <= n <= 8).",
        },
        "returns": "a list of (row, col) tuples for one valid N-queen placement, sorted by col; empty list if no solution exists.",
        "solve": '''
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
''',
        "setup": '''
import random
rng = random.Random(seed)
# Always solvable: pick n in {1, 4, 5, 6, 7, 8}. (Skip n=2
# and n=3 which have no solution.)
n = rng.choice([1, 4, 5, 6, 7, 8])
challenge._n = n
return {"n": n}
''',
        "verify": '''
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
''',
        "samples": [
            ("n = 1", "[(0, 0)]"),
            ("n = 4", "[(1, 0), (3, 1), (0, 2), (2, 3)] (one valid placement)"),
            ("n = 8", "a valid 8-queen placement, e.g. [(0,0),(4,1),(7,2),(5,3),(2,4),(6,5),(1,6),(3,7)]"),
        ],
        "hint": "Place queens column by column. For each column, try every row, skipping any row that is already attacked. Use row_used, slash[r+c], backslash[c-r+(n-1)] for O(1) safety checks.",
        "parents": ["bb_04"],
        "children": ["bb_06"],
    },

    # ============================================================
    # bb_06: TSP via Reduced-Matrix Method (LC Branch and Bound)
    # ============================================================
    {
        "id": "bb_06",
        "name": "TSP via Reduced Matrix (B&B)",
        "category": "branch_and_bound",
        "difficulty": 7,
        "complexity": "O_N2",
        "description": (
            "Solve the traveling salesman problem using the\n"
            "reduced-matrix branch-and-bound method. Each node\n"
            "in the search tree is a state (current path, cost\n"
            "so far, the reduced cost matrix). Branching:\n"
            "include or exclude the next unvisited city's edge.\n"
            "Bounding: subtract the row and column minimums to\n"
            "produce a 'reduced' matrix; the cost of the\n"
            "reduction is the lower bound. The algorithm uses\n"
            "a priority queue (min-heap) of live nodes keyed by\n"
            "their lower bound; the goal is to find a complete\n"
            "tour with the minimum total cost. Return the\n"
            "minimum tour cost.\n"
            "Source: https://www.geeksforgeeks.org/dsa/travelling-salesman-problem-tsp-using-reduced-matrix-method/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/travelling-salesman-problem-tsp-using-reduced-matrix-method/",
        "params": ["cost", "n"],
        "inputs": {
            "cost": "n x n cost matrix (cost[i][j] is the cost from i to j).",
            "n": "number of cities.",
        },
        "returns": "the minimum TSP tour cost (int).",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("cost = [[INF, 10, 15, 20], [10, INF, 35, 25], [15, 35, INF, 30], [20, 25, 30, INF]], n = 4", "80 (the optimal tour)"),
        ],
        "hint": "Reduce the cost matrix (subtract row/column minimums). The reduction amount is the lower bound. Branch on include/exclude the next edge; recurse. Prune nodes whose lower bound exceeds the best tour found.",
        "parents": ["bb_05"],
        "children": [],
    },
]
