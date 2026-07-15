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

### Required Complexity
- **Time:** $O(n^2)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Start with each tower standing alone**

A tower of positive height `h` exposes one top face, one bottom face, and four vertical sides of height `h`, for `4 * h + 2` unit faces. An empty position contributes nothing.

**Remove faces hidden by neighboring towers**

Two horizontally adjacent towers of heights `h1` and `h2` touch along `min(h1, h2)` cube levels. At every touching level, one face from each tower becomes internal, so subtract `2 * min(h1, h2)` from the standalone total.

While scanning the matrix, compare each tower only with its north and west neighbors. Every horizontal adjacency is then processed exactly once. Vertical contacts within a tower are already excluded by the `4 * h + 2` tower formula. Therefore the remaining total contains every exterior top, bottom, boundary side, and height-difference face exactly once.

#### Complexity detail

Each of the $n^2$ grid positions performs constant work and at most two neighbor comparisons, so the running time is $O(n^2)$. The accumulator and local heights use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Expand every unit cube:** Storing occupied cube coordinates and testing six neighbors is correct but costs time and space proportional to the total number of cubes.
- **Inspect all four neighbors per tower:** Adding positive height differences against every direction also works in $O(n^2)$ time, but requires careful separate handling of top and bottom faces.
- **Subtract every shared face after summing six per cube:** This is conceptually direct but repeats work across vertical stacks that the tower formula collapses.
- **Zero-height cell:** It has no top or bottom and creates no shared face with a neighbor.
- **Bottom surfaces:** Every nonempty tower contributes one bottom face even though it rests on a grid cell.
- **Unequal adjacent heights:** Only the lower shared portion is hidden; the taller tower's excess side remains exposed.
- **Disconnected shapes:** Surface areas add normally because no face is shared across separated components.

</details>
