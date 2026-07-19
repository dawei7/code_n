# Largest Triangle Area

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 812 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-triangle-area/) |

## Problem Description

### Goal

Given an array of unique points on the two-dimensional coordinate plane, choose any three different points as the vertices of a triangle.

Return the maximum geometric area obtainable over all such triples. Collinear triples have area `0` and remain valid candidates but cannot beat a positive-area triangle. The vertex order does not create a different triangle, and an answer within $10^{-5}$ of the exact maximum is accepted.

### Function Contract

**Inputs**

- `points`: at least three distinct integer coordinate pairs `[x, y]`.

**Return value**

- The largest triangle area obtainable from any three input points.

### Examples

**Example 1**

- Input: `points = [[0,0],[0,1],[1,0],[0,2],[2,0]]`
- Output: `2.0`
- Explanation: The points `[0,0]`, `[0,2]`, and `[2,0]` form a right triangle with area 2.

**Example 2**

- Input: `points = [[0,0],[4,0],[0,3]]`
- Output: `6.0`
- Explanation: The only triangle has base 4, height 3, and area 6.

**Example 3**

- Input: `points = [[0,0],[1,1],[2,2]]`
- Output: `0.0`
- Explanation: The three collinear points form a degenerate triangle.
