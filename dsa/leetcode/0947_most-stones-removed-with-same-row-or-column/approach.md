## General

**View removable relationships as connected components**

Make each stone a graph vertex. Connect two stones when they share a row or share a column. Stones joined through several such edges belong to the same connected component, even if the endpoints do not directly share a coordinate.

Within a connected component containing `k` stones, exactly `k - 1` stones can be removed. At least one must remain because the final stone has no other remaining stone in its component. Conversely, the other `k - 1` can be removed by preserving a suitable connected backbone until the end.

If the graph has `c` components among `n` stones, the maximum removals are:

`n - c`.

The solution obtains this quantity indirectly by counting successful union operations.

**Union-Find representation**

The `UnionFind` object begins with every stone in its own component:

- `p[i] = i` makes each stone its own parent;
- `size[i] = 1` records one stone in each initial tree.

Method `find(x)` follows parent links to the component root. Its recursive assignment `self.p[x] = self.find(self.p[x])` performs path compression: after finding the root, every node on that path points directly to it. Later searches become very fast.

Method `union(a, b)` finds roots `pa` and `pb`. If they are equal, the stones already belong to the same component, so the method returns false.

Otherwise, it attaches the smaller component tree beneath the larger one using `size` and returns true. This union-by-size rule keeps trees shallow.

**How the stone pairs are examined**

The outer loop processes stone `i` with coordinates `x1, y1`.

The inner enumeration ranges over `stones[:i]`, so it compares stone `i` with every earlier stone exactly once. It does not compare a stone with itself and does not later repeat the pair in reverse order.

When `x1 == x2` or `y1 == y2`, the two vertices have an edge and should be in one component. The code calls `uf.union(i, j)`.

The Boolean return value participates directly in arithmetic. In Python, true contributes one and false contributes zero:

`ans += uf.union(i, j)`.

Thus `ans` counts only unions that merge two previously separate components. Redundant edges inside an already-connected component do not increase it.

**Why successful unions equal removable stones**

Initially there are `n` components and zero successful unions. Every successful union reduces the component count by exactly one. A failed union changes nothing.

After all graph edges have been considered, stones connected by any path share a Union-Find root, so the number of successful unions is `n - c`.

That is exactly the maximum removal count derived from component sizes. Counting successful merges avoids a separate final pass that counts roots.

**Why a component can lose all but one stone**

Consider any connected component. Choose a spanning tree of its stone graph. A tree with `k` vertices has `k - 1` edges.

Remove leaf stones one at a time while keeping their tree neighbor. Each leaf shares a row or column with that remaining neighbor, so its removal is legal. Removing a leaf leaves the remaining tree connected. Continue until one stone remains.

This shows that `k - 1` removals are achievable. Removing the final stone is impossible because no other stone in that component remains. The bound is both achievable and maximal.

**Example structure**

Suppose three stones form a chain: the first shares a row with the second, and the second shares a column with the third. The first and third need not share either coordinate.

The first relevant union merges two singleton components and increments `ans`. The second relevant union joins the third stone to that component and increments again. The component has three stones and contributes two removable stones.

If a later pair adds another edge between stones already connected through the chain, `union` returns false. Counting that edge as another removal would be wrong because a connected component contributes vertices minus one, not its number of edges.

**Why all connectivity is discovered**

Every unordered stone pair is checked. Therefore, every graph edge implied by a shared row or column is passed to Union-Find. Union operations compute the transitive closure of connectivity: if stone `a` joins `b` and `b` joins `c`, all three receive the same root even without a direct `a, c` edge.

At the end, Union-Find components exactly match graph connected components, making the merge count correct.

## Complexity detail

Let `n` be the number of stones.

The exact implementation compares every unordered pair, which is `n(n - 1) / 2 = O(n^2)` comparisons. Each qualifying pair performs Union-Find operations costing amortized `O(alpha(n))`, where `alpha` is the inverse Ackermann function. The total bound is `O(n^2 alpha(n))`, commonly simplified to `O(n^2)`.

The parent and size arrays use `O(n)` space. The slice `stones[:i]` creates a temporary list of up to `O(n)` references during an outer iteration; peak auxiliary space remains `O(n)`.

The current manifest states `O(n alpha(n))` time, but that would require grouping stones by row and column rather than checking all pairs. This document reports the exact checked-in code.

## Alternatives and edge cases

- **Row and column representative maps:** Union each stone with a previously seen stone in its row and column. This avoids all-pairs comparison and can achieve `O(n alpha(n))` expected time.
- **Coordinate-node Union-Find:** Treat each row and each encoded column as graph nodes and union a stone's row with its column. Count connected coordinate roots afterward.
- **Depth-first search:** Build row and column adjacency and count graph components. It is correct, but naive pairwise adjacency construction still costs `O(n^2)`.
- **Single stone:** No pair or successful union exists, so zero stones can be removed.
- **All stones in one row:** Each new stone joins the same component; exactly `n - 1` unions succeed and all but one stone are removable.
- **No shared row or column:** Every stone remains isolated, no union succeeds, and the answer is zero.
- **Redundant cycles:** Extra edges within a component return false and do not inflate the answer.
- **Transitive connection:** Stones need not directly share coordinates with every component member; a path of row and column relationships is enough.
- **Unique coordinates:** No two stones occupy the same point, though sharing one coordinate is precisely what creates edges.
- **Boolean addition:** The code relies on Python treating true as one and false as zero. An explicit conditional would be needed in languages without that behavior.
