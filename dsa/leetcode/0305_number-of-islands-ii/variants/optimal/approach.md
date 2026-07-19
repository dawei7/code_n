## General
**Treat each new land cell as a provisional island**

Store only cells that have become land. When a genuinely new cell arrives, create a one-element disjoint-set component and increase the island count by one. If the coordinate already exists, the grid has not changed, so append the existing count immediately.

Map `(row, column)` to one integer identifier such as `row * n + column`. Parent and component-size maps then support path-compressed root lookup and union by size without allocating the entire potentially sparse grid.

**Each successful neighboring union removes one island**

Inspect the four neighboring coordinates. Water and out-of-bounds neighbors have no component. For a land neighbor, find both roots. If they differ, union the components and decrement the island count exactly once. If they already share a root, the adjacency adds a redundant connection and does not change the count.

A new cell may touch several positions belonging to the same island, so comparing roots—not merely counting land neighbors—is essential. It may also bridge several distinct islands, in which case every successful union reduces the total.

For additions `[[0,0],[0,2],[1,0],[1,2],[1,1]]`, the counts are `[1,2,2,2,1]`. The final center cell touches both existing components; its first union absorbs one and its second merges the other.

**Disjoint-set roots correspond exactly to current islands**

Initially there are no land cells and no roots. Adding a new cell creates exactly the new singleton component represented by its root. A successful union occurs precisely across a four-directional land edge joining two formerly separate components, so replacing their two roots with one mirrors the corresponding island merge. Redundant edges preserve both the physical component and its root.

By induction after every operation, disjoint-set components and grid islands are in one-to-one correspondence. The maintained component count is therefore the required island count.

## Complexity detail
For `k` additions, each new coordinate performs at most four unions and a constant number of path-compressed finds. Union by size gives $O(k \cdot \alpha(k))$ total time, conventionally near-linear. Parent and size maps contain at most the `k` distinct land cells and use $O(k)$ space.

## Alternatives and edge cases
- **Recount islands with DFS after every addition:** is correct but repeatedly revisits old land and can take $O(kmn)$ or $O(k^2)$ on a sparse active region.
- **Subtract the number of land neighbors:** is wrong when several neighbors already belong to the same island.
- Duplicate additions leave the count unchanged. Boundary and corner cells simply have fewer valid neighbors.
