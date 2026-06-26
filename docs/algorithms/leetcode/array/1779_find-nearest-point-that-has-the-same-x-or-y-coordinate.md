# Find Nearest Point That Has the Same X or Y Coordinate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1779 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [find-nearest-point-that-has-the-same-x-or-y-coordinate](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/) |

## Problem Description & Examples
### Goal
Given a current coordinate and a list of points, find the valid point with the smallest Manhattan distance. A point is valid if it shares either the same `x` coordinate or the same `y` coordinate.

### Function Contract
**Inputs**

- `x`: current x-coordinate.
- `y`: current y-coordinate.
- `points`: a list of `[x, y]` coordinates.

**Return value**

Return the index of the closest valid point, or `-1` if none exists. If tied, return the smallest index.

### Examples
**Example 1**

- Input: `x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]`
- Output: `2`

**Example 2**

- Input: `x = 3, y = 4, points = [[3,4]]`
- Output: `0`

**Example 3**

- Input: `x = 3, y = 4, points = [[2,3]]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Scan the points in order. For every point sharing `x` or `y`, compute `abs(px - x) + abs(py - y)` and update the best index only when the distance is strictly smaller, preserving the earliest index on ties.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
