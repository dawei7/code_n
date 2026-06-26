# Count Fertile Pyramids in a Land

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2088 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [count-fertile-pyramids-in-a-land](https://leetcode.com/problems/count-fertile-pyramids-in-a-land/) |

## Problem Description & Examples
### Goal
Count all upright and inverted pyramids made entirely of fertile cells in a binary grid. A pyramid must have height at least two.

### Function Contract
**Inputs**

- `grid`: a binary matrix where `1` is fertile land.

**Return value**

Return the total number of fertile pyramids in both orientations.

### Examples
**Example 1**

- Input: `grid = [[0,1,1,0],[1,1,1,1]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1,1,1],[1,1,1]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Use DP for one orientation: if a cell is fertile, its pyramid height is one plus the minimum height of the three supporting cells in the next row. Add `height - 1` for each cell. Run the same computation on the vertically reversed grid for inverted pyramids.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)` or `O(n)` with rolling rows.
