# Shortest Path to Get Food

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1730 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-path-to-get-food/) |

## Problem Description

### Goal

You are located at the unique `'*'` cell of an $m\times n$ character grid and want to reach food as quickly as possible. A `'#'` cell contains food, an `'O'` cell is open space, and an `'X'` cell is an obstacle. The grid may contain multiple food cells.

One step moves to an orthogonally adjacent cell—north, east, south, or west—provided that cell lies inside the grid and is not an obstacle. Return the minimum number of steps needed to reach any food cell. If no food is reachable, return `-1`.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ matrix whose entries are `'*'`, `'#'`, `'O'`, or `'X'`, where $1 \le m,n \le 200$ and exactly one `'*'` appears.

**Return value**

- Return the length of a shortest valid path from `'*'` to any `'#'`, or `-1` when no such path exists.

### Examples

**Example 1**

- Input: `grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]`
- Output: `3`
- Explanation: The nearest food can be reached in three orthogonal steps.

**Example 2**

- Input: `grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]`
- Output: `-1`
- Explanation: Obstacles separate the start from the food.

**Example 3**

- Input: `grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]`
- Output: `6`
- Explanation: Of the two food cells, the lower one is reachable in six steps.

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Start a breadth-first search at the unique location**

Scan the grid to locate `'*'`, then place that coordinate in a queue with distance zero. Each legal move has the same cost of one, so breadth-first search visits reachable cells in non-decreasing path length.

**Expand each open cell only once**

For every dequeued cell, inspect its four orthogonal neighbors. Ignore coordinates outside the grid, obstacles, and positions already visited. Mark an open neighbor visited when it is enqueued, not when it is later removed; this prevents several frontier cells from inserting the same position.

**Return at the first food frontier**

If a legal neighbor is `'#'`, return the current distance plus one immediately. Every earlier BFS layer has already been exhausted, while later queue entries cannot have smaller distance, so this is the nearest reachable food even when several food cells exist. If the queue becomes empty without finding food, every reachable non-obstacle cell has been examined and the correct result is `-1`.

#### Complexity detail

The initial scan and the breadth-first search each inspect at most all $mn$ cells. Every visited cell enters the queue once and contributes four constant-time neighbor checks, for $O(mn)$ time. The visited set and queue can each contain $O(mn)$ coordinates, giving $O(mn)$ auxiliary space.

#### Alternatives and edge cases

- **Depth-first search with all distances:** DFS can enumerate reachable cells, but finding the shortest path requires careful distance relaxation or potentially many repeated paths; unweighted BFS provides the distance order directly.
- **Dijkstra's algorithm:** It is correct but adds an unnecessary priority queue because every move has identical cost.
- **Multiple food cells:** Return the distance to the first food reached by BFS, not a path to a predetermined food.
- **Adjacent food:** The result is one.
- **No reachable food:** Exhausting the queue returns `-1`, whether food is blocked or absent.
- **Boundary start:** Neighbor bounds must be checked before indexing the grid.
- **Visited timing:** Marking only when dequeued allows duplicate queue entries and can inflate work substantially.

</details>
