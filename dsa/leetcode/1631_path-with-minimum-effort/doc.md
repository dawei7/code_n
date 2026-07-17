# Path With Minimum Effort

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1631 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/path-with-minimum-effort/) |

## Problem Description
### Goal
A hiker starts at the top-left cell of a rectangular `heights` grid and must reach the bottom-right cell. Each cell records its elevation. From a cell, the hiker may move up, down, left, or right while remaining inside the grid.

The effort of a route is not the sum of its climbs. It is the greatest absolute height difference across any single pair of consecutive cells on that route. Return the minimum possible effort among all routes from the start to the destination.

### Function Contract
**Inputs**

- `heights`: an $R\times C$ integer matrix, where $1 \le R,C \le 100$ and $1 \le \texttt{heights[r][c]} \le 10^6$.
- Let $V=RC$ be the number of cells.

**Return value**

Return the minimum achievable maximum edge difference on a four-directional path from `(0,0)` to `(R - 1,C - 1)`.

### Examples
**Example 1**

- Input: `heights = [[1,2,2],[3,8,2],[5,3,5]]`
- Output: `2`

A route through heights `[1,3,5,3,5]` never changes by more than 2.

**Example 2**

- Input: `heights = [[1,2,3],[3,8,4],[5,3,5]]`
- Output: `1`

Following `[1,2,3,4,5]` keeps every step difference at 1.

**Example 3**

- Input: `heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]`
- Output: `0`

There is a start-to-finish route consisting entirely of height-1 cells.

### Required Complexity
- **Time:** $O(V\log V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Replace additive distance with a bottleneck distance.** For each cell, store the smallest route effort currently known from the start. Extending a route with an edge of height difference $w$ produces effort `max(current_effort, w)`. This relaxation is monotone: extending a route can never reduce its effort.

**Run Dijkstra with the minimax relaxation.** Put `(0,0)` in a min-heap with effort zero. Repeatedly remove the cell with the least tentative effort and relax its four neighbors using the maximum rule. Ignore stale heap entries whose effort no longer matches the cell's best record. Once the destination is removed, return its effort.

The standard Dijkstra finalization argument still applies. Suppose the removed cell had an undiscovered route with a smaller bottleneck. Along that route, the first not-yet-removed cell follows a removed predecessor whose effort was no greater; relaxing their edge would have inserted a heap candidate no larger than the claimed route effort. That candidate would precede the current removal, a contradiction. Thus the destination's first current heap removal is the optimum.

#### Complexity detail

The grid graph has $V=RC$ vertices and fewer than $4V$ directed neighbor edges. Each successful relaxation adds one heap entry, and heap operations cost $O(\log V)$, giving $O(V\log V)$ time. The effort matrix and heap use $O(V)$ space.

#### Alternatives and edge cases

- **Binary search plus reachability:** Search an effort threshold and run DFS or BFS using only admissible edges. This takes $O(V\log H)$ time for height range $H$ and is often practical.
- **Kruskal union-find:** Sort adjacent edges by difference and union them until start and destination connect. This also takes $O(V\log V)$ time.
- **Array-based Dijkstra:** Selecting the next cell by scanning every unsettled vertex preserves correctness but takes $O(V^2)$ time.
- A one-cell grid requires no moves and therefore has effort zero.
- A route may use more steps to avoid one large height jump; path length is not the objective.
- Flat connected regions can be traversed at zero effort.
- Movement is four-directional only; diagonal cells are not adjacent.

</details>
