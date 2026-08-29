## General

After each operation, the land cells form an undirected graph:

- every active land cell is a vertex;
- two vertices share an edge when their cells are horizontally or vertically adjacent.

An island is exactly a connected component of this graph. The operations only add land; they never remove it. This makes disjoint-set union, also called union-find, a natural way to maintain component membership incrementally.

The source also keeps a Boolean-like `grid` to distinguish land from water and an integer `cnt` for the current number of land components. Each genuinely new land cell begins as one new component. Joining it to a neighboring component reduces the count by one only when the two cells were previously in different components.

**Flattening grid positions**

The usual row-major identifier for cell $(i,j)$ is

$$
id(i,j)=i\cdot n+j.
$$

For an $m\times n$ grid, this maps every cell to one unique integer from 0 through $mn-1$. Horizontal or vertical adjacency is still checked with row and column coordinates; flattening is used only as the union-find key.

The exact `UnionFind.union` method calls `find(a - 1)` and `find(b - 1)` rather than `find(a)` and `find(b)`. This looks like an off-by-one error, but under Python indexing it acts as a consistent cyclic relabeling of the valid identifiers:

$$
0\mapsto -1\equiv mn-1,
$$

$$
1\mapsto0,\quad2\mapsto1,\quad\ldots,\quad mn-1\mapsto mn-2.
$$

Python list index `-1` refers to the final entry. Thus, every valid cell identifier still maps to a distinct union-find slot, and the same mapping is applied to both endpoints of every union. Connectivity is unchanged by a one-to-one relabeling. The convention is unusual and would be unsafe in languages where negative indexing is invalid, but it is internally consistent in this exact Python source.

**Disjoint-set state**

`p[x]` stores the parent of union-find slot `x`. Initially, every slot is its own root. `size[x]` is meaningful for a root and stores the number of represented slots in that tree.

`find(x)` follows parent links until reaching a root whose parent is itself. On the recursive return path, it assigns every visited node directly to that root. This is path compression: later searches from those nodes become much shorter.

`union(a, b)` first finds the two roots after applying the source's shifted indexing. If the roots are equal, both land cells are already in the same connected component, so it returns `False` and changes nothing.

If the roots differ, union by size attaches the smaller tree below the larger tree's root. On a tie, the first root is attached below the second. The new root's size is increased by the absorbed tree's size, and the method returns `True` to report that two components became one.

Path compression and union by size together make repeated connectivity operations extremely close to constant time amortized.

**Why a separate grid is necessary**

The union-find arrays are initialized for all $mn$ slots, including cells that are still water. Therefore, parent membership alone cannot say whether a cell is active land. The matrix `grid` supplies that missing state:

- `grid[i][j] == 0` means the cell has not been added;
- `grid[i][j] == 1` means it is active land.

The algorithm attempts a union only when the neighboring coordinate is in bounds and its grid entry is already land. Inactive union-find roots are never connected into the island graph.

**Handling one land-addition operation**

For each `(i, j)` in `positions`, the source first checks `grid[i][j]`.

If it is already 1, this is a duplicate addition. The grid and all components are unchanged, so the current `cnt` is appended immediately. This early return from the operation is important: incrementing `cnt` again would invent a new island on top of existing land.

For genuinely new land, the source:

1. sets `grid[i][j] = 1`;
2. increments `cnt` because an isolated new vertex initially forms a new component;
3. checks the four neighboring coordinates;
4. unions with each neighboring land cell;
5. decrements `cnt` for each union that actually merges two different roots;
6. appends the resulting count.

The direction tuple `(-1, 0, 1, 0, -1)` is traversed with `pairwise`. Its adjacent pairs are

`(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`,

representing up, right, down, and left. Diagonal cells are never considered, matching four-directional island connectivity.

**Why the count decreases only on a successful union**

A new land cell can touch several neighbors belonging to the same old island. The first connection to that island merges the new singleton component with it and reduces the number of components by one. Another neighboring cell from that same island does not perform a second component merge; both endpoints already have the same root.

For example, imagine a new cell fills a gap and touches two cells that are already connected by another route. Incrementing `cnt` creates one temporary singleton. The first union returns `True` and cancels that increment. The second union returns `False`, correctly leaving the count unchanged. Decrementing for every land neighbor without checking roots would undercount islands.

Conversely, if the new cell touches two previously separate islands, the first successful union joins it to one island and decreases `cnt` once. The second successful union joins that combined component to the other island and decreases `cnt` again. The new bridge legitimately turns two old islands plus the new cell into one component.

