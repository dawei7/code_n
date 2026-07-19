# Maximum Matrix Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1975 |
| Difficulty | Medium |
| Topics | Array, Greedy, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-matrix-sum/) |

## Problem Description
### Goal
You are given an $n\times n$ integer matrix. In one operation, choose two
cells that share an edge and multiply both values by `-1`. You may perform the
operation any number of times and may reuse cells.

Return the greatest possible sum of all matrix entries after applying an
optimal sequence of operations. Adjacency is only horizontal or vertical;
diagonally touching cells are not adjacent.

### Function Contract
**Inputs**

- `matrix`: an $n\times n$ integer grid, where $2 \le n \le 250$.
- Every value lies in the inclusive range from $-10^5$ through $10^5$.
- Let $M=n^2$ denote the number of cells.

**Return value**

- The maximum achievable sum of all $M$ entries after any number of legal
  adjacent-pair sign flips.

### Examples
**Example 1**

- Input: `matrix = [[1, -1], [-1, 1]]`
- Output: `4`

**Example 2**

- Input: `matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]`
- Output: `16`

**Example 3**

- Input: `matrix = [[-1, 0], [-2, -3]]`
- Output: `6`
