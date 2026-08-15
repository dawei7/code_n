# Count Number of Trapezoids I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3623 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-trapezoids-i/) |

## Problem Description

### Goal

Each entry `[x, y]` in `points` marks a distinct point on the Cartesian plane. A horizontal trapezoid is a convex quadrilateral having at least one pair of sides parallel to the x-axis. Thus, the two endpoints of each such horizontal side share a y-coordinate, while the two sides lie at different heights.

Choose four distinct supplied points and count how many unique selections form horizontal trapezoids. Different four-point selections are counted separately, regardless of whether their shapes have the same dimensions. Return the total modulo $10^9+7$.

### Function Contract

**Inputs**

- `points`: Pairwise-distinct integer coordinate pairs `[x, y]`.

There are from 4 through $10^5$ points, and every coordinate lies in $[-10^8,10^8]$.

**Return value**

Return the number of distinct four-point selections forming horizontal trapezoids, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `points = [[1,0],[2,0],[3,0],[2,2],[3,2]]`
- **Output:** `3`
- **Explanation:** The lower level offers three horizontal point pairs, and the upper level offers one, producing three trapezoids.

#### Example 2

- **Input:** `points = [[0,0],[1,0],[0,1],[2,1]]`
- **Output:** `1`
- **Explanation:** Each of the two heights supplies exactly one horizontal side.

#### Example 3

- **Input:** `points = [[0,0],[1,0],[2,0],[3,0]]`
- **Output:** `0`
- **Explanation:** All points are collinear, so they cannot form a convex quadrilateral.
