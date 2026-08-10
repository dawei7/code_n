## General

**Represent each recursive region by inclusive boundaries**

A quad tree represents a square region either as one uniform leaf or as an internal node whose four children represent equal quadrants. The helper `dfs(a, b, c, d)` handles the rectangle whose top-left coordinate is `(a,b)` and bottom-right coordinate is `(c,d)`, with both endpoints included.

The initial call covers the complete grid:

`dfs(0, 0, len(grid) - 1, len(grid[0]) - 1)`.

Because the input is square and its side length is a power of two, every non-unit region can be split exactly into four equal square regions. Inclusive boundaries make the loop and child ranges explicit, but they also require careful `+1` adjustments at the right and bottom halves.

**Determine whether the current region is uniform**

The helper scans every cell from rows `a..c` and columns `b..d`. It uses two flags:

- `zero` becomes `1` after any zero is observed; and
- `one` becomes `1` after any one is observed.

Since the grid contains only zero and one, `zero + one == 1` exactly when the region contains one of the values but not the other. The region is nonempty, so both flags cannot remain zero. If both become one, the region is mixed.

The code deliberately finishes the scan even after seeing both values. An early break could improve some practical cases, but it is not part of this exact implementation.

For a uniform region, the method returns `Node(grid[a][b], True)`. Any cell has the common value, so the top-left cell is a valid source for `val`. A leaf has no meaningful children.

**Split a mixed region into four quadrants**

For a mixed region, define the midpoint row as `(a + c) // 2` and midpoint column as `(b + d) // 2`. The four recursive calls cover:

- top-left: rows `a..midRow`, columns `b..midCol`;
- top-right: rows `a..midRow`, columns `midCol+1..d`;
- bottom-left: rows `midRow+1..c`, columns `b..midCol`; and
- bottom-right: rows `midRow+1..c`, columns `midCol+1..d`.

These ranges are disjoint and together cover every cell of the parent exactly once. The `+1` on the lower/right starts prevents midpoint rows or columns from being duplicated.

Each recursive call returns the complete quad-tree representation of its quadrant. The parent is then created with `isLeaf = False` and those children in the required top-left, top-right, bottom-left, bottom-right order.

The intermediate expression `val = isLeaf and one` evaluates to false for a mixed region because `isLeaf` is false. The contract permits either value on an internal node, so choosing false is valid. In the leaf branch, the code uses `grid[a][b]` directly rather than this variable.

**Why recursion always terminates**

A mixed one-cell region is impossible: a single cell cannot contain both zero and one. Therefore every one-cell call returns as a leaf before attempting a split.

Every mixed region has side length at least two, and each child has half that side length. Since the original side is $2^x$, repeated halving reaches one after exactly $x = \log_2 n$ levels with no fractional or empty quadrant.

**How compression occurs**

Uniform regions stop immediately, regardless of their size. A large all-one quadrant becomes one leaf instead of a complete tree of its cells. Mixed regions expand only where spatial detail is necessary.

This implementation decides uniformity before recursing. It does not build four children and then merge equal leaf children. Both strategies produce equivalent canonical spatial coverage, but their running-time behavior differs.

For `[[0,1],[1,0]]`, the root scan sees both values, so it creates an internal node. Each quadrant is one cell and becomes a leaf, yielding four children with values 0, 1, 1, and 0.

**Why the returned tree represents exactly the grid**

For a uniform region, the returned leaf stores its sole value and therefore represents every cell in that region correctly. For a mixed region, the four child ranges partition the parent without gaps or overlaps. By recursive correctness, each child represents its own range; attaching all four in the specified positions represents their union, which is exactly the parent region.

Induction on region side length proves every helper result is correct. Applying it to the initial full-grid region proves the returned root represents the complete input.

**Why internal nodes cannot be replaced by a leaf**

The scan creates an internal node only after observing both zero and one. No single Boolean leaf value can represent both. Conversely, a uniform region is immediately compressed to a leaf, so the output never subdivides a region unnecessarily under this top-down rule.

## Complexity detail

Let $n$ be the grid side length. A call on a region of side $s$ scans $s^2$ cells. In the worst case, every region remains mixed down to individual cells. At each recursion depth, the regions partition the full grid, so the total number of scanned cells on that level is $n^2$. There are $\log_2 n + 1$ levels, giving worst-case time

$$
O(n^2\log n).
$$

The variant manifest lists $O(n^2)$, but that bound belongs to a bottom-up implementation that examines each input cell once and merges four equal leaf results. The exact shipped code scans parent regions before scanning their children, so $O(n^2\log n)$ is the accurate worst-case bound. A uniform grid finishes after the root scan in $O(n^2)$ time.

The active recursion depth is $O(\log n)$. Excluding the returned quad-tree nodes, auxiliary space is therefore $O(\log n)$. The output can contain $O(n^2)$ nodes in a maximally mixed pattern and necessarily occupies that much result space.

## Alternatives and edge cases

- **Bottom-up optimized recursion:** Recurse to four children first and merge them when all are equal leaves. This visits each cell once and achieves the manifest's $O(n^2)$ time with $O(\log n)$ stack space.
- **Two-dimensional prefix sums:** Query whether a region contains zero, all cells, or a mixture in $O(1)$ after $O(n^2)$ preprocessing. This also reaches $O(n^2)$ total node-processing time but uses $O(n^2)$ extra memory.
- **Copy four submatrices:** Slicing is easy to visualize but repeatedly allocates and copies cells. Boundary coordinates preserve the original grid and avoid that overhead.
- **Stop scanning once both flags are set:** This practical optimization preserves correctness but only improves constants/particular inputs; the current code does not perform it.
- **One-cell grid:** Exactly one flag becomes set, and the root is a leaf with that value.
- **All-zero or all-one grid:** The root scan finds one value type and compresses the complete grid into a single leaf.
- **Checkerboard grid:** Every non-unit region is mixed, producing the deepest/largest tree and the $O(n^2\log n)$ scanning case.
- **Internal-node `val`:** Its value is semantically ignored. The exact solution uses false, which the contract explicitly accepts.
- **Inclusive midpoint arithmetic:** Right and bottom child ranges must start at midpoint plus one; otherwise quadrants overlap and some cells are represented twice.
- **Power-of-two guarantee:** It ensures every mixed square can be divided into four equal integer-sized squares until unit cells.
