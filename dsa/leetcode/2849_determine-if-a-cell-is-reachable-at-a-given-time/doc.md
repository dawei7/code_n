# Determine if a Cell Is Reachable at a Given Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2849 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/) |

## Problem Description

### Goal

You are given a starting cell `(sx, sy)`, a destination `(fx, fy)`, and a non-negative integer `t` on an infinite two-dimensional grid.

During every second you must move from the current cell to one of its eight adjacent cells. Adjacent cells share either an edge or a corner, so a move may change the horizontal coordinate, the vertical coordinate, or both by one. Cells may be visited repeatedly.

Return whether it is possible to be at `(fx, fy)` after exactly `t` seconds. Reaching the destination earlier is not sufficient by itself because movement is mandatory during every remaining second.

### Function Contract

**Inputs**

- `sx`: The starting cell's horizontal coordinate.
- `sy`: The starting cell's vertical coordinate.
- `fx`: The destination cell's horizontal coordinate.
- `fy`: The destination cell's vertical coordinate.
- `t`: The exact number of seconds available.

The coordinate constraints are $1\le\texttt{sx},\texttt{sy},\texttt{fx},\texttt{fy}\le10^9$, and $0\le t\le10^9$.

**Return value**

- `true` exactly when a valid sequence of `t` mandatory moves ends at the destination; otherwise `false`.

### Examples

#### Example 1

- **Input:** `sx = 2, sy = 4, fx = 7, fy = 7, t = 6`
- **Output:** `true`
- **Explanation:** The destination's Chebyshev distance is `5`, and a six-move route can include one detour.

#### Example 2

- **Input:** `sx = 3, sy = 1, fx = 7, fy = 3, t = 3`
- **Output:** `false`
- **Explanation:** At least `4` moves are required because the horizontal coordinate differs by `4`.
