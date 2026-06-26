# Where Will the Ball Fall

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1706 |
| Difficulty | Medium |
| Topics | Array, Matrix, Simulation |
| Official Link | [where-will-the-ball-fall](https://leetcode.com/problems/where-will-the-ball-fall/) |

## Problem Description & Examples
### Goal
Drop one ball from the top of each column in a grid of diagonal boards. A `1` redirects a ball down-right, and a `-1` redirects it down-left. Report where each ball exits, or `-1` if it gets stuck against a wall or a V-shaped pair of boards.

### Function Contract
**Inputs**

- `grid`: an `m x n` matrix whose values are `1` or `-1`.

**Return value**

Return a list where entry `j` is the exit column for the ball dropped at column `j`, or `-1` if it cannot reach the bottom.

### Examples
**Example 1**

- Input: `grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]`
- Output: `[1,-1,-1,-1,-1]`

**Example 2**

- Input: `grid = [[-1]]`
- Output: `[-1]`

**Example 3**

- Input: `grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]`
- Output: `[0,1,2,3,4,-1]`

---

## Underlying Base Algorithm(s)
Simulate each ball row by row. At a cell `(r, c)`, the next column is `c + grid[r][c]`. The ball gets stuck if that column is outside the grid or if the neighboring board points in the opposite direction. Otherwise continue from the next row and new column.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(1)` besides the output array
