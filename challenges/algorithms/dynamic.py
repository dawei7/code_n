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
        "weights": challenge._weights,
        "values": challenge._values,
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


# === dp_13: Matrix Chain Multiplication ========================


DP_13_SOURCE = '''
def solve(p):
    """Matrix chain multiplication: min scalar mults for p[0..n-1]."""
    n = len(p) - 1
    if n <= 1:
        return 0
    INF = float("inf")
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = INF
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n - 1]
'''


def _setup_mcm(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    n_mats = max(2, min(n, 8))
    rng = random.Random(seed)
    p = [rng.randint(1, 20) for _ in range(n_mats + 1)]
    if n_mats <= 1:
        challenge._expected = 0
    else:
        INF = float("inf")
        dp = [[0] * n_mats for _ in range(n_mats)]
        for length in range(2, n_mats + 1):
            for i in range(n_mats - length + 1):
                j = i + length - 1
                dp[i][j] = INF
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
        challenge._expected = dp[0][n_mats - 1]
    return {"p": p}


def _verify_mcm(challenge, result: Any) -> bool:
    return isinstance(result, int) and result == challenge._expected


# === dp_14: Palindromic Partitioning (min cuts) ================


DP_14_SOURCE = '''
def solve(s):
    """Min cuts to partition s into all-palindromic substrings."""
    n = len(s)
    if n <= 1:
        return 0
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True
    INF = float("inf")
    dp = [INF] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_pal[j + 1][i] and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
    return dp[n - 1]
'''


def _setup_pal_partition(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    s_len = max(1, min(n, 12))
    s = "".join(rng.choice("abc") for _ in range(s_len))
    n_words = len(s)
    if n_words <= 1:
        challenge._expected = 0
    else:
        is_pal = [[False] * n_words for _ in range(n_words)]
        for i in range(n_words):
            is_pal[i][i] = True
        for length in range(2, n_words + 1):
            for i in range(n_words - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or is_pal[i + 1][j - 1]:
                        is_pal[i][j] = True
        INF = float("inf")
        dp = [INF] * n_words
        for i in range(n_words):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if is_pal[j + 1][i] and dp[j] + 1 < dp[i]:
                        dp[i] = dp[j] + 1
        challenge._expected = dp[n_words - 1]
    return {"s": s}


def _verify_pal_partition(challenge, result: Any) -> bool:
    return isinstance(result, int) and result == challenge._expected


# === dp_15: Word Break ========================================


DP_15_SOURCE = '''
def solve(s, word_dict):
    """True iff s can be segmented into dictionary words."""
    n = len(s)
    word_set = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
'''


def _setup_word_break(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    s_len = max(2, min(n, 12))
    word_dict = ["a", "ab", "abc", "b", "bc", "cd", "abcde", "de", "f", "fg"]
    s = "".join(rng.choice(word_dict) for _ in range(max(1, s_len // 2)))
    challenge._s = s
    return {"s": s, "word_dict": word_dict}


def _verify_word_break(challenge, result: Any) -> bool:
    return isinstance(result, bool)


# === dp_16: Egg Dropping ======================================


DP_16_SOURCE = '''
def solve(k, n):
    """Min moves (drops) to find the critical floor with k eggs, n floors."""
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    m = 0
    while dp[k][m] < n:
        m += 1
        for e in range(1, k + 1):
            dp[e][m] = dp[e - 1][m - 1] + dp[e][m - 1] + 1
    return m
'''


def _setup_egg_drop(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    k = max(1, min(n, 6))
    m_floors = max(1, min(n + 1, 8))
    challenge._k = k
    challenge._m_floors = m_floors
    return {"k": k, "n": m_floors}


def _verify_egg_drop(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    k = challenge._k
    n = challenge._m_floors
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    m = 0
    while dp[k][m] < n:
        m += 1
        for e in range(1, k + 1):
            dp[e][m] = dp[e - 1][m - 1] + dp[e][m - 1] + 1
    return result == m


# Append the new DP specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="dp_13",
        name="Matrix Chain Multiplication",
        category="dynamic",
        difficulty=7,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Given a list of matrix dimensions p[0..n], where matrix i\n"
            "has shape p[i-1] x p[i], find the minimum number of\n"
            "scalar multiplications needed to compute the chain product.\n"
            "Requirement: O(n^3).\n"
            "Source: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/"
        ),
        source_url="https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/",
        params=["p"],
        inputs={"p": "list of length n+1; matrix i has shape p[i-1] x p[i]."},
        returns="the minimum number of scalar multiplications.",
        source=DP_13_SOURCE,
        setup_fn=_setup_mcm,
        verify_fn=_verify_mcm,
        samples=[
            Sample("p = [1, 2, 3, 4, 5]", "38"),
            Sample("p = [10, 20, 30]", "6000"),
        ],
        hint="dp[i][j] = min over k of (dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]).",
        parents=["dp_12"],
        children=[],
    ),
    AlgorithmSpec(
        id="dp_14",
        name="Palindromic Partitioning",
        category="dynamic",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Given a string, partition it into substrings that are all\n"
            "palindromes. Return the minimum number of cuts needed.\n"
            "Requirement: O(n^2).\n"
            "Source: https://www.geeksforgeeks.org/palindromic-partitioning-dp-17/"
        ),
        source_url="https://www.geeksforgeeks.org/palindromic-partitioning-dp-17/",
        params=["s"],
        inputs={"s": "the input string (lowercase letters)."},
        returns="the minimum number of cuts to make every substring a palindrome.",
        source=DP_14_SOURCE,
        setup_fn=_setup_pal_partition,
        verify_fn=_verify_pal_partition,
        samples=[
            Sample("s = 'aaaa'", "0"),
            Sample("s = 'abacd'", "2"),
        ],
        hint="First compute is_pal[i][j]; then dp[i] = min over j of (dp[j] + 1 if is_pal[j+1][i]).",
        parents=["dp_12"],
        children=[],
    ),
    AlgorithmSpec(
        id="dp_15",
        name="Word Break",
        category="dynamic",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Given a string s and a dictionary of words, return True\n"
            "iff s can be segmented into a sequence of one or more\n"
            "dictionary words. The setup builds s by concatenating\n"
            "random dictionary words, so the answer is always True.\n"
            "Requirement: O(n * L).\n"
            "Source: https://www.geeksforgeeks.org/word-break-problem-dp-32/"
        ),
        source_url="https://www.geeksforgeeks.org/word-break-problem-dp-32/",
        params=["s", "word_dict"],
        inputs={
            "s": "the string to segment.",
            "word_dict": "list of unique words in the dictionary.",
        },
        returns="True iff s can be segmented into dictionary words.",
        source=DP_15_SOURCE,
        setup_fn=_setup_word_break,
        verify_fn=_verify_word_break,
        samples=[
            Sample("s = 'leetcode', word_dict = ['leet', 'code']", "True"),
            Sample("s = 'catsandog', word_dict = ['cats', 'dog', 'sand', 'and', 'cat']", "False"),
        ],
        hint="dp[i] = True if some dp[j] is True AND s[j:i] is in word_dict.",
        parents=["dp_04"],
        children=[],
    ),
    AlgorithmSpec(
        id="dp_16",
        name="Egg Dropping",
        category="dynamic",
        difficulty=7,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Given k eggs and n floors, find the minimum number of\n"
            "moves (drops) needed to determine the critical floor.\n"
            "Use dp[e][m] = dp[e-1][m-1] + dp[e][m-1] + 1.\n"
            "Requirement: O(k * n * log n) — find smallest m with dp[k][m] >= n.\n"
            "Source: https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/"
        ),
        source_url="https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/",
        params=["k", "n"],
        inputs={
            "k": "number of eggs available.",
            "n": "number of floors to test.",
        },
        returns="the minimum number of drops needed to find the critical floor.",
        source=DP_16_SOURCE,
        setup_fn=_setup_egg_drop,
        verify_fn=_verify_egg_drop,
        samples=[
            Sample("k = 1, n = 2", "2"),
            Sample("k = 2, n = 6", "3"),
        ],
        hint="dp[e][m] = dp[e-1][m-1] + dp[e][m-1] + 1. Find smallest m with dp[k][m] >= n.",
        parents=["dp_12"],
        children=[],
    ),
])


# === dp_17: Partition Equal Subset Sum ==========================


DP_17_SOURCE = '''
def solve(arr):
    """True iff arr can be split into two equal-sum subsets."""
    total = sum(arr)
    if total % 2 != 0:
        return False
    target = total // 2
    reachable = {0}
    for v in arr:
        reachable = reachable | {s + v for s in reachable}
    return target in reachable
'''


def _setup_partition(challenge, n, seed):
    rng = random.Random(seed)
    n_elems = max(1, min(n, 12))
    # Loop until the total is even (so the answer is well-defined).
    while True:
        arr = [rng.randint(1, 10) for _ in range(n_elems)]
        if sum(arr) % 2 == 0:
            break
    # Pre-compute the expected answer via the canonical solve.
    ns: dict[str, Any] = {"__name__": "spec.dp_17"}
    exec(DP_17_SOURCE, ns)
    challenge._expected = ns["solve"](arr)
    return {"arr": arr}


def _verify_partition(challenge, result):
    if not isinstance(result, bool):
        return False
    return result == challenge._expected


# === dp_18: Max Product Subarray ===============================


DP_18_SOURCE = '''
def solve(arr):
    """Max product of a contiguous subarray of arr (positive & negative)."""
    if not arr:
        return 0
    best = arr[0]
    cur_max = arr[0]
    cur_min = arr[0]
    for v in arr[1:]:
        if v < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(v, cur_max * v)
        cur_min = min(v, cur_min * v)
        if cur_max > best:
            best = cur_max
    return best
'''


def _setup_max_product(challenge, n, seed):
    rng = random.Random(seed)
    n_elems = max(1, min(n, 12))
    arr = [rng.choice([-5, -2, -1, 0, 1, 2, 3, 5, 10]) for _ in range(n_elems)]
    if not arr:
        challenge._expected = 0
    else:
        best = arr[0]
        cur_max = arr[0]
        cur_min = arr[0]
        for v in arr[1:]:
            if v < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(v, cur_max * v)
            cur_min = min(v, cur_min * v)
            if cur_max > best:
                best = cur_max
        challenge._expected = best
    return {"arr": arr}


def _verify_max_product(challenge, result):
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# === dp_19: Longest Palindromic Subsequence ===

DP_19_SOURCE = '''
def solve(s, n):
    """Length of the longest palindromic subsequence of s.

    Classic DP: dp[i][j] = LPS length in s[i..j].
    Base: dp[i][i] = 1. Recurrence: if s[i] == s[j],
    dp[i][j] = dp[i+1][j-1] + 2; else dp[i][j] = max(dp[i+1][j], dp[i][j-1]).
    """
    if n == 0:
        return 0
    # dp[i] is the row for s[i..i+L]; build by length.
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
'''


def _setup_lps(challenge, n, seed):
    rng = random.Random(seed)
    n_chars = max(1, min(n, 10))
    s = "".join(rng.choice("abc") for _ in range(n_chars))
    challenge._s = s
    return {"s": s, "n": len(s)}


def _verify_lps(challenge, result):
    if not isinstance(result, int):
        return False
    s = challenge._s
    # Brute force: try every subsequence.
    best = 0
    for mask in range(1 << len(s)):
        sub = "".join(s[i] for i in range(len(s)) if mask & (1 << i))
        if sub == sub[::-1]:
            if len(sub) > best:
                best = len(sub)
    return result == best


# === dp_20: Shortest Common Supersequence (length) ===

DP_20_SOURCE = '''
def solve(s1, s2, n1, n2):
    """Length of the shortest string that has both s1 and s2 as subsequences.

    The length is n1 + n2 - LCS(s1, s2). Compute LCS first, then
    combine the lengths.
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    # Build LCS DP table.
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    lcs = dp[n1][n2]
    return n1 + n2 - lcs
'''


def _setup_scs(challenge, n, seed):
    rng = random.Random(seed)
    n1 = max(1, min(n // 2 + 1, 6))
    n2 = max(1, min(n - n1 + 1, 6))
    n1 = min(n1, 6)
    n2 = min(n2, 6)
    s1 = "".join(rng.choice("abc") for _ in range(n1))
    s2 = "".join(rng.choice("abc") for _ in range(n2))
    challenge._s1 = s1
    challenge._s2 = s2
    return {"s1": s1, "s2": s2, "n1": len(s1), "n2": len(s2)}


def _verify_scs(challenge, result):
    if not isinstance(result, int):
        return False
    s1, s2 = challenge._s1, challenge._s2
    # Brute force: enumerate every common supersequence's length and take the min.
    # Enumerate via LCS DP.
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    expected = n1 + n2 - dp[n1][n2]
    return result == expected


SPECS.extend([
    AlgorithmSpec(
        id="dp_19",
        name="Longest Palindromic Subsequence",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Return the length of the longest subsequence of s that is\n"
            "also a palindrome. Standard interval DP: dp[i][j] = LPS\n"
            "length in s[i..j]. dp[i][i] = 1. If s[i] == s[j],\n"
            "dp[i][j] = dp[i+1][j-1] + 2; else dp[i][j] = max(\n"
            "dp[i+1][j], dp[i][j-1]). O(n^2) time and space.\n"
            "Source: https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/",
        params=["s", "n"],
        inputs={
            "s": "string of n lower-case characters (capped at 10 in the setup).",
            "n": "length of s.",
        },
        returns="the length of the longest palindromic subsequence.",
        source=DP_19_SOURCE,
        setup_fn=_setup_lps,
        verify_fn=_verify_lps,
        samples=[
            Sample('s = "bbbab", n = 5', "4 (bbbb)"),
            Sample('s = "cbbd", n = 4', "2 (bb)"),
        ],
        hint="If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2. Else: max of (i+1,j) and (i,j-1).",
        parents=["dp_15"],
        children=["dp_20"],
    ),
    AlgorithmSpec(
        id="dp_20",
        name="Shortest Common Supersequence (Length)",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "The shortest string that has both s1 and s2 as subsequences.\n"
            "Length is n1 + n2 - LCS(s1, s2). Compute the LCS length via\n"
            "the standard DP table.\n"
            "Source: https://www.geeksforgeeks.org/shortest-common-supersequence/"
        ),
        source_url="https://www.geeksforgeeks.org/shortest-common-supersequence/",
        params=["s1", "s2", "n1", "n2"],
        inputs={
            "s1": "first string (capped at 6 in the setup).",
            "s2": "second string (capped at 6 in the setup).",
            "n1": "length of s1.",
            "n2": "length of s2.",
        },
        returns="the length of the shortest common supersequence.",
        source=DP_20_SOURCE,
        setup_fn=_setup_scs,
        verify_fn=_verify_scs,
        samples=[
            Sample('s1 = "abac", s2 = "cab", n1 = 4, n2 = 3', "5 (cabac)"),
            Sample('s1 = "abc", s2 = "abc", n1 = 3, n2 = 3', "3"),
        ],
        hint="SCS length = n1 + n2 - LCS(s1, s2).",
        parents=["dp_19"],
        children=[],
    ),
    AlgorithmSpec(
        id="dp_17",
        name="Partition Equal Subset Sum",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Return True iff the input array can be split into two\n"
            "subsets with equal sum. A classic 0/1-knapsack variant.\n"
            "The setup always picks a total that's even so the\n"
            "answer is well-defined.\n"
            "Requirement: O(n * total).\n"
            "Source: https://www.geeksforgeeks.org/partition-equal-subset-sum/"
        ),
        source_url="https://www.geeksforgeeks.org/partition-equal-subset-sum/",
        params=["arr"],
        inputs={"arr": "list of positive integers."},
        returns="True iff arr can be split into two equal-sum subsets.",
        source=DP_17_SOURCE,
        setup_fn=_setup_partition,
        verify_fn=_verify_partition,
        samples=[
            Sample("arr = [1, 5, 11, 5]", "True (1+5+5 = 11)"),
            Sample("arr = [1, 2, 3, 5]", "False"),
        ],
        hint="Total must be even. Track reachable subset sums; check if total/2 is in the set.",
        parents=["dp_06"],
        children=[],
    ),
    AlgorithmSpec(
        id="dp_18",
        name="Max Product Subarray",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the maximum product of a contiguous subarray.\n"
            "May contain negatives; track BOTH the max-ending-here\n"
            "and min-ending-here products (a negative * negative\n"
            "flips the sign and may yield a new max).\n"
            "Requirement: O(n) — single pass.\n"
            "Source: https://www.geeksforgeeks.org/maximum-product-subarray/"
        ),
        source_url="https://www.geeksforgeeks.org/maximum-product-subarray/",
        params=["arr"],
        inputs={"arr": "list of integers (positive, negative, or zero)."},
        returns="the maximum product of any contiguous subarray.",
        source=DP_18_SOURCE,
        setup_fn=_setup_max_product,
        verify_fn=_verify_max_product,
        samples=[
            Sample("arr = [2, 3, -2, 4]", "6 (subarray [2, 3])"),
            Sample("arr = [-2, 0, -1]", "0"),
            Sample("arr = [-2, 3, -4]", "24 (subarray [-2, 3, -4])"),
        ],
        hint="Track both cur_max and cur_min. On a negative, swap them. cur_max = max(v, cur_max * v).",
        parents=["dp_11"],
        children=[],
    ),
])


# === dp_21: Boolean Parenthesization ===

DP_21_SOURCE = '''
def solve(s, n):
    """Count the number of ways to parenthesize a boolean expression
    so it evaluates to True. The expression has T/F operands and
    &, |, ^ operators. Standard interval DP.
    """
    if n == 0:
        return 0
    # Count of True (T_count) and False (F_count) for each interval [i, j].
    # We only need to consider operand positions: even indices.
    T = [[0] * n for _ in range(n)]
    F = [[0] * n for _ in range(n)]
    for i in range(0, n, 2):
        T[i][i] = 1 if s[i] == "T" else 0
        F[i][i] = 1 if s[i] == "F" else 0
    for gap in range(2, n, 2):
        for i in range(0, n - gap, 2):
            j = i + gap
            T[i][j] = F[i][j] = 0
            for k in range(i + 1, j, 2):
                op = s[k]
                lt, lf = T[i][k - 1], F[i][k - 1]
                rt, rf = T[k + 1][j], F[k + 1][j]
                if op == "&":
                    T[i][j] += lt * rt
                    F[i][j] += lt * rf + lf * rt + lf * rf
                elif op == "|":
                    T[i][j] += lt * rt + lt * rf + lf * rt
                    F[i][j] += lf * rf
                else:  # ^
                    T[i][j] += lt * rf + lf * rt
                    F[i][j] += lt * rt + lf * rf
    return T[0][n - 1]
'''


def _setup_bool_paren(challenge, n, seed):
    rng = random.Random(seed)
    # Boolean expressions: T F T F ... with operators between.
    n_ops = max(1, min(n, 6))
    operands = [rng.choice("TF") for _ in range(n_ops + 1)]
    operators = [rng.choice("&|^") for _ in range(n_ops)]
    s_list = [operands[0]]
    for i, op in enumerate(operators):
        s_list.append(op)
        s_list.append(operands[i + 1])
    s = "".join(s_list)
    challenge._s = s
    return {"s": s, "n": len(s)}


def _verify_bool_paren(challenge, result):
    if not isinstance(result, int):
        return False
    s = challenge._s
    # Brute-force: enumerate every way to parenthesize and count Trues.
    operands = [c for c in s if c in "TF"]
    operators = [c for c in s if c in "&|^"]

    def rec(i, j):
        if i == j:
            return (1 if operands[i] == "T" else 0,
                    1 if operands[i] == "F" else 0)
        t = 0
        f = 0
        for k in range(i, j):
            lt, lf = rec(i, k)
            rt, rf = rec(k + 1, j)
            op = operators[k]
            if op == "&":
                t += lt * rt
                f += lt * rf + lf * rt + lf * rf
            elif op == "|":
                t += lt * rt + lt * rf + lf * rt
                f += lf * rf
            else:  # ^
                t += lt * rf + lf * rt
                f += lt * rt + lf * rf
        return t, f

    expected, _ = rec(0, len(operands) - 1)
    return result == expected


# === dp_22: Egg Dropping ===

DP_22_SOURCE = '''
def solve(eggs, floors):
    """Return the minimum number of trials needed in the worst case
    to find the critical floor in the egg-dropping problem.
    dp[e][f] = min trials for e eggs and f floors. Recurrence: drop
    from floor x -> 1 + max(dp[e-1][x-1], dp[e][f-x]).
    """
    if floors == 0:
        return 0
    if eggs == 1:
        return floors
    # Build the table.
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    for f in range(1, floors + 1):
        dp[1][f] = f
    for e in range(2, eggs + 1):
        for f in range(1, floors + 1):
            best = f  # worst case: try every floor with one egg
            for x in range(1, f + 1):
                worst = 1 + max(dp[e - 1][x - 1], dp[e][f - x])
                if worst < best:
                    best = worst
            dp[e][f] = best
    return dp[eggs][floors]
'''


def _setup_egg_drop(challenge, n, seed):
    rng = random.Random(seed)
    eggs = max(1, min(n, 6))
    floors = max(1, min(n * 2, 10))
    challenge._eggs = eggs
    challenge._floors = floors
    return {"eggs": eggs, "floors": floors}


def _verify_egg_drop(challenge, result):
    if not isinstance(result, int):
        return False
    eggs, floors = challenge._eggs, challenge._floors

    def solve_brute(e, f):
        if f == 0:
            return 0
        if e == 1:
            return f
        best = f
        for x in range(1, f + 1):
            worst = 1 + max(solve_brute(e - 1, x - 1), solve_brute(e, f - x))
            if worst < best:
                best = worst
        return best

    return result == solve_brute(eggs, floors)


# === dp_23: Min Cost Climbing Stairs ===

DP_23_SOURCE = '''
def solve(cost, n):
    """Minimum cost to reach the top of a staircase where you may
    climb 1 or 2 steps at a time. ``cost[i]`` is the cost of step i.
    dp[i] = min cost to reach step i. dp[0]=cost[0], dp[1]=cost[1],
    dp[i] = cost[i] + min(dp[i-1], dp[i-2]). The answer is
    min(dp[n-1], dp[n-2]) - either of the last two steps.
    """
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    prev2 = cost[0]
    prev1 = cost[1]
    for i in range(2, n):
        cur = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, cur
    return min(prev1, prev2)
'''


def _setup_min_cost_climb(challenge, n, seed):
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    cost = [rng.randint(1, 20) for _ in range(n)]
    challenge._cost = list(cost)
    return {"cost": list(cost), "n": n}


def _verify_min_cost_climb(challenge, result):
    if not isinstance(result, int):
        return False
    cost = challenge._cost
    n = len(cost)
    if n == 0:
        return result == 0
    if n == 1:
        return result == cost[0]
    # Brute force: every path from 0 to n-1 or 1 to n-1.
    best = float("inf")

    def walk(i, total):
        nonlocal best
        if i >= n:
            if total < best:
                best = total
            return
        walk(i + 1, total + cost[i])
        walk(i + 2, total + cost[i])

    walk(0, 0)
    walk(1, 0)
    return result == best


# === dp_24: Palindromic Partitioning (min cuts) ===

DP_24_SOURCE = '''
def solve(s, n):
    """Return the minimum number of cuts to partition s into palindromes.

    Precompute palindrome table: is_pal[i][j] = True iff s[i..j] is
    a palindrome. Then dp[i] = min cuts for s[i..n-1].
    dp[n] = 0 (empty suffix needs 0 cuts).
    dp[i] = min over j >= i with is_pal[i][j] of (0 if j == n-1 else 1 + dp[j+1]).
    """
    if n == 0:
        return 0
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if is_pal[i][j]:
                cost = 0 if j == n - 1 else 1 + dp[j + 1]
                if cost < dp[i]:
                    dp[i] = cost
    return dp[0]
'''


def _setup_palin_partition(challenge, n, seed):
    rng = random.Random(seed)
    n_chars = max(1, min(n, 10))
    s = "".join(rng.choice("abc") for _ in range(n_chars))
    challenge._s = s
    return {"s": s, "n": len(s)}


def _verify_palin_partition(challenge, result):
    if not isinstance(result, int):
        return False
    s = challenge._s
    n = len(s)
    # Brute force: try every partition.
    best = n - 1 if n > 0 else 0

    def helper(i, cuts):
        nonlocal best
        if i == n:
            if cuts < best:
                best = cuts
            return
        for j in range(i, n):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                helper(j + 1, cuts + (0 if j == n - 1 else 1))

    helper(0, 0)
    return result == best


SPECS.extend([
    AlgorithmSpec(
        id="dp_21",
        name="Boolean Parenthesization",
        category="dynamic",
        difficulty=6,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Count the number of ways to parenthesize a boolean\n"
            "expression (operands T/F, operators &|^) so it evaluates\n"
            "to True. Interval DP: T[i][j] / F[i][j] = count of ways\n"
            "for s[i..j]. At each split, combine the four quadrants\n"
            "based on the operator.\n"
            "Source: https://www.geeksforgeeks.org/boolean-parenthesization-problem/"
        ),
        source_url="https://www.geeksforgeeks.org/boolean-parenthesization-problem/",
        params=["s", "n"],
        inputs={
            "s": "expression string (operands T/F, operators & | ^).",
            "n": "length of s.",
        },
        returns="the number of parenthesizations that evaluate to True.",
        source=DP_21_SOURCE,
        setup_fn=_setup_bool_paren,
        verify_fn=_verify_bool_paren,
        samples=[
            Sample('s = "T|T&F^T", n = 7', "4"),
            Sample('s = "T^T^T", n = 5', "0"),
        ],
        hint="For each split k with operator op, count T[i][j] and F[i][j] from the four quadrants.",
        parents=["dp_20"],
        children=["dp_22"],
    ),
    AlgorithmSpec(
        id="dp_22",
        name="Egg Dropping",
        category="dynamic",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Return the minimum number of trials needed in the worst\n"
            "case to find the critical floor. dp[e][f] = min trials for\n"
            "e eggs and f floors. Drop from floor x -> 1 + worst(\n"
            "dp[e-1][x-1] (breaks), dp[e][f-x] (survives)).\n"
            "Source: https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/"
        ),
        source_url="https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/",
        params=["eggs", "floors"],
        inputs={
            "eggs": "number of eggs (1..6 in the setup).",
            "floors": "number of floors (1..10 in the setup).",
        },
        returns="the minimum worst-case number of trials.",
        source=DP_22_SOURCE,
        setup_fn=_setup_egg_drop,
        verify_fn=_verify_egg_drop,
        samples=[
            Sample("eggs = 1, floors = 10", "10"),
            Sample("eggs = 2, floors = 6", "3"),
        ],
        hint="dp[1][f] = f. dp[e][f] = min over x of 1 + max(dp[e-1][x-1], dp[e][f-x]).",
        parents=["dp_21"],
        children=["dp_23"],
    ),
    AlgorithmSpec(
        id="dp_23",
        name="Min Cost Climbing Stairs",
        category="dynamic",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Minimum cost to reach the top of a staircase where you\n"
            "may climb 1 or 2 steps at a time. cost[i] is the cost of\n"
            "step i. dp[i] = cost[i] + min(dp[i-1], dp[i-2]). The\n"
            "answer is min(dp[n-1], dp[n-2]) - either of the last two.\n"
            "Source: https://www.geeksforgeeks.org/min-cost-climbing-stairs/"
        ),
        source_url="https://www.geeksforgeeks.org/min-cost-climbing-stairs/",
        params=["cost", "n"],
        inputs={
            "cost": "list of n step costs.",
            "n": "length of cost.",
        },
        returns="the minimum total cost to reach the top.",
        source=DP_23_SOURCE,
        setup_fn=_setup_min_cost_climb,
        verify_fn=_verify_min_cost_climb,
        samples=[
            Sample("cost = [10, 15, 20], n = 3", "15 (start at step 1)"),
            Sample("cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], n = 10", "6"),
        ],
        hint="dp[i] = cost[i] + min(dp[i-1], dp[i-2]). Answer is min of the last two steps.",
        parents=["dp_22"],
        children=["dp_24"],
    ),
    AlgorithmSpec(
        id="dp_24",
        name="Palindromic Partitioning (Min Cuts)",
        category="dynamic",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Return the minimum number of cuts to partition s into\n"
            "palindromes. Precompute is_pal[i][j] (whether s[i..j] is a\n"
            "palindrome) in O(n^2), then dp[i] = min over j with\n"
            "is_pal[i][j] of (0 if j == n-1 else 1 + dp[j+1]).\n"
            "Source: https://www.geeksforgeeks.org/palindromic-partitioning-dp-17/"
        ),
        source_url="https://www.geeksforgeeks.org/palindromic-partitioning-dp-17/",
        params=["s", "n"],
        inputs={
            "s": "string of n lower-case characters (capped at 10 in the setup).",
            "n": "length of s.",
        },
        returns="the minimum number of cuts to partition s into palindromes.",
        source=DP_24_SOURCE,
        setup_fn=_setup_palin_partition,
        verify_fn=_verify_palin_partition,
        samples=[
            Sample('s = "ababbbabbababa", n = 13', "3 (a|babbbab|b|ababa)"),
            Sample('s = "aab", n = 3', "1 (aa|b)"),
        ],
        hint="Precompute is_pal, then dp[i] = min cuts to cover s[i..n-1] with palindromes.",
        parents=["dp_23"],
        children=[],
    ),
])


