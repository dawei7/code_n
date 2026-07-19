# Shortest Path in a Hidden Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1778 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/shortest-path-in-a-hidden-grid/) |

## Problem Description

### Goal

A robot occupies the starting cell of a hidden $m \times n$ grid. Every cell is either open or blocked, and a distinct open cell is the target. The grid dimensions, coordinates, obstacles, and target location are not directly available.

The native interface supplies a `GridMaster`. `canMove(direction)` reports whether the robot can move one cell in `"U"`, `"R"`, `"D"`, or `"L"`; `move(direction)` performs a legal move and otherwise leaves the robot in place; and `isTarget()` reports whether its current cell is the target. Discover enough of the hidden grid to return the minimum number of moves from the starting cell to the target, or `-1` if no path exists.

For deterministic app-local execution, the same contract is represented by `grid`: `-1` marks the unique start, `2` the unique target, `1` an open cell, and `0` a blocked cell.

### Function Contract

**Native input**

- `master`: a stateful `GridMaster` positioned at the start.
- Grid dimensions satisfy $1 \le m,n \le 500$.

**App-local input**

- `grid`: a rectangular matrix containing exactly one `-1` and one `2`; every other value is `0` or `1`.
- Movement is permitted only between orthogonally adjacent nonzero cells.
- Let $V$ be the number of open cells reachable from the start.

**Return value**

Return the number of edges in a shortest start-to-target path, or `-1` when the target is unreachable.

### Examples

**Example 1**

- Input: `grid = [[-1,2]]`
- Output: `1`
- Explanation: The target is one legal move to the right.

**Example 2**

- Input: `grid = [[0,0,-1],[1,1,1],[2,0,0]]`
- Output: `4`
- Explanation: The robot moves left across the middle row and then down to the target.

**Example 3**

- Input: `grid = [[-1,0],[0,2]]`
- Output: `-1`
- Explanation: Blocked cells isolate the target from the start.
