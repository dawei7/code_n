# Maximum Rows Covered by Columns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2397 |
| Difficulty | Medium |
| Topics | Array, Backtracking, Bit Manipulation, Matrix, Enumeration |
| Official Link | [maximum-rows-covered-by-columns](https://leetcode.com/problems/maximum-rows-covered-by-columns/) |

## Problem Description & Examples
### Goal
Given a binary matrix and an integer `numSelect`, determine the maximum number of rows that can be fully "covered" by selecting exactly `numSelect` columns. A row is considered covered if all its cells containing a 1 are located within the chosen set of columns.

### Function Contract
**Inputs**

- `matrix`: A 2D list of integers (0 or 1) representing the grid.
- `numSelect`: An integer representing the number of columns to choose.

**Return value**

- An integer representing the maximum number of rows that can be covered.

### Examples
**Example 1**

- Input: `matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2`
- Output: `3`

**Example 2**

- Input: `matrix = [[1],[0]], numSelect = 1`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using **Combinatorial Enumeration** (specifically combinations) combined with **Bit Manipulation**. Since the number of columns is small (up to 12), we can represent each row as a bitmask. We iterate through all possible combinations of `numSelect` columns, represent the selection as a bitmask, and check if each row's bitmask is a subset of the selected columns' mask.

---

## Complexity Analysis
- **Time Complexity**: `O(C(n, k) * m)`, where `n` is the number of columns, `k` is `numSelect`, and `m` is the number of rows. We evaluate all combinations of columns and for each, iterate through all rows.
- **Space Complexity**: `O(m)` to store the bitmask representation of each row.
