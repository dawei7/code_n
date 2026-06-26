# Paths in Matrix Whose Sum Is Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2435 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [paths-in-matrix-whose-sum-is-divisible-by-k](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) |

## Problem Description & Examples
### Goal
Given a 2D grid of non-negative integers, determine the total number of distinct paths from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1). A path is valid if and only if the sum of all integers encountered along the path is evenly divisible by a given integer k. Movement is restricted to only moving right or down.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the matrix.
- `k`: An integer divisor.

**Return value**

- An integer representing the count of paths whose sum modulo k equals 0. Since the result can be very large, return it modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3`
- Output: `2`

**Example 2**

- Input: `grid = [[0,0]], k = 5`
- Output: `1`

**Example 3**

- Input: `grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1`
- Output: `10`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. We maintain a 3D DP table `dp[i][j][rem]`, representing the number of paths reaching cell `(i, j)` such that the path sum modulo `k` is `rem`. The state transition is `dp[i][j][(rem + grid[i][j]) % k] = dp[i-1][j][rem] + dp[i][j-1][rem]`.

---

## Complexity Analysis
- **Time Complexity**: O(m * n * k), where m is the number of rows, n is the number of columns, and k is the divisor. We iterate through every cell and update k states.
- **Space Complexity**: O(m * n * k) to store the DP table. This can be optimized to O(n * k) by observing that we only need the previous row's values.
