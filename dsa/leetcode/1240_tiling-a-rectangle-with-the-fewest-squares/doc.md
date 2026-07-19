# Tiling a Rectangle with the Fewest Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1240 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) |

## Problem Description

### Goal

Given an `n` by `m` rectangle, tile its entire area with axis-aligned squares whose side lengths are positive integers. Squares may have different sizes, but they must remain inside the rectangle, must not overlap, and must leave no uncovered area.

Return the minimum number of squares required. Rotating the rectangle does not change the problem, and a square matching the whole rectangle counts as one tile. The objective concerns the number of squares rather than their total area, since every valid tiling necessarily covers the same area.

### Function Contract

**Inputs**

- `n`: One rectangle dimension, where $1\le n\le13$.
- `m`: The other rectangle dimension, where $1\le m\le13$.

Define $h=\min(n,m)$ and $w=\max(n,m)$.

**Return value**

- The minimum number of integer-sided squares in a complete tiling of the rectangle.

### Examples

**Example 1**

- Input: `n = 2`, `m = 3`
- Output: `3`

One $2$ by $2$ square and two $1$ by $1$ squares tile the rectangle.

**Example 2**

- Input: `n = 5`, `m = 8`
- Output: `5`

No tiling with four squares exists, while five appropriately sized squares suffice.

**Example 3**

- Input: `n = 11`, `m = 13`
- Output: `6`

This rectangle has a six-square tiling, which is optimal.
