# Maximum Number of Visible Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1610 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Sliding Window, Sorting |
| Official Link | [maximum-number-of-visible-points](https://leetcode.com/problems/maximum-number-of-visible-points/) |

## Problem Description & Examples
### Goal
From a fixed location, count the maximum number of points visible inside any
viewing angle of the given size.

### Function Contract
**Inputs**

- `points`: point coordinates.
- `angle`: the viewing angle in degrees.
- `location`: the observer coordinate.

**Return value**

The maximum number of visible points.

### Examples
**Example 1**

- Input: `points = [[2, 1], [2, 2], [3, 3]], angle = 90, location = [1, 1]`
- Output: `3`

**Example 2**

- Input: `points = [[2, 1], [2, 2], [3, 4], [1, 1]], angle = 90, location = [1, 1]`
- Output: `4`

**Example 3**

- Input: `points = [[1, 0], [2, 1]], angle = 13, location = [1, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Points equal to the observer location are always visible, so count them
separately. Convert every other point to its polar angle around the observer,
sort those angles, and duplicate the list with each angle plus `360` to handle
wraparound. Use a sliding window to find the largest angle span within `angle`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(n)`.
