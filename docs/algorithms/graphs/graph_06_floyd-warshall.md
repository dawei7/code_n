# Floyd-Warshall (All-Pairs Shortest Path)

| | |
|---|---|
| **ID** | `graph_06` |
| **Category** | graphs |
| **Complexity (required)** | O(n³) |
| **Difficulty** | 6/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) |

## Problem statement

Given a **weighted graph** `G = (V, E)` (with possibly
negative weights but **no negative cycles**), find the
**shortest distance between every pair of vertices**.

**Input:** a graph with `n` vertices and edge weights.
**Output:** an `n × n` distance matrix `dist[u][v]` = the
shortest distance from `u` to `v` (or `+∞` if unreachable).

**Example:**

```
Weighted directed graph (4 nodes):
  0 → 1   (5)
  0 → 3   (10)
  1 → 2   (3)
  2 → 3   (1)
  3 → 0   (2)  ← note the back edge

Initial distance matrix:
       0    1    2    3
  0  [ 0,   5,   ∞,  10 ]
  1  [ ∞,   0,   3,   ∞ ]
  2  [ ∞,   ∞,   0,   1 ]
  3  [ 2,   ∞,   ∞,   0 ]

After Floyd-Warshall:
       0    1    2    3
  0  [ 0,   5,   8,   9 ]   ← 0→1→2 = 8, 0→1→2→3 = 9
  1  [ 5,   0,   3,   4 ]   ← 1→2→3 = 4
  2  [ 3,   ∞,   0,   1 ]   ← 2→3→0 = 3
  3  [ 2,   7,  10,   0 ]   ← 3→0→1 = 7, 3→0→1→2 = 10
```

## When to use it

- The **all-pairs** shortest-path problem. When you need
  distances from every vertex to every other, Floyd-Warshall
  is the standard answer.
- Foundation for **transitive closure**, **graph diameter**,
  **betweenness centrality** (with Johnson's reweighting),
  and **detecting negative cycles**.

## Approach

For each intermediate vertex `k`, check whether going
through `k` shortens the path between every pair `(i, j)`.

**Recurrence:**
```
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

for every intermediate `k = 0..n-1`. After processing all
intermediate vertices, `dist[i][j]` is the shortest
`i → j` distance.

**Why it works:** after processing intermediate vertices
`{0..k-1}`, the matrix `dist` holds the shortest paths
that use only those intermediates. Adding `k` as a possible
intermediate: the shortest `i → j` using intermediates from
`{0..k}` is either the old `i → j` or a path that goes
through `k`, i.e. `i → k → j`. Both halves use only
intermediates from `{0..k-1}` (already computed), so
`dist[i][k]` and `dist[k][j]` are correct.

**Negative cycle detection:** after the algorithm, if any
`dist[i][i] < 0`, there's a negative cycle reachable from
`i`.

**Path reconstruction:** maintain a parallel `next[i][j]`
matrix. Update it whenever you update `dist[i][j]`.

## Algorithm (pseudocode)

```
floyd_warshall(weight):
    n = len(weight)
    dist = [row[:] for row in weight]      # copy
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```

## Walk-through

Graph from the example. 4×4 matrix.

After `k=0`: paths can use vertex 0 as intermediate.
- (1, 3): 1→0→3 = ∞ + 2 = ∞. No improvement.
- (1, 0): 1→0 = ∞. No improvement.
- (3, 1): 3→0→1 = 2 + 5 = 7. **dist[3][1] = 7**. ✓
- (2, 1): 2→3→0→1 = 1+2+5 = 8. No (we need 0 as only intermediate; 2→3 is OK but 3→0 is direct, but then 0→1 is also direct, and we need k=1 to be done first). Wait — the algorithm considers k in order. After k=0, we can use vertex 0 as intermediate. (2, 1) needs 2→...→1: 2→3→0→1. After k=0, 2→3→0 is computed if 0's value is already in dist[2][3] (= 1) and dist[3][0] (= 2). Wait, those are direct edges, set in initialization. So dist[2][0] = 1+2 = 3. Then dist[2][1] = 3+5 = 8. ✓

After k=1: paths can use vertices {0, 1} as intermediates.
- (0, 2): 0→1→2 = 5+3 = 8. **dist[0][2] = 8**. ✓
- (0, 3): 0→1→2→3 = 5+3+1 = 9. **dist[0][3] = 9**. ✓
- (2, 3): 2→3 = 1 (direct) vs 2→0→1→3 = 3+5+∞ = ∞. No improvement.
- (2, 0): 2→3→0 = 1+2 = 3. ✓ (or 2→1→0 = 3+∞ = ∞)
- (3, 2): 3→0→1→2 = 2+5+3 = 10. **dist[3][2] = 10**. ✓

After k=2: paths can use {0, 1, 2}.
- All already optimal.

After k=3: paths can use {0, 1, 2, 3}.
- (1, 0): 1→2→3→0 = 3+1+2 = 6. No (already 5).
- All optimal.

Final matrix matches the example. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n³) | O(n²) |
| **Average** | O(n³) | O(n²) |
| **Worst** | O(n³) | O(n²) |

Three nested loops, each O(n). The in-place version uses
O(n²) space (just the distance matrix).

## Variants & optimizations

- **Transitive closure** — `weight` is a boolean (reachable
  or not). Floyd-Warshall computes the transitive closure
  in O(n³) — same code, different type.
- **Reconstruct the path** — track `next[i][j]` alongside
  `dist[i][j]`. To get the path `i → j`, if `next[i][j] =
  None`, no path; else include `j` and recurse on `i →
  next[i][j]`, then include `i` at the start.
- **Faster for sparse graphs** — Johnson's algorithm
  reweights to non-negative and runs `n` Dijkstras. Total
  O(n · (n + m) log n), which is faster when `m << n²`.
- **Detect negative cycles** — if `dist[i][i] < 0` after
  running, `i` is on a negative cycle.
- **Frequent queries on a small graph** — Floyd-Warshall
  preprocess once, query in O(1).

## Real-world applications

- **Routing protocols** — OSPF uses Dijkstra for single
  source, but BGP and similar use Floyd-Warshall-style
  analysis for inter-domain routing.
- **Network analysis** — all-pairs latency between
  datacenters.
- **Compiler optimization** — common subexpression
  elimination across basic blocks.
- **Social network analysis** — shortest path between
  every pair of users (graph diameter, betweenness).
- **Game theory** — finding equilibria via graph distances.
- **Biology** — phylogenetic distance matrices.

## Related algorithms in cOde(n)

- **[graph_04 — Dijkstra](graph_04_dijkstra.md)** — single
  source on non-negative weights. (d=5/10, r=8/10)
- **[graph_05 — Bellman-Ford](graph_05_bellman-ford.md)** —
  single source, allows negative weights. (d=6/10, r=8/10)
- **[graph_02 — BFS](graph_02_bfs.md)** — the unweighted
  special case of all-pairs (matrix-of-distances = matrix
  of reachability). (d=4/10, r=8/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
