# Shortest Distance from All Buildings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 317 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-from-all-buildings/) |

## Problem Description
### Goal
Given a rectangular grid, `0` marks empty land, `1` marks a building, and `2` marks an obstacle. Choose one empty cell as a gathering location. Travel uses horizontal or vertical steps through empty land; routes cannot pass through buildings, obstacles, or outside the grid.

For each candidate that can reach every building, sum its shortest path distance to all buildings. Return the smallest such total, or `-1` when no empty cell reaches them all. The destination building cell supplies the final step but cannot be crossed to reach another building. Return only the distance total, not the chosen location or paths.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix where `0` is empty land, `1` is a building, and `2` is an obstacle

**Return value**

The minimum total distance from one valid empty cell to all buildings, or `-1` if no such cell exists.

### Examples
**Example 1**

- Input: `grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]`
- Output: `7`

**Example 2**

- Input: `grid = [[1,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1]]`
- Output: `-1`
