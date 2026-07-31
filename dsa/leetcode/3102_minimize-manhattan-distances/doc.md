# Minimize Manhattan Distances

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3102 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Geometry, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimize-manhattan-distances](https://leetcode.com/problems/minimize-manhattan-distances/) |

## Problem Description

### Goal

An array `points` describes points on a two-dimensional plane, with `points[i] = [x_i, y_i]`. The Manhattan distance between two points is the sum of the absolute differences of their coordinates:

$$
lvert x_i - x_j vert + lvert y_i - y_j vert.
$$

Remove exactly one point. For each possible removal, consider every pair among the remaining points and take their maximum Manhattan distance. Return the minimum value that this maximum can have over all choices of the removed point.

The input always contains at least three points, so at least two points remain and the pairwise maximum is well-defined. Equal coordinates are allowed and still represent separate removable points.

### Function Contract

**Inputs**

- `points`: An array of $n$ coordinate pairs `[x, y]`, where $3 \le n \le 10^5$, every pair has length two, and $1 \le x, y \le 10^8$.

**Return value**

- The minimum possible maximum Manhattan distance between any two remaining points after removing exactly one point.

### Examples

**Example 1**

- Input: `points = [[3, 10], [5, 15], [10, 2], [4, 4]]`
- Output: `12`
- Explanation: Removing `[10, 2]` leaves a maximum distance of $12$, attained by `[5, 15]` and `[4, 4]`. Removing any other point leaves a maximum of $15$ or $18$.

**Example 2**

- Input: `points = [[1, 1], [1, 1], [1, 1]]`
- Output: `0`
- Explanation: Whichever point is removed, the two remaining points coincide, so their Manhattan distance is zero.
