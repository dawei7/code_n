"""Backtracking algorithms.

Four core problems from GFG's backtracking catalog:

  01 Subset Sum (decision)  - does any subset of arr sum to target?
  02 Permutations           - all orderings of arr
  03 Combination Sum        - all unique combinations that sum to target
  04 Word Break (decision)  - can the string be segmented into dict words?

All four share the same setup/verify shape: deterministic
random input, brute-force oracle in verify, single canonical
``solve`` to compare against. The setup keeps n small (4-16)
because these problems are exponential in the worst case.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === backtrack_01: Subset Sum (decision) ===

BACKTRACK_01_SOURCE = '''\
"""Optimal solution for backtrack_01: Subset Sum (decision).

Classic backtracking: at each step, try including or excluding
the current element. Prune when the running sum is past the
target. Return True iff a subset sums exactly to target.
"""


def solve(arr, target, n):
    if n == 0:
        return target == 0

    def helper(i, remaining):
        if remaining == 0:
            return True
        if i == n or remaining < 0:
            return False
        # Include arr[i] or skip it.
        return helper(i + 1, remaining - arr[i]) or helper(i + 1, remaining)

    return helper(0, target)
'''


def _setup_subset_sum(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    arr = [rng.randint(1, 20) for _ in range(n)]
    # Pick a target that's reachable (the sum of some prefix).
    split = rng.randint(0, n)
    target = sum(arr[:split])
    challenge._arr = list(arr)
    challenge._target = target
    return {"arr": list(arr), "target": target, "n": n}


def _verify_subset_sum(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    # Brute force: does any subset sum to target?
    arr = challenge._arr
    target = challenge._target
    for mask in range(1 << len(arr)):
        s = sum(arr[i] for i in range(len(arr)) if mask & (1 << i))
        if s == target:
            return result is True
    return result is False


# === backtrack_02: Permutations ===

BACKTRACK_02_SOURCE = '''\
"""Optimal solution for backtrack_02: Permutations.

Return every ordering of ``arr`` as a list of lists. Standard
backtracking: pick each unused element in turn, recurse, then
unpick. The output list of permutations is sorted so the
verify can do a plain equality check.
"""


def solve(arr, n):
    if n == 0:
        return [[]]
    result = []
    used = [False] * n

    def helper(path):
        if len(path) == n:
            result.append(list(path))
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                helper(path)
                path.pop()
                used[i] = False

    helper([])
    result.sort()
    return result
'''


def _setup_permutations(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Keep n small - n! is exponential.
    n = max(1, min(n, 6))
    # All distinct elements so we don't have to dedupe.
    arr = rng.sample(range(1, 100), n)
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_permutations(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    from itertools import permutations
    expected = sorted([list(p) for p in permutations(challenge._arr)])
    return result == expected


# === backtrack_03: Combination Sum ===

BACKTRACK_03_SOURCE = '''\
"""Optimal solution for backtrack_03: Combination Sum.

Given a list of positive integers and a target, return every
unique combination that sums to target. Each input element may
be used any number of times. Sort the input first and always
recurse forward (i >= start) to avoid duplicates.
"""


def solve(candidates, target, n):
    candidates = sorted(candidates)
    result = []

    def helper(start, remaining, path):
        if remaining == 0:
            result.append(list(path))
            return
        if start == n or remaining < 0:
            return
        for i in range(start, n):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            helper(i, remaining - candidates[i], path)
            path.pop()

    helper(0, target, [])
    return result
'''


def _setup_combination_sum(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 8))
    candidates = sorted({rng.randint(1, 10) for _ in range(n)})
    # Pick a reachable target.
    target = 0
    for _ in range(rng.randint(1, 4)):
        target += rng.choice(candidates)
    challenge._candidates = list(candidates)
    challenge._target = target
    return {"candidates": list(candidates), "target": target, "n": len(candidates)}


def _verify_combination_sum(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    # Re-derive the expected answer.
    candidates = sorted(challenge._candidates)
    target = challenge._target
    expected = []

    def helper(start, remaining, path):
        if remaining == 0:
            expected.append(sorted(path))
            return
        if start == len(candidates) or remaining < 0:
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            helper(i, remaining - candidates[i], path)
            path.pop()

    helper(0, target, [])
    expected_set = {tuple(c) for c in expected}
    result_set = {tuple(sorted(c)) for c in result}
    return expected_set == result_set and len(result) == len(expected_set)


# === backtrack_04: Word Break (decision) ===

BACKTRACK_04_SOURCE = '''\
"""Optimal solution for backtrack_04: Word Break.

