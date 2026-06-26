# Max Points on a Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 149 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Geometry |
| Official Link | [max-points-on-a-line](https://leetcode.com/problems/max-points-on-a-line/) |

## Problem Description & Examples
### Goal
Find the largest number of given points that lie on the same straight line.

### Function Contract
**Inputs**

- `points`: a list of two-dimensional integer coordinates.

**Return value**

The maximum number of collinear points.

### Examples
**Example 1**

- Input: `points = [[1, 1], [2, 2], [3, 3]]`
- Output: `3`

**Example 2**

- Input: `points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]`
- Output: `4`

**Example 3**

- Input: `points = [[0, 0], [1, 0], [2, 0], [3, 1]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Use each point as an anchor and count normalized slopes to every later point.
Normalize each `(dy, dx)` pair by their greatest common divisor and keep a
stable sign convention so equal lines share the same key. The best slope count
for an anchor plus the anchor itself gives a candidate answer.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`.
- **Space Complexity**: `O(n)` for slope counts per anchor.
