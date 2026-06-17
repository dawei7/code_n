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

All ten share the same data contract (a plain list of n random
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


# --- Setup / verify shared by every sort challenge. ---


def _setup_sort(challenge, n: int, seed: Optional[int], *, rows: int = 3) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._data = [rng.randint(1, 99) for _ in range(n)]

    challenge.grid = Grid(n, rows)
    challenge.grid.fill_row(0, challenge._data, CellType.UNSORTED)

    # The player receives the same list reference the engine
    # keeps in challenge._data — so the verifier reads the
    # player's mutations via challenge._data (in the in-place
    # contract) or via the returned value. The old
    # ``_working_data = TrackedList(challenge._data)`` indirection
    # (removed in v0.8.5) is no longer needed.
    return {"data": challenge._data, "n": n}


def _verify_sort(challenge, result: Any) -> bool:
    return is_sorted_result(result, challenge._data)


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


SORT_11_SOURCE = '''\
"""Optimal solution for sort_11: Cycle Sort.

In-place, write-optimal sort. For each position, count elements
smaller than it to find its final index, then place the value
there. The displaced value starts a new cycle. O(n^2) time,
O(1) extra space, and at most n-1 writes.
"""


def solve(data, n):
    for cycle_start in range(n - 1):
        item = data[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if data[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        # Skip past duplicates of `item` already at `pos`.
        while item == data[pos]:
            pos += 1
        data[pos], item = item, data[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if data[i] < item:
                    pos += 1
            while item == data[pos]:
                pos += 1
            data[pos], item = item, data[pos]
    return data
'''


SORT_12_SOURCE = '''\
"""Optimal solution for sort_12: Pancake Sort.

The only allowed operation is ``reverse prefix [0..k]`` for
some k. For each pass, find the maximum in the current
unsorted prefix, flip it to the front, then flip the prefix
to drop the max to the end. O(n^2) flips.
"""


def solve(data, n):
    def flip(end):
        start = 0
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1

    size = n
    while size > 1:
        # Find index of the maximum element in data[0..size-1].
        max_idx = 0
        for i in range(1, size):
            if data[i] > data[max_idx]:
                max_idx = i
        if max_idx != size - 1:
            if max_idx != 0:
                flip(max_idx)
            flip(size - 1)
        size -= 1
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
    _sort_spec(
        spec_id="sort_11",
        name="Cycle Sort",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "An in-place sort that minimises the number of writes:\n"
            "for each position, count how many elements are smaller\n"
            "and place the value directly at its sorted position,\n"
            "rotating the displaced value into the next cycle.\n"
            "Worst case is O(n^2) but writes are at most n-1.\n"
            "Requirement: O(n^2) time, O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/cycle-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/cycle-sort/",
        source=SORT_11_SOURCE,
        hint="For each position, count smaller items to find the right slot, then place & rotate.",
        parents=["sort_10"],
        children=["sort_12"],
        complexity_notes={
            "best":     "O(n²) — must count for every position even on sorted input.",
            "average":  "Θ(n²) — dominated by the per-position smaller-element count.",
            "worst":    "O(n²) — same; cycle sort is unique in that writes are bounded at n-1.",
            "space":    "O(1) — strictly in-place.",
            "stable":   "No — equal elements get reordered inside each cycle.",
            "in_place": "Yes — and write-optimal (≤ n-1 writes).",
        },
    ),
    _sort_spec(
        spec_id="sort_12",
        name="Pancake Sort",
        difficulty=6,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Sort using only 'flip' operations: reverse the prefix\n"
            "[0..k] for any k. Strategy: for each max value, flip it\n"
            "to the front, then flip the whole unsorted prefix to\n"
            "drop it into its sorted slot at the end.\n"
            "Requirement: O(n^2) flips, O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/pancake-sorting/"
        ),
        source_url="https://www.geeksforgeeks.org/pancake-sorting/",
        source=SORT_12_SOURCE,
        hint="Find the current max, flip it to the front, then flip the unsorted prefix to drop it at the end.",
        parents=["sort_11"],
        children=[],
        complexity_notes={
            "best":     "O(n) flips on already-sorted input (one flip per position is unnecessary; with the naive 2*n loop it is O(n²)).",
            "average":  "Θ(n²) flips — two flips per element once the max search is O(n).",
            "worst":    "O(n²) flips.",
            "space":    "O(1) — only a few scalar temporaries.",
            "stable":   "No — flips reorder equal elements.",
            "in_place": "Yes.",
        },
    ),
    _sort_spec(
        spec_id="sort_13",
        name="Tim Sort (Simplified)",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Tim Sort: divide into runs (already-sorted subsequences),\n"
            "then merge with a stack-based merge policy. This simplified\n"
            "version uses Python's built-in sorted() for each run\n"
            "and merges them, demonstrating the O(n log n) average\n"
            "case and O(n) on already-sorted data.\n"
            "Source: https://www.geeksforgeeks.org/tim-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/tim-sort/",
        source='''
"""Simplified Tim Sort: identify natural runs, then merge.

The real Tim Sort tracks minrun and uses a complex stack-based
merge policy. This simplified version sorts each run with
Python's built-in sorted() and merges pairwise.
"""


def solve(data, n):
    if n <= 1:
        return data
    work = list(data)
    RUN = max(1, min(32, n // 4))
    runs = []
    i = 0
    while i < n:
        j = i + 1
        while j < n and work[j] >= work[j - 1]:
            j += 1
        runs.append((i, j))
        # Extend the run to RUN length with sort.
        if j - i < RUN:
            end = min(i + RUN, n)
            sub = work[i:end]
            sub.sort()
            work[i:end] = sub
            j = end
            runs[-1] = (runs[-1][0], j)
        i = j
    # Merge runs pairwise.
    while len(runs) > 1:
        new_runs = []
        for k in range(0, len(runs), 2):
            if k + 1 < len(runs):
                lo1, hi1 = runs[k]
                lo2, hi2 = runs[k + 1]
                merged = []
                a, b = lo1, lo2
                while a < hi1 and b < hi2:
                    if work[a] <= work[b]:
                        merged.append(work[a])
                        a += 1
                    else:
                        merged.append(work[b])
                        b += 1
                merged.extend(work[a:hi1])
                merged.extend(work[b:hi2])
                work[lo1:hi2] = merged
                new_runs.append((lo1, hi2))
            else:
                new_runs.append(runs[k])
        runs = new_runs
    return work
''',
        hint="Find natural runs (ascending or descending). Extend to minrun. Merge pairwise.",
        parents=["sort_12"],
        children=["sort_14"],
    ),
    _sort_spec(
        spec_id="sort_14",
        name="Intro Sort (Simplified)",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Intro Sort: quicksort with a depth limit; when the\n"
            "recursion depth exceeds a threshold (typically 2 log n),\n"
            "fall back to heapsort. This gives the O(n log n)\n"
            "guarantee of heapsort and the average-case speed of\n"
            "quicksort.\n"
            "Source: https://www.geeksforgeeks.org/intro-sort/"
        ),
        source_url="https://www.geeksforgeeks.org/intro-sort/",
        source='''
"""Simplified Intro Sort: quicksort with a depth limit.

If recursion depth exceeds depth_limit, fall back to heap
sort on the current range.
"""


def solve(data, n):
    if n <= 1:
        return data
    work = list(data)
    import math
    depth_limit = 2 * int(math.log2(n)) if n > 1 else 0

    def sift_down(lo, hi, root):
        while True:
            child = 2 * (root - lo) + 1 + lo
            if child >= hi:
                break
            if child + 1 < hi and work[child + 1] > work[child]:
                child += 1
            if work[child] > work[root]:
                work[root], work[child] = work[child], work[root]
                root = child
            else:
                break

    def heap_sort(lo, hi):
        # Build max-heap.
        for start in range((hi - lo) // 2 - 1 + lo, lo - 1, -1):
            sift_down(lo, hi, start)
        # Extract.
        for end in range(hi - 1, lo, -1):
            work[lo], work[end] = work[end], work[lo]
            sift_down(lo, end, lo)

    def partition(lo, hi):
        # The range is [lo, hi); use work[hi - 1] as the pivot.
        pivot = work[hi - 1]
        i = lo
        for j in range(lo, hi - 1):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi - 1] = work[hi - 1], work[i]
        return i

    def intro_sort(lo, hi, depth):
        if hi - lo <= 1:
            return
        if depth == 0:
            heap_sort(lo, hi)
            return
        p = partition(lo, hi)
        intro_sort(lo, p, depth - 1)
        intro_sort(p + 1, hi, depth - 1)

    intro_sort(0, n, depth_limit)
    return work
''',
        hint="Quicksort with depth limit. When depth hits 0, call heapsort on the current range.",
        parents=["sort_13"],
        children=[],
    ),
]
