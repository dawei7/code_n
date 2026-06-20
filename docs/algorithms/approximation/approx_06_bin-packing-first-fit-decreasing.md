# Bin Packing (First Fit Decreasing)

| | |
|---|---|
| **ID** | `approx_06` |
| **Category** | approximation |
| **Complexity (required)** | $O(N \log N)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 5/10 |
| **Wikipedia** | [Bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem) |

## Problem statement

Given N items of different weights and an infinite supply of bins each with maximum capacity C, find the **minimum number of bins** required to pack all the items.
This is a classic NP-Hard problem. You must implement the **First Fit Decreasing (FFD)** algorithm, which is guaranteed to use no more than exactly \frac{11}{9} OPT + 1 bins (an incredibly tight approximation ratio of ~1.22!).

**Input:** A list of item `weights` and a bin `capacity` C.
**Output:** An integer representing the minimum number of bins used.

## When to use it

- To pack data packets into fixed-size network MTU frames.
- To schedule tasks of varying durations onto identical machines where each machine is only available for an 8-hour shift.

## Approach

A naive greedy approach (First Fit) just looks at items in the order they are given and shoves them into the first bin that has enough room. If no bin has room, it opens a new bin. This provides a 1.7 approximation.
We can dramatically improve this by doing one simple thing: **Sort the items from largest to smallest first!**

**First Fit Decreasing (FFD):**
If we place the massive, hard-to-fit items first, they will naturally claim their own bins. Then, the tiny items will perfectly slot into the "leftover" gaps of those already-opened bins!

1. Sort the items in **descending** order.
2. Maintain a list of currently open bins, initialized to empty. Each bin tracks its *remaining capacity*.
3. Iterate through the sorted items:
   - For each item, linearly scan the list of open bins from left to right (First Fit).
   - If a bin has `remaining_capacity >= item_weight`, put the item in that bin, update its capacity, and break the scan loop.
   - If NO open bin has enough room, open a brand new bin, put the item in it, and add it to the list of open bins.
4. Return the total number of open bins.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for approx_06: Bin Packing (First-Fit Decreasing).

Given a list of item sizes in (0, 1] and unit-
"""


def solve(sizes, n):
    """First-Fit Decreasing bin packing."""
    if n == 0:
        return 0
    # Sort items by size descending.
    items = sorted(sizes, reverse=True)
    bins = []  # each entry is the remaining capacity of a bin
    for s in items:
        placed = False
        for i in range(len(bins)):
            if bins[i] >= s:
                bins[i] -= s
                placed = True
                break
        if not placed:
            bins.append(1.0 - s)
    return len(bins)
```

</details>

## Walk-through

`weights = [2, 5, 4, 7, 1, 3, 8]`, `capacity = 10`.

1. **Sort Descending:** `[8, 7, 5, 4, 3, 2, 1]`.
2. **Iterate:**
   - `8`: No bins. Open Bin 1. `bins = [2]`.
   - `7`: Bin 1 has 2 left. Too small. Open Bin 2. `bins = [2, 3]`.
   - `5`: Bin 1(2), Bin 2(3) too small. Open Bin 3. `bins = [2, 3, 5]`.
   - `4`: Bin 1(2), Bin 2(3) too small. Fits in Bin 3! `bins = [2, 3, 1]`.
   - `3`: Bin 1(2) too small. Fits in Bin 2! `bins = [2, 0, 1]`.
   - `2`: Fits in Bin 1! `bins = [0, 0, 1]`.
   - `1`: Bin 1(0), Bin 2(0). Fits in Bin 3! `bins = [0, 0, 0]`.

Output: `3` bins. ✓
*(Notice how the smaller items 4, 3, 2, 1 perfectly backfilled the gaps left by the large items! If we had processed them in ascending order, we would have wasted massive amounts of space).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N^2)$ | $O(N)$ |
| **Worst** | $O(N^2)$ | $O(N)$ |

Sorting takes $O(N \log N)$. In the worst case (where every item forces a new bin to be opened), the inner loop scans 1, then 2, then 3... bins, resulting in $O(N^2)$ time complexity.
Space complexity is $O(N)$ because in the worst case we might open exactly N bins.

## Variants & optimizations

- **$O(N \log N)$ FFD via Segment Trees:** The $O(N^2)$ scan can be optimized to $O(\log N)$ per item using a Segment Tree! The Segment Tree stores the *maximum available space* in any bin in a given range. When placing an item, we use the Segment Tree to binary search for the first bin (furthest left leaf) that has a max space \ge item weight! This drops the total time of FFD to strictly $O(N \log N)$.
- **Best Fit Decreasing (BFD):** Instead of picking the *first* bin that fits, pick the bin that will have the *tightest remaining space* after placing the item (leaving the smallest gap). It has the exact same \frac{11}{9} approximation bound as FFD, but performs slightly better in empirical tests.

## Real-world applications

- **Cloud Computing:** Packing Virtual Machines (items with RAM requirements) onto physical hypervisor servers (bins with RAM capacity).
- **Logistics:** Loading variable-sized boxes onto standard shipping pallets.

## Related algorithms in cOde(n)

- **[segment_tree_01 - Point Update](../segment_tree/segtree_01_point-update-range-query.md)** — The data structure required to optimize this algorithm's inner scan loop to $O(\log N)$.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
