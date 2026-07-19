# Valid Boomerang

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1037 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/valid-boomerang/) |

## Problem Description

### Goal

You are given exactly three points on the x-y plane, with `points[i] = [xi, yi]`.

Return `true` when the three points form a boomerang. A boomerang requires all three points to be distinct and requires that they do not lie on one straight line. Thus any repeated coordinate makes the answer false, as does any placement where one common line contains every point, regardless of their input order.

### Function Contract

**Inputs**

- `points`: exactly three coordinate pairs.
- Every x- and y-coordinate is an integer between $0$ and $100$, inclusive.

**Return value**

- Whether the three points are distinct and non-collinear.

### Examples

**Example 1**

- Input: `points = [[1,1],[2,3],[3,2]]`
- Output: `true`

**Example 2**

- Input: `points = [[1,1],[2,2],[3,3]]`
- Output: `false`
- Explanation: All three points lie on the same diagonal line.
