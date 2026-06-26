# Minimum Cost Homecoming of a Robot in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2087 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [minimum-cost-homecoming-of-a-robot-in-a-grid](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/) |

## Problem Description & Examples
### Goal
A robot moves from a start cell to a home cell. Entering a row or column has a given cost; find the minimum travel cost.

### Function Contract
**Inputs**

- `startPos`: starting `[row, col]`.
- `homePos`: target `[row, col]`.
- `rowCosts`: cost paid when entering each row.
- `colCosts`: cost paid when entering each column.

**Return value**

Return the minimum cost to reach home.

### Examples
**Example 1**

- Input: `startPos = [1,0], homePos = [2,3], rowCosts = [5,4,3], colCosts = [8,2,6,7]`
- Output: `18`

**Example 2**

- Input: `startPos = [0,0], homePos = [0,0], rowCosts = [1], colCosts = [1]`
- Output: `0`

**Example 3**

- Input: `startPos = [0,1], homePos = [2,3], rowCosts = [1,2,3], colCosts = [4,5,6,7]`
- Output: `18`

---

## Underlying Base Algorithm(s)
Because row and column movement costs are independent and all costs are positive, any shortest monotonic path between start and home is optimal. Sum the row costs for rows entered while moving vertically and column costs for columns entered while moving horizontally.

---

## Complexity Analysis
- **Time Complexity**: `O(abs(row diff) + abs(col diff))`
- **Space Complexity**: `O(1)`
