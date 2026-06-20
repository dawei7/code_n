# Quick Sort

| | |
|---|---|
| **ID** | `sort_05` |
| **Category** | sorting |
| **Complexity (required)** | $O(n log n)$ |
| **Difficulty** | 6/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Quicksort](https://en.wikipedia.org/wiki/Quicksort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order using the Quick Sort algorithm.

**Input:** An unsorted array of integers `arr`.
**Output:** The array sorted in strictly ascending order.

**Example:**
| Input `arr` | Output |
|---|---|
| `[10, 80, 30, 90, 40, 50, 70]` | `[10, 30, 40, 50, 70, 80, 90]` |

## When to use it

- When you need a highly efficient, general-purpose sorting algorithm. It is the default sorting algorithm (`std::sort`) in C++ and many other languages because its constant-factor overhead is extremely low.
- When memory space is constrained. Unlike Merge Sort which requires $O(n)$ auxiliary space, Quick Sort is an **in-place** sort requiring only $O(log n)$ space for the recursive call stack.
- When caching and memory locality matter. The partitioning step scans memory sequentially, which plays exceptionally well with CPU hardware caches.

## Approach

Quick Sort is a **Divide and Conquer** algorithm based on the concept of partitioning.

1. **Pick a Pivot:** Choose an element from the array to act as a pivot. Common strategies include picking the last element, the first element, a random element, or the median of three.
2. **Partition:** Rearrange the array so that all elements smaller than the pivot are moved to its left, and all elements greater than the pivot are moved to its right. At the end of this step, the pivot is permanently in its correct sorted position.
3. **Recurse:** Recursively apply the above steps to the sub-array of elements smaller than the pivot, and the sub-array of elements greater than the pivot.

The most common partitioning scheme is **Lomuto partition scheme** (simpler, uses the last element) or the **Hoare partition scheme** (faster, uses two pointers moving towards each other).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
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
```

</details>

## Walk-through

Let `arr = [10, 80, 30, 90, 40, 50, 70]`. `low = 0`, `high = 6`.

**Partitioning (Pivot = 70):**
- `i = -1`
- `j=0` (10): `10 < 70`. `i=0`. Swap `arr[0]` with `arr[0]`. `[10, 80, 30, 90, 40, 50, 70]`
- `j=1` (80): `80 > 70`. No action.
- `j=2` (30): `30 < 70`. `i=1`. Swap `arr[1]` (80) with `arr[2]` (30). `[10, 30, 80, 90, 40, 50, 70]`
- `j=3` (90): `90 > 70`. No action.
- `j=4` (40): `40 < 70`. `i=2`. Swap `arr[2]` (80) with `arr[4]` (40). `[10, 30, 40, 90, 80, 50, 70]`
- `j=5` (50): `50 < 70`. `i=3`. Swap `arr[3]` (90) with `arr[5]` (50). `[10, 30, 40, 50, 80, 90, 70]`
- Loop ends. Swap `arr[i+1]` (80) with `pivot` (70).
- Final partitioned array: `[10, 30, 40, 50, 70, 90, 80]`.
- Return pivot index `4`.

The pivot `70` is perfectly placed. We now recursively `quick_sort` the left sub-array `[10, 30, 40, 50]` and right sub-array `[90, 80]`.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n log n)$ | $O(log n)$ |
| **Average** | $O(n log n)$ | $O(log n)$ |
| **Worst** | $O(n^2)$ | $O(n)$ |

The time complexity is highly dependent on the pivot selection. If the pivot divides the array exactly in half every time, the recursion tree is `log n` deep, and we do `n` work at each level, yielding `O(n log n)`. 
However, if the array is already sorted and we pick the last element as the pivot, the partition only isolates 1 element per level, yielding a disastrous recursion tree of depth `n`, resulting in `O(n^2)` time and `O(n)` stack space limit exception risks. 
To mitigate this, randomized pivots or "Median of 3" pivots are used to guarantee average `O(n log n)`.

## Variants & optimizations

- **3-Way Quicksort (Dutch National Flag):** Instead of partitioning into two groups (< pivot, > pivot), it partitions into three (<, ==, >). This completely nullifies Quicksort's worst-case $O(n^2)$ behavior on arrays heavily populated with duplicate elements.
- **Introsort:** Starts as Quicksort, but tracks the recursion depth. If the depth exceeds `2 * log n`, it assumes the pivots are bad and switches entirely to **Heap Sort** to strictly guarantee an $O(n log n)$ worst-case.

## Real-world applications

- **Language Standard Libraries:** Variations of Quicksort (mostly Introsort) are the backbone of C++ `std::sort`, Go's `sort.Slice`, and many Java primitives arrays (`Arrays.sort(int[])` uses Dual-Pivot Quicksort).

## Related algorithms in cOde(n)

- **[sort_04 - Merge Sort](sort_04_merge-sort.md)** — The stable $O(n log n)$ alternative that sacrifices $O(n)$ space to avoid Quicksort's $O(n^2)$ worst-case.
- **[sort_14 - Introsort](sort_14_intro-sort-simplified.md)** — The production algorithm that fixes Quicksort's worst-case flaws.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
