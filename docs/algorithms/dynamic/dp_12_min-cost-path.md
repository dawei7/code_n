# Min Cost Path

| | |
|---|---|
| **ID** | `dp_12` |
| **Category** | dynamic |
| **Complexity (required)** | O(n²) |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem) |

## Problem statement

Given an `m × n` grid of **non-negative** integers (the
"cost" of each cell), find a path from the top-left to the
bottom-right that **minimizes the total cost**. You can only
move **right or down**.

**Input:** a 2D grid of non-negative integers.
**Output:** the minimum total cost of a path from
`grid[0][0]` to `grid[m-1][n-1]`.

**Example:**

```
  1  3  1
  1  5  1
  4  2  1

Min-cost path: 1 → 1 → 1 → 1 → 1 = 5
  (right, down, right, down, right;
   cells: (0,0)→(0,1)→(0,2)→(1,2)→(2,2) = 1+3+1+1+1 = 7
   actually that's 7; the minimum is:
   (0,0)→(1,0)→(2,0)→(2,1)→(2,2) = 1+1+4+2+1 = 9 (worse))
   
   Let me retrace: 1+1+1+1+1 = 5 with cells (0,0),(1,0),(1,1),(1,2),(2,2)? No, (1,0)→(1,1) is "right" not "down". Movement is right or down.
   (0,0)→(0,1)→(0,2)→(1,2)→(2,2) = 1+3+1+1+1 = 7
   (0,0)→(0,1)→(1,1)→(2,1)→(2,2) = 1+3+5+2+1 = 12
   (0,0)→(0,1)→(1,1)→(1,2)→(2,2) = 1+3+5+1+1 = 11
   (0,0)→(1,0)→(1,1)→(1,2)→(2,2) = 1+1+5+1+1 = 9
   (0,0)→(1,0)→(2,0)→(2,1)→(2,2) = 1+1+4+2+1 = 9
   (0,0)→(0,1)→(1,1)→(2,1)→(2,2) = 1+3+5+2+1 = 12
   (0,0)→(0,1)→(0,2)→(1,2)→(2,2) = 1+3+1+1+1 = 7
   Hmm 7 seems best. Let me try:
   (0,0)→(1,0)→(1,1)→(1,2)→(2,2) = 1+1+5+1+1 = 9
   (0,0)→(0,1)→(1,1)→(1,2)→(2,2) = 1+3+5+1+1 = 11
   So the answer is 7.
```

| Grid | Min cost |
|---|---:|
| `[[1, 3, 1], [1, 5, 1], [4, 2, 1]]` | 7 |
| `[[1, 2, 3], [4, 5, 6]]` | 12 (1+2+3+6) |
| `[[1]]` | 1 |

## When to use it

- The classic "**count paths with a cost**" DP. Asked in
  phone screens, often with a small twist (obstacles, with
  diagonals, with up/down/left/right).
- Foundation for **robot motion planning** on weighted
  grids, **lowest-effort routes** in terrain analysis, and
  many **lowest-cost path** variants.

## Approach

Let `dp[i][j]` = the minimum cost to reach cell `(i, j)`
from `(0, 0)`.

**Recurrence:** to reach `(i, j)`, we must have come from
either `(i-1, j)` (down) or `(i, j-1)` (right). Take the
cheaper of those, plus the cost of the current cell:
```
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
```

**Base case:** `dp[0][0] = grid[0][0]`.
`dp[0][j] = grid[0][j] + dp[0][j-1]` (only right moves).
`dp[i][0] = grid[i][0] + dp[i-1][0]` (only down moves).

**Answer:** `dp[m-1][n-1]`.

**Space optimization:** `dp[i][j]` only depends on the cell
above and the cell to the left, so the 2D table collapses
into a 1D array of size `n`. Iterate left-to-right, and
the "above" cell is `dp[j]` (current) while the "left" cell
is `dp[j-1]` (just updated):
```
dp[j] = grid[i][j] + min(dp[j], dp[j-1])
```

## Algorithm (pseudocode)

```
min_cost_path(grid):
    m, n = len(grid), len(grid[0])
    dp = [grid[0][0]] + [0] * (n - 1)
    for j from 1 to n - 1:
        dp[j] = dp[j-1] + grid[0][j]
    for i from 1 to m - 1:
        dp[0] += grid[i][0]
        for j from 1 to n - 1:
            dp[j] = grid[i][j] + min(dp[j], dp[j-1])
    return dp[n - 1]
```

## Walk-through

Grid: `[[1, 3, 1], [1, 5, 1], [4, 2, 1]]`.

After row 0: `dp = [1, 4, 5]`.

**i = 1:**
- `dp[0] += grid[1][0]` → `dp[0] = 1 + 1 = 2`.
- `dp[1] = 5 + min(4, 2) = 7`.
- `dp[2] = 1 + min(5, 7) = 6`.

After row 1: `dp = [2, 7, 6]`.

**i = 2:**
- `dp[0] += grid[2][0]` → `dp[0] = 2 + 4 = 6`.
- `dp[1] = 2 + min(7, 6) = 8`.
- `dp[2] = 1 + min(6, 8) = 7`.

After row 2: `dp = [6, 8, 7]`.

Answer: `dp[2] = 7`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(m·n) | O(n) with rolling |
| **Average** | O(m·n) | O(n) |
| **Worst** | O(m·n) | O(n) |

The required complexity is O(n²) for the cOde(n) engine
where `n = max(m, n)`.

## Variants & optimizations

- **With obstacles** — treat blocked cells as infinity.
- **With diagonals** — add `(i-1, j-1)` to the candidates.
- **Maximum-cost path** — replace `min` with `max`.
- **With up/down/left/right** — turn it into Dijkstra
  on the grid graph (since all costs are non-negative).
- **Reconstruct the path** — store a `parent[i][j]` (or
  `parent[j]` in the rolling version) and walk back.
- **Min-cost path with K turns** — the count of direction
  changes is bounded. Add a state dimension.

## Real-world applications

- **Robot motion planning** — find the cheapest path
  through a weighted terrain.
- **Lowest-energy route** in a road network (where weights
  are fuel or time).
- **Game AI** — pathfinding on a cost grid.
- **Image processing** — seam carving (find the lowest-cost
  path from top to bottom).
- **Logistics** — cheapest delivery route.
- **Bioinformatics** — sequence alignment with non-negative
  scores (the weighted edit distance for proteins).

## Related algorithms in cOde(n)

- **[dp_10 — Unique Paths](dp_10_unique-paths.md)** —
  *counts* all paths; this finds the *cheapest*. (d=4/10, r=9/10)
- **[dp_23 — Min Cost Climbing Stairs](dp_23_min-cost-climbing-stairs.md)** —
  1D version. (d=3/10, r=9/10)
- **[graph_04 — Dijkstra](graph_04_dijkstra.md)** — min-cost
  path on a general graph with weighted edges. (d=5/10, r=8/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
