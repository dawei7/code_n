# Minimum Score Triangulation of Polygon

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1039 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [minimum-score-triangulation-of-polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) |

## Problem Description & Examples
### Goal
Given values on the vertices of a convex polygon in order, split the polygon into triangles. The score of a triangle is the product of its three vertex values. Return the minimum total triangulation score.

### Function Contract
**Inputs**

- `values`: List[int] polygon vertex values in circular order

**Return value**

int - minimum possible triangulation score

### Examples
**Example 1**

- Input: `values = [1, 2, 3]`
- Output: `6`

**Example 2**

- Input: `values = [3, 7, 4, 5]`
- Output: `144`

**Example 3**

- Input: `values = [1, 3, 1, 4, 1, 5]`
- Output: `13`

---

## Underlying Base Algorithm(s)
Interval dynamic programming.

---

## Complexity Analysis
- **Time Complexity**: `O(n^3)`
- **Space Complexity**: `O(n^2)`
