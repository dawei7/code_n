"""Divide and conquer algorithms.

Three problems from GFG's divide-and-conquer catalog:

  01 Power(x, n)           - x^n via half-the-exponent recursion
  02 Majority Element      - Boyer-Moore linear-time vote
  03 Kth Smallest (Quickselect) - partition like quicksort, but
    only recurse into the side that contains the answer

The verify_fn re-runs the canonical algorithm and compares, so
each spec is a self-contained oracle pair. Setup is
deterministic via ``random.Random(seed)``.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === dc_01: Power(x, n) ===

DC_01_SOURCE = '''\
"""Optimal solution for dc_01: Power(x, n).

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. Handle negative n by computing the reciprocal. O(log n).
"""


def solve(x, n):
    if n == 0:
        return 1
    # Use absolute exponent, then take reciprocal at the end if needed.
    abs_n = -n if n < 0 else n
    result = 1.0
    base = float(x)
    while abs_n > 0:
        if abs_n & 1:
            result *= base
        abs_n >>= 1
        if abs_n:
            base *= base
    if n < 0:
        return 1.0 / result
    return result
'''


def _setup_power(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # x is a small integer or float; n is bounded by 2^k so we
    # can verify with a small loop.
    x = rng.choice([rng.randint(-5, 5) or 1, rng.uniform(-3.0, 3.0)])
    exp = rng.randint(0, max(2, n))
    challenge._x = x
    challenge._n = exp
    return {"x": x, "n": exp}


def _verify_power(challenge, result: Any) -> bool:
    if not isinstance(result, (int, float)):
        return False
    expected = challenge._x ** challenge._n
    if expected == 0:
        return result == 0
    return abs(result - expected) < 1e-9 * (1 + abs(expected))


# === dc_02: Majority Element ===

DC_02_SOURCE = '''\
"""Optimal solution for dc_02: Majority Element.

Boyer-Moore: track a candidate and a counter. Walk the array;
on each new element, if the counter is zero, promote it to
candidate. Increment on a match, decrement otherwise. The
candidate at the end is the majority element if one exists.
The setup always produces a list with a majority, so the
candidate is the answer.
"""


def solve(arr, n):
    if n == 0:
        return -1
    candidate = None
    count = 0
    for value in arr:
        if count == 0:
            candidate = value
        count += 1 if value == candidate else -1
    return candidate
'''


def _setup_majority(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    # Pick a majority value; ensure it appears strictly more than n/2 times.
    majority = rng.randint(0, 9)
    majority_count = (n // 2) + 1
    arr = [majority] * majority_count
    # Fill the rest with other values (not equal to majority).
    for _ in range(n - majority_count):
        v = rng.randint(0, 9)
        while v == majority:
            v = rng.randint(0, 9)
        arr.append(v)
    rng.shuffle(arr)
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_majority(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    arr = challenge._arr
    if not arr:
        return result == -1
    # The setup guarantees a majority exists.
    counts = {}
    for v in arr:
        counts[v] = counts.get(v, 0) + 1
    majority_value = max(counts, key=counts.get)
    return result == majority_value


# === dc_03: Kth Smallest (Quickselect) ===

DC_03_SOURCE = '''\
"""Optimal solution for dc_03: Kth Smallest (Quickselect).

