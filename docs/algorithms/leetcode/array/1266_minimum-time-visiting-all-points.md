# Minimum Time Visiting All Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1266 |
| Difficulty | Easy |
| Topics | Array, Math, Geometry |
| Official Link | [minimum-time-visiting-all-points](https://leetcode.com/problems/minimum-time-visiting-all-points/) |

## Problem Description & Examples
### Goal
Visit points in the given order on a 2D grid. In one second you may move horizontally, vertically, or diagonally by one unit. Return the minimum total time.

### Function Contract
**Inputs**

- `points`: ordered list of `[x, y]` coordinates.

**Return value**

The minimum seconds needed to visit all points in order.

### Examples
**Example 1**

- Input: `points = [[1,1],[3,4],[-1,0]]`
- Output: `7`

**Example 2**

- Input: `points = [[3,2],[-2,2]]`
- Output: `5`

**Example 3**

- Input: `points = [[0,0],[0,0],[2,1]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Chebyshev distance.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
