# Minimum Path Cost in a Hidden Grid

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/) |
| Frontend ID | 1810 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Interactive, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A robot starts on one open cell of a hidden $m \times n$ grid and must reach a distinct open target cell. Other cells are either blocked or open with a positive entry cost. Moving orthogonally into an open cell pays that destination cell's cost each time; the starting cell's own cost is not charged before the first move. The grid dimensions, layout, coordinates, target, and costs are unavailable to the submitted algorithm.

The native `GridMaster` interface reveals the grid through interaction. `canMove(direction)` reports whether `"U"`, `"R"`, `"D"`, or `"L"` is currently legal. `move(direction)` performs a legal move and returns the cost of the entered cell; an illegal move leaves the robot in place and returns `-1`. `isTarget()` reports whether the robot currently occupies the target. Return the minimum possible total entry cost from the initial cell to the target, or `-1` when no valid path connects them.

### Function Contract

**Native input**

- `master`: a stateful `GridMaster` initially positioned at the start cell.

**App-local input**

- `grid`: an $m \times n$ integer matrix with $1 \le m,n \le 100$. A value of `0` marks a blocked cell; a value from `1` through `100` is the cost of entering an open cell.
- `r1`, `c1`: the row and column of the open starting cell.
- `r2`, `c2`: the row and column of the distinct open target cell.
- Let $V$ be the number of open cells reachable from the start.

**Return value**

- Return the minimum sum of destination-cell costs along any orthogonal path from `(r1, c1)` to `(r2, c2)`.
- Do not include the starting cell's cost.
- Return `-1` if the target is outside the start's reachable component.

### Examples

**Example 1**

- Input: `grid = [[2,3],[1,1]], r1 = 0, c1 = 1, r2 = 1, c2 = 0`
- Output: `2`

Moving down and then left enters cells with costs `1` and `1`.

**Example 2**

- Input: `grid = [[0,3,1],[3,4,2],[1,2,0]], r1 = 2, c1 = 0, r2 = 0, c2 = 2`
- Output: `9`

The cheapest reachable route enters cells costing `2`, `4`, `2`, and `1`.

**Example 3**

- Input: `grid = [[1,0],[0,1]], r1 = 0, c1 = 0, r2 = 1, c2 = 1`
- Output: `-1`

Blocked cells separate the start and target.
