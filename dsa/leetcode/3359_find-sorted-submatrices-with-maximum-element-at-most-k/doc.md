# Find Sorted Submatrices With Maximum Element at Most K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3359 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Matrix, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/) |

## Problem Description

### Goal

Given an $m\times n$ integer matrix `grid` and a non-negative threshold $k$, count the rectangular submatrices whose largest element is at most $k$. A submatrix is determined by inclusive row bounds and inclusive column bounds and contains every cell inside that rectangle; rows or columns cannot be skipped.

Within every selected row, the values across the selected columns must be in non-increasing order from left to right. Equality is allowed, and no ordering relation is required between different rows. Return the total number of rectangles satisfying both the threshold condition and the per-row ordering condition.

### Function Contract

**Inputs**

- `grid`: A non-empty rectangular list of lists containing positive integers.
- `k`: A non-negative integer upper bound for every selected cell.

Let $m=\lvert\texttt{grid}\rvert$ and $n=\lvert\texttt{grid[0]}\rvert$. Both dimensions are at most $10^3$, and every matrix value and $k$ are at most $10^9$.

**Return value**

- The number of rectangular submatrices whose maximum value is at most $k$ and whose values are non-increasing across every selected row.

### Examples

**Example 1**

- Input: `grid = [[4, 3, 2, 1], [8, 7, 6, 1]], k = 3`
- Output: `8`
- Explanation: The qualifying rectangles use only values at most $3$ and preserve non-increasing order in each selected row. They include six one-row choices and two rectangles that span both rows at the last column.

**Example 2**

- Input: `grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]], k = 1`
- Output: `36`
- Explanation: Every rectangle qualifies. There are $3\cdot4/2=6$ row intervals and the same number of column intervals, giving $36$ submatrices.

**Example 3**

- Input: `grid = [[1]], k = 1`
- Output: `1`
- Explanation: The single cell itself is the only submatrix and satisfies both conditions.