**Tracing the example**

For a $3\times3$ grid:

- Add `(0, 0)`: it has no land neighbor. `cnt` rises from 0 to 1.
- Add `(0, 1)`: `cnt` first rises to 2, then union with `(0, 0)` succeeds and lowers it to 1.
- Add `(1, 2)`: none of its four neighbors is land, so `cnt` rises to 2.
- Add `(2, 1)`: it is also isolated at that moment, so `cnt` rises to 3.

The recorded sequence is `[1, 1, 2, 3]`.

**Why the maintained count is exact**

Initially, there are no land vertices and `cnt = 0`. Assume `cnt` equals the number of land components before an operation.

A duplicate operation changes no graph vertex or edge, and the source leaves the count unchanged. A new cell first appears as a singleton, so incrementing the count by one is correct before adding its incident edges. Each successful union adds an edge between two different components, combining exactly two components into one and reducing their count by exactly one. A failed union adds no new connectivity between components because its endpoints are already connected, so the count must not change.

After all four possible edges are processed, `cnt` again equals the graph's component count. By induction over operations, every appended value is the correct number of islands.

## Complexity detail

Let $k$ be the number of operations and let $N=mn$ be the number of grid cells.

The exact source allocates and initializes parent and size arrays of length $N$ and an $m\times n$ grid, costing $O(N)=O(mn)$ time and space before processing operations.

Each operation performs constant grid work and checks exactly four neighbors. A check may invoke one union, containing a constant number of finds. With path compression and union by size, a sequence of union-find operations costs $O(\alpha(N))$ amortized per operation, where $\alpha$ is the inverse Ackermann function. Total time is

$$
O(mn+k\alpha(mn)).
$$

In practice, $\alpha(mn)$ is tiny, but it is retained in the formal bound.

The parent array, size array, and dense activity grid each use $O(mn)$ storage. The returned list uses $O(k)$ output space. Excluding output, auxiliary space is $O(mn)$.

The manifest describes a sparse $O(k)$ union-find and gives $O(k\alpha(k))$ time. The exact `solution.py` is dense, so those sparse bounds do not describe this implementation. A dictionary-backed variant could realize them when the grid is much larger than the number of additions.

## Alternatives and edge cases

- **Sparse dictionary union-find:** Create parent and size entries only when a position first becomes land. This avoids $O(mn)$ initialization and uses $O(u)$ state for $u\le k$ unique added cells, matching the manifest's sparse summary.
- **Recount islands after every operation:** Run DFS or BFS over the entire grid each time. This can cost $O(kmn)$ and repeats almost all connectivity work.
- **Flood-fill only from the new cell:** It can discover connected land, but maintaining and relabeling components across many additions is less efficient than union-find.
- **Decrement for every land neighbor:** This is wrong when two neighboring cells already belong to the same island. Only a union of different roots reduces the component count.
- **Union diagonal neighbors:** Islands use horizontal and vertical adjacency only. Adding diagonals would incorrectly merge separate islands.
- **Duplicate position:** The current count must be repeated unchanged. The early `grid[i][j]` check prevents a false new component and repeated unions.
- **First operation:** A new cell has no previously active neighbor, so the answer is always one.
- **One-cell grid:** The first add returns one; any duplicate additions continue returning one.
- **Boundary cell:** Neighbor coordinates are checked before indexing the grid, preventing negative wrapping or out-of-range access.
- **A new isolated cell:** No union succeeds, so the initial count increment remains and the island count rises by one.
- **A new cell touching one island:** Exactly one root merge succeeds, canceling the singleton increment; the island count stays unchanged.
- **A bridge between several islands:** One successful union occurs for each distinct neighboring component, so the count can decrease by more than one during a single operation.
- **Several neighbors in one component:** Path compression makes their roots equal, and only the first merge succeeds.
- **Shifted union-find indices:** Subtracting one works here only because every valid flattened ID receives the same bijective Python-index transformation. Reusing this class with arbitrary IDs, zero-length arrays, or a language without negative indexing would be unsafe.
- **Recursive `find`:** Union by size limits tree height before compression, and compression flattens paths further. An iterative implementation could avoid recursion entirely but would preserve the same component logic.
- **Maximum grid product:** Dense storage is feasible under the stated $mn\le10^4$ constraint, even though it does not achieve the sparse follow-up bound.
