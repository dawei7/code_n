# Check If It Is a Straight Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1232 |
| Difficulty | Easy |
| Topics | Array, Math, Geometry |
| Official Link | [check-if-it-is-a-straight-line](https://leetcode.com/problems/check-if-it-is-a-straight-line/) |

## Problem Description & Examples
### Goal
Determine whether all given points lie on one straight line.

### Function Contract
**Inputs**

- `coordinates`: list of `[x, y]` points.

**Return value**

`true` if all points are collinear, otherwise `false`.

### Examples
**Example 1**

- Input: `coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]`
- Output: `true`

**Example 2**

- Input: `coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]`
- Output: `false`

**Example 3**

- Input: `coordinates = [[0,0],[0,5],[0,-2]]`
- Output: `true`

---

## Underlying Base Algorithm(s)
Cross-product collinearity test.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
