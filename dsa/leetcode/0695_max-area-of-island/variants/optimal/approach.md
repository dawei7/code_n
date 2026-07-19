## General
**Start only at undiscovered land**

Scan the grid in row-major order. A land cell outside the visited set begins a new island; water and already visited cells need no further work.

**Count one connected component**

Push the starting cell onto a stack and mark it immediately. Each pop contributes one unit of area, then considers the four orthogonal neighbors. Valid unvisited land neighbors are marked before being pushed, preventing duplicate stack entries.

**Keep the largest completed count**

Once a traversal empties its stack, its counter equals that island's area because it counted every reachable land cell once and no other cell. Compare the count with the running maximum before continuing the scan.

**Why no island is missed or combined**

Every island has a first cell encountered by the outer scan, which starts its traversal. Four-directional traversal reaches exactly that cell's island, and the global visited set prevents any of those cells from starting another count. Thus each island contributes exactly one complete area and the maximum is correct.

## Complexity detail
The outer scan examines $R \cdot C$ cells, and every land cell is pushed and popped at most once, for $O(RC)$ time. The visited set and traversal stack can each contain $O(RC)$ coordinates in the worst case.

## Alternatives and edge cases
- **Recursive depth-first search:** return `1` plus the areas of valid unvisited neighbors; it is concise but a large island may exceed the language's recursion limit.
- **Mutate visited land to water:** this removes the explicit visited set but changes the caller's grid.
- **Union-find:** unite adjacent land cells and track component sizes; it works but uses more machinery than a direct traversal.
- An all-water grid returns `0` because no traversal starts.
- Diagonally touching land cells belong to different islands.
- A single land cell has area `1`.
- An island may touch any grid boundary; only coordinates outside the matrix are excluded.
