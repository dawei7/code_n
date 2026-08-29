## General

**Represent coordinates as a bipartite graph**

Create one kind of node for every x-coordinate and another kind of node for every y-coordinate. An existing point `(x,y)` becomes an edge between x-node `x` and y-node `y`.

Two points sharing an x-coordinate correspond to two edges incident to the same x-node. Two points sharing a y-coordinate correspond to edges incident to the same y-node. Following repeated activation steps is therefore the same as walking through connected edges in this bipartite graph.

An activation component of points is exactly one connected component of edge-bearing coordinate nodes. Starting from any point in that component eventually activates every point-edge in it and cannot reach an edge in another component.

**Keep x and y namespaces separate**

The numerical coordinate `5` used as an x-coordinate is not the same graph node as numerical coordinate `5` used as a y-coordinate. They represent different axes and should connect only when an actual point supplies an edge between them.

The source chooses `m = int(3e9)` and represents y-coordinate `y` as `y+m`. Original x-coordinates lie in `[-10^9,10^9]`, while shifted y-coordinates lie in `[2\cdot10^9,4\cdot10^9]`. These ranges are disjoint, so an x-node can never collide with a y-node.

For every point, `uf.union(x, y + m)` inserts its two coordinate nodes if needed and connects them. Path compression in `find` and union by component size make the sequence of operations almost linear.

The union-find `size` field counts coordinate nodes, not points. A component can have differing numbers of unique coordinates and point edges, so those sizes are not the desired activation counts.

**Count point edges per component**

After all unions are complete, the source scans every point once. It finds the root of the point's x-node and increments `cnt[root]`.

The x-node and shifted y-node of that point were unioned, so either endpoint has the same final root. Counting through x is simply convenient. Each input point contributes exactly once, so `cnt[root]` is the number of existing points in that activation component.

It is important that counting occurs after all unions. Roots may change while later edges merge coordinate components; a counter built too early would need to be merged alongside union-find state.

**What one added point can connect**

The new point `(x,y)` is one new graph edge. Its x endpoint belongs to at most one existing component, or to no component if that x-coordinate is new. Its y endpoint likewise belongs to at most one existing component.

Therefore one new edge can touch and merge at most two existing activation components. Including the new point itself, no construction can activate more than

$$
1+\text{size of one component}+\text{size of another component}.
$$

The strongest possible upper bound is obtained from the two largest existing component point counts.

**Why the two largest components can always be joined**

Choose any existing x-coordinate from the largest component and any existing y-coordinate from the second-largest component. Add the point using that coordinate pair.

The pair cannot already be an existing point. If `(x,y)` already existed, its graph edge would connect those x and y coordinate nodes, which would mean the two supposed components were already one component. This contradicts their being distinct.

The new point is therefore legal. Its x-coordinate activates the first component, its y-coordinate activates the second, and transitive propagation reaches every point in both. The count is their two sizes plus one for the added point.

If there is only one existing component, use one coordinate from it and choose a fresh integer coordinate on the other axis. The new point connects that component and adds itself. Conceptually the missing second component has size zero.

If there are at least two isolated single-point components, choosing an x-coordinate from one and a y-coordinate from another activates those two points plus the new one, for three.

This construction attains the upper bound, proving that “largest two plus one” is exact.

**Track the two largest counts without sorting**

The source maintains `mx1` and `mx2`.

For each component size `x`:

- if `x` exceeds `mx1`, the old largest becomes second-largest and `x` becomes largest;
- otherwise, if `x` exceeds `mx2`, it becomes second-largest.

Strict comparisons still handle equal maximum sizes: the first fills `mx1`, and an equal later value fails the first comparison but exceeds the initially smaller `mx2`.

The return value `mx1 + mx2 + 1` includes the new point.

**Union-find behavior**

`find` lazily creates unseen coordinate nodes as singleton sets. Recursive path compression rewrites every visited parent to the root. `union` attaches the smaller coordinate-node component under the larger one; when sizes tie, its `else` branch chooses the second root. The particular root identity does not matter because `cnt` is built only after connectivity is finalized.

For the first example, the points `(1,1)`, `(1,2)`, and `(2,2)` form one connected bipartite component, so `mx1=3` and `mx2=0`. Adding a point incident to that component activates all three existing points plus itself, yielding four.

For diagonal points `(1,1)`, `(2,2)`, and `(3,3)`, there are three components of size one. One edge can join only two, so the maximum is `1+1+1=3`.

## Complexity detail

Let `N` be the number of points. There are at most `2N` distinct coordinate nodes and exactly `N` point edges. The union phase performs `N` unions, and the counting phase performs `N` finds. With path compression and union by size, time is `O(N\alpha(N))`, where `\alpha` is the inverse Ackermann function.

Scanning component counts for the top two adds `O(N)` time, which is absorbed by the same bound. The parent, union-size, and component-count dictionaries store `O(N)` entries, giving `O(N)` space. These match the manifest.

Python integers safely represent shifted coordinates through four billion. The offset is an exact integer even though it is written as `int(3e9)`.

## Alternatives and edge cases

- **Build a point-to-point graph:** Connect every pair sharing x or y, then find components. A coordinate with many points creates quadratically many explicit edges; coordinate-node union avoids that explosion.
- **Breadth-first activation for every possible new point:** The coordinate domain is infinite and repeated graph traversal is too expensive. Component compression reduces every choice to selecting at most two sizes.
- **Use raw numeric coordinates for both axes:** This falsely merges x-value `v` with y-value `v` even without a point connecting them. Separate types or a safe offset are mandatory.
- **Use union-find node sizes as point counts:** Coordinate-node count is not edge count. The separate `Counter` correctly counts actual points.
- **Sort component sizes:** Sorting works in `O(C\log C)` for `C` components, but only the largest two are needed and can be found linearly.
- **One existing component:** The result is `N+1`; the second-largest size remains zero.
- **One existing point:** Add a distinct point sharing either coordinate, activating both, so the answer is two.
- **Two components with chosen coordinate pair already occupied:** Impossible; such an existing edge would already unite the components.
- **New coordinates on both axes:** The added point activates only itself, which is never better when at least one existing point is available.
- **Duplicate maximum component sizes:** The streaming top-two logic keeps both equal values.
- **Distinct point guarantee:** It ensures each input edge is unique. Multiple points may still share one coordinate and are correctly joined.
- **Negative coordinates:** The offset keeps shifted y nodes disjoint even at the extreme negative bound.
- **Added point count:** The final plus one is essential because the return includes the newly inserted and initially activated point.
