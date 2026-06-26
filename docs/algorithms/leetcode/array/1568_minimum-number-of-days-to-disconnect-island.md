# Minimum Number of Days to Disconnect Island

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1568 |
| Difficulty | Hard |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Strongly Connected Component |
| Official Link | [minimum-number-of-days-to-disconnect-island](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) |

## Problem Description & Examples
### Goal
Remove land cells one day at a time until the grid is no longer exactly one
connected island. Find the minimum number of days needed.

### Function Contract
**Inputs**

- `grid`: a binary matrix where `1` is land and `0` is water.

**Return value**

The fewest land removals required to make the island disconnected or empty.

### Examples
**Example 1**

- Input: `grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1, 1]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1, 0, 1, 0]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
First count islands. If the grid is already disconnected or has no island,
return `0`. Otherwise, try removing each land cell and recounting islands; if
any single removal disconnects the grid, return `1`. If not, the answer is `2`
because any connected island can be disconnected by removing at most two cells.

---

## Complexity Analysis
- **Time Complexity**: `O((m * n)^2)` for testing every land cell with a grid traversal.
- **Space Complexity**: `O(m * n)` for visited state during traversal.
