# Pascal's Triangle II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 119 |
| Difficulty | Easy |
| Topics | Array, Dynamic Programming |
| Official Link | [pascals-triangle-ii](https://leetcode.com/problems/pascals-triangle-ii/) |

## Problem Description & Examples
### Goal
Return the row with zero-based index `rowIndex` from Pascal's triangle.

### Function Contract
**Inputs**

- `rowIndex`: zero-based row index.

**Return value**

The requested Pascal row.

### Examples
**Example 1**

- Input: `rowIndex = 3`
- Output: `[1,3,3,1]`

**Example 2**

- Input: `rowIndex = 0`
- Output: `[1]`

**Example 3**

- Input: `rowIndex = 5`
- Output: `[1,5,10,10,5,1]`

---

## Underlying Base Algorithm(s)
In-place dynamic programming.

---

## Complexity Analysis
- **Time Complexity**: `O(rowIndex^2)`
- **Space Complexity**: `O(rowIndex)`
