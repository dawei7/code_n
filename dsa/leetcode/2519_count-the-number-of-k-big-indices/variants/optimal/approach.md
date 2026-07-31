## General

For each index, the required information is an order statistic on each side: how many earlier values and how many later values are strictly smaller than the current value. Recounting either side from scratch would repeat most comparisons.

Because every value lies between `1` and $n$, use the value itself as a one-based coordinate in a Fenwick tree. A prefix query through `value - 1` counts previously inserted values that are strictly smaller; stopping before `value` is what excludes duplicates. A point update at `value` records the current element for later queries.

Scan left to right first and store the smaller-left count for every index. Then reset the tree and scan right to left. Before inserting the current value, query its smaller-right count. The index is `k`-big exactly when the stored left count and the current right count are both at least `k`.

A Fenwick node stores the frequency total for a power-of-two range. Updating by `index += index & -index` visits every containing range, while querying by `index -= index & -index` combines disjoint ranges covering the requested prefix. These operations therefore return exact frequency counts and take logarithmic time.

## Complexity detail

Let $n$ be the length of `nums`. Each element performs one Fenwick query and one update in each of two scans, and each operation costs $O(\log n)$, giving $O(n \log n)$ total time. The Fenwick tree and stored left counts each use $O(n)$ space.

## Alternatives and edge cases

- **Direct side scans:** Counting smaller elements before and after every index is straightforward but takes $O(n^2)$ time.
- **Merge-sort counting:** Modified merge sorts can count smaller values on each side in $O(n \log n)$ time, but require more intricate index bookkeeping.
- Query through `nums[i] - 1`, not `nums[i]`, because equal values are not strictly smaller.
- Indices with fewer than `k` positions on either side can never qualify, regardless of the values.
- A monotone increasing array has no qualifying index because no later value is smaller; the reverse argument applies to a decreasing array's left side.
