## General
**Fold the board by symmetry.** Reflections across either axis and swapping the coordinates preserve knight distances. Replace both coordinates by their absolute values and arrange them as $a\ge b\ge0$. Only this first-octant target needs to be analyzed.

**Combine two unavoidable lower bounds.** One move changes either coordinate by at most 2, so at least $\lceil a/2\rceil$ moves are needed. It changes Manhattan distance by at most 3, so at least $\lceil(a+b)/3\rceil$ moves are needed. Start with

$$
d=\max\left(\left\lceil\frac{a}{2}\right\rceil,\left\lceil\frac{a+b}{3}\right\rceil\right).
$$

A knight changes square color on every move. Therefore the parity of the move count must match the parity of $a+b$; if `d + a + b` is odd, increment `d`. Away from the two small exceptional configurations, these coordinate, Manhattan, and parity constraints are also sufficient: knight moves can be paired and oriented to distribute the required progress across both coordinates without exceeding any bound.

**Repair the local exceptions.** The target $(1,0)$ needs three moves even though the global bounds suggest one, because no first move can land there and the knight must loop around. The target $(2,2)$ needs four moves rather than two for the same local-geometry reason. Handle those two symmetric forms explicitly; the bound-and-parity value is exact for every other target, including the origin.

## Complexity detail
The method performs a fixed number of absolute-value, ordering, ceiling-division, maximum, parity, and exception checks regardless of coordinate magnitude. It therefore takes $O(1)$ time and uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Incremental move-count search:** Testing successive move counts until all coordinate, Manhattan, and parity bounds hold is correct after the two exceptions, but takes $O(r)$ time for distance scale $r$.
- **Breadth-first search:** BFS over board positions directly guarantees the shortest path, but explores $O(r^2)$ positions and uses $O(r^2)$ space for target distance scale $r$.
- **Bidirectional breadth-first search:** Expanding from both endpoints reduces constants but still maintains growing frontiers and visited maps.
- **Origin:** Both lower bounds and parity yield zero, so no special positive move count is introduced.
- **Negative coordinates:** Absolute values are safe because reflecting every move reflects an entire shortest route.
- **Swapped coordinates:** A 90-degree rotation exchanges axes without changing path length.
- **Target `(1,0)`:** The generic global bounds miss the three-move local detour.
- **Target `(2,2)`:** The generic two-move estimate is geometrically impossible and must become four.
- **Parity:** Raising a valid lower bound by one is necessary whenever its color parity differs from the target square.
