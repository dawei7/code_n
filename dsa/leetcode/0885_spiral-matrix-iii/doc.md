# Spiral Matrix III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 885 |
| Difficulty | Medium |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/spiral-matrix-iii/) |

## Problem Description
### Goal
Consider a `rows x cols` grid whose northwest corner is `(0, 0)` and whose southeast corner is `(rows - 1, cols - 1)`. Begin at the in-bounds cell `(rStart, cStart)` while facing east.

Walk along a clockwise spiral until every grid position has been visited. The path continues normally when it moves outside the grid boundary and may later re-enter the grid; leaving the rectangle does not cause an early turn. Return all `rows * cols` in-bounds coordinates in the order the spiral first visits them.

### Function Contract
Let $m = \max(\texttt{rows}, \texttt{cols})$.

**Inputs**

- `rows`: the number of grid rows, where $1 \leq \texttt{rows} \leq 100$.
- `cols`: the number of grid columns, where $1 \leq \texttt{cols} \leq 100$.
- `rStart`: the starting row, where $0 \leq \texttt{rStart} < \texttt{rows}$.
- `cStart`: the starting column, where $0 \leq \texttt{cStart} < \texttt{cols}$.

**Return value**

Return the grid coordinates in the exact order in which the clockwise spiral visits them.

### Examples
**Example 1**

- Input: `rows = 1, cols = 4, rStart = 0, cStart = 0`
- Output: `[[0,0],[0,1],[0,2],[0,3]]`

**Example 2**

- Input: `rows = 5, cols = 6, rStart = 1, cStart = 4`
- Output: `[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]`

**Example 3**

- Input: `rows = 2, cols = 2, rStart = 1, cStart = 0`
- Output: `[[1,0],[1,1],[0,0],[0,1]]`

The spiral leaves the grid after visiting the bottom row, then later re-enters at the top-left cell.

### Required Complexity
- **Time:** $O(m^2)$
- **Space:** $O(\texttt{rows} \cdot \texttt{cols})$

<details>
<summary>Approach</summary>

#### General

**Generate the spiral on the infinite lattice**

A clockwise spiral starting east travels one step east, one south, two west, two north, three east, three south, and so on. Keep the current coordinate, cycle through the directions east, south, west, and north, and increase the segment length after every two directions. This movement rule is independent of the finite grid boundary.

**Record only positions inside the rectangle**

The starting cell is valid and enters the result first. After every subsequent unit step, test whether `0 <= row < rows` and `0 <= column < cols`; append the coordinate only when both inequalities hold. Stop immediately once the result contains `rows * cols` coordinates.

The direction and segment-length schedule traces consecutive expanding square rings without revisiting a lattice point. Every grid cell lies within some finite ring around the start, so the walk eventually reaches it even if intervening portions are outside the rectangle. Filtering preserves the spiral's visit order, and stopping after the grid's full number of distinct cells proves that the result is complete.

#### Complexity detail

The farthest grid corner is at coordinate distance $O(m)$ from the start. Reaching the enclosing spiral ring takes $O(m^2)$ unit steps. The returned list contains exactly `rows * cols` coordinate pairs and therefore uses $O(\texttt{rows} \cdot \texttt{cols})$ space; apart from that required output, the simulation uses $O(1)$ space.

#### Alternatives and edge cases

- **Turn at grid boundaries:** This ordinary matrix-spiral rule is incorrect because the required path continues outside the rectangle before its scheduled turn.
- **Construct each square ring by its four sides:** Ring endpoints can be generated directly with the same $O(m^2)$ bound, but careful corner handling is needed to preserve the exact order.
- **Track visited coordinates:** The infinite spiral never revisits a lattice position, so a visited set is unnecessary; a list-membership check can make the implementation quadratic in the output size.
- **One-cell grid:** Return the starting coordinate immediately without taking a step.
- **Single row or column:** Most spiral steps are outside the grid, but later re-entry still produces every cell in the required order.
- **Start near an edge:** Do not clamp coordinates or skip movement; update the full outside position on every unit step.
- **Completion condition:** Count recorded in-bounds cells rather than spiral rings, since the final cell may be reached partway through a segment.

</details>
