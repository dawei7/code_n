# Perfect Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 391 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Geometry, Sweep Line |
| Official Link | [LeetCode](https://leetcode.com/problems/perfect-rectangle/) |

## Problem Description
### Goal
Given axis-aligned rectangles described by lower-left and upper-right coordinates, determine whether their union is exactly one larger axis-aligned rectangle. Every small rectangle has positive area and may meet others along edges or corners.

Return `True` only when the small rectangles cover every point of the bounding rectangle exactly once in area: no positive-area overlap, internal gap, detached component, or protrusion is allowed. Shared internal boundaries are permitted. The total covered area and exposed corner structure must both agree with one rectangle, since either test alone can miss an invalid arrangement. Return `False` for every imperfect cover.

### Function Contract
**Inputs**

- `rectangles`: rectangles encoded as `[x1, y1, x2, y2]`, where `(x1, y1)` is the lower-left corner and `(x2, y2)` is the upper-right corner

**Return value**

- Return `True` only when the rectangles form an exact rectangular cover; otherwise return `False`.

### Examples
**Example 1**

- Input: `rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]`
- Output: `True`

**Example 2**

- Input: `rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]`
- Output: `False`

**Example 3**

- Input: `rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]`
- Output: `False`
