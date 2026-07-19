# Minimum Falling Path Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1289 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-falling-path-sum-ii/) |

## Problem Description
### Goal
Given an $n \times n$ integer matrix `grid`, form a falling path with non-zero shifts by choosing exactly one element from every row. The elements chosen from any two adjacent rows must come from different columns.

Return the minimum possible sum of the $n$ selected values. Values may be negative, and for a one-row grid the only selected value is the answer.

### Function Contract
**Inputs**

- `grid`: an $n \times n$ integer matrix, where $1 \le n \le 200$ and $-99 \le \texttt{grid[r][c]} \le 99$.

**Return value**

The minimum sum among all choices of one cell per row whose column differs between every pair of adjacent rows.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `13`
- Explanation: Selecting 1, 5, and 7 uses different columns in adjacent rows and gives the minimum sum.

**Example 2**

- Input: `grid = [[7]]`
- Output: `7`

**Example 3**

- Input: `grid = [[-19,57],[-40,-5]]`
- Output: `-24`
- Explanation: The best valid choice is $-19 + (-5)$; the two row minima share a column and cannot both be selected.