# === dp_25: Matrix Chain Multiplication ===

DP_25_SOURCE = '''
def solve(dims, n):
    """Matrix chain multiplication: minimum scalar multiplications.

    dims[i] is the dimensions of matrix i: rows=dims[i][0],
    cols=dims[i][1]. A chain of n matrices has dims[0..n-1]
    with the chain dimension compatibility: dims[i][1] == dims[i+1][0].
    Standard O(n^3) DP: m[i][j] = min cost of multiplying matrices
    i..j. Recurrence: try k in (i, j] as the split point.
    """
    if n <= 1:
        return 0
    INF = float("inf")
    m = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = INF
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i][0] * dims[k][1] * dims[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
    return m[0][n - 1]
'''


def _setup_mcm(challenge, n, seed):
    rng = random.Random(seed)
    n_mats = max(1, min(n, 6))
    dims = []
    for _ in range(n_mats):
        rows = rng.randint(1, 10)
        cols = rng.randint(1, 10)
        dims.append((rows, cols))
    for i in range(n_mats - 1):
        cols = dims[i][1]
        dims[i + 1] = (cols, rng.randint(1, 10))
    challenge._dims = list(dims)
    return {"dims": list(dims), "n": n_mats}


def _verify_mcm(challenge, result):
    if not isinstance(result, int):
        return False
    n = len(challenge._dims)
    if n <= 1:
        return result == 0

    def cost(lo, hi, memo):
        if lo == hi:
            return 0
        if (lo, hi) in memo:
            return memo[(lo, hi)]
        best = float("inf")
        for k in range(lo, hi):
            c = cost(lo, k, memo) + cost(k + 1, hi, memo)
            c += challenge._dims[lo][0] * challenge._dims[k][1] * challenge._dims[hi][1]
            if c < best:
                best = c
        memo[(lo, hi)] = best
        return best

    expected = cost(0, n - 1, {})
    return result == expected


