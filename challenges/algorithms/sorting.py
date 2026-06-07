"""Sorting algorithms.

Ten algorithms from GFG's "Sorting Algorithms" catalog:

  01 Bubble Sort   - swap neighbours, O(n^2)
  02 Selection     - find min, swap to front, O(n^2)
  03 Insertion     - shift into sorted prefix, O(n^2)
  04 Merge Sort    - divide & conquer, O(n log n)
  05 Quick Sort    - pivot partition, O(n log n) avg
  06 Heap Sort     - max-heap then extract, O(n log n)
  07 Counting Sort - bucketed by value, O(n + k)
  08 Radix Sort    - LSD by digit, O(d * n)
  09 Bucket Sort   - uniform buckets, O(n + k) avg
  10 Shell Sort    - insertion with shrinking gaps, O(n^1.5)

All ten share the same data contract (``TrackedList`` of n random
integers, mutate in place or return a sorted list) and the same
samples, so the player learns the algorithm not the boilerplate.
"""

from __future__ import annotations

import random
from typing import Any, Optional

from challenges.algorithms._sort_helpers import is_sorted_result
from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList


# --- Setup / verify shared by every sort challenge. ---


def _setup_sort(challenge, n: int, seed: Optional[int], *, rows: int = 3) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._data = [rng.randint(1, 99) for _ in range(n)]

    challenge.grid = Grid(n, rows)
    challenge.grid.fill_row(0, challenge._data, CellType.UNSORTED)

    challenge._working_data = TrackedList(challenge._data)
    return {"data": challenge._working_data, "n": n}


def _verify_sort(challenge, result: Any) -> bool:
    return is_sorted_result(result, challenge._data, challenge._working_data)


# --- Canonical source for every sort. The Solve button writes
# exactly this source to ``solutions/<id>.py``; the description
# field references the GFG article. ---


SORT_01_SOURCE = '''\
"""Optimal solution for sort_01: Bubble Sort.

Sort the list in place by repeatedly swapping adjacent pairs.
O(n^2) time, O(1) extra space.
"""


def solve(data, n):
    for end in range(n - 1, 0, -1):
        for i in range(end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data
'''

SORT_02_SOURCE = '''\
"""Optimal solution for sort_02: Selection Sort.

For each index i, find the minimum element in data[i..n-1] and
swap it into position i. O(n^2) time, O(1) extra space, at most n
swaps.
"""


def solve(data, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
    return data
'''

SORT_03_SOURCE = '''\
"""Optimal solution for sort_03: Insertion Sort.

For each element, shift larger elements right to make room, then
drop the element into the gap. O(n^2) worst case, O(n) on nearly
sorted data.
"""


def solve(data, n):
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
'''

SORT_04_SOURCE = '''\
"""Optimal solution for sort_04: Merge Sort.

Divide the array in half, sort each half recursively, then merge
the two sorted halves. O(n log n) time, O(n) extra space.
"""


def solve(data, n):
    def merge_sort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])
        return _merge(left, right)

    def _merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sorted_items = merge_sort(data)
    # Copy back into the player's TrackedList so the in-place contract
    # is satisfied. Each `data[i] = value` counts as one write.
    for i, value in enumerate(sorted_items):
        data[i] = value
    return data
'''

SORT_05_SOURCE = '''\
"""Optimal solution for sort_05: Quick Sort.

Three-way (Dutch National Flag) partition so duplicate keys are
handled in O(n) instead of O(n^2), then drive the recursion
iteratively. Three-way partition is the standard textbook fix
for quicksort's classic "all-equal" infinite loop with Lomuto
partition + the <= comparator, and it also halves the op count
on real data with duplicates.
"""


def solve(data, n):
    def partition_3way(items, low, high):
        # Dutch National Flag partition: items[low..lt-1] are < pivot,
        # items[lt..i-1] are == pivot, items[gt+1..high] are > pivot.
        pivot = items[high]
        lt = low
        i = low
        gt = high
        while i <= gt:
            if items[i] < pivot:
                items[lt], items[i] = items[i], items[lt]
                lt += 1
                i += 1
            elif items[i] > pivot:
                items[i], items[gt] = items[gt], items[i]
                gt -= 1
            else:
                i += 1
        return lt, gt

    stack = [(0, n - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            lt, gt = partition_3way(data, low, high)
            # Both halves may be non-empty.
            if lt - 1 > low:
                stack.append((low, lt - 1))
            if gt + 1 < high:
                stack.append((gt + 1, high))

    return data
'''

