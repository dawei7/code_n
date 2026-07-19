# Minimum Operations to Make a Uni-Value Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2033 |
| Difficulty | Medium |
| Topics | Array, Math, Sorting, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/) |

## Problem Description

### Goal

An integer grid has $M$ rows and $N$ columns. In one operation, choose one cell
and either add `x` to its value or subtract `x` from it. Operations affect only
the selected cell and may be repeated.

Make every grid cell contain the same integer using as few operations as
possible. Return that minimum count when a common value is reachable; if the
step size prevents some cells from ever becoming equal, return `-1`.

### Function Contract

Let $P = MN$ be the number of cells.

**Inputs**

- `grid`: a nonempty $M$-by-$N$ rectangular integer matrix with
  $1 \le P \le 10^5$ and cell values from $1$ through $10^4$.
- `x`: the positive amount added or subtracted by one operation, where
  $1 \le x \le 10^4$.

**Return value**

- The minimum operation count needed to make all $P$ values equal, or `-1`
  when no common value is reachable.

### Examples

**Example 1**

- Input: `grid = [[2, 4], [6, 8]], x = 2`
- Output: `4`
- Explanation: Targeting `4` costs one operation for `2`, none for `4`, one
  for `6`, and two for `8`.

**Example 2**

- Input: `grid = [[1, 5], [2, 3]], x = 1`
- Output: `5`

**Example 3**

- Input: `grid = [[1, 2], [3, 4]], x = 2`
- Output: `-1`
