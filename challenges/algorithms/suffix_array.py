"""Suffix Array data structure.

Two problems from GFG's suffix-array catalog:

  01 Build Suffix Array    - O(n^2 log n) naive; O(n log n) with sort
  02 Pattern Search (SA)   - binary search on the sorted suffixes

The suffix array is the sorted list of starting indices of all
suffixes of a string. Search uses the sorted order to binary-
search the pattern. Setup uses small strings (length 4-12).
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === suffix_01: Build Suffix Array ===

SUFFIX_01_SOURCE = '''
def solve(s, n):
    """Return the suffix array of s (sorted list of suffix starts).

    Naive: build all n suffixes (as strings) and sort them.
    O(n^2 log n). A real implementation would use a
    doubling-based O(n log n) algorithm.
    """
    if n == 0:
        return []
    return sorted(range(n), key=lambda i: s[i:])
'''


def _setup_suffix_array(challenge, n, seed):
    rng = random.Random(seed)
    n_chars = max(2, min(n, 10))
    s = "".join(rng.choice("ab") for _ in range(n_chars))
    challenge._s = s
    return {"s": s, "n": len(s)}


def _verify_suffix_array(challenge, result):
    if not isinstance(result, list):
        return False
    s = challenge._s
    n = len(s)
    if len(result) != n:
        return False
    # Result must be a permutation of range(n).
    if sorted(result) != list(range(n)):
        return False
    # Suffixes at result[i] must be in non-decreasing order.
    for i in range(1, n):
        if s[result[i]:] < s[result[i - 1]:]:
            return False
    return True


# === suffix_02: Pattern Search with Suffix Array ===

SUFFIX_02_SOURCE = '''
def solve(s, n, pattern, m):
    """Search for ``pattern`` in ``s`` using a suffix array.

    Build the suffix array of s, then binary-search for the
    pattern among the suffixes. Return the list of indices
    (in s) where the pattern occurs, sorted.
    """
    sa = sorted(range(n), key=lambda i: s[i:])
    out = []
    if m == 0:
        return out
    lo, hi = 0, n
    # Lower bound.
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:] < pattern:
            lo = mid + 1
        else:
            hi = mid
    lower = lo
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:].startswith(pattern):
            lo = mid + 1
        elif s[sa[mid]:] < pattern:
            lo = mid + 1
        else:
            hi = mid
    upper = lo
    for i in range(lower, upper):
        out.append(sa[i])
    return sorted(out)
'''


def _setup_suffix_search(challenge, n, seed):
    rng = random.Random(seed)
    n_chars = max(2, min(n, 12))
    s = "".join(rng.choice("abc") for _ in range(n_chars))
    # Pick a pattern that may or may not appear.
    m = rng.randint(1, 3)
    pattern = "".join(rng.choice("abc") for _ in range(m))
    challenge._s = s
    challenge._pattern = pattern
    return {"s": s, "n": len(s), "pattern": pattern, "m": m}


def _verify_suffix_search(challenge, result):
    if not isinstance(result, list):
        return False
    s = challenge._s
    pattern = challenge._pattern
    # Brute force: find all starting positions where pattern occurs.
    expected = []
    for i in range(len(s) - len(pattern) + 1):
        if s[i:i + len(pattern)] == pattern:
            expected.append(i)
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="suffix_01",
        name="Build Suffix Array",
        category="suffix_array",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Return the suffix array of s - a sorted list of\n"
            "starting indices of every suffix. Naive: build all n\n"
            "suffixes (as strings) and sort. O(n^2 log n). The\n"
            "verify just checks the result is a permutation and the\n"
            "suffixes are non-decreasing.\n"
            "Source: https://www.geeksforgeeks.org/suffix-array-set-1-introduction/"
        ),
        source_url="https://www.geeksforgeeks.org/suffix-array-set-1-introduction/",
        params=["s", "n"],
        inputs={
            "s": "string of n characters.",
            "n": "length of s.",
        },
        returns="a permutation of [0..n-1] in suffix-sorted order.",
        source=SUFFIX_01_SOURCE,
        setup_fn=_setup_suffix_array,
        verify_fn=_verify_suffix_array,
        samples=[
            Sample("s = 'banana', n = 6", "[5, 3, 1, 0, 4, 2] (suffixes a, ana, anana, banana, na, nana)"),
        ],
        hint="Build all n suffixes. Sort them. The array of starting indices is the answer.",
        parents=["string_12"],
        children=["suffix_02"],
    ),
    AlgorithmSpec(
        id="suffix_02",
        name="Pattern Search with Suffix Array",
        category="suffix_array",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Search for ``pattern`` in ``s`` using a suffix array.\n"
            "Build the SA, then binary-search for the range of\n"
            "suffixes that start with pattern. The pattern occurs\n"
            "at every index in that range.\n"
            "Source: https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/",
        params=["s", "n", "pattern", "m"],
        inputs={
            "s": "string to search in.",
            "n": "length of s.",
            "pattern": "the pattern to find.",
            "m": "length of pattern.",
        },
        returns="a sorted list of starting indices in s where pattern occurs.",
        source=SUFFIX_02_SOURCE,
        setup_fn=_setup_suffix_search,
        verify_fn=_verify_suffix_search,
        samples=[
            Sample("s = 'banana', n = 6, pattern = 'ana', m = 3", "[1, 3]"),
        ],
        hint="Build the SA. Binary-search for the range of suffixes that start with pattern.",
        parents=["suffix_01"],
        children=[],
    ),
]