SORT_06_SOURCE = '''\
"""Optimal solution for sort_06: Heap Sort.

Build a max-heap in O(n), then repeatedly swap the root (the
largest remaining element) to the end and sift-down the new root.
O(n log n) time, O(1) extra space.
"""


def solve(data, n):
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

    # Pop the root into the last position, one at a time.
    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        sift_down(0, end)
    return data
'''

SORT_07_SOURCE = '''\
"""Optimal solution for sort_07: Counting Sort.

Non-comparison sort. Count how many times each value appears,
then walk the count array and write each value the right number
of times. O(n + k) time and O(k) extra space, where k is the
value range. Stable, deterministic, and very fast when k is
not much larger than n.
"""


def solve(data, n):
    if n == 0:
        return data
    min_val = min(data)
    max_val = max(data)
    span = max_val - min_val + 1
    counts = [0] * span
    for value in data:
        counts[value - min_val] += 1
    # Rewrite data in place by walking the count array.
    index = 0
    for offset, count in enumerate(counts):
        for _ in range(count):
            data[index] = offset + min_val
            index += 1
    return data
'''

SORT_08_SOURCE = '''\
"""Optimal solution for sort_08: Radix Sort.

LSD radix sort with counting sort as the stable inner sort.
Process the numbers digit-by-digit from least-significant to
most-significant. O(d * (n + 10)) time, O(n) extra space, where
d is the number of digits in the largest value.
"""


def solve(data, n):
    if n == 0:
        return data
    max_val = max(data)
    exp = 1
    while max_val // exp > 0:
        # Counting sort on the current digit.
        counts = [0] * 10
        for value in data:
            counts[(value // exp) % 10] += 1
        # Turn counts into a stable-position table.
        for i in range(1, 10):
            counts[i] += counts[i - 1]
        # Walk the input right-to-left so the sort stays stable.
        output = [0] * n
        for i in range(n - 1, -1, -1):
            digit = (data[i] // exp) % 10
            counts[digit] -= 1
            output[counts[digit]] = data[i]
        # Copy the per-digit sorted output back into data.
        for i in range(n):
            data[i] = output[i]
        exp *= 10
    return data
'''

SORT_09_SOURCE = '''\
"""Optimal solution for sort_09: Bucket Sort.

Distribute elements into a small number of buckets, sort each
bucket individually, then concatenate. Works best when the input
is roughly uniformly distributed. O(n + k) average time.
"""


def solve(data, n):
    if n == 0:
        return data
    min_val = min(data)
    max_val = max(data)
    span = max_val - min_val
    if span == 0:
        return data
    bucket_count = min(n, 10)
    bucket_size = span / bucket_count
    buckets = [[] for _ in range(bucket_count)]
    for value in data:
        idx = int((value - min_val) / bucket_size)
        if idx == bucket_count:
            # Float rounding: the max value can land one bucket too far.
            idx -= 1
        buckets[idx].append(value)
    for bucket in buckets:
        bucket.sort()
    index = 0
    for bucket in buckets:
        for value in bucket:
            data[index] = value
            index += 1
    return data
'''

SORT_10_SOURCE = '''\
"""Optimal solution for sort_10: Shell Sort.

Generalisation of insertion sort that compares elements far apart
first, then progressively shrinks the gap. The Knuth gap sequence
(3k+1) gives O(n^1.5) on average. In-place, not stable.
"""


def solve(data, n):
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 3
    return data
'''


# --- Sample I/O for all sorts (same shape, one shared list). ---

SORTING_SAMPLES: list[Sample] = [
    Sample("data = [3, 1, 2], n = 3", "[1, 2, 3]"),
    Sample("data = [5, 5, 2, 9], n = 4", "[2, 5, 5, 9]"),
    Sample("data = [8, 4, 7, 1, 3], n = 5", "[1, 3, 4, 7, 8]"),
]


