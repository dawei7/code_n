# Minimum Number of Lines to Cover Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2152 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Backtracking, Bit Manipulation, Geometry, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-number-of-lines-to-cover-points](https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/) |

## Problem Description

### Goal

An array `points` gives distinct points on the Cartesian plane. You may add
straight lines of any position or slope. A point is covered when it lies on at
least one added line, and one line may cover any number of collinear points.

Return the minimum number of straight lines whose union covers every given
point. Lines may intersect and a point may lie on more than one selected line;
only complete coverage and the number of lines matter.

### Function Contract

**Inputs**

- `points`: An array of $n$ distinct coordinate pairs `[x, y]`, where
  $1 \leq n \leq 10$ and $-100 \leq x,y \leq 100$.

**Return value**

Return the fewest straight lines needed to cover all points.

### Examples

**Example 1**

- Input: `points = [[0, 1], [2, 3], [4, 5], [4, 3]]`
- Output: `2`
- Explanation: One line covers `(0, 1)` and `(4, 5)` together with `(2, 3)`;
  another line covers the remaining point.

**Example 2**

- Input: `points = [[0, 2], [-2, -2], [1, 4]]`
- Output: `1`
- Explanation: All three points lie on the same straight line.
