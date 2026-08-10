## General

**The first child is forced onto the main diagonal.** This child starts at `(0,0)` and must reach `(n-1,n-1)` in exactly $n-1$ moves. Both coordinates must increase by $n-1$ overall. In one move, each coordinate can increase by at most one, so every move must increase both. The only possible path is

`(0,0), (1,1), ..., (n-1,n-1)`.

Its contribution is therefore the fixed sum `sum(fruits[i][i] for i in range(n))`.

**Keep the other paths on opposite sides of the diagonal.** The upper-right child advances exactly one row per move. Before its final move into `(n-1,n-1)`, it can be represented entirely in the strict upper triangle $j>i$. The lower-left child is symmetric and stays in the strict lower triangle $i>j$ before its final move.

These regions are disjoint from each other and from the forced diagonal. This removes the fruit-sharing interaction: each off-diagonal room can belong to at most one of the two dynamic programs, while the common destination is counted once through the diagonal sum.

**Upper-triangle state.** The table entry `f[i][j]` initially means the maximum fruits collected by the upper-right child upon reaching room $(i,j)$. Its start is initialized as

`f[0][n - 1] = fruits[0][n - 1]`.

All other states begin at negative infinity, which marks them unreachable rather than incorrectly treating a missing path as a zero-fruit path.

To reach $(i,j)$ from the previous row, the child could have been at columns $j$, $j-1$, or $j+1$. The recurrence takes the maximum of the available parent states and adds `fruits[i][j]`. The loop restricts `j` to `i+1..n-1`, so no diagonal cell is included.

The relevant endpoint is `f[n - 2][n - 1]`. From room $(n-2,n-1)$, the child's final legal move reaches the destination. That destination's fruits are already in the diagonal sum and must not be added again.

**Lower-triangle state reuses the same table.** Next, `f[n - 1][0]` initializes the lower-left child. The second traversal advances one column at a time. To reach $(i,j)$ from the previous column, possible parents are $(i,j-1)$, $(i-1,j-1)$, and $(i+1,j-1)$, matching right, up-right, and down-right moves.

The loop uses `i > j` and therefore fills only the strict lower triangle, which was untouched by the upper computation. Its endpoint is `f[n - 1][n - 2]`, immediately left of the shared destination.

**Why the two uses of `f` do not corrupt each other.** Upper states have $j>i$ and lower states have $i>j$. They occupy disjoint cells. Each recurrence also reads only parents in its own triangle or its own initialized corner. One square table can hold both computations, although it does not provide the rolling-space optimization described by the editorial.

**Combine the three independent contributions.** The return adds the forced diagonal, the best upper endpoint, and the best lower endpoint. Each starting corner is included by its respective component. The final room appears only in the diagonal component. Therefore every collected room is counted exactly once.

**Trace the $2\times2$ boundary case.** The diagonal child collects `(0,0)` and `(1,1)`. The upper child starts at `(0,1)`, which is already `(n-2,n-1)`, while the lower child starts at `(1,0)`, already `(n-1,n-2)`. All four rooms are added once, matching the example.

**Why local maxima form global maxima.** Once the first path is fixed and the strict triangles separate the other two children, a choice made in the upper triangle cannot change any room available in the lower triangle. Each recurrence considers every legal predecessor, so its endpoint is the maximum path sum for that child. Adding the two independent optima and fixed diagonal is consequently globally optimal.

## Complexity detail

Each triangular traversal processes $O(n^2)$ states with constant work, so time is $O(n^2)$.

The exact source allocates `f = [[-inf] * n for _ in range(n)]`, which contains $n^2$ entries. Its auxiliary space is therefore $O(n^2)$, not the manifest's stated $O(n)$. A two-row rolling DP for the upper triangle and a two-column rolling DP for the lower triangle would achieve $O(n)$ space, but that is not what this file executes.

## Alternatives and edge cases

- **Rolling arrays:** Preserve only the preceding row or column and achieve the editorial's $O(n)$ space.
- **Three-child joint DP:** It models interactions explicitly but creates a much larger state space; triangle separation makes it unnecessary.
- **Greedy highest neighboring fruit:** A locally large room can lead to an unreachable or low-value suffix, so complete DP is required.
- **Zero-fruit rooms:** They remain valid path states; negative infinity, not zero, distinguishes unreachable states.
- **Shared destination:** Its fruits are counted only in the diagonal sum.
- **Starting corners:** Upper-right and lower-left fruits are included in their initialized DP states.
- **`n = 2`:** Both off-diagonal endpoints equal their starting corners and require no recurrence step.
- **Strict triangle restriction:** Diagonal rooms are reserved for the forced child and excluded from both other totals.
- **Boundary parent:** Checks on `j+1` and `i+1` prevent indexing beyond the grid.
- **Negative indexing risk:** Loop ranges ensure `j-1` and `i-1` are valid where used.
- **Table reuse:** It saves a second quadratic table but remains quadratic space.
- **Manifest mismatch:** The exact implementation does not use rolling memory.
- **Import requirement:** `inf` and `List` must be available.
- **Input preservation:** The table is separate; `fruits` is never transposed or modified.
