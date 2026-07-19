# Valid Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 593 |
| Difficulty | Medium |
| Topics | Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-square/) |

## Problem Description
### Goal
Given the coordinates of four points `p1`, `p2`, `p3`, and `p4` in two-dimensional space, determine whether those points construct a valid square. The points are not supplied in any geometric order, and the square may be rotated relative to the coordinate axes.

Return `True` only when the four sides have equal positive length and the four interior angles are all 90 degrees; otherwise return `False`. Coincident points cannot form a square because its side length must be positive, and a rhombus without right angles is not sufficient.

### Function Contract
**Inputs**

- `p1, p2, p3, p4: list[int]`: four points represented as `[x, y]`

**Return value**

- `True` when the points form a nondegenerate square; otherwise `False`

### Examples
**Example 1**

- Input: `[0,0], [1,1], [1,0], [0,1]`
- Output: `True`

**Example 2**

- Input: `[0,0], [2,0], [2,1], [0,1]`
- Output: `False`

**Example 3**

- Input: `[0,0], [0,0], [1,0], [0,1]`
- Output: `False`
