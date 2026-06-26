# Best Position for a Service Centre

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1515 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Randomized |
| Official Link | [best-position-for-a-service-centre](https://leetcode.com/problems/best-position-for-a-service-centre/) |

## Problem Description & Examples
### Goal
Choose a point for a service centre so that the sum of Euclidean distances from
that point to all given customer positions is as small as possible.

### Function Contract
**Inputs**

- `positions`: a list of `[x, y]` coordinates.

**Return value**

The minimum possible total distance, accepted within a small floating-point
tolerance.

### Examples
**Example 1**

- Input: `positions = [[0, 1], [1, 0], [1, 2], [2, 1]]`
- Output: `4.0`

**Example 2**

- Input: `positions = [[1, 1], [3, 3]]`
- Output: `2.82843`

**Example 3**

- Input: `positions = [[1, 1]]`
- Output: `0.0`

---

## Underlying Base Algorithm(s)
The objective is convex over the plane. A common approach is nested ternary
search: for a fixed `x`, ternary-search the best `y`, then ternary-search `x`
using that inner optimum. Gradient descent with a shrinking step size is another
practical method for the same convex surface.

---

## Complexity Analysis
- **Time Complexity**: `O(n * I^2)` for nested ternary search with `I` iterations per dimension.
- **Space Complexity**: `O(1)` extra space.