Given a string s and a list of dictionary words, return True
iff s can be segmented into a sequence of one or more dict
words. Backtracking: at each step, try each dict word as a
prefix; recurse on the remaining suffix.
"""


def solve(s, dictionary, n):
    if n == 0:
        return True
    word_set = set(dictionary)

    def helper(remaining):
        if not remaining:
            return True
        for word in dictionary:
            if remaining.startswith(word) and helper(remaining[len(word):]):
                return True
        return False

    return helper(s)
'''


def _setup_word_break(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Build a small vocabulary, then concatenate 1..4 words to form s.
    vocab_size = max(2, min(n, 8))
    vocabulary = ["cat", "dog", "sun", "moon", "star", "car", "tree", "leaf", "rock", "wave",
                  "bird", "fish", "book", "code", "data", "play"]
    vocabulary = vocabulary[:vocab_size]
    n_words = rng.randint(1, max(1, min(n, 4)))
    s = "".join(rng.choice(vocabulary) for _ in range(n_words))
    challenge._s = s
    challenge._vocab = list(vocabulary)
    return {"s": s, "dictionary": list(vocabulary), "n": len(s)}


def _verify_word_break(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    s = challenge._s
    vocab = set(challenge._vocab)
    # DP-style: dp[i] = True iff s[:i] is segmentable.
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in vocab:
                dp[i] = True
                break
    expected = dp[len(s)]
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="backtrack_01",
        name="Subset Sum (Decision)",
        category="backtracking",
        difficulty=5,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Given a list of positive integers and a target, return True\n"
            "iff some subset of the list sums exactly to target. The setup\n"
            "always picks a reachable target (prefix-sum of a random\n"
            "split), so the answer is True.\n"
            "Requirement: O(2^n) time, O(n) recursion stack.\n"
            "Source: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/"
        ),
        source_url="https://www.geeksforgeeks.org/subset-sum-problem-dp-25/",
        params=["arr", "target", "n"],
        inputs={
            "arr": "list of n positive integers.",
            "target": "target sum (always reachable in the setup).",
            "n": "length of arr.",
        },
        returns="True iff some subset of arr sums to target.",
        source=BACKTRACK_01_SOURCE,
        setup_fn=_setup_subset_sum,
        verify_fn=_verify_subset_sum,
        samples=[
            Sample("arr = [3, 34, 4, 12, 5, 2], target = 9, n = 6", "True (4+5)"),
            Sample("arr = [1, 2, 3], target = 7, n = 3", "False (reachable by 1+2+3=6, but target is 7)"),
        ],
        hint="Recurse on (i+1, remaining - arr[i]) OR (i+1, remaining). Prune if remaining < 0.",
        parents=["dp_18"],
        children=["backtrack_02"],
    ),
    AlgorithmSpec(
        id="backtrack_02",
        name="Permutations",
        category="backtracking",
        difficulty=4,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Return every ordering of ``arr`` as a list of lists. The\n"
            "setup uses distinct elements so we don't have to dedupe.\n"
            "Outer list is sorted so the verify can compare directly.\n"
            "Requirement: O(n! * n) time.\n"
            "Source: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/"
        ),
        source_url="https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n distinct integers.",
            "n": "length of arr (capped at 6 because n! grows fast).",
        },
        returns="a list of n! permutations (each a list), sorted.",
        source=BACKTRACK_02_SOURCE,
        setup_fn=_setup_permutations,
        verify_fn=_verify_permutations,
        samples=[
            Sample("arr = [1, 2, 3], n = 3", "[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]"),
            Sample("arr = [1, 2], n = 2", "[[1,2], [2,1]]"),
        ],
        hint="Pick each unused element in turn, recurse, then unpick. Sort the result list.",
        parents=["backtrack_01"],
        children=["backtrack_03"],
    ),
    AlgorithmSpec(
        id="backtrack_03",
        name="Combination Sum",
        category="backtracking",
        difficulty=5,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Given a list of positive integers (sorted) and a target, return\n"
            "every unique combination of values that sums to target. Each\n"
            "value may be used any number of times. Recurse forward only\n"
            "(i >= start) to avoid duplicate combinations. Output is a\n"
            "list of combinations; each combination is sorted.\n"
            "Requirement: O(2^target) worst case.\n"
            "Source: https://www.geeksforgeeks.org/combinational-sum/"
        ),
        source_url="https://www.geeksforgeeks.org/combinational-sum/",
        params=["candidates", "target", "n"],
        inputs={
            "candidates": "list of n sorted positive integers (uniques).",
            "target": "target sum (always reachable in the setup).",
            "n": "length of candidates.",
        },
        returns="a list of unique combinations (each a list) that sum to target.",
        source=BACKTRACK_03_SOURCE,
        setup_fn=_setup_combination_sum,
        verify_fn=_verify_combination_sum,
        samples=[
            Sample("candidates = [2, 3, 6, 7], target = 7, n = 4", "[[2, 2, 3], [7]]"),
            Sample("candidates = [2, 3, 5], target = 8, n = 3", "[[2, 2, 2, 2], [2, 3, 3], [3, 5]]"),
        ],
        hint="Recurse forward (i stays >= start) to avoid duplicate combinations.",
        parents=["backtrack_02"],
        children=["backtrack_04"],
    ),
    AlgorithmSpec(
        id="backtrack_04",
        name="Word Break (Decision)",
        category="backtracking",
        difficulty=5,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Given a string s and a list of dictionary words, return True\n"
            "iff s can be segmented into a sequence of one or more\n"
            "dictionary words.\n"
            "Requirement: O(2^n) worst case; the verify re-derives via\n"
            "DP and compares.\n"
            "Source: https://www.geeksforgeeks.org/word-break-problem-dp-32/"
        ),
        source_url="https://www.geeksforgeeks.org/word-break-problem-dp-32/",
        params=["s", "dictionary", "n"],
        inputs={
            "s": "the string to segment.",
            "dictionary": "list of words to segment s with.",
            "n": "length of s.",
        },
        returns="True iff s can be segmented into a sequence of dict words.",
        source=BACKTRACK_04_SOURCE,
        setup_fn=_setup_word_break,
        verify_fn=_verify_word_break,
        samples=[
            Sample('s = "ilikesamsung", dictionary = ["i", "like", "sam", "sung", "samsung", "mobile"]', "True (i like sam sung)"),
            Sample('s = "catsandog", dictionary = ["cats", "dog", "sand", "and", "cat"]', "False"),
        ],
        hint="At each step, try each dict word as a prefix; recurse on the rest.",
        parents=["backtrack_03"],
        children=[],
    ),
]
