## General

**Turn a bottleneck path into descending connectivity**

For any threshold $T$, cells with values at least $T$ are usable, and a path has score at least $T$ exactly when start and destination are connected through those cells. As $T$ decreases, more cells become usable and connectivity can only increase.

The protected solution activates cells from greatest value to smallest. The first activation level at which the two endpoints become connected is the largest feasible threshold, hence the maximum possible path minimum.

Although the manifest summary mentions maximum-bottleneck Dijkstra, the exact code implements this equivalent descending union-find method.

**Sort all cells by value**

`q` stores triples `(value, row, column)` for every cell and sorts them ascending. Repeated `q.pop()` removes the greatest remaining triple, so activation proceeds in nonincreasing value order. Tie order among equal-valued cells does not affect the final threshold.

`vis` contains activated coordinates. The parent array `p` gives every flattened cell index `row * n + column` a DSU representative. `find` uses path compression.

**Union a newly active cell with active neighbors**

After popping `v, i, j`, the code records `ans = v` and adds the coordinate to `vis`. The tuple `dirs = (-1, 0, 1, 0, -1)` combined through `pairwise` produces four offsets: up, right, down, and left.

For each offset, the neighboring coordinate is unioned only if it is already in `vis`. This membership test also makes explicit bounds checks unnecessary: out-of-grid coordinates were never activated and cannot belong to `vis`.

Connecting only active cells means every DSU component consists entirely of cells whose values are at least the current `v`. Conversely, after all cells of values above a threshold and enough cells at the threshold have been activated, DSU captures their four-direction connectivity.

**Stop when endpoints connect**

The loop condition compares roots of flattened index zero and index `m*n-1`. While they differ, another high-valued cell is activated. When they first match, the current `ans` is the lowest value among activated cells needed to establish connectivity.

There is then a path whose cells all have values at least `ans`, so a score of at least `ans` is achievable. Before processing this value level, the endpoints were disconnected using only greater-valued cells, so no path can have minimum greater than `ans`. These two facts prove optimality.

**One-cell limitation in the exact code**

When the grid has one cell, start and destination are connected before the loop begins. The loop never pops the cell, and `ans` remains zero. This is correct only when that cell value is zero. Under the stated constraints, a one-cell grid may contain a positive value, whose correct path score is that value.

A corrected implementation must return `grid[0][0]` when `m*n == 1` or structure activation so the endpoint threshold is established before the connectivity check. The approach should not hide this protected-source edge-case defect.

## Complexity detail

Let $V=mn$. Building the cell triples costs $O(V)$, and sorting them costs $O(V\log V)$. Each cell is activated once and examines four neighbors. DSU operations are nearly constant amortized with path compression, so sorting dominates and total time is $O(V\log V)$.

The triples, parent array, and visited set each store $O(V)$ items, giving $O(V)$ space. The recursive find stack is bounded by parent-tree height and is reduced by compression.

As with ID 1101, the code does not use union by rank, so the strict classical $\alpha(V)$ operation guarantee is stronger with that additional heuristic. The overall sorting bound remains $O(V\log V)$ regardless.

## Alternatives and edge cases

- **Maximum-bottleneck Dijkstra:** Store for each cell the best minimum value achievable so far and process the greatest score first with a max-heap. It has the same $O(V\log V)$ time and matches the manifest summary.
- **Binary search the threshold:** For each candidate value, run BFS through cells meeting it. This is correct but repeats graph traversal and usually costs more.
- **Maximum spanning tree:** Sort grid edges by bottleneck value and union endpoints until start and destination connect. The minimum edge or cell threshold on their maximum-spanning-tree path gives the answer.
- **One-cell grid:** The exact code returns zero without activation; a correct solution must return the sole cell’s value.
- **Equal cell values:** Arbitrary tie activation order is safe because `ans` remains the shared threshold while all required cells at that level are processed.
- **Endpoint values:** No path score can exceed either endpoint. Descending activation naturally waits until both endpoints are active.
- **Out-of-bounds neighbors:** They are absent from `vis`, so the membership test safely rejects them.
- **Four-direction rule:** Diagonals are never unioned because the offset sequence contains only cardinal moves.
- **Duplicate union attempts:** Attaching roots already connected is harmless, though a root-equality check could avoid an assignment.
- **Input preservation:** The grid is read but not modified; activation state lives in `vis`.
