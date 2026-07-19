## General
**Filter before measuring distance**

Scan `points` from left to right. Ignore a point unless its x-coordinate equals `x` or its y-coordinate equals `y`. For a valid point, compute its Manhattan distance. Because one coordinate difference is zero, this is also the absolute displacement along the shared row or column.

**Let scan order implement the tie-break**

Store the smallest valid distance seen and its index. Replace the stored index only when a new distance is strictly smaller. An equal distance does not replace it, so the earliest—and therefore smallest—index survives automatically. If no update ever occurs, the initial index `-1` is the required result.

## Complexity detail
The scan examines each of the $n$ points once and performs constant work per point, for $O(n)$ time. The best index and distance are the only auxiliary state, so space is $O(1)$.

## Alternatives and edge cases
- **Collect and sort valid candidates:** Sorting `(distance, index)` pairs produces the same result but costs $O(n\log n)$ time and $O(n)$ space.
- **Repeated prefix search:** Recomputing the best point after every new input point is correct but can take $O(n^2)$ time.
- A point at `(x, y)` is valid with distance zero and cannot be beaten by a later point.
- Sharing either coordinate is sufficient; sharing both is not required.
- Equal minimum distances must preserve the smaller original index.
- When every point differs in both coordinates, return `-1`.