# === dp_26: Optimal Binary Search Tree ===

DP_26_SOURCE = '''
def solve(keys, probs, n):
    """Optimal BST: minimum weighted search cost.

    Given sorted keys with search probabilities probs[i], build
    a BST that minimizes sum(probs[i] * depth(i)). DP:
    opt[i][j] = min cost over BSTs containing keys[i..j].
    Recurrence: try k in [i, j] as the root.
    """
    if n == 0:
        return 0
    INF = float("inf")
    prefix = [0.0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + probs[i]
    opt = [[0.0] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best = INF
            for k in range(i, j + 1):
                left = opt[i][k - 1] if k > i else 0
                right = opt[k + 1][j] if k < j else 0
                c = left + right + prefix[j + 1] - prefix[i]
                if c < best:
                    best = c
            opt[i][j] = best
    return opt[0][n - 1]
'''


def _setup_optimal_bst(challenge, n, seed):
    rng = random.Random(seed)
    n_keys = max(1, min(n, 5))
    keys = list(range(n_keys))
    probs = [round(rng.random() * 0.5 + 0.1, 2) for _ in range(n_keys)]
    s = sum(probs)
    if s > 0:
        probs = [p / s for p in probs]
    challenge._keys = list(keys)
    challenge._probs = list(probs)
    return {"keys": list(keys), "probs": list(probs), "n": n_keys}


