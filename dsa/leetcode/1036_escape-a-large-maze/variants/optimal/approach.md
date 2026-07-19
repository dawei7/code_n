## General
**Use the small blocked set, not the huge grid:** At most $B=200$ cells are blocked. Those cells can surround only a bounded region; they cannot form a wall across a million-wide grid.

**Bound the size of an enclosure:** A barrier made from $B$ blocked cells can enclose at most
$$
E=\frac{B(B-1)}{2}
$$
reachable open cells. Run breadth-first search from one endpoint, stopping when it reaches the other endpoint or visits more than $E$ cells. Exceeding the bound proves the start is not enclosed, so continuing across the enormous open grid is unnecessary.

**Check both endpoints:** Escaping the source's local region does not prove the target is not separately enclosed. Apply the same bounded search from source toward target and from target toward source. A path exists exactly when each search either reaches the other endpoint or exceeds the enclosure limit.

Blocked coordinates are stored in a hash set, so every neighbor test is expected constant-time. If a bounded search exhausts its queue within $E$ cells, the explored region is sealed and escape is impossible. If it exceeds $E$, the blocked set is too small to surround it. When neither endpoint is enclosed, both lie in the grid's common unbounded open region and can connect.

## Complexity detail
Each bounded search visits at most $E+1=O(B^2)$ cells and checks four neighbors per cell. Hash-set membership is expected $O(1)$, so two searches take $O(B^2)$ time and store $O(B^2)$ visited coordinates.

## Alternatives and edge cases
- **Unbounded grid BFS:** Searching toward a distant target may explore an impractical fraction of the $10^{12}$ cells.
- **Linear blocked lookup:** Scanning all $B$ blocked coordinates for every neighbor keeps the bounded search correct but takes $O(B^3)$ time.
- **Coordinate compression:** Preserve blocked cells, endpoints, and representative gaps, then search the compressed grid. This is valid but more elaborate.
- **No or one blocked cell:** The enclosure bound is zero, and neither endpoint can be trapped.
- **Grid-corner enclosure:** The outer grid boundary can combine with only two blocked neighbors to trap a corner.
- **Target enclosure:** The reverse search is essential even when the source quickly escapes.
- **Finite barrier:** A short row or column of blocked cells can be walked around in the enormous remaining grid.
