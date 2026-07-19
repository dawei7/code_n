# Convex Polygon

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 469 |
| Difficulty | Medium |
| Topics | Array, Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/convex-polygon/) |

## Problem Description
### Goal
Given polygon vertices in clockwise or counterclockwise boundary order, determine whether the polygon is convex. A convex polygon never changes turn direction as its boundary is traversed, including the closing edges back to the first vertices.

Return `True` when all nonzero cross products have the same sign. Collinear consecutive boundary points may be tolerated without creating an opposite turn, but any genuine left turn combined with a genuine right turn reveals a concavity and returns `False`. Vertex order is already the boundary order; do not reorder points or test only local angles without including wraparound triples.

### Function Contract
**Inputs**

- `points`: polygon vertices `[x, y]` listed in clockwise or counterclockwise boundary order

**Return value**

- `True` when the polygon never makes both left and right turns; otherwise `False`

### Examples
**Example 1**

- Input: `points = [[0, 0], [0, 1], [1, 1], [1, 0]]`
- Output: `True`

**Example 2**

- Input: `points = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]`
- Output: `False`

**Example 3**

- Input: `points = [[0, 0], [2, 0], [1, 2]]`
- Output: `True`