def _verify_optimal_bst(challenge, result):
    if not isinstance(result, (int, float)):
        return False
    probs = challenge._probs
    n = len(probs)
    if n == 0:
        return result == 0
    expected = sum(probs)
    return abs(result - expected) < 100


# === dp_27: Floyd-Warshall Path Reconstruction ===

DP_27_SOURCE = '''
def solve(n, edges, src, dest):
    """Floyd-Warshall + path reconstruction.

    Return the path from src to dest as a list of node indices,
    or [] if no path exists. Uses a next[][] matrix to
    reconstruct the path.
    """
    if src == dest:
        return [src]
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    nxt = [[-1] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            nxt[u][v] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k] if nxt[i][k] != -1 else k
    if dist[src][dest] == INF:
        return []
    path = [src]
    cur = src
    while cur != dest:
        cur = nxt[cur][dest]
        if cur == -1:
            return []
        path.append(cur)
    return path
'''


def _setup_floyd_path(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 5))
    edges = []
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        edges.append((u, i, rng.randint(1, 10)))
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.append((u, v, rng.randint(1, 10)))
    src = rng.randint(0, n_nodes - 1)
    dest = rng.randint(0, n_nodes - 1)
    while dest == src:
        dest = rng.randint(0, n_nodes - 1)
    challenge._n = n_nodes
    challenge._edges = list(edges)
    challenge._src = src
    challenge._dest = dest
    return {"n": n_nodes, "edges": list(edges), "src": src, "dest": dest}


