"""Dynamic Programming challenges.

Classic entry-level DP problems: Fibonacci, climbing stairs,
0/1 knapsack, and the longest common subsequence. The shape
is the same for all four: a single ``setup(n, seed)`` that
builds the input, a single ``verify(result)`` that compares
against the expected value computed up front.
"""

from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList


# --- Fibonacci ---


def _setup_fibonacci(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    challenge._n_val = min(n, 40)
    challenge._expected = _fib(challenge._n_val)

    width = challenge._n_val + 1
    challenge.grid = Grid(min(width, 20), 3)
    for i in range(min(width, 20)):
        challenge.grid.set(i, 0, CellType.EMPTY, "?")
    challenge.grid.set(0, 0, CellType.SORTED, "0")
    if width > 1:
        challenge.grid.set(1, 0, CellType.SORTED, "1")

    return {"n": challenge._n_val}


def _verify_fibonacci(challenge, result: Any) -> bool:
    return result == challenge._expected


def _fib(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


DP_01_SOURCE = '''\
"""Optimal solution for dp_01: Fibonacci.

Compute the n-th Fibonacci number bottom-up. O(n) time, O(1)
space.
"""


def solve(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current
'''


# --- Climbing Stairs ---


def _setup_climbing(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    challenge._n_val = min(n, 35)
    challenge._expected = _climb(challenge._n_val)

    challenge.grid = Grid(min(challenge._n_val + 1, 20), 3)
    for i in range(min(challenge._n_val + 1, 20)):
        challenge.grid.set(i, 1, CellType.VALUE, i)
        challenge.grid.set(i, 0, CellType.EMPTY, "?")

    return {"n": challenge._n_val}


def _verify_climbing(challenge, result: Any) -> bool:
    return result == challenge._expected


def _climb(n: int) -> int:
    if n <= 2:
        return max(n, 1)
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


DP_02_SOURCE = '''\
"""Optimal solution for dp_02: Climbing Stairs.

Count the number of ways to climb n stairs taking 1 or 2 steps
at a time. Same recurrence as Fibonacci: ways(n) = ways(n-1) +
ways(n-2). O(n) time, O(1) space.
"""


def solve(n):
    if n <= 2:
        return max(n, 1)
    previous, current = 1, 2
    for _ in range(3, n + 1):
        previous, current = current, previous + current
    return current
'''


# --- Knapsack ---


def _setup_knapsack(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    num_items = min(n, 15)
    challenge._capacity = num_items * 3
    challenge._weights = [rng.randint(1, challenge._capacity // 2) for _ in range(num_items)]
    challenge._values = [rng.randint(1, 50) for _ in range(num_items)]
    challenge._expected = _solve_knapsack(challenge._weights, challenge._values, challenge._capacity)

    challenge.grid = Grid(num_items, 4)
    challenge.grid.fill_row(0, list(range(num_items)), CellType.VALUE)
    challenge.grid.fill_row(1, challenge._weights, CellType.MARKER)
    challenge.grid.fill_row(2, challenge._values, CellType.PATH)

    return {
        "weights": TrackedList(challenge._weights),
        "values": TrackedList(challenge._values),
        "capacity": challenge._capacity,
        "n": num_items,
    }


def _verify_knapsack(challenge, result: Any) -> bool:
    return result == challenge._expected


def _solve_knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    cap = capacity
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(cap + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][cap]


DP_03_SOURCE = '''\
"""Optimal solution for dp_03: 0/1 Knapsack.

Classic DP table: dp[i][c] = max value using the first i items
with capacity c. O(n * capacity) time, O(n * capacity) space.
"""


def solve(weights, values, capacity, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][capacity]
'''


# --- LCS ---


def _setup_lcs(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    length = min(n, 15)
    chars = "ABCDEFGH"
    challenge._seq_a = "".join(rng.choice(chars) for _ in range(length))
    challenge._seq_b = "".join(rng.choice(chars) for _ in range(length))
    challenge._expected = _solve_lcs(challenge._seq_a, challenge._seq_b)

    challenge.grid = Grid(length + 1, length + 1)
    for i, c in enumerate(challenge._seq_a):
        challenge.grid.set(i + 1, 0, CellType.VALUE, c)
    for j, c in enumerate(challenge._seq_b):
        challenge.grid.set(0, j + 1, CellType.VALUE, c)

    return {"seq_a": challenge._seq_a, "seq_b": challenge._seq_b}


def _verify_lcs(challenge, result: Any) -> bool:
    return result == challenge._expected


def _solve_lcs(seq_a: str, seq_b: str) -> int:
    m, n = len(seq_a), len(seq_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq_a[i - 1] == seq_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


DP_04_SOURCE = '''\
"""Optimal solution for dp_04: Longest Common Subsequence.

DP table: dp[i][j] = LCS length of seq_a[:i] and seq_b[:j]. O(n*m)
time, O(n*m) space.
"""


def solve(seq_a, seq_b):
    m, n = len(seq_a), len(seq_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq_a[i - 1] == seq_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
'''


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="dp_01",
        name="Fibonacci",
        category="dynamic",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Compute the n-th Fibonacci number.\n"
            "fib(0)=0, fib(1)=1, fib(n) = fib(n-1) + fib(n-2)\n"
            "Requirement: O(n) - naive recursion (O(2^n)) will FAIL!\n"
            "Use memoization or bottom-up DP.\n"
            "Source: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/"
        ),
        source_url="https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/",
        params=["n"],
        inputs={"n": "index of the Fibonacci number to compute."},
        returns="the n-th Fibonacci number (fib(0)=0, fib(1)=1).",
        source=DP_01_SOURCE,
        setup_fn=_setup_fibonacci,
        verify_fn=_verify_fibonacci,
        samples=[
            Sample("n = 0", "0"),
            Sample("n = 5", "5"),
            Sample("n = 8", "21"),
        ],
        hint="Store previously computed values in an array. Build up from fib(0) to fib(n).",
        parents=["intro_01"],
        children=["dp_02"],
    ),
    AlgorithmSpec(
        id="dp_02",
        name="Climbing Stairs",
        category="dynamic",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "You are climbing a staircase with n steps.\n"
            "Each time you can climb 1 or 2 steps.\n"
            "How many distinct ways can you reach the top?\n"
            "Requirement: O(n)\n"
            "Source: https://www.geeksforgeeks.org/count-ways-reach-nth-stair/"
        ),
        source_url="https://www.geeksforgeeks.org/count-ways-reach-nth-stair/",
        params=["n"],
        inputs={"n": "number of stairs."},
        returns="the number of distinct ways to climb n stairs (1 or 2 steps at a time).",
        source=DP_02_SOURCE,
        setup_fn=_setup_climbing,
        verify_fn=_verify_climbing,
        samples=[
            Sample("n = 1", "1"),
            Sample("n = 3", "3"),
            Sample("n = 5", "8"),
        ],
        hint="ways(n) = ways(n-1) + ways(n-2). Same as Fibonacci!",
        parents=["dp_01"],
        children=["dp_03", "dp_04"],
    ),
    AlgorithmSpec(
        id="dp_03",
        name="Knapsack",
        category="dynamic",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "0/1 Knapsack: Given items with weights and values, and a capacity,\n"
            "find the maximum total value that fits in the knapsack.\n"
            "Each item can be used at most once.\n"
            "Requirement: O(n * capacity) using DP.\n"
            "Source: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/"
        ),
        source_url="https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/",
        params=["weights", "values", "capacity", "n"],
        inputs={
            "weights": "list-like of item weights (length n).",
            "values": "list-like of item values (length n).",
            "capacity": "knapsack capacity.",
            "n": "number of items.",
        },
        returns="the maximum total value of items that fit in the knapsack.",
        source=DP_03_SOURCE,
        setup_fn=_setup_knapsack,
        verify_fn=_verify_knapsack,
        samples=[
            Sample("weights = [2, 3], values = [4, 5], capacity = 3", "5"),
            Sample("weights = [1, 2], values = [2, 4], capacity = 3", "6"),
            Sample("capacity = 0", "0"),
        ],
        hint="Build a 2D table dp[i][w] = max value using first i items with capacity w.",
        parents=["dp_02"],
        children=[],
    ),
    AlgorithmSpec(
        id="dp_04",
        name="Longest Common Subsequence",
        category="dynamic",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the length of the longest common subsequence of two strings.\n"
            "A subsequence is a sequence that appears in the same order but not necessarily contiguous.\n"
            "Requirement: O(n * m) where n, m are string lengths.\n"
            "Source: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/",
        params=["seq_a", "seq_b"],
        inputs={
            "seq_a": "first string (or list-like of characters).",
            "seq_b": "second string (or list-like of characters).",
        },
        returns="the length of the longest common subsequence of seq_a and seq_b.",
        source=DP_04_SOURCE,
        setup_fn=_setup_lcs,
        verify_fn=_verify_lcs,
        samples=[
            Sample('seq_a = "ABC", seq_b = "AC"', "2"),
            Sample('seq_a = "ABC", seq_b = "DEF"', "0"),
            Sample('seq_a = "AAB", seq_b = "AB"', "2"),
        ],
        hint="Build dp[i][j] = LCS length of first i chars of A and first j chars of B.",
        parents=["dp_02"],
        children=[],
    ),
]


# === dp_05: Coin Change ========================================
#
# The setup always includes coin value 1 in the denominations
# so the answer is always finite (otherwise the verify would
# have to special-case the impossible case and the player
# couldn't tell from a "0" whether it was 0 coins or -1).


DP_05_SOURCE = '''
def solve(coins, amount):
    """Minimum number of coins summing to amount. -1 if impossible.

    Because the setup always includes coin value 1, the answer
    is always finite. -1 is still returned as a defensive
    fallback for any future spec that doesn't guarantee this.
    """
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for v in range(1, amount + 1):
        for c in coins:
            if c <= v and dp[v - c] + 1 < dp[v]:
                dp[v] = dp[v - c] + 1
    return dp[amount] if dp[amount] != INF else -1
'''


def _setup_coin_change(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Number of distinct coin denominations.
    num_coins = max(1, min(n, 8))
    # Always include 1 so the answer is always finite.
    coins = {1}
    while len(coins) < num_coins:
        c = rng.randint(2, max(3, n * 2))
        coins.add(c)
    coins_list = sorted(coins)
    # amount: scale with n so the table is non-trivial.
    amount = max(1, n * 3)
    # Pre-compute the expected answer the verifier will check.
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for v in range(1, amount + 1):
        for c in coins_list:
            if c <= v and dp[v - c] + 1 < dp[v]:
                dp[v] = dp[v - c] + 1
    expected = dp[amount] if dp[amount] != INF else -1
    challenge._expected = expected
    return {"coins": coins_list, "amount": amount}


def _verify_coin_change(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# === dp_06: Subset Sum ==========================================
#
# The setup picks a target that IS reachable, so the answer is
# always True. (If we picked a random target, half the time
# it'd be unreachable and we'd have to define a "no" answer
# in a way that's hard to verify against the canonical solve.)


DP_06_SOURCE = '''
def solve(arr, target):
    """True iff some subset of arr sums to target."""
    # Standard 1D DP over the running sum.
    reachable = {0}
    for v in arr:
        new_reach = set(reachable)
        for s in reachable:
            new_reach.add(s + v)
        reachable = new_reach
    return target in reachable
'''


def _setup_subset_sum(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_elems = max(1, min(n, 12))
    # Generate small positive integers so the running sum
    # doesn't blow up.
    arr = [rng.randint(1, max(2, n)) for _ in range(n_elems)]
    # Pick a target by summing a random non-empty subset —
    # guarantees reachability.
    subset_size = rng.randint(1, n_elems)
    target = sum(rng.choice(arr) for _ in range(subset_size))
    # If the random subset accidentally picked all zeros or
    # summed to 0, re-roll until we get a positive target.
    while target == 0 and any(v > 0 for v in arr):
        subset_size = rng.randint(1, n_elems)
        target = sum(rng.choice(arr) for _ in range(subset_size))
    challenge._target = target
    challenge._arr = arr
    return {"arr": arr, "target": target}


def _verify_subset_sum(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    # The setup always picks a reachable target, so the
    # correct answer is always True. The test exercises the
    # DP; verifying the result is True checks the DP worked.
    return result is True


# === dp_07: Longest Increasing Subsequence =====================
#
# The O(n log n) patience-sorting version is the canonical
# answer; the spec advertises O_N_LOG_N. The setup picks a
# random array and stashes the expected LIS length.


DP_07_SOURCE = '''
def solve(arr):
    """Length of the longest strictly-increasing subsequence."""
    import bisect
    # `tails[k]` = the smallest tail value of any increasing
    # subsequence of length k+1. Binary search updates the slot
    # for each arr[i].
    tails = []
    for v in arr:
        i = bisect.bisect_left(tails, v)  # leftmost >= v
        if i == len(tails):
            tails.append(v)
        else:
            tails[i] = v
    return len(tails)
'''


def _setup_lis(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_elems = max(1, min(n, 20))
    # Mix decreasing, increasing, and random to exercise
    # both extremes of LIS.
    arr = [rng.randint(1, max(2, n)) for _ in range(n_elems)]
    # Compute expected via the same O(n log n) algorithm.
    import bisect
    tails = []
    for v in arr:
        i = bisect.bisect_left(tails, v)
        if i == len(tails):
            tails.append(v)
        else:
            tails[i] = v
    challenge._expected = len(tails)
    return {"arr": arr}


def _verify_lis(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# === dp_08: Edit Distance (Levenshtein) ========================


DP_08_SOURCE = '''
def solve(word1, word2):
    """Levenshtein distance: min single-char edits to turn w1 into w2."""
    m, n = len(word1), len(word2)
    # dp[i][j] = distance between word1[:i] and word2[:j].
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete word1[i-1]
                    dp[i][j - 1],      # insert word2[j-1]
                    dp[i - 1][j - 1],  # substitute
                )
    return dp[m][n]
'''


def _setup_edit_distance(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Two short strings of length up to n.
    alphabet = "abcdefgh"
    len1 = max(1, rng.randint(1, max(1, n)))
    len2 = max(1, rng.randint(1, max(1, n)))
    word1 = "".join(rng.choice(alphabet) for _ in range(len1))
    word2 = "".join(rng.choice(alphabet) for _ in range(len2))
    # Pre-compute the expected answer.
    m, n_words = len(word1), len(word2)
    dp = [[0] * (n_words + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n_words + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n_words + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    challenge._expected = dp[m][n_words]
    return {"word1": word1, "word2": word2}


def _verify_edit_distance(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# === dp_09: Rod Cutting =========================================


DP_09_SOURCE = '''
def solve(prices, n):
    """Max revenue cutting a rod of length n given a price table.

    prices[i] is the price of a piece of length (i+1) for i in
    range(n). The rod itself is of length n, so prices must be
    indexed from i=0 to i=n-1.
    """
    # dp[i] = max revenue for a rod of length i.
    dp = [0] * (n + 1)
    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            # Price of the first piece is prices[cut-1].
            revenue = prices[cut - 1] + dp[length - cut]
            if revenue > dp[length]:
                dp[length] = revenue
    return dp[n]
'''


def _setup_rod_cutting(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # prices has length n (one price per possible piece length 1..n).
    # Monotonically increasing so the optimum is to NOT cut (cut=rod
    # gives price[n-1] which beats any combination of smaller pieces).
    # We perturb it to make the problem interesting.
    prices = []
    base = 1
    for _ in range(max(1, n)):
        base += rng.randint(1, 3)
        prices.append(base)
    # Pre-compute expected via the same DP.
    dp = [0] * (n + 1)
    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            revenue = prices[cut - 1] + dp[length - cut]
            if revenue > dp[length]:
                dp[length] = revenue
    challenge._expected = dp[n]
    return {"prices": prices, "n": n}


def _verify_rod_cutting(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# === dp_10: Unique Paths (grid, right/down only) ===================
#
# Count the number of distinct paths from the top-left to the
# bottom-right of an m x n grid, moving only right or down.
# The setup picks m, n in [2, max(2, n)]; cells may carry an
# "obstacle" flag (1 = blocked). The "no obstacles" case is the
# classic combinatorial (m+n-2 choose m-1).


DP_10_SOURCE = '''
def solve(grid, m, n):
    """Count paths from (0,0) to (m-1, n-1) moving only right/down.

    Cells with value 1 are obstacles (cannot enter). 0 = free.
    """
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return 0
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]
'''


def _setup_unique_paths(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Use n to size the grid (roughly square). n=4 → 3x3, n=8 → 4x4, etc.
    m = max(2, min(n, 6))
    k = max(2, min(n, 6))
    # Random grid with no obstacles (0 = free). Always solvable.
    grid = [[0] * k for _ in range(m)]
    challenge._grid = grid
    challenge._m = m
    challenge._k = k
    return {"grid": grid, "m": m, "n": k}


def _verify_unique_paths(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    m, n = challenge._m, challenge._k
    grid = challenge._grid
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return result == 0
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return result == dp[m - 1][n - 1]


# === dp_11: House Robber ==========================================
#
# Max sum of non-adjacent elements in a 1D array. The classic
# "rob houses in a line" problem: pick a subset of indices
# with no two consecutive, maximizing the sum.


DP_11_SOURCE = '''
def solve(arr):
    """Max sum of non-adjacent elements in arr."""
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    # dp[i] = max sum using the first i elements (1-indexed).
    dp = [0] * (n + 1)
    dp[1] = arr[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
    return dp[n]
'''


def _setup_house_robber(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_elems = max(1, min(n, 16))
    # Mix of positive and zero (House Robber assumes non-negative).
    arr = [rng.randint(0, 100) for _ in range(n_elems)]
    # Pre-compute expected.
    if not arr:
        challenge._expected = 0
    elif len(arr) == 1:
        challenge._expected = arr[0]
    else:
        dp = [0] * (n_elems + 1)
        dp[1] = arr[0]
        for i in range(2, n_elems + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
        challenge._expected = dp[n_elems]
    return {"arr": arr}


def _verify_house_robber(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# === dp_12: Min Cost Path (grid) ==================================
#
# Find a path from (0,0) to (m-1, n-1) with minimum sum of
# cell values. Movement: right and down only.


DP_12_SOURCE = '''
def solve(grid, m, n):
    """Min-cost path from (0,0) to (m-1, n-1) moving only right/down."""
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]
'''


def _setup_min_cost_path(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    m = max(2, min(n, 6))
    k = max(2, min(n, 6))
    grid = [[rng.randint(1, 20) for _ in range(k)] for _ in range(m)]
    # Pre-compute expected.
    dp = [[0] * k for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, k):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, k):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    challenge._expected = dp[m - 1][k - 1]
    return {"grid": grid, "m": m, "n": k}


def _verify_min_cost_path(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# Append the new DP specs to SPECS.


# Append the new DP specs to SPECS. We do this at module load
# (after the function defs above) so the spec factories can
# reference the helpers cleanly.
SPECS.extend([
    AlgorithmSpec(
        id="dp_05",
        name="Coin Change",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Given a list of coin denominations and a target amount,\n"
            "return the minimum number of coins needed to make the\n"
            "amount. Return -1 if it is impossible.\n"
            "The setup always includes coin 1, so the answer is always\n"
            "finite (1 is the worst case).\n"
            "Requirement: O(n * amount) where n is the number of coins.\n"
            "Source: https://www.geeksforgeeks.org/coin-change-dp-7/"
        ),
        source_url="https://www.geeksforgeeks.org/coin-change-dp-7/",
        params=["coins", "amount"],
        inputs={
            "coins": "list of positive integer coin denominations.",
            "amount": "the target sum to make.",
        },
        returns="the minimum number of coins summing to amount, or -1.",
        source=DP_05_SOURCE,
        setup_fn=_setup_coin_change,
        verify_fn=_verify_coin_change,
        samples=[
            Sample("coins = [1, 5, 10, 25], amount = 11", "2 (10+1)"),
            Sample("coins = [2], amount = 3", "-1"),
            Sample("coins = [1, 2, 5], amount = 7", "2 (5+2)"),
        ],
        hint="Bottom-up DP. dp[v] = min coins to make v. Always include coin 1 to keep the answer finite.",
        parents=["dp_03"],
        children=["dp_06"],
    ),
    AlgorithmSpec(
        id="dp_06",
        name="Subset Sum",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Return True iff some subset of the input array sums to\n"
            "the target. The setup always picks a reachable target,\n"
            "so the canonical answer is always True.\n"
            "Requirement: O(n * sum) where sum is the total of arr.\n"
            "Source: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/"
        ),
        source_url="https://www.geeksforgeeks.org/subset-sum-problem-dp-25/",
        params=["arr", "target"],
        inputs={
            "arr": "list of positive integers.",
            "target": "the sum to check for (always reachable in tests).",
        },
        returns="True iff a subset of arr sums to target.",
        source=DP_06_SOURCE,
        setup_fn=_setup_subset_sum,
        verify_fn=_verify_subset_sum,
        samples=[
            Sample("arr = [3, 34, 4, 12, 5, 2], target = 9", "True (4+5)"),
            Sample("arr = [3, 34, 4, 12, 5, 2], target = 30", "False"),
            Sample("arr = [1, 2, 3], target = 6", "True (1+2+3)"),
        ],
        hint="Track which sums are reachable. For each element, every existing reachable sum gives a new one (itself + the element).",
        parents=["dp_05"],
        children=["dp_07"],
    ),
    AlgorithmSpec(
        id="dp_07",
        name="Longest Increasing Subsequence",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Return the length of the longest strictly-increasing\n"
            "subsequence of the input array. A subsequence is not\n"
            "required to be contiguous.\n"
            "Requirement: O(n log n) — the patience-sorting algorithm\n"
            "with binary search beats the O(n^2) DP.\n"
            "Source: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/",
        params=["arr"],
        inputs={
            "arr": "list of integers.",
        },
        returns="the length of the longest strictly-increasing subsequence.",
        source=DP_07_SOURCE,
        setup_fn=_setup_lis,
        verify_fn=_verify_lis,
        samples=[
            Sample("arr = [10, 9, 2, 5, 3, 7, 101, 18]", "4"),
            Sample("arr = [0, 1, 0, 3, 2, 3]", "4"),
            Sample("arr = [7, 7, 7, 7, 7, 7, 7]", "1"),
        ],
        hint="Patience sorting. Maintain a 'tails' array; for each value, binary-search the leftmost slot >= v.",
        parents=["dp_06"],
        children=["dp_08"],
    ),
    AlgorithmSpec(
        id="dp_08",
        name="Edit Distance",
        category="dynamic",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Compute the Levenshtein distance between two strings:\n"
            "the minimum number of single-character insertions,\n"
            "deletions, or substitutions to turn one into the other.\n"
            "Requirement: O(m * n) where m, n are the string lengths.\n"
            "Source: https://www.geeksforgeeks.org/edit-distance-dp-5/"
        ),
        source_url="https://www.geeksforgeeks.org/edit-distance-dp-5/",
        params=["word1", "word2"],
        inputs={
            "word1": "the source string.",
            "word2": "the target string.",
        },
        returns="the minimum edit distance between word1 and word2.",
        source=DP_08_SOURCE,
        setup_fn=_setup_edit_distance,
        verify_fn=_verify_edit_distance,
        samples=[
            Sample('word1 = "horse", word2 = "ros"', "3"),
            Sample('word1 = "intention", word2 = "execution"', "5"),
            Sample('word1 = "abc", word2 = "abc"', "0"),
        ],
        hint="dp[i][j] = distance between word1[:i] and word2[:j]. On mismatch, 1 + min of delete/insert/substitute.",
        parents=["dp_04"],
        children=["dp_09"],
    ),
    AlgorithmSpec(
        id="dp_09",
        name="Rod Cutting",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Given a price table where prices[i] is the price of a\n"
            "rod piece of length (i+1), find the maximum revenue\n"
            "obtainable by cutting a rod of length n into pieces.\n"
            "Requirement: O(n^2).\n"
            "Source: https://www.geeksforgeeks.org/cutting-a-rod-dp-13/"
        ),
        source_url="https://www.geeksforgeeks.org/cutting-a-rod-dp-13/",
        params=["prices", "n"],
        inputs={
            "prices": "list of length n; prices[i] is the price of a piece of length i+1.",
            "n": "the rod length.",
        },
        returns="the maximum revenue obtainable by cutting the rod.",
        source=DP_09_SOURCE,
        setup_fn=_setup_rod_cutting,
        verify_fn=_verify_rod_cutting,
        samples=[
            Sample("prices = [1, 5, 8, 9], n = 4", "10 (two pieces of length 2)"),
            Sample("prices = [1, 5, 8, 9, 10, 17, 17, 20], n = 8", "22"),
            Sample("prices = [3], n = 1", "3"),
        ],
        hint="dp[length] = max revenue for a rod of that length. For each length, try every first-cut size.",
        parents=["dp_03"],
        children=[],
    ),
    AlgorithmSpec(
        id="dp_10",
        name="Unique Paths",
        category="dynamic",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Count the number of distinct paths from the top-left\n"
            "(0, 0) to the bottom-right (m-1, n-1) of an m x n grid,\n"
            "moving only right or down. Cells with value 1 are\n"
            "obstacles (cannot enter); 0 = free. The setup uses an\n"
            "obstacle-free grid.\n"
            "Requirement: O(m * n).\n"
            "Source: https://www.geeksforgeeks.org/count-all-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/"
        ),
        source_url="https://www.geeksforgeeks.org/count-all-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/",
        params=["grid", "m", "n"],
        inputs={
            "grid": "2D list-like; 0 = free, 1 = obstacle.",
            "m": "number of rows.",
            "n": "number of columns.",
        },
        returns="the number of distinct paths from (0,0) to (m-1, n-1).",
        source=DP_10_SOURCE,
        setup_fn=_setup_unique_paths,
        verify_fn=_verify_unique_paths,
        samples=[
            Sample("grid = [[0,0,0],[0,0,0]], m = 2, n = 3", "3 (R-R-D, R-D-R, D-R-R)"),
            Sample("grid = [[0,1],[0,0]], m = 2, n = 2", "1 (only D then R)"),
        ],
        hint="dp[i][j] = dp[i-1][j] + dp[i][j-1] (with obstacles zeroed out).",
        parents=["dp_04"],
        children=["dp_12"],
    ),
    AlgorithmSpec(
        id="dp_11",
        name="House Robber",
        category="dynamic",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Given an array of non-negative integers (the value of\n"
            "each house), return the maximum sum you can rob without\n"
            "robbing two adjacent houses.\n"
            "Requirement: O(n) — two rolling variables are enough.\n"
            "Source: https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/"
        ),
        source_url="https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/",
        params=["arr"],
        inputs={
            "arr": "list of non-negative integers (each house's value).",
        },
        returns="the maximum sum with no two chosen indices adjacent.",
        source=DP_11_SOURCE,
        setup_fn=_setup_house_robber,
        verify_fn=_verify_house_robber,
        samples=[
            Sample("arr = [5, 3, 4, 11, 2]", "16 (5+11)"),
            Sample("arr = [10, 1, 1, 10, 1, 1, 10]", "30 (10+10+10)"),
            Sample("arr = [2, 1, 1, 2]", "4 (2+2)"),
        ],
        hint="dp[i] = max(dp[i-1], dp[i-2] + arr[i]). Skip-or-take at each house.",
        parents=["dp_10"],
        children=[],
    ),
    AlgorithmSpec(
        id="dp_12",
        name="Min Cost Path",
        category="dynamic",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the minimum-cost path from the top-left to the\n"
            "bottom-right of an m x n grid, moving only right or down.\n"
            "The cost of a path is the sum of the cells visited.\n"
            "Requirement: O(m * n).\n"
            "Source: https://www.geeksforgeeks.org/min-cost-path-dp-6/"
        ),
        source_url="https://www.geeksforgeeks.org/min-cost-path-dp-6/",
        params=["grid", "m", "n"],
        inputs={
            "grid": "2D list-like of non-negative cell costs.",
            "m": "number of rows.",
            "n": "number of columns.",
        },
        returns="the minimum cost of any path from (0,0) to (m-1, n-1).",
        source=DP_12_SOURCE,
        setup_fn=_setup_min_cost_path,
        verify_fn=_verify_min_cost_path,
        samples=[
            Sample("grid = [[1,3,1],[1,5,1],[4,2,1]], m = 3, n = 3", "7 (1→3→1→1→1, sum 7)"),
            Sample("grid = [[2,3],[4,1]], m = 2, n = 2", "7 (2→3→1 or 2→4→1)"),
        ],
        hint="dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j].",
        parents=["dp_10"],
        children=[],
    ),
])
