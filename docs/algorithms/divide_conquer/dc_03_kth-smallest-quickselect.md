# Kth Smallest Element (Quickselect)

| | |
|---|---|
| **ID** | `dc_03` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) |

## Problem statement

Given an unsorted integer array `nums` and an integer `k`, return the k-th smallest element in the array.
Note that it is the k-th smallest element in the sorted order, not the k-th distinct element.
You must solve it in $O(N)$ average time complexity.

*(Note: Finding the k-th **Largest** is identical; just target the index `len(nums) - k`).*

**Input:** An integer array `nums` and an integer `k`.
**Output:** An integer representing the k-th smallest element.

## When to use it

- When you need to find a specific rank (median, min, max, 10th percentile) in an array WITHOUT paying the $O(N \log N)$ cost of fully sorting it.
- **Quickselect** is the canonical "Decrease and Conquer" algorithm.

## Approach

**1. The Flaw of Full Sorting:**
If you run `nums.sort()` and return `nums[k-1]`, it takes $O(N \log N)$ time.
But we don't care about the order of the other elements! We ONLY care about the element that lands perfectly at index `k-1`.

**2. The Quicksort Partition:**
Remember how Quicksort works? You pick a "Pivot". You throw all numbers smaller than the pivot to its left, and all numbers larger to its right.
The magic property of Quicksort is that after exactly one partition, **the Pivot is locked into its absolute, final, globally sorted position!**
Let's say the Pivot lands at index `P`.
- If `P == k - 1`: We found it! The Pivot IS the k-th smallest element! We can stop immediately!
- If `P > k - 1`: The k-th smallest element MUST be somewhere in the left chunk. We completely throw away the right chunk and recurse ONLY on the left!
- If `P < k - 1`: The k-th smallest element MUST be somewhere in the right chunk. We throw away the left chunk and recurse ONLY on the right!

**3. Decrease and Conquer vs Divide and Conquer:**
Unlike Quicksort which recursively calls BOTH the left and right halves (Divide and Conquer), Quickselect throws away half the array every time.
The time taken is N + N/2 + N/4 + N/8 \dots
This geometric series converges mathematically to exactly 2N. Therefore, the average time complexity is strictly $O(N)$!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_03: Kth Smallest (Quickselect).

Quickselect: partition the array around a pivot (Lomuto-style),
then only recurse into the half that contains the kth smallest.
O(n) average case, O(n^2) worst case on pathological data.
The setup shuffles the array first to keep the worst case rare.
"""


def solve(arr, k, n):
    if k < 1 or k > n:
        return -1
    work = list(arr)
    target = k - 1  # 0-indexed

    def select(lo, hi):
        if lo == hi:
            return work[lo]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        if i == target:
            return work[i]
        if i < target:
            return select(i + 1, hi)
        return select(lo, i - 1)

    return select(0, n - 1)
```

</details>

## Walk-through

`nums = [3, 2, 1, 5, 6, 4]`, `k = 2` (2nd smallest). `target_index = 1`.

1. `quickselect(0, 5)`:
   - Random pivot: pick index 5 (value `4`).
   - `partition`:
     - Compare all to `4`.
     - `3 < 4` (swap, store=1)
     - `2 < 4` (swap, store=2)
     - `1 < 4` (swap, store=3)
     - `5`, `6` > 4 (no swap).
     - Swap pivot back to `store=3`.
     - `nums` is now `[3, 2, 1, 4, 6, 5]`. Pivot `4` is at index 3.
   - `final_pivot_index = 3`.
   - `target_index (1) < 3`. Throw away right! Recurse left.
2. `quickselect(0, 2)`: (Focusing on `[3, 2, 1]`)
   - Random pivot: pick index 1 (value `2`).
   - `partition`:
     - Compare all to `2`.
     - `nums` becomes `[1, 2, 3]`. Pivot `2` is at index 1.
   - `final_pivot_index = 1`.
   - `target_index (1) == 1`. MATCH!

Returns `nums[1]` which is `2`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N^2)$ | $O(1)$ |

Average time is $O(N)$ because the array size halves roughly each time (N + N/2 + N/4 ~= 2N).
However, if you are incredibly unlucky and the random pivot is ALWAYS the absolute maximum element, the array size decreases by exactly 1 element each time (N + N-1 + N-2 \dots). This triggers the devastating $O(N^2)$ worst-case. (Median of Medians algorithm can guarantee $O(N)$ worst-case, but is too complex for interviews).
Space complexity is $O(1)$ auxiliary space if done iteratively, or $O(\log N)$ for the recursion stack depth.

## Variants & optimizations

- **Min-Heap (Priority Queue):** The pragmatic, non-D&C alternative. Push elements into a Max-Heap of strictly size K. If the heap exceeds size K, pop the top (largest) element. At the end, the top of the heap is the k-th smallest element! Time is $O(N log K)$, which is technically worse than $O(N)$, but it avoids the $O(N^2)$ worst-case and is significantly easier to write bug-free.

## Real-world applications

- **Database Query Planners:** Used heavily in SQL databases to answer `PERCENTILE_CONT(0.5)` (finding the Median) queries across massive unstructured tables without exhausting RAM to sort the entire table.

## Related algorithms in cOde(n)

- **[sort_02 - Quick Sort](../sorting/sort_02_quick-sort.md)** — The foundation of this algorithm, which recurses on BOTH halves.
- **[heap_01 - Kth Largest Element](../heap/heap_01_kth-largest.md)** — The alternative $O(N log K)$ approach using a Priority Queue.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
