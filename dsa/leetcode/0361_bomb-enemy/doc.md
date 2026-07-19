# Bomb Enemy

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 361 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/bomb-enemy/) |

## Problem Description
### Goal
Given a rectangular grid containing empty cells `"0"`, enemies `"E"`, and walls `"W"`, place at most one bomb on an empty cell. Its blast travels horizontally and vertically in all four directions from that cell.

The bomb eliminates each enemy reached before a wall blocks that direction; it does not pass through walls and has no diagonal effect. Return the maximum number of enemies removable by one valid placement, or `0` when no empty cell kills an enemy. The bomb cannot occupy an enemy or wall, and only enemies visible from its chosen row and column segments contribute.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix containing `"0"` for empty cells, `"E"` for enemies, and `"W"` for walls

**Return value**

- The maximum number of enemies one bomb can eliminate, or `0` when no empty placement kills an enemy.

### Examples
**Example 1**

- Input: `grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]`
- Output: `3`

**Example 2**

- Input: `grid = [["0","E"],["E","0"]]`
- Output: `2`

**Example 3**

- Input: `grid = [["W","E"],["E","W"]]`
- Output: `0`
