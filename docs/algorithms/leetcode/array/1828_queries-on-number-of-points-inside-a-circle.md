# Queries on Number of Points Inside a Circle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1828 |
| Difficulty | Medium |
| Topics | Array, Math, Geometry |
| Official Link | [queries-on-number-of-points-inside-a-circle](https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/) |

## Problem Description & Examples
### Goal
For each circular query, count how many given points lie inside or on the circle.

### Function Contract
**Inputs**

- `points`: a list of `[x, y]` coordinates.
- `queries`: a list of `[xCenter, yCenter, radius]` circles.

**Return value**

Return the count of contained points for each query.

### Examples
**Example 1**

- Input: `points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]`
- Output: `[3,2,2]`

**Example 2**

- Input: `points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]`
- Output: `[2,3,2,4]`

**Example 3**

- Input: `points = [[0,0]], queries = [[0,0,0],[1,0,1]]`
- Output: `[1,1]`

---

## Underlying Base Algorithm(s)
For each query, scan every point and compare squared distance with squared radius to avoid floating-point work: `(px - cx)^2 + (py - cy)^2 <= r^2`.

---

## Complexity Analysis
- **Time Complexity**: `O(points * queries)`
- **Space Complexity**: `O(1)` besides the output array
