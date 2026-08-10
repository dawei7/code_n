## General

**View the grid as an implicit graph**

Every land cell is a graph vertex. An edge connects two land vertices when
their cells share a horizontal or vertical side. Under this interpretation, an
island is exactly one connected component of land vertices.

The algorithm scans every coordinate. Whenever it finds land that has not been
visited, that cell belongs to a new component. A depth-first traversal erases
the entire component, and the island count increases once.

**Encode the four allowed directions compactly**

`dirs = (-1, 0, 1, 0, -1)` contains a circular sequence of coordinate offsets.
Applying `pairwise(dirs)` yields:

`(-1, 0), (0, 1), (1, 0), (0, -1)`

These are up, right, down, and left. Diagonal offsets never appear, matching
the Reference's four-direction connectivity rule. The repeated final `-1`
closes the pattern so four adjacent pairs encode all directions.

This concise construction requires `itertools.pairwise`, available in modern
Python versions. A literal tuple of four coordinate pairs would be more
portable to older Python runtimes.

**Erase a component with recursive DFS**

`dfs(i, j)` begins on a known land cell and immediately assigns
`grid[i][j] = '0'`. Changing land to water serves as the visited mark, so no
separate boolean matrix is required.

For each direction, it computes neighbor `(x, y)`, checks both row and column
bounds, and recurses only when the neighbor still contains `'1'`. Marking the
current cell before exploring neighbors is essential. Adjacent land cells can
point back to one another; early marking prevents that cycle from causing
unbounded recursive calls.

The traversal continues until every horizontally or vertically reachable land
cell has been changed to `'0'`. Water and out-of-bounds positions terminate a
direction without recursion.

**Count only traversal roots**

The nested scan visits rows and columns in order. On a `'1'`, it calls `dfs`
and then increments `ans`. The increment represents the newly discovered
island, not each cell within it.

After DFS returns, all land in that component is zero. Later scan positions
from the same island are therefore skipped. A different remaining `'1'` cannot
be connected to an erased component—if it were, DFS would have reached it—so
it legitimately starts another island and another increment.

**Trace the three-island example**

The first land at the upper left launches DFS, which erases the connected
2-by-2 block and increases the answer to one. The scan later reaches the single
middle land cell; it was not connected through any side to the first block, so
its DFS erases only itself and the answer becomes two.

Finally, the lower-right pair of adjacent land cells launches one traversal
that erases both and raises the answer to three. Diagonal proximity between
components never joins them.

**Why each component is counted exactly once**

When the scan starts DFS from a cell, the recursive neighbor rule reaches every
land cell in that cell's connected component: any component path consists of
the same four allowed edge steps, and DFS follows each available step. No cell
outside the component is reached because recursion crosses only land edges.

The starting component is fully marked before scanning continues. Therefore no
second cell in it can start another DFS. Conversely, every component contains
some earliest coordinate in scan order, which remains `'1'` until the scan
reaches it and must start a traversal. This proves one increment per island.

**Mutation is the visited structure**

The method permanently changes all input land cells to `'0'`. The Function
Contract asks for a count and does not promise that the grid will be preserved,
so in-place marking is a conventional solution. A caller that needs the
original matrix afterward must pass a copy or use a separate visited set.

Using mutation saves a separate $m \times n$ visited matrix, but it does not
remove recursive stack cost.

**The exact source is recursive, not stack-based**

The manifest summary says the island is erased with an explicit depth-first
stack. The exact file calls `dfs` recursively. Its logical traversal order is
depth first, but the call stack is implicit and controlled by Python.

For a winding or fully connected island, recursion depth can approach $mn$.
The constraints allow 90,000 cells, far above Python's usual recursion limit.
Thus the exact source can raise `RecursionError` on legal large grids even
though its graph algorithm is correct. Replacing recursion with an explicit
list stack would match the manifest description and eliminate that runtime
limit.

**Imports and nonempty assumption**

The file uses `List` and `pairwise` without displaying imports. Standalone code
needs `from typing import List` and `from itertools import pairwise`. The line
`len(grid[0])` assumes at least one row and one column; the Reference guarantees
$m,n \ge 1$, so that access is safe for canonical input.

## Complexity detail

Let the grid have $m$ rows and $n$ columns. The outer scan examines $mn$ cells.
Each land cell is marked once, and its four directions are checked once during
DFS. Total time is $O(mn)$.

The recursive call stack can contain $O(mn)$ frames for a path-shaped traversal
of one large island, so worst-case auxiliary space is $O(mn)$, matching the
manifest bound but not its explicit-stack description. In-place marks add no
separate visited matrix.

## Alternatives and edge cases

- **Explicit DFS stack:** Push discovered coordinates and mark on push; preserves $O(mn)$ worst-case space while avoiding `RecursionError`.
- **Breadth-first queue:** Equivalent component marking with different frontier order.
- **Union-find:** Join adjacent land cells and count remaining components; useful when connectivity is built incrementally but needs $O(mn)$ storage.
- **Separate visited set:** Preserves the input grid at the cost of additional memory.
- **All water:** No DFS starts and the answer remains zero.
- **All land:** One traversal erases every cell and returns one, but recursive depth can be unsafe.
- **Diagonal contact:** Does not connect islands because no diagonal direction is generated.
- **One cell:** Returns one for land and zero for water.
- **Rectangular guarantee:** Allows one shared column count `n`; ragged rows would break bounds assumptions.
- **Missing imports:** `List` and `pairwise` must be available in the execution environment.
