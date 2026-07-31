## General

The matrix is not globally sorted, but row ordering makes it possible to count how many values are at most a proposed answer without visiting every cell.

**Binary-search the value.** The median lies between the smallest row-first value and the largest row-last value. For a probe `middle`, use an upper-bound search in each row to find the number of entries less than or equal to `middle`. Summing those positions gives the probe's global rank count.

Let `target = (m * n) // 2 + 1`, the one-based median rank. If fewer than `target` entries are at most the probe, the median is larger. Otherwise the probe may be the median or lie above it, so keep it as the upper boundary.

This lower-bound search terminates at the smallest value with at least `target` matrix entries not greater than it. That definition is exactly the value occupying the median rank, including when duplicates straddle the middle.

## Complexity detail

Let $V$ be the inclusive difference between the greatest and smallest candidate values plus one. Each value probe performs $m$ binary searches over rows of length $n$, taking $O(m\log n)$ time. There are $O(\log V)$ probes, for $O(m\log n\log V)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Flatten and sort:** Sorting all $mn$ entries costs $O(mn\log(mn))$ and violates the required sub-$O(mn)$ bound.
- **Linear counting per probe:** Value-space binary search with a full matrix scan takes $O(mn\log V)$ and does not exploit row ordering sufficiently.
- **Heap merge:** Merging sorted rows until the median costs $O(mn\log m)$ in the worst case.
- **Duplicate median:** Use upper-bound counts so repeated values occupy their complete set of ranks.
- **One row:** The method still returns the ordinary middle element without special handling.
- **Disjoint row ranges:** Only the total count matters; rows do not need overlapping values or sorted columns.
