# Transpose Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 867 |
| Difficulty | Easy |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/transpose-matrix/) |

## Problem Description
### Goal
Given a rectangular two-dimensional integer array `matrix`, return its transpose. Transposition reflects the matrix across its main diagonal: every original row becomes a result column, and every original column becomes a result row.

If the input has $m$ rows and $n$ columns, the returned matrix must have $n$ rows and $m$ columns. The value originally stored at `matrix[i][j]` must appear at result position `[j][i]`; all values are preserved exactly.

### Function Contract
**Inputs**

- `matrix`: an $m \times n$ rectangular integer matrix, where $1 \leq m,n \leq 1000$, $1 \leq mn \leq 10^5$, and $-10^9 \leq \texttt{matrix[i][j]} \leq 10^9$.

**Return value**

Return the $n \times m$ transpose whose entry at `[j][i]` equals `matrix[i][j]`.

### Examples
**Example 1**

- Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[[1,4,7],[2,5,8],[3,6,9]]`

**Example 2**

- Input: `matrix = [[1,2,3],[4,5,6]]`
- Output: `[[1,4],[2,5],[3,6]]`

**Example 3**

- Input: `matrix = [[5]]`
- Output: `[[5]]`
