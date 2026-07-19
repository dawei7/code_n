# Dungeon Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 174 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/dungeon-game/) |

## Problem Description
### Goal
A knight starts in the top-left cell of a rectangular dungeon and must reach the bottom-right cell, moving only one cell right or one cell down. Entering any cell immediately changes the knight's health by that cell's integer value, which may be harmful, neutral, or beneficial.

Choose a path and return the smallest positive initial health that keeps health at least `1` after every visited cell, including the starting and destination cells. Reaching zero or below at any intermediate moment is fatal even if a later cell would restore health. The answer concerns the best survivable path, not the path with the largest raw sum or the final health amount.

### Function Contract
**Inputs**

- `dungeon`: rectangular integer matrix of health gains and losses

**Return value**

The minimum positive initial health permitting at least one valid path to the destination.

### Examples
**Example 1**

- Input: `dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]`
- Output: `7`

**Example 2**

- Input: `dungeon = [[0]]`
- Output: `1`

**Example 3**

- Input: `dungeon = [[-3]]`
- Output: `4`
