# Number of Distinct Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 694 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Sorting, Matrix, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-distinct-islands/) |

## Problem Description
### Goal
Given a binary grid, an island is a maximal group of `1` cells connected horizontally or vertically. Determine how many distinct island shapes occur across the grid.

Two islands have the same shape when one can be translated so that all of its land cells coincide with the other island's cells. Rotation and reflection do not make shapes equivalent, and an island's absolute location does not matter. Return the number of distinct translation-normalized shapes; water cells and diagonal contact do not join islands.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix whose `1` cells are land and whose `0` cells are water

**Return value**

- The number of distinct island shapes under translation

### Examples
**Example 1**

- Input: `grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]`
- Output: `1`
- Explanation: both islands are translated copies of the same `2 x 2` block.

**Example 2**

- Input: `grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1,0,1],[0,0,0],[1,0,1]]`
- Output: `1`
- Explanation: every island consists of one cell.
