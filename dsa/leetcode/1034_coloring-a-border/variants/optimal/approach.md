## General

**First identify the selected component**

The operation applies only to the four-directionally connected component containing `grid[row][col]`. Let `c` be that starting color. A cell belongs to the component exactly when it can be reached from the start through adjacent cells whose original color is `c`.

Depth-first search explores that component. The helper `dfs(i, j, c)` is called only for a cell known to have color `c` before it is visited. It marks `vis[i][j] = True` immediately, preventing cycles in the grid graph.

The search never crosses into a different color. Such a neighbor is evidence that the current component cell is on the border, but it is not recursively visited.

**What makes a component cell a border cell**

The source gives two independent border conditions:

- At least one of the cell's four neighbors lies outside the grid.
- At least one in-bounds neighbor is not in the selected component.

The DFS checks both while examining the four directions. Whenever either condition is found, it sets `grid[i][j] = color`.

A cell can trigger the assignment several times through different neighbors. Repeating the same assignment is harmless. The method does not need a separate Boolean such as `is_border` because writing the target color immediately records the final action.

**Generate four-directional movement**

Applying `pairwise` to `(-1, 0, 1, 0, -1)` produces offsets for up, right, down, and left.

For each offset, `x = i + a` and `y = j + b` identify a neighbor. The bounds test `0 <= x < m and 0 <= y < n` separates real grid neighbors from directions that leave the matrix.

If the coordinate is out of bounds, the current cell lies on the outer boundary of the grid, so it is recolored.

If it is in bounds and unvisited, its value decides what happens. Original color `c` means it belongs to the component and DFS continues there. A different value means the neighbor lies outside the component, so the current cell is a border cell and is recolored.

**Why visited neighbors are skipped**

An in-bounds visited neighbor was reached by this same DFS, so it belongs to the selected component. It is not evidence of a border.

Skipping visited neighbors is especially important because the algorithm recolors in place during traversal. A visited component neighbor may already have been changed from `c` to the target `color`. Testing its current grid value again could falsely make an interior cell look adjacent to a different component.

The condition `if not vis[x][y]` prevents that mistake. Membership of visited cells is known from how they were reached, regardless of their current mutated value.

**Why in-place recoloring does not block exploration**

Before any cell is recolored, its visited flag has already been set. An unvisited cell can never have been recolored by another call: each call writes only its own current coordinate, and entering a call marks that coordinate visited first.

Therefore, when the algorithm sees an unvisited neighbor, `grid[x][y] == c` still tests its original color. Once entered, future encounters use `vis` rather than the possibly changed value.

The original component structure is thus preserved logically by the visited matrix even while the physical grid is updated.

**Trace a solid `3 \times 3` component**

Suppose every cell initially has color one, the start is the center, and the new color is two.

DFS reaches all nine cells. Every outer-ring cell has at least one direction outside the grid and is recolored to two.

The center's four neighbors are all component cells. Some may already have been recolored when the center later examines them, but they are also visited, so the algorithm correctly skips their changed values. The center never sees an out-of-bounds or different-component neighbor and remains one.

The result has a ring of twos around the original center one, which is exactly the component border.

**Trace contact with another color**

For `[[1,1],[1,2]]` starting at the upper-left one, DFS visits the three connected ones. Each lies on the grid boundary, and some are also adjacent to the cell containing two. All three are border cells and become the requested new color. The cell containing two is never entered and remains unchanged.

**Why every and only border cell is recolored**

Every DFS call corresponds to a cell in the selected component because recursion follows only unvisited neighbors equal to `c`. Thus no cell outside the component is ever assigned the new color.

For a visited component cell, the loop considers all four directions. If it is on the grid boundary, one direction is out of bounds and recolors it. If it touches a noncomponent cell, that unvisited different-colored neighbor recolors it. Hence every border cell is changed.

If a component cell is interior, all four neighbors are in bounds and belong to the same component. Each is either recursively discovered or already visited. No recoloring branch executes for that cell, so it retains its original color. These statements establish exact correspondence with the border definition.

**Why the starting color is passed explicitly**

The initial call uses `grid[row][col]` as `c`. Every recursive call passes that same scalar. It does not reread the current cell to decide the component color because some previously visited cells may already have changed to the new color.

Keeping `c` stable separates original membership from the output mutation.

## Complexity detail

Let `P = m \cdot n` be the number of grid cells. The DFS visits at most every cell in the selected component once and checks four directions per visit, giving `O(P)` worst-case time. The constant four does not affect the bound.

The visited matrix allocates one Boolean for every grid cell, using `O(P)` space. Recursive depth can also reach `O(P)` for a winding or highly skewed component. The method changes and returns the input grid instead of allocating a second output matrix. Total auxiliary space is `O(P)`, matching the manifest.

If the selected component has size `K`, traversal work is more precisely `O(K)`, but the full visited allocation remains `O(P)`.

## Alternatives and edge cases

- **Breadth-first search:** Discover the component with a queue and evaluate the same border conditions. It has identical `O(P)` bounds and avoids recursion-depth limits.
- **Collect border coordinates first:** Traverse without changing colors, store every border cell, then recolor them afterward. This makes mutation reasoning simpler but needs an additional border list of up to `O(P)`.
- **Use a special temporary color as visited state:** Negate or otherwise encode visited cells in `grid`, then restore interiors and apply the final color. This can avoid a Boolean matrix but becomes delicate when colors and target values overlap.
- **Copy the grid:** Writing into a separate output matrix preserves the caller's input but adds another `O(P)` allocation.
- **One-cell grid:** Every direction leaves the grid, so the only cell is a border and is recolored.
- **One-row or one-column component:** Every component cell lies on the matrix boundary and must be recolored.
- **Component fills the grid:** Outer cells change; cells with four in-bounds component neighbors remain unchanged.
- **Single-cell component inside the grid:** All four neighbors have a different color, so that lone component cell is a border.
- **New color equals original color:** Assignments make no visible change, but traversal and returned grid remain correct.
- **Neighbor already recolored:** Its visited flag proves component membership, preventing mutation from creating a false border.
- **Diagonal contact:** It does not join components and is not examined because adjacency is four-directional.
- **Different-color neighbor:** It remains untouched; only the current selected-component cell is recolored.
- **Input mutation:** The exact method changes `grid` in place. Callers needing the original values afterward must pass a copy.
- **Recursive depth:** A component containing up to 2500 cells can create a deep call chain in an unfavorable shape; iterative BFS or DFS is safer when the runtime has a low recursion limit.
