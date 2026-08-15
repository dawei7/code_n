# Escape the Spreading Fire

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2258 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/escape-the-spreading-fire/) |

## Problem Description

### Goal

A field is represented by an $m\times n$ grid. Grass cells are `0`, initial
fire cells are `1`, and impassable walls are `2`. You begin at the top-left
grass cell and need to reach the safehouse at the bottom-right grass cell.

During each minute, you first move to one cardinally adjacent grass cell.
After that move, every fire cell spreads simultaneously to adjacent non-wall
cells. You may wait at the starting cell before making the first move, but the
route must remain safe. Reaching the safehouse at the same minute the fire
reaches it is allowed; occupying any other cell when the fire arrives is not.

Return the greatest initial waiting time that still permits escape. Return
`-1` when even leaving immediately cannot succeed. If arbitrarily long waits
remain safe, return $10^9$.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix with $2\le m,n\le300$ and $4\le mn\le2\cdot10^4$.
- Each cell is `0`, `1`, or `2`; the start and safehouse are both grass.

**Return value**

Return the maximum safe number of minutes to wait at `(0, 0)`, using `-1` for
an impossible escape and `1000000000` when every finite waiting time is safe.

### Examples

#### Example 1

- **Input:** `grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]`
- **Output:** `3`

#### Example 2

- **Input:** `grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]`
- **Output:** `-1`

#### Example 3

- **Input:** `grid = [[0,0,0],[2,2,0],[1,2,0]]`
- **Output:** `1000000000`
