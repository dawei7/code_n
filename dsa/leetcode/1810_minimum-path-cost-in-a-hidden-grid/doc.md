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

**Inputs**

- `master`: the stateful `GridMaster` initially positioned at the start cell.
- JSON fixtures configure it with `master.mode = "weighted"`, an $m \times n$ `master.grid`, and two-coordinate `master.start` and `master.target` arrays. A grid value of `0` marks a blocked cell; a value from `1` through `100` is the cost of entering an open cell. These fields are hidden harness state, not additional solution parameters.
- Grid dimensions satisfy $1 \le m,n \le 100$.
- Let $V$ be the number of open cells reachable from the start.

**Return value**

- Return the minimum sum of destination-cell costs along any orthogonal path from the hidden start to the hidden target.
- Do not include the starting cell's cost.
- Return `-1` if the target is outside the start's reachable component.

### Examples

#### Example 1

- Input fixture: `master = {"mode":"weighted","grid":[[2,3],[1,1]],"start":[0,1],"target":[1,0]}`
- **Output:** `2`

Moving down and then left enters cells with costs `1` and `1`.

#### Example 2

- Input fixture: `master = {"mode":"weighted","grid":[[0,3,1],[3,4,2],[1,2,0]],"start":[2,0],"target":[0,2]}`
- **Output:** `9`

The cheapest reachable route enters cells costing `2`, `4`, `2`, and `1`.

#### Example 3

- Input fixture: `master = {"mode":"weighted","grid":[[1,0],[0,1]],"start":[0,0],"target":[1,1]}`
- **Output:** `-1`

Blocked cells separate the start and target.
