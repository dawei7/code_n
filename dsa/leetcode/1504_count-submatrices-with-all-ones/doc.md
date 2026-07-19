# Count Submatrices With All Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1504 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Stack, Matrix, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/count-submatrices-with-all-ones/) |

## Problem Description
### Goal

Given an $m\times n$ binary matrix `mat`, consider every nonempty rectangular submatrix formed by choosing a contiguous range of rows and a contiguous range of columns. Different boundary choices count as different submatrices, even when they contain identical values.

Return the total number of those rectangles whose every cell is `1`. Rectangles of every legal height and width must be included, from individual cells through the entire matrix; any rectangle containing at least one `0` does not contribute.

### Function Contract
**Inputs**

Let $m$ be the row count and $n$ the column count.

- `mat`: a rectangular $m\times n$ matrix with $1\le m,n\le150$.
- Every `mat[row][column]` is either `0` or `1`.

**Return value**

Return an integer equal to the number of nonempty, axis-aligned, contiguous submatrices containing only ones. The app-local implementation does not modify `mat`.

### Examples
**Example 1**

- Input: `mat = [[1,0,1],[1,1,0],[1,1,0]]`
- Output: `13`
- Explanation: The total consists of six $1\times1$, two $1\times2$, three $2\times1$, one $2\times2$, and one $3\times1$ all-one rectangles.

**Example 2**

- Input: `mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]`
- Output: `24`
- Explanation: Counting all valid shapes gives eight single cells plus sixteen wider or taller rectangles.

**Example 3**

- Input: `mat = [[1,1,1],[1,1,1]]`
- Output: `18`
- Explanation: An all-one $2\times3$ matrix has $2\cdot3/2=3$ row intervals and $3\cdot4/2=6$ column intervals, producing $3\cdot6=18$ rectangles.
