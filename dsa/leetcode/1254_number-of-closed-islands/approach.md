## General

**Treat every land component as an island**

Land cells have value zero and connect only up, down, left, or right. A depth-first search from one unvisited land cell reaches exactly its maximal island.

The method reuses `grid` as its visited structure. As soon as `dfs(i,j)` enters land, it sets `grid[i][j] = 1`. That turns visited land into water for later searches and prevents cycles inside the current recursion.

**A component is closed exactly when every cell is interior**

An island touches the outside world exactly when at least one of its cells lies on the grid boundary. The local value

`int(0 < i < m - 1 and 0 < j < n - 1)`

is one for an interior cell and zero for a boundary cell.

`dfs` combines this value with the results of all connected land neighbors using bitwise AND. The final component result remains one only if the current cell and every recursively reached cell are interior. If any boundary land cell occurs, zero propagates through the AND operations to the island’s root.

**Why the entire island is explored even after finding a boundary**

The source uses:

`res &= dfs(x, y)`.

Unlike short-circuit Boolean `and`, augmented bitwise AND evaluates the recursive right-hand side even when `res` is already zero. This is essential. Once an island is known to be open, the traversal must still mark all of its cells visited; otherwise, a later outer-loop position could start inside the same island and count or traverse it again.

The result values are integers zero and one, so bitwise AND acts exactly like logical conjunction while preserving eager evaluation.

**Generate the four directions compactly**

`dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce direction pairs:

- \((-1,0)\), up;
- \((0,1)\), right;
- \((1,0)\), down;
- \((0,-1)\), left.

Only in-bounds neighboring land cells trigger recursion. The function does not recurse outside the grid; boundary membership is detected directly from the current cell.

**The outer scan counts one result per island**

The return expression scans every coordinate:

`grid[i][j] == 0 and dfs(i, j)`.

For water or previously visited land, the left side is false and short-circuits without calling DFS. For fresh land, DFS explores and marks the entire island, returning one if closed or zero if open.

Python treats these Boolean and integer results as numbers in `sum`, so exactly one is added for each closed island.

**Following an open island**

If DFS reaches a land cell in row zero, its initial `res` is zero. It still recursively visits every other connected land cell because `&=` is eager. The root receives zero, so the component is not counted, and all its cells are now ones.

**Following a closed island**

Every cell lies strictly between the four boundaries, so each frame starts with `res = 1`. Water neighbors are ignored, connected land frames also return one, and the root returns one. The surrounding water need not be examined as part of the island; its presence is implicit in the absence of any boundary land connection.


For any fresh land cell, marking before recursion ensures each cell in its component is visited once. Recursive neighbor traversal reaches all and only four-connected land in that component.

By induction over the DFS tree, a frame returns one exactly when every land cell in its explored subtree is interior. AND across all branches means the root returns one exactly when every cell in the island is interior, which is equivalent to being closed. The outer scan starts one DFS per island, so summing the returns gives the number of closed islands.

**Input mutation**

Every visited land cell becomes one permanently. By method completion, all land has been converted to water. This saves a separate visited matrix but means callers do not retain the original grid.

## Complexity detail

Let \(N=mn\) be the number of cells. The outer scan visits all \(N\) positions. Every land cell enters DFS at most once and examines four neighbors, so total time is \(O(N)\).

The algorithm allocates no visited matrix, but recursive depth can reach \(O(N)\) for a winding island. Auxiliary call-stack space is therefore \(O(N)\) in the worst case. Direction storage is constant.

For a 100-by-100 all-land shape, recursion depth can exceed a typical Python default recursion limit. An iterative stack or queue is safer in an unrestricted standalone environment.

## Alternatives and edge cases

- **Flood boundary land first:** Remove every island connected to an edge, then count remaining components. This separates openness detection from counting and remains \(O(N)\).
- **Breadth-first search:** Use a queue and a boundary flag, avoiding recursion-limit risk.
- **Separate visited matrix:** Preserve the input grid at the cost of \(O(N)\) explicit memory.
- **All water:** No DFS starts and the sum is zero.
- **All land:** The component touches every boundary and contributes zero.
- **Single-cell interior island:** Surrounded by water, its DFS returns one.
- **One-row or one-column grid:** Every land cell is on a boundary, so no closed island exists.
- **Eager bitwise AND:** Replacing `&=` with short-circuit logic carelessly could leave part of an open island unvisited.
- **Input mutation:** The exact method converts land to water; copy the grid first if preservation is needed.
- **Required helper:** Standalone code needs `pairwise` from `itertools`.
