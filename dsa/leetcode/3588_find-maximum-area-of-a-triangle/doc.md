# Find Maximum Area of a Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3588 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Greedy, Geometry, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-maximum-area-of-a-triangle/) |

## Problem Description

### Goal

The array `coords` gives $n$ distinct points on an infinite Cartesian plane. Choose three of those points as the vertices of a triangle, with the additional requirement that at least one of its sides is parallel to either the x-axis or the y-axis.

Among all qualifying non-degenerate triangles, maximize the area. Return twice that maximum area, so the result is the integer product of the chosen axis-parallel base length and its perpendicular height. A collinear choice has zero area and is not a triangle for this problem.

If no three supplied points form a positive-area triangle with an axis-parallel side, return `-1`.

### Function Contract

**Inputs**

- `coords`: An array of $n$ unique coordinate pairs `[x, y]`, where $1 \le n \le 10^5$ and $1 \le x,y \le 10^6$.

**Return value**

Return twice the greatest positive area of a qualifying triangle, or `-1` if no such triangle exists.

### Examples

#### Example 1

- **Input:** `coords = [[1, 1], [1, 2], [3, 2], [3, 3]]`
- **Output:** `2`
- **Explanation:** A vertical base of length $1$ and horizontal height $2$ gives twice-area $1 \cdot 2 = 2$.

#### Example 2

- **Input:** `coords = [[1, 1], [2, 2], [3, 3]]`
- **Output:** `-1`
- **Explanation:** No pair of points shares an x-coordinate or a y-coordinate, so no side is axis-parallel.

#### Example 3

- **Input:** `coords = [[1, 2], [5, 2], [3, 10]]`
- **Output:** `32`
- **Explanation:** The horizontal base has length $4$ and the third point is $8$ units from its line.
