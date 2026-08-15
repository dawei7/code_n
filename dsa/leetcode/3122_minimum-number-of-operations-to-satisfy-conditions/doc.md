# Minimum Number of Operations to Satisfy Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3122 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/) |

## Problem Description

### Goal

You are given an $m\times n$ integer matrix `grid`. In one operation, you may replace the value of any one cell with any non-negative integer. Modify the matrix until every cell equals the cell directly below it whenever that cell exists, and differs from the cell directly to its right whenever that cell exists.

Equivalently, every column must become constant, while the chosen values of adjacent columns must be different. Return the minimum number of individual cell changes needed to make both conditions hold throughout the matrix.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix whose entries are digits from 0 through 9.

The dimensions satisfy $1 \le m,n \le 1000$.

**Return value**

Return the minimum number of cell-replacement operations needed to make each column constant and every adjacent pair of columns different.

### Examples

#### Example 1

- **Input:** `grid = [[1,0,2],[1,0,2]]`
- **Output:** `0`
- **Explanation:** Each column is already constant, and neighboring column values differ.

#### Example 2

- **Input:** `grid = [[1,1,1],[0,0,0]]`
- **Output:** `3`
- **Explanation:** Three changes can produce `[[1,0,1],[1,0,1]]`, which satisfies both conditions.

#### Example 3

- **Input:** `grid = [[1],[2],[3]]`
- **Output:** `2`
- **Explanation:** With one column, two cells can be changed to `1` so the entire column is equal.
