# Minimum Number of Operations to Satisfy Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3122 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [minimum-number-of-operations-to-satisfy-conditions](https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/) |

## Problem Description & Examples
### Goal
Given a 2D grid of integers, determine the minimum number of cell modifications required to ensure that every column contains only one unique value, and that no two adjacent columns contain the same unique value.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the input matrix of dimensions `m x n`.

**Return value**

- An integer representing the minimum number of operations (changing a cell's value) to satisfy the column constraints.

### Examples
**Example 1**

- Input: `grid = [[1,0,2],[1,0,2]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,1,1],[0,0,0]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1],[2],[3]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Dynamic Programming. We first pre-calculate the cost to make each column consist entirely of a specific digit (0-9). Then, we define `dp[col][val]` as the minimum cost to satisfy the conditions for all columns up to `col`, where `col` is assigned the digit `val`. The transition is `dp[col][val] = cost[col][val] + min(dp[col-1][prev_val])` for all `prev_val != val`.

---

## Complexity Analysis
- **Time Complexity**: `O(n * 10^2)`, where `n` is the number of columns. Since the number of possible values is fixed at 10, this simplifies to `O(n)`.
- **Space Complexity**: `O(n * 10)`, which simplifies to `O(n)` to store the DP table.
