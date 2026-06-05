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
