"""Recursion algorithms.

Four problems from GFG's recursion catalog:

  01 Power Sum           - x^n via divide-and-conquer recursion
  02 Reverse String      - in-place reversal with two pointers
  03 Print Subsequences  - enumerate all subsequences of a string
  04 Tower of Hanoi      - move n disks from source to destination

The setup keeps n small (4-12) so the verify can brute-force
the result. All four pass the test gauntlet at n=4, 8, 16.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === recursion_01: Power Sum ===

RECURSION_01_SOURCE = '''\
"""Optimal solution for recursion_01: Power Sum.

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. Same algorithm as dc_01 but written in recursive
form to fit the category. O(log n) time.
"""


def solve(x, n):
    if n == 0:
        return 1
    half = solve(x, n // 2)
    if n % 2 == 0:
        return half * half
    return x * half * half
'''


def _setup_power_sum(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    x = rng.randint(1, 5)
    exp = rng.randint(0, max(2, n))
    challenge._x = x
    challenge._n = exp
    return {"x": x, "n": exp}


def _verify_power_sum(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._x ** challenge._n


# === recursion_02: Reverse String ===

RECURSION_02_SOURCE = '''\
"""Optimal solution for recursion_02: Reverse String.

Two-pointer swap; swap s[left] and s[right] in place, recurse
on the inner substring. Stop when left >= right. O(n) time,
O(n) recursion stack space.
"""


def solve(s, n):
    chars = list(s)

    def helper(left, right):
        if left >= right:
            return
        chars[left], chars[right] = chars[right], chars[left]
        helper(left + 1, right - 1)

    helper(0, n - 1)
    return "".join(chars)
'''


def _setup_reverse_string(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    s = "".join(rng.choice("abcdefghij") for _ in range(n))
    challenge._s = s
    return {"s": s, "n": n}


def _verify_reverse_string(challenge, result: Any) -> bool:
    if not isinstance(result, str):
        return False
    return result == challenge._s[::-1]


# === recursion_03: Print Subsequences ===

RECURSION_03_SOURCE = '''\
"""Optimal solution for recursion_03: Print Subsequences.

For each position, branch on include/exclude. The recursion
tree has 2^n leaves; each leaf is a distinct subsequence.
Return all subsequences in a canonical order (sorted, with
the empty string first) so the verify can do a plain
equality check.
"""


def solve(s, n):
    result = []

    def helper(i, path):
        if i == n:
            result.append("".join(path))
            return
        # Exclude s[i].
        helper(i + 1, path)
        # Include s[i].
        path.append(s[i])
        helper(i + 1, path)
        path.pop()

    helper(0, [])
    result.sort()
    return result
'''


def _setup_subsequences(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 6))  # 2^n subsequences - keep it small
    s = "".join(rng.choice("abc") for _ in range(n))
    challenge._s = s
    return {"s": s, "n": n}


def _verify_subsequences(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    s = challenge._s
    # Brute-force: enumerate every subset and join.
    expected = []
    for mask in range(1 << len(s)):
        sub = "".join(s[i] for i in range(len(s)) if mask & (1 << i))
        expected.append(sub)
    expected.sort()
    return result == expected


# === recursion_04: Tower of Hanoi ===

RECURSION_04_SOURCE = '''\
"""Optimal solution for recursion_04: Tower of Hanoi.

