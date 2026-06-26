# Dungeon Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 174 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [dungeon-game](https://leetcode.com/problems/dungeon-game/) |

## Problem Description & Examples
### Goal
A knight starts in the top-left dungeon cell and can only move right or down to reach the princess in the bottom-right cell. Each cell changes health by its value. Health must always stay at least `1`. Find the minimum initial health needed.

### Function Contract
**Inputs**

- `dungeon`: a 2D grid of integers, where negative cells cost health and positive cells restore health.

**Return value**

Return the smallest starting health that guarantees survival to the bottom-right cell.

### Examples
**Example 1**

- Input: `dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]`
- Output: `7`

**Example 2**

- Input: `dungeon = [[0]]`
- Output: `1`

**Example 3**

- Input: `dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Use dynamic programming from the destination backward. Let `dp[r][c]` be the minimum health required before entering cell `(r, c)`. From a cell, choose the cheaper of moving right or down, then subtract the current cell value and clamp to at least `1`.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(n)` with a rolling row, or `O(m * n)` for a full table
