# Maximum Sum of an Hourglass

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2428 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [maximum-sum-of-an-hourglass](https://leetcode.com/problems/maximum-sum-of-an-hourglass/) |

## Problem Description & Examples
### Goal
Given a 2D integer matrix, identify all possible "hourglass" shapes within the grid. An hourglass is defined as a 3x3 subgrid pattern consisting of the top row (3 elements), the center element, and the bottom row (3 elements). The objective is to calculate the sum of the elements for every possible hourglass and return the maximum sum found.

### Function Contract
**Inputs**

- `grid`: A List[List[int]] representing an m x n matrix where m, n >= 3.

**Return value**

- `int`: The maximum sum obtained from any valid 3x3 hourglass pattern in the grid.

### Examples
**Example 1**

- Input: `grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]`
- Output: `30`

**Example 2**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `35`

**Example 3**

- Input: `grid = [[3,2,1],[1,0,0],[0,0,0]]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Brute Force Sliding Window** approach. Since the hourglass shape is fixed at 3x3, we iterate through all possible top-left corners `(i, j)` such that `0 <= i <= m-3` and `0 <= j <= n-3`. For each corner, we compute the sum of the seven specific cells forming the hourglass and track the global maximum.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns. We visit each valid top-left corner once, performing a constant number of additions (7) per window.
- **Space Complexity**: `O(1)`, as we only store a few integer variables to track the current and maximum sums, regardless of the input matrix size.
