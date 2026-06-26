# Matrix Diagonal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1572 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [matrix-diagonal-sum](https://leetcode.com/problems/matrix-diagonal-sum/) |

## Problem Description & Examples
### Goal
Sum the values on both diagonals of a square matrix, counting the center only
once when the matrix size is odd.

### Function Contract
**Inputs**

- `mat`: an `n x n` integer matrix.

**Return value**

The sum of all primary and secondary diagonal cells.

### Examples
**Example 1**

- Input: `mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `25`

**Example 2**

- Input: `mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]`
- Output: `8`

**Example 3**

- Input: `mat = [[5]]`
- Output: `5`

---

## Underlying Base Algorithm(s)
For each row `i`, add `mat[i][i]` and `mat[i][n - 1 - i]`. If both indices are
the same center cell, add it only once.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.
