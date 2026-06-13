"""Hashing algorithms.

Four core problems from GFG's hashing catalog:

  01 Two Sum                          - find two indices that sum to target
  02 Subarray Sum Equals K            - count subarrays with sum == k
  03 Longest Substring Without Repeat - sliding window + last-seen map
  04 Group Anagrams                   - sort-by-chars key

All four rely on a Python dict (or set) and follow the same
shape: deterministic random input, brute-force oracle in
verify, single canonical ``solve`` to compare against.
"""


from __future__ import annotations

import random
from collections import Counter, defaultdict
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === hash_01: Two Sum ===

HASH_01_SOURCE = '''\
"""Optimal solution for hash_01: Two Sum.

Single pass: walk the array, for each value check whether
target - value has been seen. If yes, return the two indices.
Otherwise, store the current value's index in the map. O(n).
"""


def solve(arr, target, n):
    seen = {}
    for i in range(n):
        complement = target - arr[i]
        if complement in seen:
            return sorted([seen[complement], i])
        seen[arr[i]] = i
    return [-1, -1]
'''


def _setup_two_sum(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(2, min(n, 16))
    arr = [rng.randint(-9, 9) for _ in range(n)]
    # Pick a guaranteed-reachable target: sum of two random distinct indices.
    i, j = rng.sample(range(n), 2)
    target = arr[i] + arr[j]
    challenge._arr = list(arr)
    challenge._target = target
    return {"arr": list(arr), "target": target, "n": n}


def _verify_two_sum(challenge, result: Any) -> bool:
    if not isinstance(result, list) or len(result) != 2:
        return False
    if sorted(result) != result:
        return False
    i, j = result
    if i < 0 or j < 0 or i >= len(challenge._arr) or j >= len(challenge._arr):
        return False
    return challenge._arr[i] + challenge._arr[j] == challenge._target


# === hash_02: Subarray Sum Equals K ===

HASH_02_SOURCE = '''\
"""Optimal solution for hash_02: Subarray Sum Equals K.

The number of subarrays with sum k equals the number of prefix
sums p_j such that p_j == p_i - k for some earlier prefix p_i.
Track running prefix sums and the count of each. O(n).
"""


def solve(arr, k, n):
    count = 0
    prefix = 0
    freq = {0: 1}
    for i in range(n):
        prefix += arr[i]
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count
'''


def _setup_subarray_sum_k(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    arr = [rng.randint(-5, 5) for _ in range(n)]
    k = rng.randint(-5, 5)
    challenge._arr = list(arr)
    challenge._k = k
    return {"arr": list(arr), "k": k, "n": n}


def _verify_subarray_sum_k(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    arr = challenge._arr
    k = challenge._k
    # Brute-force: count all subarrays with sum k.
    expected = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == k:
                expected += 1
    return result == expected


# === hash_03: Longest Substring Without Repeating Characters ===

HASH_03_SOURCE = '''\
"""Optimal solution for hash_03: Longest Substring Without Repeating.

Sliding window: extend the right end, record the last index of
each character seen. If a repeat sits inside the window, jump
the left end past the previous occurrence. O(n).
"""


def solve(s, n):
    if n == 0:
        return 0
    last = {}
    best = 0
    left = 0
    for right in range(n):
        ch = s[right]
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        if right - left + 1 > best:
            best = right - left + 1
    return best
'''


def _setup_longest_unique(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    # Lower-case ASCII so the result is meaningful.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(rng.choice(alphabet) for _ in range(n))
    challenge._s = s
    return {"s": s, "n": n}


def _verify_longest_unique(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    s = challenge._s
    # Brute-force: check every substring for uniqueness.
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            if j - i + 1 > best:
                best = j - i + 1
    return result == best


# === hash_04: Group Anagrams ===

HASH_04_SOURCE = '''\
"""Optimal solution for hash_04: Group Anagrams.

Two strings are anagrams iff their sorted characters are equal.
Use a dict keyed on the sorted-tuple; collect the original
strings into per-key lists. Sort each group's inner list and
the outer list of group keys so the verify can compare
directly. O(n * k log k) where k is the string length.
"""


def solve(strs, n):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        groups.setdefault(key, []).append(s)
    # Normalize: sort each inner list, then sort the outer list
    # by the smallest element of each group.
    out = []
    for key in groups:
        out.append(sorted(groups[key]))
    out.sort(key=lambda g: g[0])
    return out
'''


def _setup_group_anagrams(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 8))
    # Make a small pool of words; some will be anagrams of each other.
    pool = ["abc", "bca", "cab", "xyz", "zyx", "yxz", "ab", "ba", "hello", "olleh", "world", "dlrow"]
    strs = [rng.choice(pool) for _ in range(n)]
    challenge._strs = list(strs)
    return {"strs": list(strs), "n": n}


def _verify_group_anagrams(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    strs = challenge._strs
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        groups.setdefault(key, []).append(s)
    expected = []
    for key in groups:
        expected.append(sorted(groups[key]))
    expected.sort(key=lambda g: g[0])
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="hash_01",
        name="Two Sum",
        category="hashing",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Given an array and a target, return the indices of the two\n"
            "values that sum to target. The setup picks a reachable target\n"
            "(sum of two random distinct positions). Single pass with a\n"
            "value->index hash map; O(n).\n"
            "Source: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/"
        ),
        source_url="https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/",
        params=["arr", "target", "n"],
        inputs={
            "arr": "list of n random integers (can include negatives).",
            "target": "sum of two distinct positions in arr.",
            "n": "length of arr.",
        },
        returns="a sorted pair of indices [i, j] with arr[i] + arr[j] == target, or [-1, -1].",
        source=HASH_01_SOURCE,
        setup_fn=_setup_two_sum,
        verify_fn=_verify_two_sum,
        samples=[
            Sample("arr = [2, 7, 11, 15], target = 9, n = 4", "[0, 1]"),
            Sample("arr = [3, 2, 4], target = 6, n = 3", "[1, 2]"),
            Sample("arr = [3, 3], target = 6, n = 2", "[0, 1]"),
        ],
        hint="Walk the array. For each value, check if (target - value) is already in the map.",
        parents=["search_10"],
        children=["hash_02"],
    ),
    AlgorithmSpec(
        id="hash_02",
        name="Subarray Sum Equals K",
        category="hashing",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Count the number of contiguous subarrays whose sum equals k.\n"
            "Trick: the number of subarrays ending at i with sum k equals the\n"
            "number of earlier prefix sums equal to prefix[i] - k. Hash the\n"
            "prefix-sum counts. O(n).\n"
            "Source: https://www.geeksforgeeks.org/number-subarrays-sum-exactly-k/"
        ),
        source_url="https://www.geeksforgeeks.org/number-subarrays-sum-exactly-k/",
        params=["arr", "k", "n"],
        inputs={
            "arr": "list of n random integers (can include negatives).",
            "k": "target sum.",
            "n": "length of arr.",
        },
        returns="the number of contiguous subarrays with sum k.",
        source=HASH_02_SOURCE,
        setup_fn=_setup_subarray_sum_k,
        verify_fn=_verify_subarray_sum_k,
        samples=[
            Sample("arr = [1, 1, 1], k = 2, n = 3", "2 (1+1, 1+1)"),
            Sample("arr = [1, 2, 3], k = 3, n = 3", "2 (1+2, 3)"),
        ],
        hint="Track running prefix sum; look up (prefix - k) in a frequency dict.",
        parents=["hash_01"],
        children=["hash_03"],
    ),
    AlgorithmSpec(
        id="hash_03",
        name="Longest Substring Without Repeating",
        category="hashing",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the length of the longest substring with no repeated\n"
            "characters. Sliding window: keep a last-seen-position map;\n"
            "when a repeat is inside the window, jump the left end past\n"
            "the previous occurrence. O(n).\n"
            "Source: https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/"
        ),
        source_url="https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/",
        params=["s", "n"],
        inputs={
            "s": "string of n lower-case ASCII characters.",
            "n": "length of s.",
        },
        returns="the length of the longest substring with all distinct characters.",
        source=HASH_03_SOURCE,
        setup_fn=_setup_longest_unique,
        verify_fn=_verify_longest_unique,
        samples=[
            Sample('s = "geeksforgeeks", n = 13', "7 (eksforg)"),
            Sample('s = "aaaa", n = 4', "1"),
            Sample('s = "abcdef", n = 6', "6"),
        ],
        hint="Map each char to its last-seen index. If the last-seen is inside the window, advance the left end.",
        parents=["hash_02"],
        children=["hash_04"],
    ),
    AlgorithmSpec(
        id="hash_04",
        name="Group Anagrams",
        category="hashing",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Group strings that are anagrams of each other. The canonical\n"
            "key is the sorted tuple of characters. Return a list of groups;\n"
            "each group's inner list is sorted; the outer list is sorted by\n"
            "the smallest element of each group.\n"
            "Requirement: O(n * k log k) where k is the string length.\n"
            "Source: https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/"
        ),
        source_url="https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/",
        params=["strs", "n"],
        inputs={
            "strs": "list of n short strings.",
            "n": "length of strs.",
        },
        returns="a list of groups; each group is a sorted list of anagrams; outer list sorted by group min.",
        source=HASH_04_SOURCE,
        setup_fn=_setup_group_anagrams,
        verify_fn=_verify_group_anagrams,
        samples=[
            Sample('strs = ["eat", "tea", "tan", "ate", "nat", "bat"], n = 6', '[["ate","eat","tea"], ["bat"], ["nat","tan"]]'),
            Sample('strs = [""], n = 1', '[[""]]'),
        ],
        hint="Sort each string's characters to form a key; collect the originals into per-key lists.",
        parents=["hash_03"],
        children=["hash_05"],
    ),
]


