# Insertion Sort

| | |
|---|---|
| **ID** | `sort_03` |
| **Category** | sorting |
| **Complexity (required)** | $O(n^2)$ |
| **Difficulty** | 2/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order using the Insertion Sort algorithm.

**Input:** An unsorted array of integers `arr`.
**Output:** The array sorted in strictly ascending order.

**Example:**
| Input `arr` | Output |
|---|---|
| `[12, 11, 13, 5, 6]` | `[5, 6, 11, 12, 13]` |

## When to use it

- **As a subroutine in modern production sorting engines** like Timsort (used in Python and Java) or Introsort (used in C++ `std::sort`). When a recursive Quicksort or Mergesort divides the array into very small chunks (typically < 16 elements), the overhead of recursion is too high, and they switch to Insertion Sort.
- When the data is **nearly sorted**. Insertion Sort operates in $O(n)$ time if the array is already mostly in order.
- When sorting a data stream arriving **online** one piece at a time.

## Approach

Insertion Sort mimics how humans sort a hand of playing cards.
We iterate over the array from left to right. At each position `i`, we consider the element `arr[i]` as the "card" we just picked up. 

Everything to the left of `i` is already sorted. We compare our "card" to the cards on its left, shifting the larger cards to the right to make room. Once we find a card smaller than our current card (or reach the start of the array), we drop our card into the newly created gap.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
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
```

</details>

## Walk-through

Let `arr = [4, 3, 2, 10, 12, 1, 5, 6]`. We will just trace the first few steps.

**Pass 1 (`i = 1`, `key = 3`):**
- Array: `[4, | 3, 2, 10, ...]`
- `arr[0]` (4) > 3, so shift 4 to the right.
- Insert 3.
- Array: `[3, 4, | 2, 10, ...]`

**Pass 2 (`i = 2`, `key = 2`):**
- Array: `[3, 4, | 2, 10, ...]`
- `arr[1]` (4) > 2, shift 4 right.
- `arr[0]` (3) > 2, shift 3 right.
- Insert 2.
- Array: `[2, 3, 4, | 10, ...]`

**Pass 3 (`i = 3`, `key = 10`):**
- Array: `[2, 3, 4, | 10, ...]`
- `arr[2]` (4) is NOT > 10. The `while` loop doesn't even run!
- Array remains: `[2, 3, 4, 10, | ...]`

*Notice that when an element is naturally larger than its sorted neighbors, it costs absolutely nothing ($O(1)$) to leave it in place. This is why Insertion Sort is so fast on nearly-sorted data.*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(1)$ |
| **Average** | $O(n^2)$ | $O(1)$ |
| **Worst** | $O(n^2)$ | $O(1)$ |

The worst-case $O(n^2)$ occurs when the array is in reverse order, meaning every new element must be shifted all the way to the beginning of the array. The best-case $O(n)$ occurs when the array is already sorted—the inner `while` loop condition `arr[j] > key` fails immediately on every pass, reducing the algorithm to a single linear $O(n)$ scan. Space is $O(1)$ in-place.

## Variants & optimizations

- **Binary Insertion Sort:** Use Binary Search to find the exact location to insert `key` in $O(log n)$ time. However, because arrays are contiguous memory structures, you still have to physically shift all the elements to the right, which remains an $O(n)$ operation per element, so the overall time complexity remains $O(n^2)$.

## Real-world applications

- **Timsort (Python / Java):** The default sorting algorithm in modern programming languages. Timsort divides massive arrays into small "runs" of ~32 to 64 elements, sorts those small chunks using Insertion Sort, and then merges them back together.
- **Introsort (C++ `std::sort`):** C++ uses Quicksort natively, but switches to Heapsort if the recursion goes too deep, and drops to Insertion Sort when the partitioned sub-arrays fall below 16 elements.

## Related algorithms in cOde(n)

- **[sort_10 - Shell Sort](sort_10_shell-sort.md)** — A brilliant optimization of Insertion Sort that compares elements spaced far apart to move them rapidly across the array, overcoming Insertion Sort's weakness of only shifting by 1.
- **[sort_13 - Timsort](sort_13_tim-sort-simplified.md)** — The production algorithm that relies on Insertion Sort as its backbone.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
