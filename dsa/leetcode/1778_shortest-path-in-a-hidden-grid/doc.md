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

### Required Complexity

- **Time:** $O(V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Map the hidden component without losing the robot**

Assign relative coordinate `(0, 0)` to the unknown start. Explore every direction from each discovered cell. After moving into a new cell, record its relative coordinate and whether it is the target. When that branch is finished, issue the opposite move so the physical robot returns to the parent cell. An explicit stack stores the next direction and required backtrack move for every active exploration frame, avoiding recursion-depth dependence.

**Why exploration records exactly the reachable cells**

A coordinate is added only after `canMove` confirms an edge and `move` traverses it, so every recorded cell is genuinely reachable. Conversely, exploration tests all four directions from every recorded cell. Any reachable but unrecorded cell would have a first edge from the recorded component, and that edge would have been tested and followed, which is a contradiction. Backtracking restores the robot to the coordinate represented by the parent frame, keeping later queries aligned with the map.

**Separate discovery from shortest-path search**

Depth-first exploration efficiently discovers the component but does not guarantee shortest distances. Once exploration finishes, run breadth-first search over the recorded coordinates from `(0, 0)`. BFS visits cells in nondecreasing distance, so the first visit to the target has the minimum number of moves. If exploration never observes `isTarget()`, return `-1`. The app-local adapter already has the matrix and performs this BFS directly.

#### Complexity detail

The native exploration enters each of the $V$ reachable cells once and tests four directions per cell. Its backtracking traverses each discovery edge a constant number of times. BFS also processes each reachable cell and at most four incident edges once, so total time is $O(V)$. The discovered-coordinate set, exploration stack, BFS queue, and visited set use $O(V)$ space.

#### Alternatives and edge cases

- **Recursive exploration:** A recursive DFS mirrors the physical backtracking naturally, but a long open corridor can exceed Python's recursion limit.
- **BFS directly through `GridMaster`:** A single stateful robot cannot occupy every queued frontier cell at once; it must first build a reusable map or repeatedly navigate between states.
- The target can be adjacent to the start, but the contract guarantees they are distinct.
- The target may exist in the hidden matrix while lying outside the start's reachable component.
- Cycles require a visited-coordinate set; otherwise physical exploration can repeat forever.
- Every exploratory move must have a matching opposite move when its branch ends.

</details>
