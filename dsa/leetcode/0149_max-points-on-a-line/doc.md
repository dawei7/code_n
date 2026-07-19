# Max Points on a Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 149 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-points-on-a-line/) |

## Problem Description
### Goal
Given a collection of unique points with integer coordinates in the two-dimensional plane, consider every straight line that can pass through one or more of them. A point belongs to a line only when its coordinates satisfy exactly the same geometric direction and offset as the other points on that line.

Return the greatest number of input points lying on a single line. Vertical, horizontal, positive-slope, and negative-slope lines all count, and equivalent slopes must not be separated merely because they are represented by different fractions or signs. With one point the answer is one; the function returns only the maximum count, not a line equation or the selected points.

### Function Contract
**Inputs**

- `points`: a list of distinct coordinates `[x, y]`

**Return value**

The maximum number of collinear points.

### Examples
**Example 1**

- Input: `points = [[1,1],[2,2],[3,3]]`
- Output: `3`

**Example 2**

- Input: `points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]`
- Output: `4`

**Example 3**

- Input: `points = [[0,0],[0,1],[0,-1],[2,3]]`
- Output: `3`
