# Max Area of Island

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 695 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/max-area-of-island/) |

## Problem Description
### Goal
Given an $m \times n$ binary matrix `grid`, an island is a group of `1` cells representing land that are connected horizontally or vertically. The grid's outer edges are surrounded by water, and diagonal contact alone does not connect land cells.

Define an island's area as its number of land cells. Return the maximum area among all islands in the grid. If the matrix contains no land, return `0`; separate islands are measured independently even when they touch diagonally.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix whose `1` cells are land and whose `0` cells are water

**Return value**

- The maximum area of any island, or `0` when the grid contains no land

### Examples
**Example 1**

- Input: `grid = [[1,1],[0,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1,1],[0,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[0,0],[1,0]]`
- Output: `1`
