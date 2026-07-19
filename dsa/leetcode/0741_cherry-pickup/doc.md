# Cherry Pickup

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 741 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/cherry-pickup/) |

## Problem Description
### Goal
An $n \times n$ grid contains empty cells `0`, cherries `1`, and impassable thorns `-1`. Travel from `(0, 0)` to $(n - 1, n - 1)$ using only right or down moves through valid cells, then return using only left or up moves.

Collect a cherry when a route first visits its cell; that cell becomes empty, so the return trip cannot collect it again. Return the maximum cherries obtainable over both journeys. If no valid outward-and-return trip exists, return `0`; neither route may enter a thorn.

### Function Contract
**Inputs**

- `grid`: an $n \times n$ matrix containing `-1` for thorns, `0` for empty cells, and `1` for cherries; the two endpoints are not thorns

**Return value**

- The maximum cherries collectable by a right/down outward path and a left/up return path, or `0` when no complete trip exists

### Examples
**Example 1**

- Input: `grid = [[0,1,-1],[1,0,-1],[1,1,1]]`
- Output: `5`

**Example 2**

- Input: `grid = [[1,1,-1],[1,-1,1],[-1,1,1]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `8`
