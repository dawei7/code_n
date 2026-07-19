## General
**Collect each connected component once**

Scan the grid with a global visited set. At every unvisited land cell, run a four-directional traversal and collect all of that island's coordinates relative to the traversal origin.

**Generate all eight rigid orientations**

For each relative point `(x, y)`, the combinations
`(±x, ±y)` and `(±y, ±x)` describe the four rotations and their reflected forms. Build the transformed point set for each of these eight coordinate rules.

**Remove translation after every transform**

A rotation can move coordinates into negative ranges. Normalize each transformed set by subtracting its minimum x-coordinate and minimum y-coordinate from every point. The resulting `frozenset` depends only on that oriented shape, not its position.

**Use the complete transform family as the identity**

Wrap the eight normalized sets in another `frozenset`. Rotating or reflecting an island merely permutes this family, so congruent islands produce exactly the same nested set without needing to choose an arbitrary orientation. Insert each family into the global shape set.

**Why distinct families mean noncongruent islands**

If two islands are congruent, applying the inverse rigid transform makes one normalized orientation equal to the other, and their full transform families coincide. Conversely, a shared normalized orientation directly supplies a rotation or reflection plus translation that makes the occupied cells coincide. Thus family equality is exactly the required equivalence.

## Complexity detail
Every cell is scanned and each land cell is traversed once. Constructing eight transforms performs constant work per land cell, so total time is $O(RC)$. Visited coordinates, traversal storage, transformed shapes, and distinct canonical families together use $O(RC)$ space.

## Alternatives and edge cases
- **Lexicographically minimum transform:** sort every normalized orientation and choose the smallest tuple; it is conventional but introduces $O(a \log a)$ work for an island of area `a`.
- **Pairwise shape matching:** try all transforms whenever a new island is compared with earlier representatives; repeated comparisons can become quadratic in the number of islands.
- **Reflood from every land cell:** normalization still deduplicates results, but repeatedly traversing one component can take quadratic time in its area.
- An all-water grid returns `0`.
- All isolated cells belong to one shape class.
- Shapes with equal area are not necessarily congruent.
- Symmetric shapes may produce fewer than eight distinct normalized orientations; the outer set naturally removes duplicates.
