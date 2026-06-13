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
