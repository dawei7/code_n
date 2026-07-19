# Surface Area of 3D Shapes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 892 |
| Difficulty | Easy |
| Topics | Array, Math, Geometry, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/surface-area-of-3d-shapes/) |

## Problem Description
### Goal
An $n \times n$ `grid` describes stacks of axis-aligned unit cubes. The value `grid[i][j]` is the number of cubes placed vertically above cell `(i, j)`; a zero leaves that cell empty.

Every pair of cubes sharing a face is glued together, possibly forming several separate irregular three-dimensional shapes. Return the total area of all faces exposed to the outside. Horizontal bottom faces resting beneath nonempty towers count toward the surface area.

### Function Contract
**Inputs**

- `grid`: an $n \times n$ matrix of tower heights, where $1 \leq n \leq 50$ and $0 \leq \texttt{grid[i][j]} \leq 50$.

**Return value**

Return the total exposed surface area of all shapes formed by the glued cubes, including their bottom faces.

### Examples
**Example 1**

- Input: `grid = [[1,2],[3,4]]`
- Output: `34`

**Example 2**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `32`

**Example 3**

- Input: `grid = [[2,2,2],[2,1,2],[2,2,2]]`
- Output: `46`
