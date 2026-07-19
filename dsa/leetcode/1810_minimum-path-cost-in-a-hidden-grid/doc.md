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

### Required Complexity

- **Time:** $O(V\log V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Discover the weighted component while preserving physical position**

Assign relative coordinate `(0, 0)` to the unknown start. From each discovered coordinate, test all four directions. When a move reaches a new cell, store the cost returned by `master.move`, note the coordinate if `master.isTarget()` is true, and explore from there. After finishing that branch, move in the opposite direction to restore the robot to its parent position. An explicit stack tracks the next direction and backtrack command, avoiding recursion failure on a long component.

**Why the recorded map is complete and correctly weighted**

A coordinate is recorded only after a legal physical move, so every mapped cell is reachable. Every direction of every mapped cell is eventually tested; if another reachable cell were missing, the first edge from the mapped component to that cell would have been followed. The forward `move` returns exactly the cost of entering the newly recorded coordinate. Costs returned by later backtracking moves are deliberately ignored: exploration is only measurement, while the requested answer describes the cheapest hypothetical start-to-target path.

**Run Dijkstra after the target and costs are known**

The mapped component is a graph with at most four edges per vertex. Traversing an edge into coordinate $v$ costs the stored entry cost of $v$, and the start distance is zero. All weights are positive, so Dijkstra's algorithm is applicable. Repeatedly remove the coordinate with the smallest tentative distance from a min-heap and relax its mapped neighbors. The first non-stale removal of the target has minimum total cost. If exploration never encounters the target, return `-1`.

The app-local adapter receives the matrix and endpoints directly, so it skips physical discovery and runs the same Dijkstra relaxation over legal matrix neighbors.

#### Complexity detail

Native discovery tests four directions for each of the $V$ reachable cells and traverses every discovery edge only a constant number of times, taking $O(V)$ time. The grid graph has $O(V)$ edges. Dijkstra performs $O(V)$ heap removals and $O(V)$ successful relaxations, each costing $O(\log V)$, for $O(V\log V)$ total time. The mapped costs, exploration stack, distance map, and heap use $O(V)$ space.

#### Alternatives and edge cases

- **Breadth-first search:** BFS minimizes the number of moves, not the sum of unequal entry costs, and can choose an expensive short route.
- **Bellman-Ford relaxation:** It handles positive weights correctly but repeatedly scans all grid edges and can require $O(V^2)$ time here.
- **Recursive discovery:** It mirrors backtracking naturally but may exceed Python's recursion depth on a long reachable corridor.
- **Dijkstra directly through `GridMaster`:** One stateful robot cannot remain at every heap frontier coordinate; build a reusable map before weighted search.
- **Exploration cost versus answer cost:** Physical probing may enter cells many times, but those moves do not contribute to the returned minimum path value.
- **Starting cell:** Its stored matrix cost is excluded; initialize its distance to zero.
- **Unreachable target:** The target may exist in the hidden matrix without belonging to the discovered component.
- **Cycles:** Record coordinates before exploring them so a cycle cannot trigger repeated physical traversal.
- **Several routes:** A longer route can be cheaper when it avoids high-cost cells; Dijkstra compares total cost rather than step count.
- **Backtracking:** Every forward discovery move must be paired with its opposite move before the parent frame resumes.

</details>
