# Maximum Amount of Money Robot Can Earn

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3418 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [maximum-amount-of-money-robot-can-earn](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/) |

## Problem Description & Examples
### Goal
Calculate the maximum profit a robot can accumulate while traversing a grid from the top-left corner to the bottom-right corner. The robot can only move right or down. Each cell contains a monetary value (which can be negative). The robot is granted a special ability to "neutralize" up to two negative-value cells, effectively treating their value as zero.

### Function Contract
**Inputs**

- `coins`: A 2D list of integers representing the grid of monetary values.

**Return value**

- An integer representing the maximum possible sum of coins collected from (0, 0) to (m-1, n-1) given the ability to ignore up to two negative values.

### Examples
**Example 1**

- Input: `coins = [[0,1,-1],[1,-2,3]]`
- Output: `8`

**Example 2**

- Input: `coins = [[1,-1,-1,1]]`
- Output: `1`

**Example 3**

- Input: `coins = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Dynamic Programming with State Compression. We maintain a 3D DP table `dp[i][j][k]`, where `i, j` are the grid coordinates and `k` (0 to 2) represents the number of negative values already neutralized.

---

## Complexity Analysis
- **Time Complexity**: O(M * N), where M is the number of rows and N is the number of columns, as we visit each cell and perform a constant number of operations (3 states for k).
- **Space Complexity**: O(M * N), which can be optimized to O(N) since each state only depends on the previous row/column.
