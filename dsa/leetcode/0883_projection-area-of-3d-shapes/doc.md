# Projection Area of 3D Shapes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 883 |
| Difficulty | Easy |
| Topics | Array, Math, Geometry, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/projection-area-of-3d-shapes/) |

## Problem Description
### Goal
An $n \times n$ `grid` describes a three-dimensional shape built from axis-aligned unit cubes. At position `[i][j]`, exactly `grid[i][j]` cubes are stacked into one vertical tower; a zero entry leaves that position empty.

Project the complete shape orthogonally onto the $xy$-, $yz$-, and $zx$-planes. Each projection is the shadow formed by looking along the remaining coordinate axis, and overlapping cubes contribute only once to a shadow. Return the sum of the three projection areas, measured in unit squares.

### Function Contract
**Inputs**

- `grid`: an $n \times n$ matrix of integer tower heights, where $1 \leq n \leq 50$ and $0 \leq \texttt{grid[i][j]} \leq 50$.

**Return value**

Return the total area of the shape's projections onto the $xy$-, $yz$-, and $zx$-planes.

### Examples
**Example 1**

- Input: `grid = [[1,2],[3,4]]`
- Output: `17`

**Example 2**

- Input: `grid = [[2]]`
- Output: `5`

**Example 3**

- Input: `grid = [[1,0],[0,2]]`
- Output: `8`
