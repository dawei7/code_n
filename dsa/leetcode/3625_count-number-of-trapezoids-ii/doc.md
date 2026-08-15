# Count Number of Trapezoids II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3625 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-trapezoids-ii/) |

## Problem Description

### Goal

You are given a list `points` of pairwise distinct points on the Cartesian plane. Each entry `points[i] = [x_i, y_i]` supplies the integer coordinates of one point.

Choose four distinct points. They form a trapezoid when their convex hull is a convex quadrilateral having at least one pair of parallel opposite sides. Parallel lines have equal slopes. A parallelogram therefore qualifies as a trapezoid because it has two parallel-side pairs, but the same set of four vertices is still only one unique trapezoid. Return the number of distinct four-point selections that satisfy this definition.

### Function Contract

**Inputs**

- `points`: A list of $n$ pairwise distinct integer-coordinate points, where $4 \le n \le 500$ and every coordinate lies from $-1000$ through $1000$.

**Return value**

Return the number of unique four-point subsets whose convex hull is a trapezoid.

### Examples

#### Example 1

- **Input:** `points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]`
- **Output:** `2`
- **Explanation:** Two different four-point selections form convex quadrilaterals with parallel opposite sides.

#### Example 2

- **Input:** `points = [[0,0],[1,0],[0,1],[2,1]]`
- **Output:** `1`
- **Explanation:** The four points form one trapezoid with horizontal parallel sides.
