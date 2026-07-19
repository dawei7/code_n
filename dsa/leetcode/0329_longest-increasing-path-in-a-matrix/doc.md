# Longest Increasing Path in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 329 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) |

## Problem Description
### Goal
Given a nonempty rectangular integer matrix, choose a path that can start at any cell and move one step up, down, left, or right. Every visited cell after the first must contain a value strictly greater than the previous cell's value.

Return the maximum number of cells in any valid path. Diagonal moves, wrapping, and equal-value steps are forbidden. Strict increase prevents revisiting a cell within one path, although different candidate paths may share cells. A one-cell path is always valid, and the function returns only the longest length rather than the coordinates or values along that path.

### Function Contract
**Inputs**

- `matrix`: a nonempty rectangular integer matrix

**Return value**

The number of cells in the longest strictly increasing orthogonal path.

### Examples
**Example 1**

- Input: `matrix = [[9,9,4],[6,6,8],[2,1,1]]`
- Output: `4`

**Example 2**

- Input: `matrix = [[3,4,5],[3,2,6],[2,2,1]]`
- Output: `4`

**Example 3**

- Input: `matrix = [[1]]`
- Output: `1`
