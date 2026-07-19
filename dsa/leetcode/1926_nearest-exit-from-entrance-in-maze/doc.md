# Nearest Exit from Entrance in Maze

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) |
| Frontend ID | 1926 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a rectangular maze whose cells are either open (`"."`) or walls (`"+"`), together with the coordinates of an open entrance cell. From one open cell, one step may move up, down, left, or right to another open cell. Movement through a wall or outside the grid is forbidden.

An exit is an open cell on the outer border of the maze, except that the entrance itself never counts even when it lies on that border. Return the fewest steps needed to reach any exit from the entrance, or `-1` when no exit is reachable.

### Function Contract

**Inputs**

- `maze`: an $R \times C$ matrix containing only `"."` and `"+"`.
- `entrance`: `[row, column]` for an open cell in `maze`.
- $1 \le R,C \le 100$.

**Return value**

- Return the shortest four-directional path length from `entrance` to a different open boundary cell.
- Return `-1` if no such boundary cell is reachable.

### Examples

**Example 1**

- Input: `maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]`
- Output: `1`

The open cell directly above the entrance is an exit.

**Example 2**

- Input: `maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]`
- Output: `2`

The entrance is on the border but is excluded; the exit is at the other end of the row.

**Example 3**

- Input: `maze = [[".","+"]], entrance = [0,0]`
- Output: `-1`

### Required Complexity

- **Time:** $O(RC)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**Explore in increasing distance**

Run breadth-first search from the entrance. The queue initially contains the entrance at distance zero. When a cell is removed, inspect its four neighbors. Ignore coordinates outside the grid, walls, and cells already visited.

Mark a cell visited as soon as it is enqueued rather than when it is removed. This prevents two frontier cells from adding the same location and ensures each open cell is processed at most once.

**Recognize exits without accepting the entrance**

Mark the entrance before the search begins. For each newly discovered open neighbor, test whether its row is `0` or `R - 1`, or its column is `0` or `C - 1`. If so, return the current distance plus one.

Because BFS processes all cells at distance $d$ before any cell at distance $d+1$, the first discovered exit has the minimum possible path length. The entrance is never reconsidered, so a boundary entrance cannot be mistaken for a zero-step exit. If the queue empties, every reachable open cell has been examined and no exit exists.

#### Complexity detail

At most $RC$ cells enter the queue, and each checks four constant-time directions, giving $O(RC)$ time. The queue and visited state can each hold $O(RC)$ cells, so the space bound is $O(RC)$. The implementation reuses the maze to mark visited cells but the queue alone can still require linear space.

#### Alternatives and edge cases

- **Depth-first search for the first exit:** The first exit found by DFS need not be the nearest.
- **Repeated distance relaxation:** Bellman-Ford-style full-grid passes eventually find shortest distances but can require many scans.
- **Mark on dequeue:** This permits duplicate queue entries and wastes work.
- **Boundary entrance:** It is explicitly excluded, so at least one move is required.
- **Single-cell maze:** The only cell is the entrance, leaving no exit.
- **Several exits:** BFS returns the minimum distance without needing to enumerate all complete paths.
- **Sealed open region:** Exhausting the queue correctly returns `-1`.

</details>
