## General
**Use the target position as a dynamic-programming layer**

For each target index and possible ending city, store the smallest mismatch count of any valid walk ending there. At index zero, the cost for a city is zero if its name equals the first target name and one otherwise.

**Transition only across roads**

To end at `city` at target index `i`, the preceding route position must be one of that city's graph neighbors. Choose the neighbor with the least cost in the preceding layer, then add one exactly when `names[city] != targetPath[i]`. Record that chosen predecessor alongside the cost.

Every legal length-`i + 1` walk ending at `city` has one such neighboring predecessor, and the transition examines all of them. Replacing its prefix with the cheapest prefix ending at the same predecessor cannot affect the final road or mismatch at `city`. Induction over the layers therefore shows that every stored cost is optimal for its state.

**Backtrack an optimal route**

After the final layer, choose any city with minimum cost. Follow the recorded predecessors backward through all target positions and reverse the collected indices. Each predecessor link is a real road, so the reconstruction is a valid walk, and its final state has the globally smallest mismatch count. Ties may be resolved arbitrarily because the contract accepts any optimal route.

## Complexity detail
Building adjacency lists takes $O(n+e)$ space and $O(e)$ time. Across the $m$ target layers, scanning every city's neighbors visits $O(n+e)$ adjacency entries per layer, so the dynamic program takes $O(m(n+e))$ time. The predecessor table uses $O(mn)$ space, while the rolling cost arrays and graph use $O(n+e)$ additional space.

## Alternatives and edge cases
- **Enumerate every graph walk:** branching at each target position creates exponentially many routes even though many share the same ending-city state.
- **Dense predecessor scan:** testing every previous city for every current city takes $O(mn^2)$ time and discards the advantage of a sparse graph.
- **Shortest path on a layered graph:** explicitly create one vertex per target-position/city pair and run a shortest-path algorithm; this is equivalent but heavier than the direct acyclic-layer DP.
- A one-name target needs no road traversal and may start at any minimum-mismatch city.
- Repeated cities and immediate traversal back over the same road are allowed.
- City names and target names can repeat, creating multiple optimal routes.
- A locally matching city can lead to a worse suffix, so greedy name matching is insufficient.
- Every returned consecutive pair must be an authored road.
- The semantic judge must accept any legal route attaining the optimum, not only one reference reconstruction.
