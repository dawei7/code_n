# Minimum Operations to Make Columns Strictly Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3402 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/) |

## Problem Description

### Goal

You are given an $m\times n$ matrix `grid` whose cells contain non-negative integers. An operation chooses any one cell `grid[i][j]` and increases its value by exactly 1; operations may be repeated on the same cell.

Make every column strictly increasing from top to bottom. In other words, after the changes, each cell below the first row must be greater than the cell immediately above it in the same column. Return the minimum total number of operations needed across the whole matrix. Rows do not need to be ordered relative to one another, and different columns impose no constraints on each other.

### Function Contract

**Inputs**

- `grid`: A rectangular list of $m$ rows, each containing $n$ non-negative integers.

Both dimensions satisfy $1\le m,n\le50$, and every original cell satisfies $0\le\texttt{grid[i][j]}<2500$.

**Return value**

- The minimum number of unit increments that makes every column strictly increasing.

### Examples

#### Example 1

- **Input:** `grid = [[3, 2], [1, 3], [3, 4], [0, 1]]`
- **Output:** `15`

The first column requires 3, 2, and 6 increments in its last three rows. The final cell of the second column requires 4 more, for a total of 15.

#### Example 2

- **Input:** `grid = [[3, 2, 1], [2, 1, 0], [1, 2, 3]]`
- **Output:** `12`

Raising only the cells that fail their column's strict inequality costs 6 operations in the first column, 4 in the second, and 2 in the third.
