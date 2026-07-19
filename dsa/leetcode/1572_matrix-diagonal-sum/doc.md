# Matrix Diagonal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1572 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/matrix-diagonal-sum/) |

## Problem Description
### Goal

Given a square matrix `mat`, add every value on its primary diagonal, whose cells run from the top-left to the bottom-right, and every value on its secondary diagonal, whose cells run from the top-right to the bottom-left.

When the matrix dimension is odd, the two diagonals share the center cell. Include that value only once. Return the resulting diagonal sum; values outside the two diagonals do not contribute.

### Function Contract
**Inputs**

- `mat`: An $N \times N$ integer matrix, where $1 \le N \le 100$ and $1 \le \texttt{mat[i][j]} \le 100$.

**Return value**

Return the sum of all cells `(i, i)` and `(i, N - 1 - i)`, counting a shared center cell once.

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `25`

**Example 2**

- Input: `mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]`
- Output: `8`

**Example 3**

- Input: `mat = [[5]]`
- Output: `5`
