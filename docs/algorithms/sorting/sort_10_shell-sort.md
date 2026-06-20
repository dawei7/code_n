# Shell Sort

| | |
|---|---|
| **ID** | `sort_10` |
| **Category** | sorting |
| **Complexity (required)** | $O(N^{4/3})$ Time, $O(1)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 1/10 |
| **Wikipedia** | [Shellsort](https://en.wikipedia.org/wiki/Shellsort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order.
You must use an in-place algorithm that drastically improves upon the terrible $O(N^2)$ performance of Insertion Sort, without the recursive space overhead of Merge/Quick sort.

**Input:** An unsorted array of integers `arr`.
**Output:** A sorted array (modified in-place).

## When to use it

- Primarily of historical and academic interest.
- Used in embedded systems where the memory stack is too small for recursion (ruling out Quicksort), but the array is too large for $O(N^2)$ Insertion Sort.

## Approach

**1. The Fatal Flaw of Insertion Sort (`sort_03`):**
Insertion Sort is incredibly fast if an array is *almost sorted*. Its fatal flaw is that elements can only shift ONE index at a time. If the absolute smallest element `1` is trapped at the very end of an array of size 1000, Insertion Sort requires 999 separate swap operations just to slowly drag it to index 0!

**2. The "Gap" Strategy (Donald Shell, 1959):**
Instead of comparing elements that are strictly adjacent (`gap = 1`), what if we compare elements that are extremely far apart (`gap = N/2`)?
We run a modified Insertion Sort that skips across the array in massive jumps. This allows small elements trapped at the end to instantly fly to the front of the array in a single swap!
Once the array is "roughly" sorted by the massive gap, we shrink the gap! `gap = gap / 2`. We run Insertion Sort again.
Finally, we run the algorithm with `gap = 1`. Because the array is already practically sorted by the previous passes, the final $O(N^2)$ Insertion Sort hits its best-case scenario and executes in strictly $O(N)$ linear time!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_10: Shell Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n²) time.
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
```

</details>

## Walk-through

`arr = [23, 29, 15, 19, 31, 7, 9, 5, 2]`. Length `9`.
`gap = 9 // 2 = 4`.

**Pass 1 (`gap = 4`):**
Sub-arrays being sorted:
- `[23, 31, 2]` (indices 0, 4, 8) -> Sorts to `[2, 23, 31]`! The `2` jumped 8 spaces instantly!
- `[29, 7]` (indices 1, 5) -> Sorts to `[7, 29]`.
- `[15, 9]` (indices 2, 6) -> Sorts to `[9, 15]`.
- `[19, 5]` (indices 3, 7) -> Sorts to `[5, 19]`.
Array is now: `[2, 7, 9, 5, 23, 29, 15, 19, 31]`. (Roughly sorted!)

**Pass 2 (`gap = 4 // 2 = 2`):**
Sub-arrays:
- `[2, 9, 23, 15, 31]` -> Sorts to `[2, 9, 15, 23, 31]`.
- `[7, 5, 29, 19]` -> Sorts to `[5, 7, 19, 29]`.
Array is now: `[2, 5, 9, 7, 15, 19, 23, 29, 31]`. (Very close to perfectly sorted!)

**Pass 3 (`gap = 2 // 2 = 1`):**
Standard Insertion Sort.
Only `7` and `9` need to swap! Everything else is already in position.
Array is sorted! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(1)$ |
| **Average** | $O(N^{4/3})$ or $O(N^{3/2})$ | $O(1)$ |
| **Worst** | $O(N^2)$ | $O(1)$ |

The complexity of Shell Sort is notoriously difficult to calculate mathematically because it strictly depends on the "Gap Sequence" chosen.
The classic Shell sequence (`N/2, N/4, N/8...`) is actually quite terrible, yielding an $O(N^2)$ worst-case.
If the **Hibbard Sequence** (2^k - 1 -> 1, 3, 7, 15...) is used, the worst-case drops mathematically to $O(N^{3/2})$.
If the **Sedgewick Sequence** (4^k + 3 \cdot 2^{k-1} + 1) is used, the worst case drops incredibly to $O(N^{4/3})$.
Space complexity is unconditionally $O(1)$ constant time as it strictly swaps elements in-place.

## Variants & optimizations

- **Knuth Gap Sequence:** h = 3h + 1 -> 1, 4, 13, 40, 121... A very popular and easy-to-implement sequence that yields $O(N^{3/2})$ performance.

## Real-world applications

- **uClibc (Micro C Library):** Used in the standard `qsort()` implementation for embedded Linux systems. The library prefers Shell Sort over Quicksort because embedded system memory stacks are too small to risk a deep recursion blowup, and the code size of Shell Sort is unbelievably tiny.

## Related algorithms in cOde(n)

- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — The fundamental building block that Shell Sort aggressively optimizes.
- **[sort_13 - Tim Sort](sort_13_tim-sort-simplified.md)** — The modern, superior algorithm for exploiting partially-sorted data using Insertion Sort.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
