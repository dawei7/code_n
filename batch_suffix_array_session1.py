"""Spec generator input - 3 more suffix-array specs for Session 1.

Covers the GfG suffix-array topic list that suffix_01..02
(Build + Pattern Search) don't already cover:

  suffix_03  LCP Array via Kasai's Algorithm    (O(n))
  suffix_04  Count Distinct Substrings          (uses LCP array, O(n))
  suffix_05  Longest Repeated Substring         (max over LCP, O(n))

After this batch, suffix_array.py covers the canonical
suffix-array + LCP-array + LCP-applications from GfG.

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module suffix_array \\
        --input batch_suffix_array_session1.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # suffix_03: LCP Array via Kasai's Algorithm
    # ============================================================
    {
        "id": "suffix_03",
        "name": "LCP Array (Kasai's Algorithm)",
        "category": "suffix_array",
        "difficulty": 5,
        "complexity": "O_N",
        "description": (
            "Given a string s, return its suffix array sa and\n"
            "the LCP (Longest Common Prefix) array. LCP[i] is\n"
            "the length of the longest common prefix of the\n"
            "suffixes s[sa[i]:] and s[sa[i-1]:]. Use Kasai's\n"
            "linear-time algorithm: walk the original string in\n"
            "order, and for each position i, walk forward from\n"
            "the previous LCP to compute the LCP of the current\n"
            "suffix and its neighbor in the suffix array.\n"
            "O(n) time after O(n log n) for the suffix array.\n"
            "Source: https://www.geeksforgeeks.org/dsa/suffix-array-set-2-a-kasai-algorithm-for-construction-of-lcp-array/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/suffix-array-set-2-a-kasai-algorithm-for-construction-of-lcp-array/",
        "params": ["s", "n"],
        "inputs": {
            "s": "the input string.",
            "n": "length of s.",
        },
        "returns": "a tuple (sa, lcp) where sa is the suffix array of s and lcp is the LCP array of length n (lcp[0] = 0).",
        "solve": '''
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
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(2, min(n, 10))
# Build a non-trivial string (mix of characters so LCP is non-zero).
chars = "abacabadabacaba"
s = "".join(rng.choice(chars) for _ in range(n))
challenge._s = s
return {"s": s, "n": len(s)}
''',
        "verify": '''
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
''',
        "samples": [
            ("s = 'banana', n = 6", "([5, 3, 1, 0, 4, 2], [0, 0, 3, 1, 0, 2])"),
            ("s = 'aaaa', n = 4", "([3, 2, 1, 0], [0, 1, 2, 3])"),
        ],
        "hint": "Build the suffix array naively (sort suffixes). Walk the original string in order. For each position i, the LCP of its suffix and the previous suffix in the SA can be computed incrementally by extending the previous LCP by at most 1 character.",
        "parents": ["suffix_01"],
        "children": ["suffix_04"],
    },

    # ============================================================
    # suffix_04: Count Distinct Substrings
    # ============================================================
    {
        "id": "suffix_04",
        "name": "Count Distinct Substrings",
        "category": "suffix_array",
        "difficulty": 4,
        "complexity": "O_N2",
        "description": (
            "Count the number of distinct non-empty substrings\n"
            "of a string s. A substring starting at index i has\n"
            "length in [1, n-i]. Equivalently, the number of\n"
            "distinct substrings equals the sum over all suffixes\n"
            "of (length of suffix - LCP with the previous suffix\n"
            "in the suffix array). Build the suffix array and\n"
            "LCP array; return the sum of (n - sa[i] - lcp[i])\n"
            "for i in [0, n-1]. O(n) after the suffix array and\n"
            "LCP are built.\n"
            "Source: https://www.geeksforgeeks.org/dsa/suffix-array-application-count-distinct-substrings/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/suffix-array-application-count-distinct-substrings/",
        "params": ["s", "n"],
        "inputs": {
            "s": "the input string.",
            "n": "length of s.",
        },
        "returns": "the number of distinct non-empty substrings of s, as an int.",
        "solve": '''
def solve(s, n):
    """Count distinct non-empty substrings via suffix array."""
    if n == 0:
        return 0
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Build the LCP array (Kasai-style, but the naive\n    # version suffices for small n).
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
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(2, min(n, 10))
chars = "abacabadabacaba"
s = "".join(rng.choice(chars) for _ in range(n))
challenge._s = s
return {"s": s, "n": len(s)}
''',
        "verify": '''
# Brute force: enumerate all non-empty substrings and count distinct.
s = challenge._s
n = len(s)
seen = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        seen.add(s[i:j])
return result == len(seen)
''',
        "samples": [
            ("s = 'banana', n = 6", "15 (the 15 distinct substrings of 'banana')"),
            ("s = 'aaa', n = 3", "3 ('a', 'aa', 'aaa')"),
            ("s = 'abcd', n = 4", "10 (each substring is unique)"),
        ],
        "hint": "Total distinct substrings = sum over all suffixes of (length - LCP with previous). Build the suffix array and LCP array naively (O(n^2 log n)), then sum.",
        "parents": ["suffix_03"],
        "children": ["suffix_05"],
    },

    # ============================================================
    # suffix_05: Longest Repeated Substring
    # ============================================================
    {
        "id": "suffix_05",
        "name": "Longest Repeated Substring",
        "category": "suffix_array",
        "difficulty": 3,
        "complexity": "O_N2",
        "description": (
            "Find the length of the longest substring of s\n"
            "that occurs at least twice (in two different\n"
            "positions, with non-overlapping allowed). Build\n"
            "the suffix array and the LCP array; the answer is\n"
            "the maximum value in the LCP array. Return 0 if\n"
            "no substring repeats. O(n) after the suffix and\n"
            "LCP arrays are built.\n"
            "Source: https://www.geeksforgeeks.org/dsa/suffix-array-set-1-introduction/"
        ),
        "source_url": "https://www.geeksforgeeks.org/dsa/suffix-array-set-1-introduction/",
        "params": ["s", "n"],
        "inputs": {
            "s": "the input string.",
            "n": "length of s.",
        },
        "returns": "the length of the longest repeated substring of s (0 if none), as an int.",
        "solve": '''
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
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(2, min(n, 10))
chars = "abacabadabacaba"
s = "".join(rng.choice(chars) for _ in range(n))
challenge._s = s
return {"s": s, "n": len(s)}
''',
        "verify": '''
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
''',
        "samples": [
            ("s = 'banana', n = 6", "3 ('ana' or 'nan' appears twice)"),
            ("s = 'abcd', n = 4", "0 (all substrings unique)"),
            ("s = 'aaaa', n = 4", "3 ('aaa' appears at positions 0, 1)"),
        ],
        "hint": "Build the suffix array and LCP array. The longest repeated substring length is max(LCP).",
        "parents": ["suffix_03"],
        "children": [],
    },
]
