# Minimum Time For K Virus Variants to Spread

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1956 |
| Difficulty | Hard |
| Topics | Array, Math, Binary Search, Geometry, Sliding Window, Enumeration, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/) |

## Problem Description
### Goal
There are $N$ distinct virus variants on an infinite integer grid. Variant
$i$ begins at `points[i]` on day zero; multiple distinct variants may share
the same starting coordinate.

On each following day, every infected grid cell spreads each variant it
contains to its four cardinally adjacent cells. Variants spread independently,
even when several occupy the same cell. Given `k`, return the earliest integer
day on which some grid point contains at least `k` distinct variants.

### Function Contract
**Inputs**

- `points`: a list of $N$ coordinate pairs, where $2\le N\le50$ and every
  coordinate is between $1$ and $100$, inclusive. Define
  $X=\max_i x_i-\min_i x_i+1$ and
  $Y=\max_i y_i-\min_i y_i+1$.
- `k`: the required number of variants, where $2\le k\le N$.

**Return value**

- The minimum nonnegative number of days after which at least one integer grid
  point contains at least `k` variants.

### Examples
**Example 1**

- Input: `points = [[1, 1], [6, 1]], k = 2`
- Output: `3`

**Example 2**

- Input: `points = [[3, 3], [1, 2], [9, 2]], k = 2`
- Output: `2`

**Example 3**

- Input: `points = [[3, 3], [1, 2], [9, 2]], k = 3`
- Output: `4`
