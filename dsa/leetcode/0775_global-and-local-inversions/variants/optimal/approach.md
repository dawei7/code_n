## General
**Look only for a nonlocal inversion**

Every local inversion is already included in the global count. The counts are equal exactly when no inversion spans two or more positions. For each possible right endpoint `j`, compare `nums[j]` with the maximum value among indices `0` through $j - 2$.

**Maintain the earlier-prefix maximum**

Scan `j` from `2` onward. Before testing `nums[j]`, extend `prefix_maximum` to include `nums[j - 2]`. If `prefix_maximum > nums[j]`, some earlier index at distance at least two forms a nonlocal inversion, so return false. If no test fails, every inversion must be adjacent.

The prefix maximum represents all and only values eligible to form a nonlocal inversion ending at `j`. A failed comparison directly exhibits such an inversion. If every comparison passes, no pair separated by at least one intermediate position is inverted, leaving local pairs as the only possible global inversions. Therefore the inversion counts are equal.

## Complexity detail
The scan processes each element at most once, taking $O(n)$ time. It stores only the running maximum, for $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Displacement test:** For a permutation, the condition is equivalent to `abs(nums[i] - i) <= 1` for every index, also giving $O(n)$ time and $O(1)$ space.
- **Merge-sort inversion count:** Count global inversions in $O(n \log n)$ time and compare with the adjacent count, but this solves a harder problem than needed.
- **Check every pair:** Direct global inversion counting is correct but takes $O(n^2)$ time.
- **One or two elements:** Every possible inversion is local, so return true.
- **Increasing permutation:** Both inversion counts are zero.
- **Disjoint adjacent swaps:** All inversions remain local.
- **Any long-distance drop:** One witness is enough to return false immediately.
