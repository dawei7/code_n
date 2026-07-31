## General

**Turn activation into connected components**

Connect two existing points when they share an x-coordinate or a y-coordinate. Repeated activation follows exactly the paths in this graph, so activating any point reaches its entire connected component and cannot leave that component.

Build these components with a disjoint-set union structure over point indices. For each x-coordinate, remember the first point seen with that x and union every later matching point with it. Do the same independently for y-coordinates. One representative per coordinate is sufficient because all points sharing that coordinate become connected transitively.

**Bound what the new point can join**

For a chosen new point `(x, y)`, its x-coordinate can attach it to at most one existing component: every existing point with that x is already connected. Its y-coordinate can likewise attach it to at most one component. Thus the new point can merge no more than two existing components, and an upper bound is

$$
1+s_1+s_2,
$$

where $s_1$ and $s_2$ are the two largest component sizes, with $s_2=0$ when only one component exists.

**Show that the bound is attainable**

Every nonempty component contains at least one represented x-coordinate and one represented y-coordinate. Choose an x-coordinate from the largest component and a y-coordinate from the second-largest component. If that pair already existed as a point, it would connect the two components, contradicting their being distinct; therefore it is a valid new coordinate and joins both components.

When only one component exists, choose one of its coordinates and a fresh coordinate on the other axis. The new point then activates that component and itself. Consequently, the two-largest-sizes bound is always attainable. After all unions, scan DSU roots, retain the two largest component sizes, and add one.

## Complexity detail

Each of the $n$ points causes at most two union operations. With path compression and union by size, the total time is $O(n\alpha(n))$, where $\alpha$ is the inverse Ackermann function. The DSU arrays and coordinate-owner maps require $O(n)$ auxiliary space.

The benchmark defines size as $n$ and uses isolated-coordinate sets of `16`, `64`, and `256` points. The accepted DSU source and an independent coordinate-bucket traversal should retain near-linear scaling. A correct control that compares every pair of points to construct the same components performs $O(n^2)$ work and should fail only the scaling verdict.

## Alternatives and edge cases

- **Coordinate-bucket traversal:** Store points under each x and y value, then run graph search while expanding each coordinate bucket once; this is another $O(n)$-space near-linear construction.
- **Bipartite coordinate graph:** Treat distinct x-values and y-values as vertices and each point as an edge. Its connected edge components are exactly the activation components.
- **Pairwise graph construction:** Testing every pair for a shared coordinate is correct but requires $O(n^2)$ comparisons before traversal.
- **One existing component:** The result is $n+1$; share one coordinate with that component and choose a fresh coordinate on the other axis.
- **All points isolated:** The added point can join only two singleton components, so the answer is `3` when at least two points exist.
- **Single input point:** A new point can share one coordinate with it, activating both points for an answer of `2`.
- **Repeated individual coordinates:** Coordinate pairs are distinct, but many points may share the same x or the same y; one remembered owner connects the entire group.
- **Signed boundaries:** Hash-map keys handle coordinates at both $-10^9$ and $10^9$ without allocating by coordinate magnitude.
