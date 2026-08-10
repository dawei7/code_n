## General

**Translate subarrays into chosen start positions**

The first subarray always starts at index zero, contributing forced cost `nums[0]`. If the original requested number of subarrays is $K$, choose $K-1$ additional start indices from positions one through $N-1$.

The distance condition says the earliest and latest of those chosen later starts differ by at most `dist`. Equivalently, all $K-1$ selected indices fit inside some consecutive index window of length `dist+1`.

For one such window, the cheapest valid choice is simply its $K-1$ smallest values. Their indices can be sorted to become subarray starts. The problem becomes: over every sliding window of `nums[1:]` with length `dist+1`, find the sum of its $K-1$ smallest values, then add `nums[0]`.

The code changes `k -= 1` so local `k` means this number of later starts.

**Maintain two ordered multisets**

`l` stores exactly the smallest `k` values in the current window. `r` stores all remaining values. Both are `SortedList` multisets, so duplicates are preserved.

Variable `s` equals `nums[0] + sum(l)`. Only movements into or out of `l` change it; values in `r` are not selected costs.

The initial window is indices one through `dist+1`. The code initially places all its values in `l` and includes their sum in `s`. While `len(l) > k`, helper `l2r` moves the largest `l` value to `r` and subtracts it. Afterward, `l` contains the required smallest `k` values.

**Slide the index window**

For incoming index `i` starting at `dist+2`, outgoing index is `i - dist - 1`. Removing it from `l` also subtracts its value from `s`; removing from `r` does not.

The incoming value `y` is compared with `l[-1]`, the largest currently selected value. If smaller, it enters `l` and is added to `s`; otherwise it enters `r`.

The helpers then restore exactly `k` elements in `l`:

- `r2l` moves the smallest `r` value into `l` when `l` is short;
- `l2r` moves the largest `l` value out when it is oversized.

These boundary moves preserve the invariant that every `l` value is no greater than every `r` value.

**Why duplicate membership is safe**

The outgoing value may have equal copies in both multisets. `if x in l` removes a copy from `l` when possible. Since equal copies are indistinguishable for sums and ordering, it does not matter whether that particular physical index had conceptually belonged to `l`. Rebalancing restores the correct multiset partition with the same numeric cost.

**Why minimizing windows solves all selections**

Every valid set of later starts lies in the window from its earliest index through earliest plus `dist`, so the scan considers a window containing it. Choosing that window’s `k` smallest values costs no more.

Conversely, any `k` positions chosen from one scanned window have earliest/latest difference at most `dist` and define valid ordered subarray starts. Therefore, the minimum window cost is exactly the problem optimum.

`ans` stores the smallest `s` over the initial and all slid windows. Since `s` already includes `nums[0]`, the final return needs no additional term.

**The exact structure differs from the manifest summary**

The manifest says the implementation uses count-and-sum Fenwick trees. The protected source instead depends on `SortedList` and two ordered multisets. Both achieve $O(N\log N)$ time and $O(N)$ space, but their mechanics are different; this document follows the executable source.

**The running-sum invariant**

At every point after rebalancing, `s = nums[0] + sum(l)`. Removing or inserting in `r` leaves `s` unchanged because those values are not selected. Every transfer across the `l`/`r` boundary updates `s` by exactly the moved value. This invariant makes evaluating a window constant time once its ordered multisets are maintained.

## Complexity detail

Let $W=\texttt{dist}+1$. Initial `SortedList` construction and rebalancing cost $O(W\log W)$ in a safe bound. Each of $O(N)$ slides performs a constant number of membership, removal, insertion, and boundary-pop operations, each $O(\log W)$ for `SortedList`.

Total time is $O(N\log N)$ and auxiliary space is $O(W)$, bounded by $O(N)$. Initial slices `nums[:dist+2]` and `nums[1:dist+2]` also allocate $O(W)$ temporary lists.

## Alternatives and edge cases

- **Fenwick count/sum trees:** Coordinate-compressed trees can query the sum of the smallest `k` values and match the manifest summary, but are not the exact source.
- **Sort every window:** This costs $O(NW\log W)$ and repeats nearly identical work.
- **One min-heap:** Deleting arbitrary outgoing values and maintaining exactly the smallest `k` require lazy deletion or additional structures.
- **Duplicate values at the boundary:** Multiset storage and numeric rebalancing handle them correctly.
- **Minimum allowed `dist = K-2`:** Each legal window has just enough positional width for the required starts; the same method applies.
- **`k` after decrement:** It means later start count, not total subarray count.
- **Forced first cost:** `nums[0]` is included in `s` from initialization onward.
- **Input preservation:** Slices and sorted multisets leave `nums` unchanged.
- **Manifest mismatch:** Complexity matches, but the actual data structure is `SortedList` rather than Fenwick trees.
