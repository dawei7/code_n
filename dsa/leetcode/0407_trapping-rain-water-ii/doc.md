# Trapping Rain Water II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 407 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/trapping-rain-water-ii/) |

## Problem Description
### Goal
Given a nonempty rectangular matrix of nonnegative terrain heights, imagine rain falling over every cell. Water can spread between horizontally or vertically adjacent cells and escapes whenever it reaches the map's outer boundary.

Return the total number of unit cubes of water that remain trapped above the terrain after levels stabilize. Boundary cells cannot hold water above themselves, while interior capacity depends on the lowest enclosing route to the outside rather than only immediate neighbors. Sum retained depth over all cells. Diagonal barriers do not directly block or connect flow, and the function returns volume rather than a final water-level matrix.

### Function Contract
**Inputs**

- `height_map`: a nonempty matrix of nonnegative terrain heights

**Return value**

- Return the total trapped-water volume above all cells.

### Examples
**Example 1**

- Input: `height_map = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]`
- Output: `4`

**Example 2**

- Input: `height_map = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]`
- Output: `10`

**Example 3**

- Input: `height_map = [[1,2,3,4]]`
- Output: `0`