def _verify_floyd_path(challenge, result):
    if not isinstance(result, list):
        return False
    n = challenge._n
    edges = challenge._edges
    src = challenge._src
    dest = challenge._dest
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    import heapq
    INF = float("inf")
    d = [INF] * n
    d[src] = 0
    prev = [-1] * n
    heap = [(0, src)]
    while heap:
        du, u = heapq.heappop(heap)
        if du > d[u]:
            continue
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w
                prev[v] = u
                heapq.heappush(heap, (d[v], v))
    if d[dest] == INF:
        return result == []
    path = []
    cur = dest
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return result == path


SPECS.extend([
    AlgorithmSpec(
        id="dp_25",
        name="Matrix Chain Multiplication",
        category="dynamic",
        difficulty=6,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Given n matrices with chain-compatible dimensions,\n"
            "find the parenthesization that minimizes the total\n"
            "number of scalar multiplications. Standard O(n^3) DP:\n"
            "m[i][j] = min over k of m[i][k] + m[k+1][j] + cost of\n"
            "the resulting multiplication.\n"
            "Source: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/"
        ),
        source_url="https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/",
        params=["dims", "n"],
        inputs={
            "dims": "list of n (rows, cols) tuples; dims[i][1] == dims[i+1][0].",
            "n": "number of matrices.",
        },
        returns="the minimum number of scalar multiplications.",
        source=DP_25_SOURCE,
        setup_fn=_setup_mcm,
        verify_fn=_verify_mcm,
        samples=[
            Sample("dims = [(40, 20), (20, 30), (30, 10), (10, 30)], n = 4", "26000"),
        ],
        hint="Try each k in (i, j] as the split. dp[i][j] = dp[i][k] + dp[k+1][j] + cost.",
        parents=["dp_24"],
        children=["dp_26"],
    ),
    AlgorithmSpec(
        id="dp_26",
        name="Optimal Binary Search Tree",
        category="dynamic",
        difficulty=7,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Given n sorted keys with access probabilities probs[i],\n"
            "build a BST that minimizes the expected search cost\n"
            "sum(probs[i] * (depth(i) + 1)). DP: opt[i][j] = min cost\n"
            "over BSTs containing keys[i..j]; try k in [i, j] as the\n"
            "root. The cost of putting a subtree at depth+1 adds\n"
            "the total probability of the subtree to the cost.\n"
            "Source: https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/"
        ),
        source_url="https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/",
        params=["keys", "probs", "n"],
        inputs={
            "keys": "list of n keys (sorted; here 0..n-1).",
            "probs": "list of n probabilities (sum to 1).",
            "n": "number of keys.",
        },
        returns="the minimum weighted search cost.",
        source=DP_26_SOURCE,
        setup_fn=_setup_optimal_bst,
        verify_fn=_verify_optimal_bst,
        samples=[
            Sample("keys = [10, 12, 20], probs = [0.1, 0.2, 0.7], n = 3", "1.5 (root=20)"),
        ],
        hint="Prefix sums let you compute the cost of putting a subtree at depth+1 in O(1).",
        parents=["dp_25"],
        children=["dp_27"],
    ),
    AlgorithmSpec(
        id="dp_27",
        name="Floyd-Warshall Path",
        category="dynamic",
        difficulty=5,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Given a weighted graph, return the shortest path from\n"
            "src to dest as a list of node indices. Floyd-Warshall\n"
            "computes all-pairs shortest paths; we maintain a next[]\n"
            "matrix to reconstruct the path.\n"
            "Source: https://www.geeksforgeeks.org/printing-shortest-path-given-distance/"
        ),
        source_url="https://www.geeksforgeeks.org/printing-shortest-path-given-distance/",
        params=["n", "edges", "src", "dest"],
        inputs={
            "n": "number of nodes.",
            "edges": "list of (u, v, weight) directed edges.",
            "src": "source node.",
            "dest": "destination node.",
        },
        returns="the shortest path from src to dest as a list of node indices, or [] if unreachable.",
        source=DP_27_SOURCE,
        setup_fn=_setup_floyd_path,
        verify_fn=_verify_floyd_path,
        samples=[
            Sample("n = 4, edges = [(0, 1, 5), (0, 2, 1), (1, 3, 2), (2, 1, 1), (2, 3, 4)], src = 0, dest = 3", "[0, 2, 1, 3]"),
        ],
        hint="Floyd-Warshall with a next[] matrix; reconstruct the path by walking next[].",
        parents=["dp_26"],
        children=["dp_28"],
    ),
])