Quickselect: partition the array around a pivot (Lomuto-style),
then only recurse into the half that contains the kth smallest.
O(n) average case, O(n^2) worst case on pathological data.
The setup shuffles the array first to keep the worst case rare.
"""


def solve(arr, k, n):
    if k < 1 or k > n:
        return -1
    work = list(arr)
    target = k - 1  # 0-indexed

    def select(lo, hi):
        if lo == hi:
            return work[lo]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        if i == target:
            return work[i]
        if i < target:
            return select(i + 1, hi)
        return select(lo, i - 1)

    return select(0, n - 1)
'''


def _setup_quickselect(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(2, min(n, 16))
    arr = [rng.randint(0, 99) for _ in range(n)]
    rng.shuffle(arr)  # help avoid pathological quickselect
    k = rng.randint(1, n)
    challenge._arr = list(arr)
    challenge._k = k
    return {"arr": list(arr), "k": k, "n": n}


def _verify_quickselect(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    expected = sorted(challenge._arr)[challenge._k - 1]
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="dc_01",
        name="Power (x to the n)",
        category="divide_conquer",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Compute x^n for a real x and a non-negative integer n.\n"
            "Use divide-and-conquer: x^n = (x^(n//2))^2, with an extra\n"
            "x when n is odd. O(log n) multiplications.\n"
            "Source: https://www.geeksforgeeks.org/write-a-program-to-calculate-powxn/"
        ),
        source_url="https://www.geeksforgeeks.org/write-a-program-to-calculate-powxn/",
        params=["x", "n"],
        inputs={
            "x": "base (real number, integer or float).",
            "n": "exponent (non-negative integer).",
        },
        returns="x ** n (float).",
        source=DC_01_SOURCE,
        setup_fn=_setup_power,
        verify_fn=_verify_power,
        samples=[
            Sample("x = 2, n = 10", "1024"),
            Sample("x = 2.0, n = -2", "0.25  (setup always uses n >= 0; this sample is illustrative)"),
            Sample("x = 3, n = 0", "1"),
        ],
        hint="Repeated squaring. Multiply the result on set bits of n.",
        parents=["math_03"],
        children=["dc_02"],
    ),
    AlgorithmSpec(
        id="dc_02",
        name="Majority Element",
        category="divide_conquer",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "The setup always generates a list with a majority element\n"
            "(occurs strictly more than n/2 times). Find and return that\n"
            "value. Boyer-Moore: track a candidate and counter; promote on\n"
            "counter=0, increment on match, decrement on mismatch. The\n"
            "final candidate is the majority if one exists.\n"
            "Requirement: O(n) time, O(1) space.\n"
            "Source: https://www.geeksforgeeks.org/majority-element/"
        ),
        source_url="https://www.geeksforgeeks.org/majority-element/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers (always has a majority).",
            "n": "length of arr.",
        },
        returns="the majority element (the one that appears > n/2 times).",
        source=DC_02_SOURCE,
        setup_fn=_setup_majority,
        verify_fn=_verify_majority,
        samples=[
            Sample("arr = [3, 1, 3, 3, 2], n = 5", "3"),
            Sample("arr = [1], n = 1", "1"),
        ],
        hint="Walk once. On counter=0, promote the current value. Increment on match, decrement on mismatch.",
        parents=["dc_01"],
        children=["dc_03"],
    ),
    AlgorithmSpec(
        id="dc_03",
        name="Kth Smallest (Quickselect)",
        category="divide_conquer",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the kth smallest element in an unsorted array (k is\n"
            "1-indexed). Quickselect: partition like quicksort, then\n"
            "recurse only into the half that contains the answer. O(n)\n"
            "average, O(n^2) worst case on pathological data; the setup\n"
            "shuffles the input to keep the worst case rare.\n"
            "Source: https://www.geeksforgeeks.org/quickselect-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/quickselect-algorithm/",
        params=["arr", "k", "n"],
        inputs={
            "arr": "list of n random integers (shuffled).",
            "k": "1-indexed rank to return.",
            "n": "length of arr.",
        },
        returns="the kth smallest element, or -1 if k is out of range.",
        source=DC_03_SOURCE,
        setup_fn=_setup_quickselect,
        verify_fn=_verify_quickselect,
        samples=[
            Sample("arr = [7, 10, 4, 3, 20, 15], k = 3, n = 6", "7"),
            Sample("arr = [5, 5, 5], k = 1, n = 3", "5"),
        ],
        hint="Partition around a pivot; only recurse into the side that contains the kth index.",
        parents=["dc_02"],
        children=[],
    ),
]
