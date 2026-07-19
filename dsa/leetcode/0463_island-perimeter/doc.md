# Island Perimeter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 463 |
| Difficulty | Easy |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/island-perimeter/) |

## Problem Description
### Goal
Given a rectangular binary grid, `1` marks land and `0` marks water. The grid contains exactly one island connected horizontally or vertically, is completely surrounded by water, and has no lakes: no interior water region is cut off from the surrounding water.

Return the island's perimeter measured in unit cell edges. Every land edge bordering a water cell or the outside contributes one, while an edge shared by two land cells is internal and contributes nothing. Diagonal contact does not remove perimeter because cells do not share an edge. Count the complete outline without modifying the grid; the function returns a length rather than the number of land cells.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix where `1` is land and `0` is water

**Return value**

- The number of unit edges separating land from water or from the outside of the grid

### Examples
**Example 1**

- Input: `grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]`
- Output: `16`

**Example 2**

- Input: `grid = [[1]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1, 1, 1]]`
- Output: `8`
