# Find the Safest Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2812 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid/) |

## Problem Description

### Goal

You are given an $n\times n$ binary grid. A cell containing `1` holds a thief, while a cell containing `0` is empty. Starting at the top-left cell, move through orthogonally adjacent cells until reaching the bottom-right cell. Moving through a thief cell is permitted.

For any visited cell, its distance from danger is the minimum Manhattan distance to any thief. A path's safeness factor is the smallest such distance among all cells on that path. Return the greatest safeness factor achievable by any path from `(0, 0)` to `(n - 1, n - 1)`. At least one thief exists, and the start or destination may itself contain one.

### Function Contract

**Inputs**

- `grid`: An $n\times n$ matrix of zeros and ones, where $1 \leq n \leq 400$ and at least one cell contains `1`.

Let $N=n^2$ denote the number of cells.

**Return value**

Return the maximum possible minimum Manhattan distance from any cell of a start-to-destination path to the nearest thief.

### Examples

**Example 1**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,1]]`
- Output: `0`
- Explanation: Both endpoints contain thieves, so every path has safeness zero.

**Example 2**

- Input: `grid = [[0,0,1],[0,0,0],[0,0,0]]`
- Output: `2`
- Explanation: A path along the left and bottom sides stays at least two Manhattan steps from the thief.

**Example 3**

- Input: `grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]`
- Output: `2`
- Explanation: A route through the middle keeps distance two from both thieves, and no route can maintain a larger minimum.
