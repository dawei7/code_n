# Check if Matrix Is X-Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2319 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [check-if-matrix-is-x-matrix](https://leetcode.com/problems/check-if-matrix-is-x-matrix/) |

## Problem Description & Examples
### Goal
Check whether every cell on either diagonal of a square matrix is nonzero and every cell off both diagonals is zero.

### Function Contract
**Inputs**

- `grid`: a square integer matrix.

**Return value**

`true` if the matrix has the required X pattern; otherwise `false`.

### Examples
**Example 1**

- Input: `grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]`
- Output: `true`

**Example 2**

- Input: `grid = [[5, 7, 0], [0, 3, 1], [0, 5, 0]]`
- Output: `false`

**Example 3**

- Input: `grid = [[9]]`
- Output: `true`

---

## Underlying Base Algorithm(s)
For each `(row, column)`, it lies on the X when `row == column` or `row + column == n - 1`. Require nonzero exactly in that case and zero otherwise; reject the first violation.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)`
