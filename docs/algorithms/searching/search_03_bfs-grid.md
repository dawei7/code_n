# BFS Grid

| | |
|---|---|
| **ID** | `search_03` |
| **Category** | searching |
| **Complexity (required)** | O(n²) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) |

## Problem statement

Given a 2D grid of `W × H` cells, where each cell is either
**passable** (e.g. `0`) or **blocked** (e.g. `1`), find the
**shortest path** (in number of cells / moves) from a start
cell to a target cell. Movement is 4-directional
(up/down/left/right). The grid wraps nothing; edges of the
grid are walls.

**Input:** a 2D grid, a start `(sr, sc)`, a target `(tr, tc)`.
**Output:** the length of the shortest path, or `-1` if no
path exists. (Optionally, the path itself.)

**Example:**

```
S . . # . .       S = start
# # . # . T       T = target
. . . . . .       . = empty
. # # # . #
. . . . . .

Shortest S → T: 9 cells. Path: down 2, right 2, down 1, right 2, down 2.
```

## When to use it

- The **most-asked grid problem** in interviews. Often given
  with a twist: "rotting oranges", "walls and gates", "shortest
  bridge", "01 matrix", "island problems".
- Foundation for understanding **graph BFS** in concrete
  terms: each cell is a node, 4 neighbors are edges, the
  unweighted-graph BFS gives the shortest path.
- The BFS layer-by-layer pattern is also the basis for
  **multi-source BFS** (e.g. "rotting oranges" starts from all
  rotten cells simultaneously).

## Approach

Model the grid as a graph: each passable cell is a node, and
two cells are adjacent if they share an edge AND both are
passable. BFS from the start, expanding one layer at a time.
The first time we reach the target, that's the shortest path.

**BFS uses a queue** (FIFO). The standard "level-by-level"
pattern:
1. Enqueue `(sr, sc, 0)` (cell + distance).
2. While queue is non-empty:
   - Dequeue.
   - If it's the target, return the distance.
   - For each 4-neighbor that's passable and not yet visited,
     mark visited, enqueue with `distance + 1`.
3. Return -1 (target unreachable).

**Visited tracking:** use a 2D `visited` boolean array, or
**mutate the grid in place** by writing the distance into the
start cell. The latter saves O(n²) space but destroys the
input.

**Reconstructing the path:** alongside `visited`, store the
parent of each cell (the cell it was first reached from).
Then walk back from the target to the start.

## Algorithm (pseudocode)

```
bfs_shortest_path(grid, sr, sc, tr, tc):
    if grid[sr][sc] != 0 or grid[tr][tc] != 0:
        # start or target is blocked (or 1-indexed convention)
        return -1
    H, W = len(grid), len(grid[0])
    visited = [[False] * W for _ in range(H)]
    queue = deque([(sr, sc, 0)])
    visited[sr][sc] = True
    while queue:
        r, c, d = queue.popleft()
        if (r, c) == (tr, tc):
            return d
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W \
               and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append((nr, nc, d + 1))
    return -1
```

## Walk-through

```
grid:
  S . . #
  # # . .
  . . . T
```

Start `(0, 0)`, target `(2, 3)`. Walls at `(1, 0)`, `(1, 1)`.

Visited: `[[T, F, F, F], [F, F, F, F], [F, F, F, F]]`.

Queue: `[(0, 0, 0)]`.

**Step 1:** dequeue `(0, 0, 0)`. Neighbors `(1, 0)` (wall),
`(0, 1)` (empty). Enqueue `(0, 1, 1)`. Visited `(0, 1)`.

**Step 2:** dequeue `(0, 1, 1)`. Neighbors `(1, 1)` (wall),
`(0, 2)` (empty). Enqueue `(0, 2, 2)`.

**Step 3:** dequeue `(0, 2, 2)`. Neighbors `(1, 2)` (empty),
`(0, 3)` (wall). Enqueue `(1, 2, 3)`.

**Step 4:** dequeue `(1, 2, 3)`. Neighbors `(2, 2)` (empty),
`(0, 2)` (visited), `(1, 3)` (empty), `(1, 1)` (wall).
Enqueue `(2, 2, 4)`, `(1, 3, 4)`.

**Step 5:** dequeue `(2, 2, 4)`. Neighbors `(2, 3)` = target!
Return `5`.

Wait — that's wrong. Let me re-check. The target `(2, 3)` is
at distance 5 from `(0, 0)`. Path: `(0,0) → (0,1) → (0,2) →
(1,2) → (2,2) → (2,3)`, length 5. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(W·H) — must scan the whole reachable region | O(W·H) |
| **Average** | O(W·H) | O(W·H) |
| **Worst** | O(W·H) | O(W·H) |

Each cell is enqueued at most once. Each edge is examined at
most once. The queue can hold up to O(W·H) cells. The visited
array is O(W·H).

The required complexity is O(n²) for the cOde(n) engine
(n = max(W, H), so a W×H grid is O(n²)).

## Variants & optimizations

- **8-directional movement** — add 4 diagonals to the
  neighbor list. Distance metric becomes Chebyshev instead
  of Manhattan.
- **Weighted cells** — uniform-cost / Dijkstra instead of BFS.
  See `graph_04` (Dijkstra).
- **Multi-source BFS** — start with multiple cells in the
  queue (e.g. all rotten oranges at once). Each BFS layer
  expands from all sources simultaneously; useful for
  "min time to reach every cell".
- **0-1 BFS** — when edges have weight 0 or 1, use a deque
  and push to the front for weight-0 edges, to the back for
  weight-1 edges. O(V+E) without Dijkstra. See `graph_17`.
- **A\*** — when you have a good heuristic, A\* visits far
  fewer cells than BFS. See `graph_18`.
- **Bidirectional BFS** — start BFS from both the source and
  the target; stop when the two frontiers meet. ~2x speedup
  in practice for unweighted graphs.

## Real-world applications

- **Shortest path on a map** — given a road network, find the
  minimum number of turns. (Real road networks use weighted
  edges, so Dijkstra or A\* instead.)
- **Network packet routing** — finding the minimum-hop path
  in a network topology.
- **Social network "degrees of separation"** — BFS from
  person A, count layers until you hit person B.
- **Web crawlers** — BFS from a seed URL, follow links
  layer by layer, with politeness delays.
- **Garbage collection** — the "mark and sweep" GC walks the
  object graph in BFS order from root references.
- **Game AI pathfinding** — grid-based games use BFS for
  short paths; weighted grids use A\*.

## Related algorithms in cOde(n)

- **[search_04 — DFS Grid](search_04_dfs-grid.md)** — the
  other fundamental graph search. DFS is for reachability
  (any path); BFS is for shortest path. (d=4/10, r=8/10)
- **[graph_02 — Breadth-First Search](graph_02_bfs.md)** —
  the abstract BFS on adjacency lists, not grids.
  (d=5/10, r=8/10)
- **[graph_04 — Dijkstra](graph_04_dijkstra.md)** — BFS for
  weighted graphs. (d=5/10, r=8/10)
- **[graph_18 — A\* Search](graph_18_a-star.md)** — heuristic-
  guided BFS for weighted grids with a useful heuristic.
  (d=6/10, r=8/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
