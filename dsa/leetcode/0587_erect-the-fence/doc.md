# Erect the Fence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 587 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/erect-the-fence/) |

## Problem Description
### Goal
You are given the coordinates of trees in a garden. Enclose every tree with a fence while using the minimum possible length of rope, and identify which trees are located exactly on the resulting fence perimeter.

Return the coordinates of all perimeter trees in any order. Trees lying between two corner trees on a straight fence edge are still exactly on the perimeter and must be included, while points strictly inside the enclosed region are excluded. If all trees are collinear, every tree lies on the fence.

### Function Contract
**Inputs**

- `trees: list[list[int]]`: distinct planar points `[x, y]`

**Return value**

- All input points on the convex hull boundary, including points in the interior of a straight boundary edge
- Points may be returned in any order

### Examples
**Example 1**

- Input: `trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]`
- Output: `[[1,1],[2,0],[4,2],[3,3],[2,4]]` in any order

**Example 2**

- Input: `trees = [[1,2],[2,2],[4,2]]`
- Output: all three collinear points

**Example 3**

- Input: `trees = [[5,5]]`
- Output: `[[5,5]]`
