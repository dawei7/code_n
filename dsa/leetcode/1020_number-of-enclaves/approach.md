## General

**Turn reachability into a boundary search**

The matrix can be viewed as an undirected graph. Every land cell is a vertex, and two land vertices are connected when their cells share an edge. Diagonal contact does not create an edge because movement is limited to the four cardinal directions.

A land cell is not an enclave precisely when its connected component touches the boundary. Once a path reaches a boundary land cell, one more move can leave the grid. Conversely, a path cannot leave the grid without first reaching a cell in the first row, last row, first column, or last column. The question can therefore be restated:

Find all land connected to boundary land, discard it, and count the land that remains.

This reverse viewpoint is easier than starting a search from every land cell and asking whether that individual search escapes. All boundary-connected cells can be discovered together, and each cell needs to be visited at most once.

**Why the DFS changes land into water**

The nested function `dfs(i, j)` is called only for a known in-bounds land cell. Its first operation, `grid[i][j] = 0`, marks that cell as visited by turning it into water. This serves two purposes at once:

- The cell is known to be boundary-reachable, so it must not contribute to the final enclave count.
- Future searches will see zero and will not visit the same cell again.

No separate `visited` matrix is necessary. This is safe because the final answer depends only on how many enclosed land cells remain, not on preserving the input matrix.

Marking happens before exploring neighbors. If two adjacent land cells call each other recursively, the first one has already become zero before the second search looks back. That ordering prevents an infinite recursion cycle.

**How the four directions are generated**

The tuple `dirs = (-1, 0, 1, 0, -1)` encodes row and column offsets compactly. Applying `pairwise(dirs)` produces the consecutive pairs `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`. These mean up, right, down, and left.

For each pair `(a, b)`, the neighbor is `(x, y) = (i + a, j + b)`. The condition

`0 <= x < m and 0 <= y < n and grid[x][y]`

first proves that the coordinates are inside the matrix and then checks whether the cell contains one. Python evaluates `and` from left to right and short-circuits, so `grid[x][y]` is never accessed for an invalid coordinate. A value of one is truthy and triggers recursion; zero is false and is ignored.

**Why every boundary position is seeded**

The first pair of loops scans the top and bottom rows. For every column `j`, it considers row zero and row `m - 1`. The second pair scans the left and right columns. For every row `i`, it considers column zero and column `n - 1`.

Whenever a boundary cell is still one, DFS erases its entire connected land component. If another boundary cell belongs to the same component, it will already be zero when its turn arrives, so the extra seed attempt is skipped.

Corners are deliberately encountered twice: once as part of a boundary row and once as part of a boundary column. This causes no duplicate work. A corner containing land is erased during its first encounter and fails the later `if grid[i][j]` test. When the grid has only one row or one column, the pairs `(0, m - 1)` or `(0, n - 1)` may even contain the same index twice. The same visited-as-zero rule keeps that harmless.

**A concrete walkthrough**

Consider the first example:

`[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]`.

The land at row one, column zero lies on the left boundary. The boundary scan calls DFS there and changes it to zero. None of its four neighbors is land, so that search ends.

The three land cells near the center are connected to one another, but none is connected through land to an outer row or column. No boundary-seeded DFS reaches them. After all four sides have been scanned, those three entries are still one. Summing the matrix returns three.

In the second example, the top-row land is a seed. Its DFS follows the vertical connected chain through every other land cell. All of them become zero, so the final sum is zero.

**Why the remaining ones are exactly the answer**

First consider any land cell erased by DFS. Every DFS starts at a boundary land cell and moves only between adjacent land cells. Reversing that sequence gives a land-only path from the erased cell to the boundary. It can therefore walk off the grid and must not be counted.

Now consider a land cell that remains one. If it had any land-only path to the boundary, the boundary endpoint of that path would have been used as a DFS seed. DFS explores every connected neighbor recursively, so it would have followed the path and erased the cell. Since the cell remains, no such path exists, which is exactly the definition of an enclave land cell.

The two directions prove equality: nothing erased belongs in the answer, and every remaining one does belong in the answer. Since the matrix is binary, `sum(row)` counts the remaining land in one row, and `sum(sum(row) for row in grid)` adds those counts across all rows.

**Why this is more efficient than testing components one at a time**

A component-by-component strategy could start at each unseen land cell, explore the component, remember its size, and track whether it touches a boundary. That can also be linear with careful visitation. The boundary-first method is simpler because it does not need component sizes or an escape flag. It removes exactly the complement of the desired set, after which an ordinary sum produces the answer.

The approach is also robust to components touching the boundary at several places. They are still erased once because the mutation is a global visited marker.

## Complexity detail

Let `R = m` be the number of rows and `C = n` be the number of columns. The boundary loops examine `2C + 2R` positions. Across all DFS calls, each land cell is entered at most once because it becomes zero immediately. Each entered cell checks exactly four directions. The final nested summation examines all `RC` cells. These contributions give `O(RC)` total time, matching the manifest.

Changing values in the input removes the need for a separate `R \times C` visited matrix. The recursive call stack can nevertheless reach `O(RC)` depth in the worst case, such as a long one-cell-wide winding land component. The manifest therefore records `O(RC)` auxiliary space. Apart from recursion, the method uses only dimensions, loop variables, and the constant-sized direction tuple.

The final generator and row sums do not build another matrix. They use constant bookkeeping while reading the already modified grid. Mutation reduces explicit storage, but it does not change the worst-case recursive-space bound.

## Alternatives and edge cases

- **Breadth-first search from the boundary:** Put every boundary land cell into a queue, mark it, and expand through four-directional neighbors. This has the same `O(RC)` time and `O(RC)` worst-case space while avoiding recursion-depth concerns.
- **Separate visited matrix:** Mark boundary-connected land in an `R \times C` Boolean structure rather than changing `grid`. This preserves the caller's input but always allocates `O(RC)` explicit memory.
- **Explore every component:** A DFS can count each land component and record whether any cell touches the boundary. Add its size only when it does not. This is correct and linear, but needs more per-component state than deleting all boundary-reachable land first.
- **Union-find:** Join adjacent land cells and connect boundary land to a virtual outside vertex. Count cells not joined to outside. It works, but parent and rank arrays add complexity and `O(RC)` storage without improving the time bound.
- **Do not use diagonal movement:** A diagonal chain of ones is not connected under this problem's rules. Only the four offsets produced by `pairwise(dirs)` are legal.
- **All water:** No DFS starts, and the final sum is zero.
- **All land:** Boundary DFS reaches every cell, changes the whole grid to zero, and returns zero enclaves.
- **One row or one column:** Every land cell lies on the boundary and is erased. Repeated boundary indices are harmless because erased cells fail later truth tests.
- **Isolated interior land:** A one surrounded on four sides by water is never reached from a boundary seed and contributes one.
- **A narrow connection to the boundary:** Even a one-cell-wide land corridor makes the entire connected component non-enclosed. DFS follows that corridor and erases all connected land.
- **Input mutation:** The exact solution intentionally changes `grid`. If the surrounding application needs the original matrix afterward, it must pass a copy or use a visited structure instead.
- **Recursive depth:** The mathematical algorithm supports up to `RC` connected cells, but a runtime with a small recursion limit may need the iterative BFS or DFS form to avoid stack overflow.
