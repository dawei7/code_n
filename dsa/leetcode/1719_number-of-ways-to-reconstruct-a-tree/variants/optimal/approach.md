## General
**Interpret each pair as undirected comparability**

Build an adjacency set for every node: two nodes are adjacent exactly when the input says one must be an ancestor of the other. The root is an ancestor of every other node, so its adjacency degree must be $V-1$. If no such node exists, reconstruction is impossible.

**Choose the nearest possible parent by degree**

For each non-root node `u`, every ancestor of `u` must be adjacent to `u`. A parent must therefore be one of `u`'s neighbors and must have degree at least `u`'s degree, because everything comparable with `u` except that parent must also be comparable with the parent. Among eligible neighbors, choose one with the smallest degree; a larger-degree choice would skip a nearer required ancestor.

After selecting parent `p`, verify that every neighbor of `u` other than `p` also belongs to `p`'s adjacency set. Failure of this containment means the claimed comparabilities cannot be nested along a rooted-tree path, so no reconstruction exists.

**Detect when the parent relation is interchangeable**

If `u` and its selected parent have equal degrees, their comparability neighborhoods provide no evidence that forces which one is above the other. Swapping their parent relationship produces another valid reconstruction, so the answer becomes `2`. Otherwise the relation is forced. If every node passes containment and no equal-degree ambiguity occurs, the reconstruction is unique.

## Complexity detail
At most $\binom{V}{2}$ distinct pairs exist. Building the adjacency sets takes $O(V^2)$ time and space in the dense case. Across all nodes, parent selection and containment inspect $O(V^2)$ adjacency entries, with each set membership check taking expected $O(1)$ time. The total bounds are therefore $O(V^2)$ time and $O(V^2)$ space.

## Alternatives and edge cases
- **Explicitly enumerate rooted trees:** Testing parent assignments against the pair set gives a direct oracle on very small node sets, but the number of labeled rooted trees grows exponentially and is unsuitable for the full domain.
- **Linear membership structures:** Adjacency lists raise dense-case containment to $O(V^3)$; checking each required relation by rescanning the raw pair list can take $O(V^4)$.
- **No universal node:** Without a degree-$V-1$ node, no possible root is comparable with every other node, so return `0`.
- **Equal degrees:** Equality between a node and its valid parent is evidence of multiple reconstructions, not an inconsistency.
- **A single pair:** Either endpoint can be the root of the two-node tree, so the result is `2`.
- **Input direction:** Although each pair is stored with its smaller value first, numeric order says nothing about which node is the ancestor.
