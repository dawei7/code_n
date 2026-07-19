# Number of Enclaves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1020 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-enclaves/) |

## Problem Description

### Goal

You are given an $R\times C$ binary matrix `grid`, where `0` represents a sea cell and `1` represents a land cell.

One move walks from a land cell to another 4-directionally adjacent land cell, or walks off the grid from a boundary land cell. Return the number of land cells from which it is impossible to walk off the grid using any number of moves. Diagonal contact does not connect land cells.

### Function Contract

**Inputs**

- `grid`: an $R\times C$ binary matrix, where $1\le R,C\le500$ and every cell is `0` or `1`.

**Return value**

- The number of land cells that are not 4-directionally connected to any boundary land cell.

### Examples

**Example 1**

- Input: `grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]`
- Output: `3`
- Explanation: Three connected interior land cells are enclosed; the boundary land cell is not.

**Example 2**

- Input: `grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]`
- Output: `0`
- Explanation: Every land cell is on the boundary or connected to boundary land.

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `0`
- Explanation: All land belongs to a component touching the boundary.
