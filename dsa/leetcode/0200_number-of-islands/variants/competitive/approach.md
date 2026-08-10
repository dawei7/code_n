## General

**Represent every cell by one union-find index**

The selected competitive `Solution` uses a disjoint-set, or union-find,
structure. A cell at row `i` and column `j` maps to flat index
`i * number_of_columns + j`. This mapping is one-to-one for a rectangular grid,
so every cell begins as a separate set.

Connected land cells are unioned. Once all relevant neighbor edges have been
processed, each land island corresponds to one remaining disjoint-set root.

**Initialize all cells, then compensate for water**

`UnionFind(len(grid) * len(grid[0]))` initially gives every cell—including
water—its own parent and sets `count` to the total number of cells. Variable
`zero_count` counts water cells during the grid scan.

Water is never unioned. At the end, `union_find.count` equals the number of
disjoint components among all cells, including each isolated water cell as one
component. Subtracting `zero_count` removes those artificial water components,
leaving the number of connected land components.

Another design would initialize parents only for land and start the component
count at the land-cell count. The stored subtraction approach reaches the same
mathematical result.

**Process only top and left neighbors**

When the scan reaches a land cell, it checks the cell above when `i` is nonzero
and the cell to the left when `j` is nonzero. If that neighbor is land, their
flat indices are unioned.

Checking only two directions is sufficient. Every vertical land edge is seen
once when the lower endpoint is processed, and every horizontal land edge is
seen once when the right endpoint is processed. Checking down and right as well
would repeat the same undirected edges without changing connectivity.

Diagonal neighbors are never checked, so the structure respects four-direction
islands.

**Merge roots and maintain the component count**

`find_set` follows parent links to a root. Its recursive assignment performs
path compression: after finding the root, it points the queried node directly
there, making future searches shorter.

`union_set` finds both roots. If they differ, it assigns the smaller numeric
root beneath the larger numeric root and decrements `count`. If they are already
equal, the land cells were connected through earlier edges and no component
count changes.

Choosing by numeric root is deterministic but is not union by rank or size.
The source comment claims the inverse-Ackermann behavior usually associated
with both path compression and balanced union. Path compression helps, but the
exact implementation lacks the rank/size rule needed for the standard strongest
bound.

**Trace a tiny grid**

For a two-by-two grid with three connected land cells and one water cell, union
find begins with four components. The scan performs two successful land unions,
reducing its count to two: one land root and one untouched water root.
`zero_count` is one, so the returned value is `2 - 1 = 1` island.

For all water, no unions occur, `count` remains $mn$, and `zero_count` is $mn$,
so the result is zero. For isolated land cells, no land unions connect them,
and each remains one counted component after water subtraction.

**Why the corrected union-find result is exact**

Every same-island path consists of horizontal and vertical land edges. Each
such edge is processed once through its lower or right endpoint, so repeated
union operations eventually place every cell in that island under one root.

No union crosses water or a diagonal, so cells from different islands never
share a root. Successful unions reduce the count exactly when two previously
separate land components become one. After subtracting one never-unioned
component for every water cell, the remaining root count is exactly the island
count.

**The exact Python 3 source fails on the first real union**

Constructor assignment `self.set = range(n)` reflects Python 2 code, where
`range` produced a mutable list. In Python 3, `range(n)` is an immutable range
object. `union_set` later executes an indexed assignment such as
`self.set[root] = other_root`, which raises `TypeError`.

Inputs with no adjacent land may avoid that assignment and appear to work, but
any successful union exposes the defect. The required Python 3 correction is
`self.set = list(range(n))`. The algorithmic explanation above assumes that
minimal representation repair; the exact stored primary implementation is not
generally executable in Python 3.

**Inactive traversal alternatives**

`Solution2` is an iterative DFS that mutates visited land to water and uses an
explicit stack. This is the implementation that actually matches the optimal
manifest summary and safely avoids recursive depth. `Solution3` performs the
same marking with a deque-based BFS. Neither numbered class is selected by the
normal `Solution` entry point.

Both inactive methods call their traversal helper even on water cells and use
its boolean return to decide whether to increment, which is logically correct
for the nonempty rectangular contract.

## Complexity detail

Let $N = mn$ be the cell count. The scan examines every cell and at most two
neighbor edges per land cell. With a mutable parent array, path compression
makes operations efficient in practice. The source advertises roughly
$O(N\alpha(N))$, but without union by rank or size that precise classical bound
is not fully justified. The manifest's $O(mn)$ describes the intended near-
linear behavior rather than a guaranteed property of the exact linking rule.

The parent structure stores one entry per cell and recursive `find_set` can use
additional stack depth, so space is $O(mn)$. As written in Python 3, the first
successful union fails before asymptotic completion.

## Alternatives and edge cases

- **Required Python 3 repair:** Wrap `range(n)` with `list(...)` so parent entries can be updated.
- **Union by rank or size:** Add balancing to support the standard near-constant amortized union-find bound.
- **Iterative DFS:** Inactive `Solution2` is direct, mutates the grid, and avoids union-find bookkeeping.
- **BFS:** Inactive `Solution3` uses a queue and has the same component-count reasoning.
- **All water:** Count subtraction returns zero without any union assignment.
- **One isolated land:** Returns one and may not expose the immutable-range defect.
- **Adjacent land:** Requires a union and triggers `TypeError` in the exact Python 3 source.
- **Diagonal land:** Remains separate because only top and left side edges are joined.
- **Empty grid:** Explicit guard returns zero, although the Reference already guarantees a row.
- **Rectangular grid:** Flat indexing relies on a common column count.
