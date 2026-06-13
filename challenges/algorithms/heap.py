"""Heap / Priority Queue algorithms.

Four core problems from GFG's heap catalog:

  01 Build Max Heap     - O(n) heapify into max-heap order
  02 Kth Largest        - selection via min-heap of size k
  03 Top K Frequent     - count + bucket/heap, return k most common
  04 Median in Stream   - two heaps: max-heap of smalls, min-heap of bigs

All four pass the same kind of deterministic random test: the
setup picks the input, the canonical solve computes the answer
in place, the verify re-runs the same algorithm and compares.
"""


from __future__ import annotations

import heapq
import random
from collections import Counter
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === heap_01: Build Max Heap ===

HEAP_01_SOURCE = '''\
"""Optimal solution for heap_01: Build Max Heap.

Treat the input as a 0-indexed binary heap and sift-down from
the last non-leaf to the root. Bottom-up heapify is O(n) - faster
than the O(n log n) naive "insert" approach.
"""


def solve(data, n):
    # Sift down ``start`` in [0, n).
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child >= end:
                break
            if child + 1 < end and data[child + 1] > data[child]:
                child += 1
            if data[child] > data[root]:
                data[root], data[child] = data[child], data[root]
                root = child
            else:
                break
    # Build the max-heap.
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n)
    return data
'''


