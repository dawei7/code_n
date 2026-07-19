# Triangle Judgement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 610 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/triangle-judgement/) |

## Problem Description
### Goal
Given a `Triangle` table whose rows contain three positive line-segment lengths `x`, `y`, and `z`, report whether the three segments in each row can form a triangle. A valid triangle is nondegenerate, so the sum of any two side lengths must be strictly greater than the remaining side.

Return every original row together with a column named `triangle`, using `Yes` when its three lengths satisfy the triangle condition and `No` otherwise. Every input row produces one output row, and the result table may be returned in any order.

### Function Contract
**Inputs**

- `Triangle(x, y, z)`: one row per triple of positive integer side lengths

**Return value**

- The original columns `x`, `y`, and `z`, plus a column named `triangle`
- `triangle` is `Yes` when the three sides can form a triangle and `No` otherwise
- Every input row produces exactly one output row

### Examples
**Example 1**

- Input row: `(13, 15, 30)`
- Output row: `(13, 15, 30, No)`

**Example 2**

- Input row: `(10, 20, 15)`
- Output row: `(10, 20, 15, Yes)`
