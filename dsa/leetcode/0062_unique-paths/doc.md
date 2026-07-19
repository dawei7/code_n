# Unique Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 62 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-paths/) |

## Problem Description
### Goal
Imagine a robot at the top-left cell of an $m \times n$ rectangular grid. Its destination is the bottom-right cell, and each move advances exactly one cell either to the right or downward; it cannot move left, upward, or outside the grid.

Return the number of unique paths that reach the destination. Paths are distinguished by their ordered choices of right and down moves. When the grid has one row or one column, only one path exists because every move is forced.

### Function Contract
**Inputs**

- `m`: the positive number of rows
- `n`: the positive number of columns

**Return value**

The integer number of valid movement sequences.

### Examples
**Example 1**

- Input: `m = 3, n = 7`
- Output: `28`

**Example 2**

- Input: `m = 3, n = 2`
- Output: `3`

**Example 3**

- Input: `m = 1, n = 8`
- Output: `1`