# === hash_05: Count Distinct Elements in Window ===
#
# Sliding window of size k. Track counts in a hash map; expand
# the right end, shrink the left. The number of keys is the
# distinct count in the current window.


HASH_05_SOURCE = '''
def solve(arr, k, n):
    """For each window of size k, return the number of distinct
    elements. O(n) total: amortized O(1) per window step.
    """
    if k <= 0 or k > n:
        return []
    counts = {}
    out = []
    for i in range(k):
        counts[arr[i]] = counts.get(arr[i], 0) + 1
    out.append(len(counts))
    for i in range(k, n):
        # Add arr[i].
        counts[arr[i]] = counts.get(arr[i], 0) + 1
        # Remove arr[i - k].
        old = arr[i - k]
        counts[old] -= 1
        if counts[old] == 0:
            del counts[old]
        out.append(len(counts))
    return out
'''


def _setup_distinct_window(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(2, min(n, 16))
    k = max(1, min(n, 4))
    arr = [rng.randint(0, max(1, n // 2)) for _ in range(n)]
    challenge._arr = list(arr)
    challenge._k = k
    return {"arr": list(arr), "k": k, "n": n}


def _verify_distinct_window(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    k = challenge._k
    expected = []
    for i in range(len(arr) - k + 1):
        window = arr[i:i + k]
        expected.append(len(set(window)))
    return result == expected


# === hash_06: Longest Consecutive Sequence ===
#
# Sort then walk; or use a hash-set and check for the start of
# each run (arr[k] - 1 not in the set). The hash-set version is
# O(n) amortized; the sort version is O(n log n) but easier to
# verify, so we use it here.


HASH_06_SOURCE = '''
def solve(arr, n):
    """Return the length of the longest consecutive run."""
    if n == 0:
        return 0
    s = sorted(set(arr))
    best = 1
    cur = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1] + 1:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 1
    return best
'''


def _setup_consecutive(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    arr = [rng.randint(0, max(2, n) * 2) for _ in range(n)]
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_consecutive(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    arr = sorted(set(challenge._arr))
    best = 0
    cur = 0
    last = None
    for v in arr:
        if last is not None and v == last + 1:
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
        last = v
    return result == best


SPECS.extend([
    AlgorithmSpec(
        id="hash_05",
        name="Count Distinct in Window",
        category="hashing",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "For each window of size k in arr, return the number of\n"
            "distinct elements. Sliding window + count map: O(n) total.\n"
            "Source: https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/"
        ),
        source_url="https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/",
        params=["arr", "k", "n"],
        inputs={
            "arr": "list of n integers (small value range).",
            "k": "window size (1..4 in the setup).",
            "n": "length of arr.",
        },
        returns="a list of n - k + 1 distinct counts (one per window).",
        source=HASH_05_SOURCE,
        setup_fn=_setup_distinct_window,
        verify_fn=_verify_distinct_window,
        samples=[
            Sample("arr = [1, 2, 1, 3, 4, 2, 3], k = 4, n = 7", "[3, 4, 4, 3]"),
            Sample("arr = [1, 1, 1, 1], k = 2, n = 4", "[1, 1, 1]"),
        ],
        hint="Sliding window. Hash map of counts; len(map) = distinct count.",
        parents=["hash_04"],
        children=["hash_06"],
    ),
    AlgorithmSpec(
        id="hash_06",
        name="Longest Consecutive Sequence",
        category="hashing",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Given an unsorted array, return the length of the longest\n"
            "sequence of consecutive integers. Sort, then walk; O(n\n"
            "log n). Real O(n) solution uses a set: for each v, if v-1\n"
            "isn't in the set, walk forward counting.\n"
            "Source: https://www.geeksforgeeks.org/longest-consecutive-subsequence/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-consecutive-subsequence/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n integers (can include duplicates).",
            "n": "length of arr.",
        },
        returns="the length of the longest consecutive-integer run.",
        source=HASH_06_SOURCE,
        setup_fn=_setup_consecutive,
        verify_fn=_verify_consecutive,
        samples=[
            Sample("arr = [1, 9, 3, 10, 4, 20, 2], n = 7", "4 (1,2,3,4)"),
            Sample("arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], n = 11", "9"),
        ],
        hint="Sort + dedupe, then walk and count runs. Set-based O(n) works too.",
        parents=["hash_05"],
        children=[],
    ),
])
