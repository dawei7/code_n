## General
**Reduce the circle to two complementary arcs.** Swapping `start` and `destination` when necessary makes `start <= destination`. The consecutive edges with indices from `start` through `destination - 1` form one route between the stops. Every remaining edge forms the route in the opposite direction.

**Accumulate both quantities in one pass.** Walk through `distance`, adding every edge to `total`. Add an edge to `direct` exactly when its index lies in the normalized half-open interval `[start, destination)`. The complementary arc then has length `total - direct`, so returning the smaller value checks both directions. These arcs partition all circle edges, which proves that neither possible route is omitted or counted twice.

## Complexity detail
The single pass examines all $n$ edge distances once, for $O(n)$ time. Apart from the two accumulated distances and normalized stop indices, no storage grows with the route, so the auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Prefix sums:** A prefix array makes later arc queries constant time, but this problem asks only one pair and the array would use unnecessary $O(n)$ space.
- **Generic shortest-path algorithm:** Modeling the stops as a weighted graph and running Dijkstra's algorithm is correct, but it ignores the fact that a cycle has exactly two simple routes between the stops.
- **Same stop:** When `start == destination`, the direct arc is empty and the answer is `0`.
- **Reversed indices:** Normalizing their order changes which arc is called direct but does not change either route length.
- **Zero-distance edges:** They contribute zero normally; multiple stops may therefore have a shortest travel distance of zero.
- **Equal arcs:** If both directions have the same length, that shared value is returned.
- **One-stop circle:** The only valid start and destination are both `0`, so the result is `0` regardless of the self-edge value.