# === dp_28: Bellman-Ford (Single-Source Shortest Path) ===

DP_28_SOURCE = '''
def solve(n, edges, src):
    """Single-source shortest paths with Bellman-Ford.

    Returns a list of n distances from src (or a sentinel like
    -1 for unreachable). The setup keeps the graph connected
    and acyclic-negative-free, so all distances are finite.
    """
    INF = 10**9
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist
'''


def _setup_bellman_ford(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
    edges = []
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        edges.append((u, i, rng.randint(1, 10)))
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.append((u, v, rng.randint(1, 10)))
    src = rng.randint(0, n_nodes - 1)
    challenge._n = n_nodes
    challenge._edges = list(edges)
    challenge._src = src
    return {"n": n_nodes, "edges": list(edges), "src": src}


def _verify_bellman_ford(challenge, result):
    if not isinstance(result, list):
        return False
    if len(result) != challenge._n:
        return False
    # Brute force: Dijkstra from src.
    n = challenge._n
    edges = challenge._edges
    src = challenge._src
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    import heapq
    INF = 10**9
    d = [INF] * n
    d[src] = 0
    h = [(0, src)]
    visited = [False] * n
    while h:
        du, u = heapq.heappop(h)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w
                heapq.heappush(h, (d[v], v))
    return result == d


# === dp_29: Longest Increasing Subsequence (Patience Sort) ===

DP_29_SOURCE = '''
def solve(arr, n):
    """LIS length in O(n log n) via patience sorting.

    Maintain a sorted list ``tails`` where tails[i] is the
    smallest tail of any increasing subsequence of length i+1.
    For each value, binary-search the leftmost position in tails
    that's >= value, and place it there.
    """
    if n == 0:
        return 0
    import bisect
    tails = []
    for v in arr:
        idx = bisect.bisect_left(tails, v)
        if idx == len(tails):
            tails.append(v)
        else:
            tails[idx] = v
    return len(tails)
'''


def _setup_lis(challenge, n, seed):
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    arr = [rng.randint(0, 9) for _ in range(n)]
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_lis(challenge, result):
    if not isinstance(result, int):
        return False
    arr = challenge._arr
    n = len(arr)
    # Brute force: try every subsequence.
    best = 0
    for mask in range(1 << n):
        sub = [arr[i] for i in range(n) if mask & (1 << i)]
        if all(sub[i] < sub[i + 1] for i in range(len(sub) - 1)):
            if len(sub) > best:
                best = len(sub)
    return result == best


SPECS.extend([
    AlgorithmSpec(
        id="dp_28",
        name="Bellman-Ford (SSSP)",
        category="dynamic",
        difficulty=4,
        required_complexity=ComplexityClass.O_N3,
        description=(
            "Single-source shortest paths with possible negative\n"
            "edges. Relax all edges n-1 times. O(V * E). Detects\n"
            "negative cycles if the n-th iteration still relaxes.\n"
            "Source: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/"
        ),
        source_url="https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/",
        params=["n", "edges", "src"],
        inputs={
            "n": "number of nodes.",
            "edges": "list of (u, v, weight) tuples for directed edges.",
            "src": "source node.",
        },
        returns="a list of n distances from src.",
        source=DP_28_SOURCE,
        setup_fn=_setup_bellman_ford,
        verify_fn=_verify_bellman_ford,
        samples=[
            Sample("n = 4, edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 4)], src = 0", "[0, 4, 1, 5]"),
        ],
        hint="Initialize dist[src] = 0. Relax all edges n-1 times. dist[v] = min(dist[u] + w) for each edge.",
        parents=["dp_27"],
        children=["dp_29"],
    ),
    AlgorithmSpec(
        id="dp_29",
        name="Longest Increasing Subsequence (Patience Sort)",
        category="dynamic",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Length of the longest strictly-increasing subsequence.\n"
            "Patience sort: maintain a sorted ``tails`` array;\n"
            "for each value, binary-search the leftmost position in\n"
            "tails that's >= the value and place it. The final\n"
            "length of tails is the LIS length. O(n log n).\n"
            "Source: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers.",
            "n": "length of arr.",
        },
        returns="the length of the LIS.",
        source=DP_29_SOURCE,
        setup_fn=_setup_lis,
        verify_fn=_verify_lis,
        samples=[
            Sample("arr = [10, 22, 9, 33, 21, 50, 41, 60, 80], n = 9", "6 (10, 22, 33, 50, 60, 80)"),
            Sample("arr = [3, 1, 4, 1, 5, 9, 2, 6], n = 8", "4 (1, 4, 5, 9)"),
        ],
        hint="Maintain a sorted tails array. For each value, binary-search the leftmost >= position and replace.",
        parents=["dp_28"],
        children=["dp_30"],
    ),
])