# --- Per-challenge spec factory. The setup/verify logic is the
# same for all 10 sorts; only the metadata differs. ---


def _sort_spec(
    *,
    spec_id: str,
    name: str,
    difficulty: int,
    required_complexity: ComplexityClass,
    description: str,
    source_url: str,
    source: str,
    hint: str,
    parents: list[str],
    children: list[str],
    rows: int = 3,
    complexity_notes: dict | None = None,
) -> AlgorithmSpec:
    return AlgorithmSpec(
        id=spec_id,
        name=name,
        category="sorting",
        difficulty=difficulty,
        required_complexity=required_complexity,
        description=description,
        source_url=source_url,
        params=["data", "n"],
        inputs={
            "data": "list-like of n random integers. Mutate in place.",
            "n": "length of data.",
        },
        returns="the same data object, sorted in place (in ascending order).",
        source=source,
        setup_fn=lambda challenge, n, seed, _rows=rows: _setup_sort(challenge, n, seed, rows=_rows),
        verify_fn=_verify_sort,
        samples=list(SORTING_SAMPLES),
        hint=hint,
        parents=parents,
        children=children,
        complexity_notes=complexity_notes or {},
    )


SPECS: list[AlgorithmSpec] = [
    _sort_spec(
        spec_id="sort_01",
        name="Bubble Sort",
        difficulty=2,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Sort the array using normal Python indexing and assignment.\n"
            "Requirement: O(n^2) - just get it sorted correctly!\n"
            "Source: https://www.geeksforgeeks.org/bubble-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/bubble-sort/",
        source=SORT_01_SOURCE,
        hint="Move larger values toward the end of the list, one pass at a time.",
        parents=["intro_01"],
        children=["sort_02"],
        complexity_notes={
            "best":     "O(n) — already-sorted input: one pass, zero swaps. With the early-exit flag this is the canonical optimal case.",
            "average":  "Θ(n²) — random input: roughly half the pairs are out of order, so about n²/4 swaps and n²/2 comparisons.",
            "worst":    "O(n²) — reverse-sorted input: every comparison triggers a swap. n·(n-1)/2 compares and n·(n-1)/2 swaps.",
            "space":    "O(1) — in-place; only a handful of scalar temporaries.",
            "stable":   "Yes — equal elements keep their relative order.",
            "in_place": "Yes — no auxiliary array needed.",
        },
    ),
    _sort_spec(
        spec_id="sort_02",
        name="Selection Sort",
        difficulty=2,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Sort the array by finding the minimum element and placing it.\n"
            "For each position, find the minimum in the remaining unsorted portion.\n"
            "Requirement: O(n^2)\n"
            "Source: https://www.geeksforgeeks.org/selection-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/selection-sort/",
        source=SORT_02_SOURCE,
        hint="For each index i, find min in [i..n-1] and swap it to position i.",
        parents=["sort_01"],
        children=["sort_03"],
        complexity_notes={
            "best":     "O(n²) — same as worst; selection sort always scans the full unsorted suffix.",
            "average":  "Θ(n²) — n²/2 comparisons and at most n swaps regardless of input order.",
            "worst":    "O(n²) — same as best; no early-exit optimization.",
            "space":    "O(1) — in-place; only a few scalar temporaries.",
            "stable":   "No — the swap across the unsorted region reorders equal elements.",
            "in_place": "Yes.",
        },
    ),
    _sort_spec(
        spec_id="sort_03",
        name="Insertion Sort",
        difficulty=3,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Sort the array by inserting each element into the sorted portion.\n"
            "Requirement: O(n^2) worst case, but aim for fewer ops on nearly-sorted data.\n"
            "Source: https://www.geeksforgeeks.org/insertion-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/insertion-sort/",
        source=SORT_03_SOURCE,
        hint="For each element, shift larger elements right to make room.",
        parents=["sort_02"],
        children=["sort_04", "sort_05"],
    ),
    _sort_spec(
        spec_id="sort_04",
        name="Merge Sort",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Sort the array in O(n log n) time using divide and conquer.\n"
            "Split the array in half, sort each half, then merge.\n"
            "Requirement: O(n log n) - quadratic solutions will FAIL!\n"
            "Source: https://www.geeksforgeeks.org/merge-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/merge-sort/",
        source=SORT_04_SOURCE,
        hint="Recursively split, then merge two sorted halves with a two-pointer technique.",
        parents=["sort_03"],
        children=["sort_06"],
        rows=5,
    ),
    _sort_spec(
        spec_id="sort_05",
        name="Quick Sort",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Sort the array using partitioning around a pivot.\n"
            "Choose a pivot, partition elements around it, recurse.\n"
            "Requirement: O(n log n) average case.\n"
            "Source: https://www.geeksforgeeks.org/quick-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/quick-sort/",
        source=SORT_05_SOURCE,
        hint="Pick a pivot, put smaller elements left and larger right, then recurse.",
        parents=["sort_03"],
        children=["sort_06"],
        rows=5,
    ),
    _sort_spec(
        spec_id="sort_06",
        name="Heap Sort",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Sort the array using a binary max-heap.\n"
            "Build the heap, then repeatedly extract the maximum by swapping the root "
            "to the end and sifting down.\n"
            "Requirement: O(n log n) worst case, in-place.\n"
            "Source: https://www.geeksforgeeks.org/heap-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/heap-sort/",
        source=SORT_06_SOURCE,
        hint="Build a max-heap in O(n), then repeatedly swap root to the end and sift down.",
        parents=["sort_04", "sort_05"],
        children=["sort_07"],
        rows=5,
    ),
    _sort_spec(
        spec_id="sort_07",
        name="Counting Sort",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "A non-comparison sort that works when the value range is bounded.\n"
            "Count how many times each value appears, then walk the counts and write "
            "each value the right number of times.\n"
            "Requirement: O(n + k) time and O(k) extra space, where k = max - min + 1.\n"
            "Source: https://www.geeksforgeeks.org/counting-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/counting-sort/",
        source=SORT_07_SOURCE,
        hint="Build a count array indexed by (value - min), then rewrite data from the counts.",
        parents=["sort_06"],
        children=["sort_08"],
    ),
    _sort_spec(
        spec_id="sort_08",
        name="Radix Sort",
        difficulty=6,
        required_complexity=ComplexityClass.O_N,
        description=(
            "A non-comparison sort that works on integers by processing them digit by "
            "digit (least significant first). Each digit pass is a stable counting sort.\n"
            "Requirement: O(d * n) where d is the number of digits in the max value.\n"
            "Source: https://www.geeksforgeeks.org/radix-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/radix-sort/",
        source=SORT_08_SOURCE,
        hint="Run counting sort on each digit (1s, then 10s, then 100s, ...).",
        parents=["sort_07"],
        children=["sort_09"],
    ),
    _sort_spec(
        spec_id="sort_09",
        name="Bucket Sort",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Distribute elements into a small number of buckets by their value, sort "
            "each bucket, then concatenate.\n"
            "Fastest when the input is roughly uniformly distributed; degenerates to "
            "O(n^2) in the worst case.\n"
            "Requirement: O(n + k) average time, where k is the number of buckets.\n"
            "Source: https://www.geeksforgeeks.org/bucket-sort-2/"
        ),
        source_url="https://www.geeksforgeeks.org/bucket-sort-2/",
        source=SORT_09_SOURCE,
        hint="Pick a bucket size from the value range, scatter values into buckets, sort each.",
        parents=["sort_08"],
        children=["sort_10"],
    ),
    _sort_spec(
        spec_id="sort_10",
        name="Shell Sort",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Generalisation of insertion sort that compares elements far apart first, "
            "then progressively shrinks the gap. In-place, not stable.\n"
            "Requirement: O(n^(3/2)) average using the Knuth gap sequence.\n"
            "Source: https://www.geeksforgeeks.org/shell-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/shell-sort/",
        source=SORT_10_SOURCE,
        hint="Use a gap sequence (e.g. Knuth's 1, 4, 13, 40, ...). gapped-insertion-sort at each gap.",
        parents=["sort_09"],
        children=[],
    ),
]
