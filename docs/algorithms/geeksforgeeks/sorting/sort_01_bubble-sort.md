# Bubble Sort

| | |
|---|---|
| **ID** | `sort_01` |
| **Category** | sorting |
| **Complexity (required)** | $O(n^2)$ |
| **Difficulty** | 1/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order using the Bubble Sort algorithm.

**Input:** An unsorted array of integers `arr`.
**Output:** The array sorted in strictly ascending order.

**Example:**
| Input `arr` | Output |
|---|---|
| `[64, 34, 25, 12, 22, 11, 90]` | `[11, 12, 22, 25, 34, 64, 90]` |

## When to use it

- **Never** in production. It is famous for being incredibly inefficient.
- In computer science 101 classes as a pedagogical tool to introduce the concepts of algorithmic complexity and swapping.
- When you are absolutely certain the array is almost fully sorted, a slightly optimized Bubble Sort can finish in $O(n)$ time, though Insertion Sort handles this scenario much better.

## Approach

Bubble Sort is named for the way larger elements "bubble" up to the top (the end) of the array.
We iterate through the array, comparing adjacent elements. If the left element is larger than the right element, we swap them.

By doing this across the entire array, the absolute largest element is guaranteed to be pushed all the way to the last index. 
We then repeat this process for the remaining `n-1` elements, then the remaining `n-2` elements, until no more swaps are needed.

**Optimization:** If we make a full pass through the array and don't make a single swap, it means the array is already perfectly sorted, and we can immediately break out of the loop.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
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
```

</details>

## Walk-through

Let `arr = [5, 1, 4, 2]`.

**Pass 1 (`i=0`):**
- Compare `5` and `1`: `5 > 1`. Swap. `[1, 5, 4, 2]`
- Compare `5` and `4`: `5 > 4`. Swap. `[1, 4, 5, 2]`
- Compare `5` and `2`: `5 > 2`. Swap. `[1, 4, 2, 5]`
*The largest element `5` has bubbled to the end.*

**Pass 2 (`i=1`):**
*(We only need to check up to the second-to-last element)*
- Compare `1` and `4`: `1 < 4`. No swap. `[1, 4, 2, 5]`
- Compare `4` and `2`: `4 > 2`. Swap. `[1, 2, 4, 5]`
*The second-largest element `4` has bubbled to its correct spot.*

**Pass 3 (`i=2`):**
- Compare `1` and `2`: `1 < 2`. No swap. `[1, 2, 4, 5]`
*No swaps were made in this pass! `swapped = False`. We break early.*

Final array: `[1, 2, 4, 5]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(1)$ |
| **Average** | $O(n^2)$ | $O(1)$ |
| **Worst** | $O(n^2)$ | $O(1)$ |

The time complexity is dominated by the nested loops. The outer loop runs `n` times, and the inner loop runs up to `n` times, resulting in `n * (n - 1) / 2` comparisons, making it $O(n^2)$. The Best Case $O(n)$ occurs when the array is already sorted and our `swapped` optimization breaks the loop after the first pass. Space is strictly $O(1)$ as swaps happen in-place.

## Variants & optimizations

- **Cocktail Shaker Sort:** A bidirectional variant of Bubble Sort. Instead of only bubbling the largest items rightwards, it bubbles the largest item rightwards, and then bubbles the smallest item leftwards on the return journey. This slightly reduces the number of passes but remains $O(n^2)$.

## Real-world applications

- None. Almost every modern library implementation of sorting (like Java's `Arrays.sort` or Python's `sort()`) uses Timsort, Quicksort, or Merge Sort. For small arrays, Insertion Sort is definitively preferred over Bubble Sort due to vastly lower constant factors.

## Related algorithms in cOde(n)

- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — A much better $O(n^2)$ algorithm that is actually used in production as a subroutine for small array segments.
- **[sort_02 - Selection Sort](sort_02_selection-sort.md)** — Another $O(n^2)$ pedagogical sort that minimizes the total number of swaps to exactly `n`.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
