# Longest Increasing Path in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_202` |
| Frontend ID | 329 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix |
| Official Link | [longest-increasing-path-in-a-matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) |

## Problem Description & Examples
### Goal
Given an `m` x `n` integers `matrix`, return the length of the longest increasing path in `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary.

### Function Contract
**Inputs**

- `matrix`: List[List[int]]

**Return value**

int - length of longest increasing path

### Examples
**Example 1**

- Input: `matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]`
- Output: `4`

**Example 2**

- Input: `matrix = [[2, 9], [17, 16]]`
- Output: `4`

**Example 3**

- Input: `matrix = [[9, 4], [16, 15]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
