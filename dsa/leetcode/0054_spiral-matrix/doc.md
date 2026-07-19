# Spiral Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 54 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/spiral-matrix/) |

## Problem Description
### Goal
You are given a nonempty rectangular matrix. Traverse its outer boundary clockwise beginning at the top-left cell: move right across the top, down the right edge, left across the bottom, and up the left edge.

After completing a boundary, continue the same pattern on the still-unvisited inner rectangle until every cell has been read. Return the values in visitation order, including each cell exactly once. The matrix may have unequal dimensions or collapse to a single row or column at an inner layer.

### Function Contract
**Inputs**

- `matrix`: an `m` by `n` `List[List[int]]`

**Return value**

A flat `List[int]` containing the spiral traversal.

### Examples
**Example 1**

- Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[1,2,3,6,9,8,7,4,5]`

**Example 2**

- Input: `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
- Output: `[1,2,3,4,8,12,11,10,9,5,6,7]`

**Example 3**

- Input: `matrix = [[1,2,3]]`
- Output: `[1,2,3]`
