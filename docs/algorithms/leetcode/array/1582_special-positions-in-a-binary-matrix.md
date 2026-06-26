# Special Positions in a Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1582 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [special-positions-in-a-binary-matrix](https://leetcode.com/problems/special-positions-in-a-binary-matrix/) |

## Problem Description & Examples
### Goal
Count cells containing `1` whose row and column each contain no other `1`.

### Function Contract
**Inputs**

- `mat`: a binary matrix.

**Return value**

The number of special positions.

### Examples
**Example 1**

- Input: `mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]`
- Output: `1`

**Example 2**

- Input: `mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]`
- Output: `3`

**Example 3**

- Input: `mat = [[0, 0], [0, 0]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Precompute the number of ones in each row and each column. Then scan every cell;
cell `(r, c)` is special exactly when `mat[r][c] == 1`, `row_count[r] == 1`,
and `col_count[c] == 1`.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`.
- **Space Complexity**: `O(m + n)`.
