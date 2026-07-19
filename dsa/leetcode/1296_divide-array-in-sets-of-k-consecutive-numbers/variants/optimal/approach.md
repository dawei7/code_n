## General
**Why the smallest unused value fixes a group start**

Count every value and process distinct values in ascending order. Suppose `start` is the smallest value whose remaining frequency is positive. It cannot be placed later inside a consecutive set: that would require a still-smaller unused predecessor, contradicting the choice of `start`. Therefore every remaining copy of `start` must begin a set.

Let `copies = counts[start]`. Those `copies` sets each need one occurrence of every value from `start` through `start + k - 1`. If any required frequency is below `copies`, no valid partition can exist. Otherwise subtract `copies` from all of those frequencies at once.

Processing starts from left to right never takes a value needed by an earlier undecided set, because all sets beginning at smaller values have already been forced and removed. If every subtraction succeeds, all occurrences have been assigned to valid sets, so the partition exists. A preliminary divisibility check rejects lengths that cannot be split into equal groups.

## Complexity detail
Building the frequency map takes $O(n)$ time. Sorting at most $n$ distinct keys costs $O(n \log n)$. Across all positive starts, the bulk-subtraction loops perform at most $n$ value visits because each such visit accounts for at least one consumed occurrence. The frequency map and sorted keys use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Min-heap of distinct values:** Repeatedly extracting the current minimum can implement the same greedy rule, but heap operations add bookkeeping without improving the $O(n \log n)$ bound.
- **Repeated minimum-map scans:** Finding the smallest remaining key by scanning the entire map is correct, but it can degrade to $O(n^2)$.
- **Length not divisible by `k`:** A partition is impossible before any frequency work begins.
- **Duplicate values:** All remaining copies of the smallest value must start separate sets simultaneously; subtracting their full frequency enforces this.
- **`k = 1`:** Every element forms a valid singleton set.
- **Missing successor:** A gap or insufficient successor frequency makes the required subtraction fail immediately.
