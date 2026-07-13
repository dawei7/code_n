# Kth Smallest Element in a Sorted Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 378 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) |

## Problem Description
### Goal
Given an $n \times n$ integer matrix whose rows and columns are each sorted in ascending order, consider the multiset of all $n^{2}$ cell values arranged from smallest to largest. Duplicate values at different cells occupy separate positions, so the task asks for the `k`th smallest element in sorted order, not the `k`th distinct element.

Return the value at the valid one-based rank `k`, rather than its coordinates or a sorted matrix. Use the two-dimensional ordering and meet the memory constraint instead of flattening and fully sorting every cell. For $k = 1$ return a minimum; for $k = n^{2}$ return a maximum.

### Function Contract
**Inputs**

- `matrix`: an $n \times n$ integer matrix sorted nondecreasing across every row and column
- `k`: a one-based rank between `1` and $n^{2}$

**Return value**

- The value at rank `k` in the multiset of all matrix entries.

### Examples
**Example 1**

- Input: `matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8`
- Output: `13`

**Example 2**

- Input: `matrix = [[-5]], k = 1`
- Output: `-5`

**Example 3**

- Input: `matrix = [[1,2],[1,3]], k = 2`
- Output: `1`

### Required Complexity

- **Time:** $O(n \log R)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Binary-search the answer value, not a matrix coordinate**

The smallest possible answer is the top-left value and the largest is the bottom-right value. For a candidate midpoint, count how many matrix entries are at most that value. If the count is at least `k`, the k-th value is no larger than the midpoint; otherwise it is larger. This monotone predicate supports binary search across the numeric range.

**Count a threshold with one staircase walk**

Start at the bottom-left cell. If `matrix[row][col] <= threshold`, every entry above it in the same column is also small enough, so add `row + 1` and move right. Otherwise the current bottom value is too large, so move up. Each move eliminates one row or column from further consideration, producing the count in $O(n)$ time.

**Why the converged value is the k-th smallest**

The predicate “at least `k` entries are at most this value” is false below the k-th multiset value and true at that value and above. Binary search retains the first value where the predicate becomes true. Duplicate entries are included separately in the staircase count, so the transition corresponds to multiset rank rather than distinct-value rank.

**Trace the cutoff**

In the first example, a threshold of `12` covers seven entries, while threshold `13` covers nine. Rank eight therefore lies at value `13`, and binary search converges there even though thirteen appears twice.

#### Complexity detail

Let `R = matrix[n - 1][n - 1] - matrix[0][0] + 1` be the inclusive value range. Binary search performs $O(\log R)$ threshold checks, each using an $O(n)$ staircase walk, for $O(n \log R)$ time. Only scalar boundaries and staircase indices are stored, using $O(1)$ space.

#### Alternatives and edge cases

- **Flatten and sort:** costs $O(n^2 \log n)$ time and $O(n^2)$ storage.
- **Merge rows with a min-heap:** returns the first `k` values in $O(k \log n)$ time and $O(n)$ space.
- **Scan every cell at each threshold:** keeps value binary search but costs $O(n^2 \log R)$ by ignoring column order.
- Duplicate values each consume one rank.
- A one-cell matrix returns its sole value.
- Negative values work because the binary search uses ordinary ordered integers.
- The first and last ranks return the matrix's global minimum and maximum.

</details>
