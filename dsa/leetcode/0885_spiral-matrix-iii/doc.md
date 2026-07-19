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
