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
        children=["heap_05"],
    ),
]


# === heap_05: Sliding Window Maximum ===

HEAP_05_SOURCE = '''\
"""Optimal solution for heap_05: Sliding Window Maximum.

For each window of size k, return the max. Use a max-heap keyed
on (-value, index); pop from the top while the index is outside
the current window. The max is then the heap's top.
"""


def solve(arr, k, n):
    if k <= 0 or k > n:
        return []
    import heapq
    heap = []
    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))
    out = [-heap[0][0]]
    for i in range(k, n):
        heapq.heappush(heap, (-arr[i], i))
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        out.append(-heap[0][0])
    return out
'''


def _setup_sliding_max(challenge, n, seed):
    rng = random.Random(seed)
    n = max(2, min(n, 16))
    k = max(1, min(n, 4))
    arr = [rng.randint(0, 99) for _ in range(n)]
    challenge._arr = list(arr)
    challenge._k = k
    return {"arr": list(arr), "k": k, "n": n}


def _verify_sliding_max(challenge, result):
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    k = challenge._k
    expected = []
    for i in range(len(arr) - k + 1):
        expected.append(max(arr[i:i + k]))
    return result == expected


# === heap_06: Kth Smallest in a Sorted Matrix ===

HEAP_06_SOURCE = '''\
"""Optimal solution for heap_06: Kth Smallest in a Sorted Matrix.

A matrix where every row and every column is sorted. The first
column is not necessarily sorted, but the matrix has the property
that the smallest element is in [0][0]. Use a min-heap of
(value, row, col) and pop k times. O(k log k).
"""


def solve(matrix, n, k):
    if n == 0 or k <= 0:
        return -1
    import heapq
    heap = [(matrix[0][0], 0, 0)]
    seen = {(0, 0)}
    popped = 0
    while heap:
        v, r, c = heapq.heappop(heap)
        popped += 1
        if popped == k:
            return v
        for dr, dc in [(0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < n and nc < n and (nr, nc) not in seen:
                heapq.heappush(heap, (matrix[nr][nc], nr, nc))
                seen.add((nr, nc))
    return -1
'''


def _setup_kth_smallest_matrix(challenge, n, seed):
    rng = random.Random(seed)
    n = max(2, min(n, 6))
    # Build a row+col sorted matrix by sorting rows then columns.
    matrix = []
    for r in range(n):
        row = [rng.randint(0, 50) for _ in range(n)]
        row.sort()
        matrix.append(row)
    # Now sort each column independently. This may break row sort
    # in some cases, but the property we really need is "the smallest
    # is at [0][0] and rows+cols are sorted within themselves". The
    # verify brute-forces via the flattened sorted list, so we don't
    # need strict row+col sorting.
    for c in range(n):
        col = [matrix[r][c] for r in range(n)]
        col.sort()
        for r in range(n):
            matrix[r][c] = col[r]
    k = max(1, min(n * n, rng.randint(1, n * n)))
    challenge._matrix = [row[:] for row in matrix]
    challenge._k = k
    return {"matrix": [row[:] for row in matrix], "n": n, "k": k}


def _verify_kth_smallest_matrix(challenge, result):
    if not isinstance(result, int):
        return False
    flat = []
    for row in challenge._matrix:
        flat.extend(row)
    flat.sort()
    return result == flat[challenge._k - 1]


SPECS.extend([
    AlgorithmSpec(
        id="heap_05",
        name="Sliding Window Maximum",
        category="heap",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "For each window of size k in arr, return the max. Use a\n"
            "max-heap keyed on (-value, index). Pop from the top\n"
            "while the index is outside the current window; the heap\n"
            "top is then the max. O(n log k).\n"
            "Source: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-size-k/"
        ),
        source_url="https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-size-k/",
        params=["arr", "k", "n"],
        inputs={
            "arr": "list of n integers.",
            "k": "window size (1..4 in the setup).",
            "n": "length of arr.",
        },
        returns="a list of n - k + 1 maxes (one per window).",
        source=HEAP_05_SOURCE,
        setup_fn=_setup_sliding_max,
        verify_fn=_verify_sliding_max,
        samples=[
            Sample("arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3, n = 8", "[3, 3, 5, 5, 6, 7]"),
        ],
        hint="Max-heap on (-value, index). Pop entries with index <= i - k.",
        parents=["heap_04"],
        children=["heap_06"],
    ),
    AlgorithmSpec(
        id="heap_06",
        name="Kth Smallest in Sorted Matrix",
        category="heap",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "A matrix where every row and every column is sorted\n"
            "(row-major with sorted columns). Return the kth smallest\n"
            "element. Min-heap of (value, row, col) starting at [0][0];\n"
            "pop k times, pushing each cell's right + down neighbours.\n"
            "O(k log k) per insertion.\n"
            "Source: https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array/"
        ),
        source_url="https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array/",
        params=["matrix", "n", "k"],
        inputs={
            "matrix": "n x n matrix (rows and columns sorted).",
            "n": "matrix dimension.",
            "k": "1-indexed kth smallest.",
        },
        returns="the kth smallest element in the matrix.",
        source=HEAP_06_SOURCE,
        setup_fn=_setup_kth_smallest_matrix,
        verify_fn=_verify_kth_smallest_matrix,
        samples=[
            Sample("matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], n = 3, k = 8", "13"),
        ],
        hint="Min-heap of (value, row, col). Pop k times. Push each cell's right + down neighbours.",
        parents=["heap_05"],
        children=[],
    ),
])
