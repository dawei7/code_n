# Unique Paths II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 63 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-paths-ii/) |

## Problem Description
### Goal
You are given a rectangular grid where `0` marks a free cell and `1` marks an obstacle. A robot begins at the top-left cell and wants to reach the bottom-right, moving exactly one cell right or down at each step.

Count the unique paths that never enter an obstacle and return that number. If the start or destination is blocked, no path exists. Obstacles may force detours or disconnect the destination entirely, while a single free cell represents one valid zero-move path.

### Function Contract
**Inputs**

- `obstacle_grid`: an `m` by `n` matrix of zeros and ones

**Return value**

The number of valid paths that never enter an obstacle.

### Examples
**Example 1**

- Input: `obstacle_grid = [[0,0,0],[0,1,0],[0,0,0]]`
- Output: `2`

**Example 2**

- Input: `obstacle_grid = [[0,1],[0,0]]`
- Output: `1`

**Example 3**

- Input: `obstacle_grid = [[1]]`
- Output: `0`
