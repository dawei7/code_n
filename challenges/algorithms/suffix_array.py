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


# === suffix_03: LCP Array (Kasai's Algorithm) ===

SUFFIX_03_SOURCE = '''
def solve(s, n):
    """Return (suffix_array, lcp_array) of s.

    Build the suffix array naively (sort suffixes), then run
    Kasai's algorithm to build the LCP array in O(n).
    """
    if n == 0:
        return [], []
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Inverse SA: rank[i] = position of suffix i in sa.
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    # Kasai's algorithm.
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            # j is the previous suffix in the suffix array.
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
        # If rank[i] == 0 (it's the smallest suffix), lcp[0] = 0
        # (already initialized).
    return sa, lcp
'''

def _setup_suffix_03(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(2, min(n, 10))
    # Build a non-trivial string (mix of characters so LCP is non-zero).
    chars = "abacabadabacaba"
    s = "".join(rng.choice(chars) for _ in range(n))
    challenge._s = s
    return {"s": s, "n": len(s)}

def _verify_suffix_03(challenge, result):
    s = challenge._s
    n = len(s)
    if not isinstance(result, tuple) or len(result) != 2:
        return False
    sa, lcp = result
    if not isinstance(sa, list) or not isinstance(lcp, list):
        return False
    if len(sa) != n or len(lcp) != n:
        return False
    # sa must be a permutation of range(n).
    if sorted(sa) != list(range(n)):
        return False
    # sa must be in non-decreasing suffix order.
    for i in range(1, n):
        if s[sa[i]:] < s[sa[i - 1]:]:
            return False
    # lcp[0] = 0.
    if lcp[0] != 0:
        return False
    # lcp[i] = lcp(s[sa[i]:], s[sa[i-1]:]).
    for i in range(1, n):
        a = s[sa[i]:]
        b = s[sa[i - 1]:]
        expected = 0
        while expected < len(a) and expected < len(b) and a[expected] == b[expected]:
            expected += 1
        if lcp[i] != expected:
            return False
    return True



# === suffix_04: Count Distinct Substrings ===

SUFFIX_04_SOURCE = '''
def solve(s, n):
    """Count distinct non-empty substrings via suffix array."""
    if n == 0:
        return 0
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Build the LCP array (Kasai-style, but the naive
    # version suffices for small n).
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    # Sum of (n - sa[i] - lcp[i]) for i in 0..n-1.
    total = 0
    for i in range(n):
        total += n - sa[i] - lcp[i]
    return total
'''

def _setup_suffix_04(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(2, min(n, 10))
    chars = "abacabadabacaba"
    s = "".join(rng.choice(chars) for _ in range(n))
    challenge._s = s
    return {"s": s, "n": len(s)}

def _verify_suffix_04(challenge, result):
    # Brute force: enumerate all non-empty substrings and count distinct.
    s = challenge._s
    n = len(s)
    seen = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            seen.add(s[i:j])
    return result == len(seen)



# === suffix_05: Longest Repeated Substring ===

SUFFIX_05_SOURCE = '''
def solve(s, n):
    """Length of the longest repeated substring."""
    if n == 0:
        return 0
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Build the LCP array.
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    # Return the max LCP (lcp[0] is 0, so the max is over i >= 1).
    return max(lcp)
'''

def _setup_suffix_05(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(2, min(n, 10))
    chars = "abacabadabacaba"
    s = "".join(rng.choice(chars) for _ in range(n))
    challenge._s = s
    return {"s": s, "n": len(s)}

def _verify_suffix_05(challenge, result):
    # Brute force: try every length L, check if some substring of
    # length L appears twice. The longest such L is the answer.
    s = challenge._s
    n = len(s)
    best = 0
    for L in range(1, n + 1):
        seen = set()
        found = False
        for i in range(n - L + 1):
            sub = s[i:i + L]
            if sub in seen:
                found = True
                break
            seen.add(sub)
        if found:
            best = L
    return result == best


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="suffix_03",
        name="LCP Array (Kasai's Algorithm)",
        category="suffix_array",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Given a string s, return its suffix array sa and
            the LCP (Longest Common Prefix) array. LCP[i] is
            the length of the longest common prefix of the
            suffixes s[sa[i]:] and s[sa[i-1]:]. Use Kasai's
            linear-time algorithm: walk the original string in
            order, and for each position i, walk forward from
            the previous LCP to compute the LCP of the current
            suffix and its neighbor in the suffix array.
            O(n) time after O(n log n) for the suffix array.
            Source: https://www.geeksforgeeks.org/dsa/suffix-array-set-2-a-kasai-algorithm-for-construction-of-lcp-array/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/suffix-array-set-2-a-kasai-algorithm-for-construction-of-lcp-array/",
        params=["s", "n"],
        inputs={
            "s": "the input string.",
            "n": "length of s.",
        },
        returns="a tuple (sa, lcp) where sa is the suffix array of s and lcp is the LCP array of length n (lcp[0] = 0).",
        source=SUFFIX_03_SOURCE,
        setup_fn=_setup_suffix_03,
        verify_fn=_verify_suffix_03,
        samples=[
            Sample("s = 'banana', n = 6", "([5, 3, 1, 0, 4, 2], [0, 0, 3, 1, 0, 2])"),
            Sample("s = 'aaaa', n = 4", "([3, 2, 1, 0], [0, 1, 2, 3])"),
        ],
        hint="Build the suffix array naively (sort suffixes). Walk the original string in order. For each position i, the LCP of its suffix and the previous suffix in the SA can be computed incrementally by extending the previous LCP by at most 1 character.",
        parents=["suffix_01"],
        children=["suffix_04"],
    ),
    AlgorithmSpec(
        id="suffix_04",
        name="Count Distinct Substrings",
        category="suffix_array",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Count the number of distinct non-empty substrings
            of a string s. A substring starting at index i has
            length in [1, n-i]. Equivalently, the number of
            distinct substrings equals the sum over all suffixes
            of (length of suffix - LCP with the previous suffix
            in the suffix array). Build the suffix array and
            LCP array; return the sum of (n - sa[i] - lcp[i])
            for i in [0, n-1]. O(n) after the suffix array and
            LCP are built.
            Source: https://www.geeksforgeeks.org/dsa/suffix-array-application-count-distinct-substrings/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/suffix-array-application-count-distinct-substrings/",
        params=["s", "n"],
        inputs={
            "s": "the input string.",
            "n": "length of s.",
        },
        returns="the number of distinct non-empty substrings of s, as an int.",
        source=SUFFIX_04_SOURCE,
        setup_fn=_setup_suffix_04,
        verify_fn=_verify_suffix_04,
        samples=[
            Sample("s = 'banana', n = 6", "15 (the 15 distinct substrings of 'banana')"),
            Sample("s = 'aaa', n = 3", "3 ('a', 'aa', 'aaa')"),
            Sample("s = 'abcd', n = 4", "10 (each substring is unique)"),
        ],
        hint="Total distinct substrings = sum over all suffixes of (length - LCP with previous). Build the suffix array and LCP array naively (O(n^2 log n)), then sum.",
        parents=["suffix_03"],
        children=["suffix_05"],
    ),
    AlgorithmSpec(
        id="suffix_05",
        name="Longest Repeated Substring",
        category="suffix_array",
        difficulty=3,
        required_complexity=ComplexityClass.O_N2,
        description=("""
            Find the length of the longest substring of s
            that occurs at least twice (in two different
            positions, with non-overlapping allowed). Build
            the suffix array and the LCP array; the answer is
            the maximum value in the LCP array. Return 0 if
            no substring repeats. O(n) after the suffix and
            LCP arrays are built.
            Source: https://www.geeksforgeeks.org/dsa/suffix-array-set-1-introduction/
            """),
        source_url="https://www.geeksforgeeks.org/dsa/suffix-array-set-1-introduction/",
        params=["s", "n"],
        inputs={
            "s": "the input string.",
            "n": "length of s.",
        },
        returns="the length of the longest repeated substring of s (0 if none), as an int.",
        source=SUFFIX_05_SOURCE,
        setup_fn=_setup_suffix_05,
        verify_fn=_verify_suffix_05,
        samples=[
            Sample("s = 'banana', n = 6", "3 ('ana' or 'nan' appears twice)"),
            Sample("s = 'abcd', n = 4", "0 (all substrings unique)"),
            Sample("s = 'aaaa', n = 4", "3 ('aaa' appears at positions 0, 1)"),
        ],
        hint="Build the suffix array and LCP array. The longest repeated substring length is max(LCP).",
        parents=["suffix_03"],
        children=[],
    ),
])
