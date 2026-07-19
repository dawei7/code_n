# Minimum Path Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 64 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-path-sum/) |

## Problem Description
### Goal
You are given a nonempty rectangular grid of nonnegative integers. Begin at the top-left cell and travel to the bottom-right, moving one cell right or one cell down at each step.

Every visited cell, including both endpoints, contributes its value to the path sum. Return the minimum path sum among all legal paths. A one-cell grid therefore returns its sole value, and the nonnegative weights ensure that no move outside the right-and-down routes can improve a path.

### Function Contract
**Inputs**

- `grid`: a nonempty rectangular matrix of nonnegative integers

**Return value**

The minimum path sum as an integer.

### Examples
**Example 1**

- Input: `grid = [[1,3,1],[1,5,1],[4,2,1]]`
- Output: `7`

**Example 2**

- Input: `grid = [[1,2,3],[4,5,6]]`
- Output: `12`

**Example 3**

- Input: `grid = [[5]]`
- Output: `5`
