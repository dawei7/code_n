## General
**Binary-search the answer value, not a matrix coordinate**

The smallest possible answer is the top-left value and the largest is the bottom-right value. For a candidate midpoint, count how many matrix entries are at most that value. If the count is at least `k`, the k-th value is no larger than the midpoint; otherwise it is larger. This monotone predicate supports binary search across the numeric range.

**Count a threshold with one staircase walk**

Start at the bottom-left cell. If `matrix[row][col] <= threshold`, every entry above it in the same column is also small enough, so add `row + 1` and move right. Otherwise the current bottom value is too large, so move up. Each move eliminates one row or column from further consideration, producing the count in $O(n)$ time.

**Why the converged value is the k-th smallest**

The predicate “at least `k` entries are at most this value” is false below the k-th multiset value and true at that value and above. Binary search retains the first value where the predicate becomes true. Duplicate entries are included separately in the staircase count, so the transition corresponds to multiset rank rather than distinct-value rank.

**Trace the cutoff**

In the first example, a threshold of `12` covers seven entries, while threshold `13` covers nine. Rank eight therefore lies at value `13`, and binary search converges there even though thirteen appears twice.

## Complexity detail
Let `R = matrix[n - 1][n - 1] - matrix[0][0] + 1` be the inclusive value range. Binary search performs $O(\log R)$ threshold checks, each using an $O(n)$ staircase walk, for $O(n \log R)$ time. Only scalar boundaries and staircase indices are stored, using $O(1)$ space.

## Alternatives and edge cases
- **Flatten and sort:** costs $O(n^2 \log n)$ time and $O(n^2)$ storage.
- **Merge rows with a min-heap:** returns the first `k` values in $O(k \log n)$ time and $O(n)$ space.
- **Scan every cell at each threshold:** keeps value binary search but costs $O(n^2 \log R)$ by ignoring column order.
- Duplicate values each consume one rank.
- A one-cell matrix returns its sole value.
- Negative values work because the binary search uses ordinary ordered integers.
- The first and last ranks return the matrix's global minimum and maximum.
