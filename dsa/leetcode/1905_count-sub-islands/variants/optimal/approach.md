## General

**Judge each complete island in `grid2`.** A sub-island condition applies to an entire four-connected component, not to isolated cells. The algorithm launches DFS from every still-land cell in `grid2`. That search consumes the whole island and returns one only if every one of its cells overlaps land in `grid1`. Summing these return values counts qualifying islands.

**Use `grid2` itself as the visited structure.** On entering `dfs(i, j)`, the source saves `ok = grid1[i][j]`, then writes `grid2[i][j] = 0`. Changing the current land cell to water marks it visited before exploring neighbors. Any later path reaching the same coordinate sees zero and does not recurse, preventing cycles and duplicate work.

This mutation is intentional and observable: after the method returns, all land cells of `grid2` have been cleared. No separate visited matrix is allocated.

**Generate exactly four directions.** `dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` yield `(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`. These are up, right, down, and left. Diagonal cells are not connected under the island definition.

For each neighbor, the code verifies row and column bounds and then checks `grid2[x][y]`. Only unvisited land triggers recursion. Outside coordinates and water require no action.

**Combine validity without stopping exploration.** A DFS call returns one precisely when its entire reachable portion is valid. If a recursive neighbor returns zero, `not dfs(x, y)` becomes true and the parent sets `ok = 0`. Importantly, a parent whose `ok` is already zero still explores later land neighbors. The condition does not short-circuit on `ok`, so the whole component is always cleared even after one mismatching cell proves it cannot be a sub-island.

This is essential. Returning immediately on the first invalid overlap would leave unvisited pieces of the same `grid2` island, and the outer scan could later count those fragments as separate islands.

**Why checking every corresponding `grid1` cell is enough.** If all cells of one `grid2` island are land in `grid1`, then adjacent cells in that island remain adjacent land cells in `grid1`. They therefore belong to one containing `grid1` island. No separate component labeling of `grid1` is needed. Conversely, one `grid2` land cell over `grid1` water makes containment impossible, and its zero propagates through DFS return values.

**Understand the compact outer sum.** The generator visits grid coordinates in row-major order and calls DFS only when `grid2[i][j]` is still one. That cell is the first encountered member of an unprocessed island. DFS clears the island and returns zero or one. Later coordinates from the same island are now zero and skipped. Thus each original `grid2` island contributes exactly one Boolean integer to `sum`.

**A small conceptual trace.** Suppose a three-cell L-shaped island in `grid2` overlaps land in `grid1` at two cells but water at the third. DFS begins with the first overlap, clears it, reaches the second, and eventually reaches the mismatching third cell where local `ok` is zero. That zero returns through ancestors, so the island contributes zero. Nevertheless all three cells are cleared, ensuring no fragment is reconsidered.

**Why DFS correctness follows by induction.** A leaf call returns its own `grid1` value, exactly describing whether that one-cell explored subtree is valid. An internal call begins with its own overlap status and changes to zero if any recursively explored neighbor component is invalid. It returns one if and only if itself and every reachable descendant overlap land. Because DFS reaches every cell of the island, the root return exactly represents the sub-island predicate.

**Neither connectivity nor values of `grid1` are mutated.** The method only reads `grid1`. It does not need to mark its islands because multiple distinct `grid2` islands may lie within the same `grid1` island and must each be counted separately.

## Complexity detail

Let the grids have $m$ rows and $n$ columns. The outer generator examines all $mn$ coordinates. Every original `grid2` land cell enters DFS once and checks four neighbors. Total time is $O(mn)$.

No visited matrix is allocated because `grid2` is reused. However, recursive call depth can reach $O(mn)$ for a long snake-shaped island, so exact auxiliary call-stack space is $O(mn)$ in the worst case, matching the manifest's broad space bound.

This depth is also a practical Python concern: a large connected island can exceed the interpreter's default recursion limit and raise `RecursionError`. An iterative stack or raised recursion limit is needed for robust execution at the maximum 500-by-500 constraints. The recurrence itself remains correct, but the implementation limitation is material.

## Alternatives and edge cases

- **Iterative DFS or BFS:** An explicit stack or queue avoids Python recursion limits while keeping $O(mn)$ time and worst-case space. It can still clear `grid2` in place.
- **Separate visited matrix:** Preserves `grid2` but allocates $O(mn)$ additional memory. The exact source chooses destructive marking.
- **Erase invalid land first:** Remove every `grid2` cell lying over `grid1` water, then count remaining islands. Care is needed because removing one cell can split an original invalid island into pieces that must not be counted.
- **Grid2 island over multiple Grid1 islands:** If every corresponding cell is land and cells are four-connected, they cannot actually belong to different `grid1` islands; their same adjacencies connect them there too.
- **Single-cell island:** It contributes one exactly when the corresponding `grid1` cell is land.
- **Diagonal contact:** Diagonally touching land belongs to separate islands because only four directions are generated.
- **Invalid cell found early:** DFS must continue clearing the component. The source preserves exploration even after `ok` becomes zero.
- **Input mutation:** All visited `grid2` land is changed to water. Pass a copy if the caller must retain the original grid.
- **Large solid island:** Correct asymptotic work is linear, but recursive depth may exceed Python's default limit; iterative traversal is safer.
