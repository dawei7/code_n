# Find a Peak Element II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1901 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Matrix |
| Official Link | [find-a-peak-element-ii](https://leetcode.com/problems/find-a-peak-element-ii/) |

## Problem Description & Examples
### Goal
Find any peak cell in a 2D grid. A peak is strictly greater than its adjacent up, down, left, and right neighbors; outside the grid is treated as smaller.

### Function Contract
**Inputs**

- `mat`: a 2D integer matrix.

**Return value**

Return the row and column of any peak.

### Examples
**Example 1**

- Input: `mat = [[1,4],[3,2]]`
- Output: `[0,1]`

**Example 2**

- Input: `mat = [[10,20,15],[21,30,14],[7,16,32]]`
- Output: `[1,1]`

**Example 3**

- Input: `mat = [[1]]`
- Output: `[0,0]`

---

## Underlying Base Algorithm(s)
Binary search columns. For the middle column, find the row containing its maximum value. If that value is greater than its left and right neighbors, it is a peak. Otherwise move toward the side with the larger neighbor, because a peak must exist in that direction.

---

## Complexity Analysis
- **Time Complexity**: `O(m log n)`
- **Space Complexity**: `O(1)`
