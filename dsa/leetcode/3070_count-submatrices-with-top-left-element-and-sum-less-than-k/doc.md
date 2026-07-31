# Count Submatrices with Top-Left Element and Sum Less Than k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3070 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/) |

## Problem Description

### Goal

You are given a zero-indexed matrix `grid` of non-negative integers and an integer `k`. Count the submatrices that contain the matrix's top-left element and whose element sum is less than or equal to `k`.

Because such a submatrix must contain `grid[0][0]`, its top and left boundaries are fixed at row `0` and column `0`. It is therefore determined by choosing its bottom-right corner `(r, c)`, and it contains every cell in rows `0` through `r` and columns `0` through `c`.

### Function Contract

**Inputs**

- `grid`: An $m \times n$ matrix of integers, where $1 \le m,n \le 1000$ and every value lies between $0$ and $1000$, inclusive.
- `k`: The inclusive sum limit, where $1 \le k \le 10^9$.

**Return value**

Return the number of top-left-anchored submatrices whose sum is at most `k`.

### Examples

**Example 1**

- Input: `grid = [[7,6,3],[6,6,1]], k = 18`
- Output: `4`
- Explanation: Four choices of bottom-right corner produce anchored submatrices with sums no greater than `18`.

**Example 2**

- Input: `grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20`
- Output: `6`
- Explanation: Six anchored submatrices have sums no greater than `20`.
