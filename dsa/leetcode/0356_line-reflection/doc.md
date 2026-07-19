# Line Reflection

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 356 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/line-reflection/) |

## Problem Description
### Goal
Given a collection of integer-coordinate points in the plane, determine whether some vertical line $x = c$ is an axis of reflection for the entire collection. Reflection preserves each point's `y` coordinate and places its partner the same horizontal distance on the opposite side.

Return `True` when every point has the required reflected point in the collection, including points lying directly on the axis, and `False` otherwise. The reflection line need not pass through an input point or have an integer coordinate. Only vertical symmetry is considered; horizontal, diagonal, and rotational symmetry do not qualify.

### Function Contract
**Inputs**

- `points`: a list of integer coordinate pairs `[x, y]`

**Return value**

- `True` when a vertical reflection line exists; otherwise `False`.

### Examples
**Example 1**

- Input: `points = [[1,1],[-1,1]]`
- Output: `True`

**Example 2**

- Input: `points = [[1,1],[-1,-1]]`
- Output: `False`

**Example 3**

- Input: `points = [[0,0],[2,0],[1,1]]`
- Output: `True`
