# Find a Peak Element II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1901 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Find a Peak Element II](https://leetcode.com/problems/find-a-peak-element-ii/) |

## Problem Description

### Goal

Given an $m \times n$ integer matrix `mat`, find any cell whose value is strictly greater than each orthogonally adjacent cell: above, below, left, and right. Diagonal cells are not neighbors. The matrix has no equal values in horizontally or vertically adjacent cells.

Treat every position just outside the matrix boundary as having value $-1$. Return the zero-based row and column of any qualifying peak. The solution must exploit the matrix structure rather than inspect every cell, running in $O(m\log n)$ or $O(n\log m)$ time.

### Function Contract

**Inputs**

- `mat`: a nonempty rectangular matrix with $m$ rows and $n$ columns, where $1 \le m,n \le 500$.
- Every entry is an integer from $1$ through $10^5$.
- No two cells sharing an edge have equal values.

**Return value**

Return `[row, column]` for any cell strictly larger than all of its existing orthogonal neighbors.

### Examples

**Example 1**

- Input: `mat = [[1, 4], [3, 2]]`
- Output: `[0, 1]`
- Explanation: Both `[0, 1]` and `[1, 0]` are valid peaks, so either answer is accepted.

**Example 2**

- Input: `mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]`
- Output: `[1, 1]`
- Explanation: The values `30` and `32` are both peaks.

**Example 3**

- Input: `mat = [[7]]`
- Output: `[0, 0]`
