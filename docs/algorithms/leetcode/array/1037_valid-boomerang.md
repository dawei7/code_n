# Valid Boomerang

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1037 |
| Difficulty | Easy |
| Topics | Array, Math, Geometry |
| Official Link | [valid-boomerang](https://leetcode.com/problems/valid-boomerang/) |

## Problem Description & Examples
### Goal
Given three 2D points, determine whether they form a non-degenerate boomerang: the points must be distinct and not lie on one straight line.

### Function Contract
**Inputs**

- `points`: List[List[int]] containing exactly three `[x, y]` coordinates

**Return value**

bool - `True` if the three points are non-collinear

### Examples
**Example 1**

- Input: `points = [[1, 1], [2, 3], [3, 2]]`
- Output: `True`

**Example 2**

- Input: `points = [[1, 1], [2, 2], [3, 3]]`
- Output: `False`

**Example 3**

- Input: `points = [[0, 0], [0, 0], [1, 1]]`
- Output: `False`

---

## Underlying Base Algorithm(s)
2D cross product collinearity test.

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
