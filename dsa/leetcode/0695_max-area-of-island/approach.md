## General

An island is a connected component of land cells under up, right, down, and left movement. Its area is simply its number of cells. The solution starts a depth-first search from every grid position; each search consumes one entire not-yet-visited island and returns its area. The maximum returned value is the answer.

**The recursive contract**

`dfs(i, j)` returns:

- zero if cell `(i, j)` is water;
- otherwise, the number of land cells in the connected island portion reached from that cell before any of those cells were visited.

The caller performs boundary checks before calling a neighbor, so `dfs` itself assumes `i` and `j` are valid indices.

If `grid[i][j] == 0`, the function immediately returns zero. A zero may be original water or land that an earlier recursive call has already visited. Treating both cases identically prevents double counting.

**Counting and marking one land cell**

For a land cell, `ans = 1` counts the current cell. Then `grid[i][j] = 0` marks it visited before any neighbors are explored.

Marking before recursion is necessary. Adjacent land cells point back to one another. If the current cell remained one while exploring a neighbor, that neighbor could recursively enter it again, creating repeated counts and possibly infinite recursion.

The grid mutation replaces a separate visited structure.

**Generating four-directional neighbors**

`dirs = (-1, 0, 1, 0, -1)` combined with `pairwise(dirs)` produces:

- `(-1, 0)`;
- `(0, 1)`;
- `(1, 0)`;
- `(0, -1)`.

These are exactly the four legal connectivity directions. Diagonal cells are intentionally absent.

For every offset `(a, b)`, the code computes `x = i + a` and `y = j + b`. It calls `dfs(x, y)` only when `0 <= x < m` and `0 <= y < n`. This keeps all grid accesses valid.

The returned neighbor areas are added into `ans`. Since visited cells become zero, the recursive branches cover disjoint sets of newly counted land cells even when the island contains cycles in its adjacency graph.

**Why returning the sum gives one island's area**

Every four-directionally reachable land cell is eventually encountered: from the start, DFS follows every valid land neighbor, then every neighbor of those cells, and so on.

Every such cell contributes exactly one, when it is first entered. It can contribute no second time because it is immediately changed to zero. Cells outside the connected component are never reachable through the recursion and contribute nothing.

Therefore, the value returned by the initial call is exactly the number of cells in that island.

**Finding the global maximum**

The return statement is:

`max(dfs(i, j) for i in range(m) for j in range(n))`.

The generator visits every coordinate in row-major order.

When it reaches the first cell of an unvisited island, `dfs` consumes that whole island and returns its full area. Later generator positions belonging to the same island now contain zero and return zero.

Original water positions also return zero. Thus the generated values include each island's area once, plus any number of zeroes. Their maximum is the largest island area.

The grid is guaranteed nonempty, so the generator always produces at least one value and `max` never receives an empty sequence.

**Example of merging recursive branches**

Imagine a plus-shaped island with a center and four land neighbors. The center counts itself as one. Each directional call reaches one arm, counts it, marks it, and returns one. The center adds the four results and returns five.

If two branches can reach the same additional land cell through different routes, the branch that arrives first marks it zero. The later branch receives zero for that cell, so the shared cell is still counted exactly once.

**All-water behavior**

If every cell is zero, every call returns zero. The maximum of these zeroes is zero, matching the required answer when no island exists. No special-case initialization is needed.

**Why the overall algorithm is correct**

For each unvisited island, the first DFS call into it returns exactly its area by exhaustive four-directional exploration and one-time marking. The outer generator eventually reaches at least one cell from every island because it enumerates the entire grid.

The final `max` therefore considers every island area. It cannot return an invalid larger value because each DFS counts only cells connected to its start. Hence the returned number is exactly the maximum island area, or zero if there are no islands.

## Complexity detail

Let `R` and `C` be the grid dimensions.

Although `dfs` is syntactically invoked from every outer coordinate and may also be invoked on water neighbors, every land cell is processed as land only once. Each processed land cell checks four directions. Water calls do constant work. The total time is

$$
O(RC).
$$

The solution allocates no visited matrix because it marks the input grid. Its main auxiliary storage is the recursion stack. In the worst case, DFS can follow a path containing all `RC` cells before returning, so space is

$$
O(RC).
$$

The generator and direction tuple use only constant additional space. If recursion depth is excluded, the explicit data-structure space is `O(1)`, but the call stack is part of auxiliary memory and must be counted.

## Alternatives and edge cases

- **Iterative DFS:** Use a stack, mark cells when pushing them, and increment a counter when popping. This avoids recursion depth limits while retaining `O(RC)` time and space.

- **Breadth-first search:** A queue explores one island level by level. It computes the same component size with the same asymptotic bounds.

- **Separate visited set:** Preserve `grid` by tracking coordinates externally. This uses explicit `O(RC)` storage but avoids input mutation.

- **All water:** Every DFS result is zero and the final answer is zero.

- **Single land cell:** It counts itself, all neighbor calls return zero or are out of bounds, and its area is one.

- **Diagonal contact only:** Diagonal land cells belong to separate islands because no diagonal offset is generated.

- **Grid-edge cells:** Boundary checks prevent invalid neighbor calls; the conceptual surrounding water needs no padded border.

- **Input mutation:** All visited land becomes zero. Reusing the same grid for another computation would observe the modified data.

- **Deep or winding island:** Recursive depth can approach `RC` and exceed Python's recursion limit even though the algorithm is asymptotically correct.

- **Mark-before-explore order:** Moving `grid[i][j] = 0` after recursive calls would permit cycles of calls between adjacent cells.

- **Nonempty-grid guarantee:** The code reads `grid[0]` and calls `max` over all cells, both safe because the source guarantees at least one row and column.

- **Generator evaluation order:** Earlier DFS calls mutate cells that later generator iterations see. This is intentional and ensures each island's area appears only once.