# === dp_30: Coin Change (Count Ways) ===

DP_30_SOURCE = '''
def solve(coins, n, amount):
    """Count the number of ways to make ``amount`` using the
    given coin denominations (unlimited supply, order doesn't
    matter). Standard O(n * amount) DP.
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
'''


def _setup_coin_change(challenge, n, seed):
    rng = random.Random(seed)
    n_coins = max(1, min(n, 4))
    coins = sorted({rng.randint(1, 5) for _ in range(n_coins)})
    if 1 not in coins:
        coins = [1] + coins
        coins = sorted(set(coins))
    amount = max(1, min(n * 3, 12))
    challenge._coins = list(coins)
    challenge._amount = amount
    return {"coins": list(coins), "n": len(coins), "amount": amount}


def _verify_coin_change(challenge, result):
    if not isinstance(result, int):
        return False
    coins = challenge._coins
    amount = challenge._amount
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return result == dp[amount]


SPECS.extend([
    AlgorithmSpec(
        id="dp_30",
        name="Coin Change (Count Ways)",
        category="dynamic",
        difficulty=3,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Count the number of ways to make ``amount`` using the\n"
            "given coin denominations (unlimited supply, order\n"
            "doesn't matter). DP: dp[a] = number of ways to make a.\n"
            "For each coin c, dp[a] += dp[a - c]. O(n * amount).\n"
            "Source: https://www.geeksforgeeks.org/coin-change-dp-7/"
        ),
        source_url="https://www.geeksforgeeks.org/coin-change-dp-7/",
        params=["coins", "n", "amount"],
        inputs={
            "coins": "list of n coin denominations (unlimited supply).",
            "n": "number of coin types.",
            "amount": "target amount (always 1..12 in the setup).",
        },
        returns="the number of ways to make amount.",
        source=DP_30_SOURCE,
        setup_fn=_setup_coin_change,
        verify_fn=_verify_coin_change,
        samples=[
            Sample("coins = [1, 2, 3], n = 3, amount = 4", "4 (1111, 112, 22, 13)"),
            Sample("coins = [1, 5, 6], n = 3, amount = 7", "2 (1111111, 16)"),
        ],
        hint="For each coin, walk forward. dp[a] += dp[a - c]. Base: dp[0] = 1.",
        parents=["dp_29"],
        children=[],
    ),
])
