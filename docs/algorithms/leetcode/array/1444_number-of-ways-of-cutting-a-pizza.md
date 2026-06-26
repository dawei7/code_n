# Number of Ways of Cutting a Pizza

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1444 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization, Matrix, Prefix Sum |
| Official Link | [number-of-ways-of-cutting-a-pizza](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/) |

## Problem Description & Examples
### Goal
Cut a rectangular pizza into `k` pieces using horizontal or vertical straight cuts. Each final piece must contain at least one apple.

### Function Contract
**Inputs**

- `pizza`: a list of strings where `A` marks an apple and `.` marks an empty cell.
- `k`: the number of final pieces.

**Return value**

The number of valid cutting sequences modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `pizza = ["A..","AAA","..."], k = 3`
- Output: `3`

**Example 2**

- Input: `pizza = ["A..","AA.","..."], k = 3`
- Output: `1`

**Example 3**

- Input: `pizza = ["A..","A..","..."], k = 1`
- Output: `1`

---

## Underlying Base Algorithm(s)
2D suffix sums plus memoized DP. A suffix apple count answers whether any rectangle has an apple; the DP tries every valid next horizontal or vertical cut and recurses on the remaining lower/right rectangle.

---

## Complexity Analysis
- **Time Complexity**: `O(kmn(m+n))` for an `m x n` pizza.
- **Space Complexity**: `O(kmn)`
