# Find the Minimum Area to Cover All Ones I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3195 |
| Difficulty | Medium |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/) |

## Problem Description
### Goal
You are given a two-dimensional binary array `grid`. Choose a rectangle whose
sides are horizontal and vertical and which contains every cell whose value is
`1`. Cells containing `0` may also lie inside the rectangle.

Among all such rectangles, return the smallest possible area. The input always
contains at least one `1`, so a nonempty covering rectangle is guaranteed to
exist.

### Function Contract
**Inputs**

- `grid`: A rectangular matrix of binary integers. Its row count $R$ and
  column count $C$ satisfy $1 \le R,C \le 1000$, and every entry is either
  `0` or `1`.

At least one cell of `grid` has value `1`.

**Return value**

The minimum area of an axis-aligned rectangle containing every `1` in the
matrix.

### Examples
**Example 1**

- Input: `grid = [[0, 1, 0], [1, 0, 1]]`
- Output: `6`

The ones span both rows and all three columns, producing a rectangle of
height `2`, width `3`, and area `6`.

**Example 2**

- Input: `grid = [[1, 0], [0, 0]]`
- Output: `1`

Only the upper-left cell must be covered, so a one-cell rectangle is enough.
