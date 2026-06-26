# Heap Sort

| | |
|---|---|
| **ID** | `sort_06` |
| **Category** | sorting |
| **Complexity (required)** | $O(n log n)$ |
| **Difficulty** | 6/10 |
| **Interview relevance** | 7/10 |
| **Wikipedia** | [Heapsort](https://en.wikipedia.org/wiki/Heapsort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order using the Heap Sort algorithm.

**Input:** An unsorted array of integers `arr`.
**Output:** The array sorted in strictly ascending order.

**Example:**
| Input `arr` | Output |
|---|---|
| `[12, 11, 13, 5, 6, 7]` | `[5, 6, 7, 11, 12, 13]` |

## When to use it

- When you require a strictly guaranteed **$O(n log n)$** worst-case time complexity, but you cannot afford the **$O(n)$** auxiliary space overhead of Merge Sort. Heap Sort is perfectly in-place ($O(1)$ space).
- As a fallback mechanism in algorithms like Introsort when Quicksort's recursion tree grows pathologically deep.
- In operating system schedulers (like older Linux kernels) where strict bounds on execution time and memory footprint are critical.

## Approach

Heap Sort is fundamentally an optimized version of **Selection Sort**.
In Selection Sort, we scan the entire array in `O(n)` to find the maximum element, making the total sort `O(n^2)`.
In Heap Sort, we organize the array into a **Max-Heap** data structure. A Max-Heap ensures that the absolute maximum element is always at the root (index 0). Finding the maximum is now `O(1)`.

The algorithm has two main phases:
1. **Heapify (Build Max-Heap):** Reorganize the flat array into a valid Max-Heap. This mathematically takes `O(n)` time when done bottom-up.
2. **Extract and Sort:** We swap the maximum element (at the root) with the very last element of the unsorted segment. Then, we reduce the logical size of the heap by 1, and "sift down" the new root to restore the Max-Heap property. This takes `O(log n)` time. We repeat this `n` times.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_06: Heap Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n log n) time.
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
```

</details>

## Walk-through

Let `arr = [4, 10, 3]`.

**Phase 1: Build Max-Heap**
- `n = 3`. Last non-leaf node `i = 3 // 2 - 1 = 0`.
- Call `heapify(arr, 3, 0)`:
  - `largest = 0` (value 4). Left child is index 1 (value 10). Right is index 2 (value 3).
  - 10 > 4, so `largest = 1`.
  - Swap index 0 and 1: `[10, 4, 3]`.
- Array is now a valid Max-Heap! The maximum (10) is at the root.

**Phase 2: Extract & Sort**
- **Iteration 1 (`i = 2`):**
  - Swap `arr[0]` (10) with `arr[2]` (3). Array: `[3, 4, 10]`. (10 is permanently sorted at the end!)
  - Call `heapify(arr, 2, 0)` to fix the root (3).
  - Left child is 4. `4 > 3`, swap. Array: `[4, 3, 10]`.
- **Iteration 2 (`i = 1`):**
  - Swap `arr[0]` (4) with `arr[1]` (3). Array: `[3, 4, 10]`. (4 is permanently sorted!)
  - Call `heapify(arr, 1, 0)`. Left child is out of bounds. Nothing to do.
- **Iteration 3 (`i = 0`):**
  - Loop finishes. 

Final array: `[3, 4, 10]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n log n)$ | $O(1)$ |
| **Average** | $O(n log n)$ | $O(1)$ |
| **Worst** | $O(n log n)$ | $O(1)$ |

Building the heap initially takes strict `O(n)` time. The extraction phase runs `n` times, and each `heapify` operation takes `O(log n)` time because the height of a binary heap is `log n`. Therefore, the overall time complexity is always `O(n log n)`. It is an in-place sort, requiring no extra memory, so space is `O(1)`.

## Variants & optimizations

- **Bottom-up Heapsort:** A highly optimized variant that reduces the number of comparisons. Instead of comparing children and then checking against the root during the sift-down, it blindly sifts the root all the way down to a leaf, and then sifts it back up. This cuts the number of comparisons almost in half.

## Real-world applications

- **Embedded Systems:** Perfect for sorting in environments with zero dynamic memory allocation capabilities.
- **Priority Queues:** The underlying Max-Heap structure is the exact same mechanism used for task scheduling in operating systems or pathfinding algorithms like Dijkstra's.

## Related algorithms in cOde(n)

- **[sort_02 - Selection Sort](sort_02_selection-sort.md)** — The conceptually identical, but structurally unoptimized `O(n^2)` predecessor.
- **[heap_01 - Min Heap Implementation](../heap/heap_01_min-heap.md)** — A deeper dive into the actual binary heap data structure itself.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
