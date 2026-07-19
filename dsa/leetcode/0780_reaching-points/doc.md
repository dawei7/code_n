# Reaching Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 780 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reaching-points/) |

## Problem Description

### Goal

Begin at a point `(sx, sy)` whose coordinates are positive integers. In one move, replace exactly one coordinate by the sum of both current coordinates, changing `(x, y)` into either $(x + y, y)$ or $(x, x + y)$.

Given target point `(tx, ty)`, return `True` if a finite sequence of allowed moves reaches it exactly and `False` otherwise. Coordinates never decrease during forward moves, and you may choose which coordinate grows independently at each step.

### Function Contract

**Inputs**

- `sx`, `sy`: the positive coordinates of the starting point.
- `tx`, `ty`: the positive coordinates of the target point.

**Return value**

- `True` if some sequence of allowed additions reaches `(tx, ty)`; otherwise `False`.

### Examples

**Example 1**

- Input: `sx = 1, sy = 1, tx = 3, ty = 5`
- Output: `True`
- Explanation: `(1,1) -> (1,2) -> (3,2) -> (3,5)`.

**Example 2**

- Input: `sx = 1, sy = 1, tx = 2, ty = 2`
- Output: `False`
- Explanation: A move increases exactly one coordinate, so equal coordinates cannot both change from `(1,1)` to `(2,2)`.

**Example 3**

- Input: `sx = 1, sy = 1, tx = 1, ty = 1`
- Output: `True`
- Explanation: No moves are required.