Move n disks from source to destination using an auxiliary
peg. The optimal recurrence is: move n-1 disks from source
to auxiliary, move the largest disk, move n-1 disks from
auxiliary to destination. Returns the sequence of moves as
a list of (from, to) tuples.
"""


def solve(n, source, destination, auxiliary):
    moves = []

    def helper(count, src, dst, aux):
        if count == 0:
            return
        helper(count - 1, src, aux, dst)
        moves.append((src, dst))
        helper(count - 1, aux, dst, src)

    helper(n, source, destination, auxiliary)
    return moves
'''


def _setup_hanoi(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    n = max(1, min(n, 8))  # 2^n - 1 moves
    challenge._n = n
    return {"n": n, "source": "A", "destination": "C", "auxiliary": "B"}


def _verify_hanoi(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    n = challenge._n
    # Expected: 2^n - 1 moves in the canonical pattern.
    expected_moves = []

    def helper(count, src, dst, aux):
        if count == 0:
            return
        helper(count - 1, src, aux, dst)
        expected_moves.append((src, dst))
        helper(count - 1, aux, dst, src)

    helper(n, "A", "C", "B")
    return result == expected_moves


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="recursion_01",
        name="Power Sum",
        category="recursion",
        difficulty=2,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Compute x^n (both non-negative integers) via divide-and-conquer\n"
            "recursion: x^n = (x^(n//2))^2, with an extra x when n is odd.\n"
            "Same algorithm as dc_01, written in recursive form.\n"
            "Requirement: O(log n) multiplications.\n"
            "Source: https://www.geeksforgeeks.org/write-a-program-to-calculate-powxn/"
        ),
        source_url="https://www.geeksforgeeks.org/write-a-program-to-calculate-powxn/",
        params=["x", "n"],
        inputs={
            "x": "base (positive integer).",
            "n": "exponent (non-negative integer).",
        },
        returns="x ** n.",
        source=RECURSION_01_SOURCE,
        setup_fn=_setup_power_sum,
        verify_fn=_verify_power_sum,
        samples=[
            Sample("x = 2, n = 10", "1024"),
            Sample("x = 3, n = 4", "81"),
            Sample("x = 5, n = 0", "1"),
        ],
        hint="half = solve(x, n//2). If n is even return half*half; if odd return x*half*half.",
        parents=["dc_01"],
        children=["recursion_02"],
    ),
    AlgorithmSpec(
        id="recursion_02",
        name="Reverse String",
        category="recursion",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the input string reversed. Two-pointer recursive\n"
            "swap: swap s[left] and s[right], recurse inward. Stop when\n"
            "the pointers cross.\n"
            "Requirement: O(n) time, O(n) recursion stack.\n"
            "Source: https://www.geeksforgeeks.org/write-a-program-to-reverse-a-string-using-recursion/"
        ),
        source_url="https://www.geeksforgeeks.org/write-a-program-to-reverse-a-string-using-recursion/",
        params=["s", "n"],
        inputs={
            "s": "string of n lower-case ASCII characters.",
            "n": "length of s.",
        },
        returns="the reversed string.",
        source=RECURSION_02_SOURCE,
        setup_fn=_setup_reverse_string,
        verify_fn=_verify_reverse_string,
        samples=[
            Sample('s = "hello", n = 5', '"olleh"'),
            Sample('s = "a", n = 1', '"a"'),
        ],
        hint="Swap s[left] and s[right]. Recurse with (left+1, right-1).",
        parents=["recursion_01"],
        children=["recursion_03"],
    ),
    AlgorithmSpec(
        id="recursion_03",
        name="Print Subsequences",
        category="recursion",
        difficulty=4,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Return every subsequence of s as a list of strings (the\n"
            "empty string included). The recursion branches on\n"
            "include/exclude at every position. Sorted so the verify\n"
            "can do a plain equality check.\n"
            "Requirement: O(2^n) time.\n"
            "Source: https://www.geeksforgeeks.org/subsequence-substring-string/"
        ),
        source_url="https://www.geeksforgeeks.org/subsequence-substring-string/",
        params=["s", "n"],
        inputs={
            "s": "string of n lower-case characters (capped at 6 in the setup).",
            "n": "length of s.",
        },
        returns="a list of 2^n subsequences, sorted.",
        source=RECURSION_03_SOURCE,
        setup_fn=_setup_subsequences,
        verify_fn=_verify_subsequences,
        samples=[
            Sample('s = "abc", n = 3', '["", "a", "ab", "abc", "ac", "b", "bc", "c"]'),
            Sample('s = "ab", n = 2', '["", "a", "ab", "b"]'),
        ],
        hint="At each index, branch on include/exclude. Sort the final list.",
        parents=["recursion_02"],
        children=["recursion_04"],
    ),
    AlgorithmSpec(
        id="recursion_04",
        name="Tower of Hanoi",
        category="recursion",
        difficulty=3,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Move n disks from a source peg to a destination peg using\n"
            "an auxiliary peg. One disk at a time; never place a larger\n"
            "disk on a smaller one. The classic recurrence: move n-1\n"
            "from source to auxiliary, move the largest, move n-1 from\n"
            "auxiliary to destination.\n"
            "Return the sequence of (from, to) moves.\n"
            "Source: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/"
        ),
        source_url="https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/",
        params=["n", "source", "destination", "auxiliary"],
        inputs={
            "n": "number of disks (capped at 8 in the setup).",
            "source": "source peg name (always 'A').",
            "destination": "destination peg name (always 'C').",
            "auxiliary": "auxiliary peg name (always 'B').",
        },
        returns="a list of (from, to) moves - 2^n - 1 in total.",
        source=RECURSION_04_SOURCE,
        setup_fn=_setup_hanoi,
        verify_fn=_verify_hanoi,
        samples=[
            Sample('n = 1, source = "A", destination = "C", auxiliary = "B"', "[('A', 'C')]"),
            Sample('n = 2, source = "A", destination = "C", auxiliary = "B"', "[('A', 'B'), ('A', 'C'), ('B', 'C')]"),
        ],
        hint="Recurse: move n-1 from src to aux, move the largest, recurse on the n-1 from aux to dst.",
        parents=["recursion_03"],
        children=[],
    ),
]