def _setup_heap_build(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    data = [rng.randint(0, 99) for _ in range(max(1, n))]
    challenge._data = list(data)
    return {"data": list(data), "n": len(data)}


def _verify_heap_build(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    n = len(result)
    # Check max-heap property at every node.
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and result[left] > result[i]:
            return False
        if right < n and result[right] > result[i]:
            return False
    # Check it's a permutation of the original.
    return sorted(result) == sorted(challenge._data)


# === heap_02: Kth Largest ===

HEAP_02_SOURCE = '''\
"""Optimal solution for heap_02: Kth Largest Element.

Maintain a min-heap of size k. For each element, push it onto
the heap and pop the smallest if the heap is over k. At the end
the heap contains the k largest elements; the smallest of those
(the heap top) is the kth largest. O(n log k).
"""


def solve(data, n, k):
    import heapq
    if k <= 0 or k > n:
        return -1
    heap = []
    for value in data:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return heap[0]
'''


def _setup_kth_largest(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    data = [rng.randint(0, 99) for _ in range(max(2, n))]
    k = max(1, min(n // 2, rng.randint(1, n)))
    challenge._data = list(data)
    challenge._k = k
    return {"data": list(data), "n": len(data), "k": k}


def _verify_kth_largest(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    expected = sorted(challenge._data, reverse=True)[challenge._k - 1]
    return result == expected


# === heap_03: Top K Frequent ===

HEAP_03_SOURCE = '''\
"""Optimal solution for heap_03: Top K Frequent Elements.

Count occurrences with a hash map, then push (count, value) into
a max-heap. Pop the top k. The output is sorted in DESCENDING
order of frequency; ties broken by value in DESCENDING order so
the verify can do a plain equality check.
"""


def solve(data, n, k):
    import heapq
    if k <= 0 or n == 0:
        return []
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    # Max-heap via (-count, -value). Inverting both ensures ties
    # are broken by DESCENDING value (the smaller -v comes first).
    heap = [(-c, -v) for v, c in counts.items()]
    heapq.heapify(heap)
    out = []
    for _ in range(min(k, len(heap))):
        neg_c, neg_v = heapq.heappop(heap)
        out.append(-neg_v)
    return out
'''


def _setup_top_k_frequent(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(2, n)
    # Use a small value range so duplicates are guaranteed.
    data = [rng.randint(0, max(1, n // 2)) for _ in range(n)]
    k = max(1, min(n // 2, rng.randint(1, n)))
    challenge._data = list(data)
    challenge._k = k
    return {"data": list(data), "n": len(data), "k": k}


def _verify_top_k_frequent(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    if len(result) != min(challenge._k, len(set(challenge._data))):
        return False
    # Re-derive the expected top k most frequent, sorted by (-count, -value).
    counts = Counter(challenge._data)
    expected = sorted(counts.keys(), key=lambda v: (-counts[v], -v))[:challenge._k]
    return result == expected


# === heap_04: Median in Stream ===

HEAP_04_SOURCE = '''\
"""Optimal solution for heap_04: Median in a Stream.

Two heaps: a max-heap of the smaller half, a min-heap of the
larger half. After each insert, rebalance so the two heaps are
within 1 of each other; the median is the top of the larger
heap (odd length) or the average of the two tops (even).
"""


def solve(data, n):
    import heapq
    if n == 0:
        return []
    small = []  # max-heap (inverted)
    large = []  # min-heap
    out = []
    for value in data:
        # Insert into the appropriate heap.
        if not small or value <= -small[0]:
            heapq.heappush(small, -value)
        else:
            heapq.heappush(large, value)
        # Rebalance.
        if len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        elif len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
        # Compute the median.
        if len(small) > len(large):
            out.append(-small[0])
        else:
            out.append((-small[0] + large[0]) / 2)
    return out
'''


def _setup_median_stream(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    data = [rng.randint(0, 99) for _ in range(max(1, n))]
    challenge._data = list(data)
    return {"data": list(data), "n": len(data)}


def _verify_median_stream(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    if len(result) != len(challenge._data):
        return False
    # Brute-force: median of data[:i+1] for each i.
    for i, _ in enumerate(challenge._data):
        prefix = sorted(challenge._data[:i + 1])
        m = len(prefix)
        if m % 2 == 1:
            expected = float(prefix[m // 2])
        else:
            expected = (prefix[m // 2 - 1] + prefix[m // 2]) / 2
        if abs(result[i] - expected) > 1e-9:
            return False
    return True


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="heap_01",
        name="Build Max Heap",
        category="heap",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Rearrange an array into a 0-indexed binary max-heap: for every\n"
            "node i, data[i] >= data[2i+1] and data[i] >= data[2i+2].\n"
            "Bottom-up heapify: sift-down from the last non-leaf to the root.\n"
            "Mutate the input in place. The output must satisfy the max-heap\n"
            "property and be a permutation of the input.\n"
            "Requirement: O(n) time, O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/building-heap-from-array/"
        ),
        source_url="https://www.geeksforgeeks.org/building-heap-from-array/",
        params=["data", "n"],
        inputs={
            "data": "list-like of n random integers (mutated in place).",
            "n": "length of data.",
        },
        returns="the same list, now in max-heap order.",
        source=HEAP_01_SOURCE,
        setup_fn=_setup_heap_build,
        verify_fn=_verify_heap_build,
        samples=[
            Sample("data = [1, 3, 5, 7, 9, 11], n = 6", "[11, 9, 5, 7, 3, 1]  (one valid max-heap)"),
            Sample("data = [5, 5, 5, 5], n = 4", "[5, 5, 5, 5]"),
        ],
        hint="Sift-down from n//2-1 down to 0. A valid max-heap isn't unique.",
        parents=["tree_19"],
        children=["heap_02"],
    ),
    AlgorithmSpec(
        id="heap_02",
        name="Kth Largest Element",
        category="heap",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Find the kth largest element in an unsorted array. Min-heap of\n"
            "size k: for each element, push it and pop the smallest if the\n"
            "heap grows past k. At the end the heap top is the answer.\n"
            "Requirement: O(n log k) time.\n"
            "Source: https://www.geeksforgeeks.org/kth-largest-element-in-an-array/"
        ),
        source_url="https://www.geeksforgeeks.org/kth-largest-element-in-an-array/",
        params=["data", "n", "k"],
        inputs={
            "data": "list-like of n random integers.",
            "n": "length of data.",
            "k": "which largest (1-indexed: k=1 is the max).",
        },
        returns="the kth largest element, or -1 if k is out of range.",
        source=HEAP_02_SOURCE,
        setup_fn=_setup_kth_largest,
        verify_fn=_verify_kth_largest,
        samples=[
            Sample("data = [3, 2, 1, 5, 6, 4], n = 6, k = 2", "5"),
            Sample("data = [7, 4, 6, 3, 9, 8], n = 6, k = 3", "7"),
        ],
        hint="Min-heap of size k. Push if smaller than heap top, otherwise skip.",
        parents=["heap_01"],
        children=["heap_03"],
    ),
    AlgorithmSpec(
        id="heap_03",
        name="Top K Frequent Elements",
        category="heap",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Given an array and an integer k, return the k most frequent\n"
            "elements. Sort the output by descending frequency; ties broken\n"
            "by descending value. Use a hash map to count, then a max-heap\n"
            "to extract the top k.\n"
            "Requirement: O(n log k) time.\n"
            "Source: https://www.geeksforgeeks.org/find-k-frequent-elements-array/"
        ),
        source_url="https://www.geeksforgeeks.org/find-k-frequent-elements-array/",
        params=["data", "n", "k"],
        inputs={
            "data": "list-like of n integers (small value range to ensure duplicates).",
            "n": "length of data.",
            "k": "how many of the most-frequent to return.",
        },
        returns="a list of k values, sorted by descending frequency (ties: descending value).",
        source=HEAP_03_SOURCE,
        setup_fn=_setup_top_k_frequent,
        verify_fn=_verify_top_k_frequent,
        samples=[
            Sample("data = [1, 1, 1, 2, 2, 3], n = 6, k = 2", "[1, 2]"),
            Sample("data = [4, 4, 4, 5, 5, 6, 7], n = 7, k = 1", "[4]"),
        ],
        hint="Count with a hash map; then a max-heap keyed on (-count, -value).",
        parents=["heap_02"],
        children=["heap_04"],
    ),
    AlgorithmSpec(
        id="heap_04",
        name="Median in a Stream",
        category="heap",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Given a stream of integers, return the median after each\n"
            "insertion. Two heaps: a max-heap of the small half and a\n"
            "min-heap of the large half; rebalance after every insert.\n"
            "If the total length is odd, the median is the top of the\n"
            "larger heap; if even, the average of the two tops.\n"
            "Requirement: O(n log n) over the whole stream.\n"
            "Source: https://www.geeksforgeeks.org/median-of-stream-of-running-integers-using-stl/"
        ),
        source_url="https://www.geeksforgeeks.org/median-of-stream-of-running-integers-using-stl/",
        params=["data", "n"],
        inputs={
            "data": "list-like of n random integers (treated as a stream).",
            "n": "length of data.",
        },
        returns="a list of n medians (one after each insertion).",
        source=HEAP_04_SOURCE,
        setup_fn=_setup_median_stream,
        verify_fn=_verify_median_stream,
        samples=[
            Sample("data = [5, 15, 1, 3], n = 4", "[5, 10.0, 5, 4.0]"),
            Sample("data = [2, 4, 6, 8, 10], n = 5", "[2, 3.0, 4, 5.0, 6]"),
        ],
        hint="Max-heap of smalls, min-heap of bigs. Median is top of the larger heap (or the average of the two).",
        parents=["heap_03"],
        children=[],
    ),
]
