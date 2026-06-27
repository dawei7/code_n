# Maximum Score From Grid Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3225 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix, Prefix Sum |
| Official Link | [maximum-score-from-grid-operations](https://leetcode.com/problems/maximum-score-from-grid-operations/) |

## Problem Description & Examples
### Goal
Given an $n \times n$ grid of non-negative integers, you must select a set of cells to "paint" such that the resulting shape is formed by a sequence of non-increasing column heights from left to right, followed by a sequence of non-decreasing column heights. Specifically, for each column $j$, you choose a height $h_j$ (number of cells from the top), and the score is the sum of all values in the grid that are *not* painted. The goal is to maximize this score by choosing an optimal configuration of heights.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers of size $n \times n$.

**Return value**

- An integer representing the maximum possible sum of the unpainted cells.

### Examples
**Example 1**

- Input: `grid = [[0,0,0,0,0],[0,0,3,0,0],[0,2,0,0,2],[0,0,0,0,1],[0,0,0,0,0]]`
- Output: `11`

**Example 2**

- Input: `grid = [[10,10,10],[10,10,10],[10,10,10]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with state compression. We define `dp[col][prev_h][state]` where `col` is the current column, `prev_h` is the height of the previous column, and `state` is a boolean indicating whether we are currently in the "non-increasing" phase or the "non-decreasing" phase. We use prefix sums to calculate the sum of grid values in a column segment in $O(1)$ time.

---

## Complexity Analysis
- **Time Complexity**: $O(n^3)$, where $n$ is the dimension of the grid. We iterate through $n$ columns, and for each, we iterate through possible heights $h$ and $prev\_h$.
- **Space Complexity**: $O(n^2)$ to store the DP table and the prefix sum array.
