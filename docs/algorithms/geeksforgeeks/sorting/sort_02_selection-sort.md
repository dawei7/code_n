# Selection Sort

| | |
|---|---|
| **ID** | `sort_02` |
| **Category** | sorting |
| **Complexity (required)** | $O(n^2)$ |
| **Difficulty** | 2/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Selection sort](https://en.wikipedia.org/wiki/Selection_sort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order using the Selection Sort algorithm.

**Input:** An unsorted array of integers `arr`.
**Output:** The array sorted in strictly ascending order.

**Example:**
| Input `arr` | Output |
|---|---|
| `[64, 25, 12, 22, 11]` | `[11, 12, 22, 25, 64]` |

## When to use it

- When writing memory to flash storage or EEPROMs where **write operations are incredibly expensive or degrade the hardware**, and read operations are practically free. Selection Sort makes the absolute minimum possible number of writes/swaps: exactly $O(n)$.
- As a pedagogical tool to teach quadratic algorithmic complexity.

## Approach

The array is logically divided into two parts:
1. The sorted part at the front.
2. The unsorted part at the back.

Initially, the sorted part is empty, and the unsorted part is the entire array.
We scan the entire unsorted part to find the absolute minimum element. Once we find it, we swap it with the leftmost element of the unsorted part, which effectively grows our sorted part by 1.

We repeat this process: find the minimum of the remaining elements, place it at the front of the remaining elements, and so on.

Unlike Bubble Sort, which rapidly swaps adjacent elements throughout the array, Selection Sort only does exactly one swap per pass.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
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
```

</details>

## Walk-through

Let `arr = [29, 10, 14, 37, 13]`.

**Pass 1 (`i = 0`):**
- Unsorted range: `[29, 10, 14, 37, 13]`
- Minimum found: `10` (at index 1)
- Swap `arr[0]` (29) with `arr[1]` (10).
- Array is now: `[10, 29, 14, 37, 13]`

**Pass 2 (`i = 1`):**
- Unsorted range: `[29, 14, 37, 13]`
- Minimum found: `13` (at index 4)
- Swap `arr[1]` (29) with `arr[4]` (13).
- Array is now: `[10, 13, 14, 37, 29]`

**Pass 3 (`i = 2`):**
- Unsorted range: `[14, 37, 29]`
- Minimum found: `14` (at index 2)
- Swap: None needed (min_idx == i).
- Array is now: `[10, 13, 14, 37, 29]`

**Pass 4 (`i = 3`):**
- Unsorted range: `[37, 29]`
- Minimum found: `29` (at index 4)
- Swap `arr[3]` (37) with `arr[4]` (29).
- Array is now: `[10, 13, 14, 29, 37]`

The final element is naturally in the correct place. Array sorted! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n^2)$ | $O(1)$ |
| **Average** | $O(n^2)$ | $O(1)$ |
| **Worst** | $O(n^2)$ | $O(1)$ |

The time complexity is strictly $O(n^2)$ in all cases (Best, Average, Worst). Even if the array is already perfectly sorted, Selection Sort must still scan the entire unsorted remainder of the array during every pass just to *verify* that the current element is the minimum. This makes it heavily inferior to Insertion Sort for nearly-sorted data. Space is $O(1)$ in-place.

## Variants & optimizations

- **Bingo Sort:** An optimized version of Selection Sort where items with identical values are grouped and moved together.
- **Heap Sort:** Conceptually, Heap Sort is just an optimized Selection Sort! Instead of taking $O(n)$ to linearly scan for the minimum during each pass, Heap Sort uses a Binary Heap data structure to find the minimum in $O(1)$ time and update the remaining heap in $O(log n)$ time, drastically reducing the overall time complexity from $O(n^2)$ to $O(n log n)$.

## Real-world applications

- Extremely constrained embedded microcontrollers where flash memory writes wear down the hardware. Selection Sort guarantees exactly `n` writes (swaps) to sort the array, the absolute theoretical minimum for an in-place sort.

## Related algorithms in cOde(n)

- **[sort_06 - Heap Sort](sort_06_heap-sort.md)** — The massively optimized $O(n log n)$ spiritual successor to Selection Sort.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
