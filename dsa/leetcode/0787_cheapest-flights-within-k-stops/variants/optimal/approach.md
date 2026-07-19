## General
**Define cost by the number of flights allowed**

Let `costs[city]` be the cheapest price using at most the number of flights processed so far. Initially only `src` costs zero. Perform $k + 1$ rounds because a route with `k` intermediate stops contains at most $k + 1$ flight edges.

**Relax every flight from the previous round**

At the start of a round, copy `costs` into `next_costs`. For each flight `u -> v`, use only `costs[u]` from the previous round to improve `next_costs[v]`. The copy retains routes that use fewer edges, while separating the arrays prevents two flights from chaining inside one round and silently exceeding the edge budget.

After round `r`, induction shows that each entry is the minimum cost among routes using at most `r` flights: retained entries cover shorter routes, and every route using exactly `r` flights is a valid previous-round route followed by one relaxed edge. Thus after $k + 1$ rounds, the destination entry considers exactly all permitted routes. An infinite entry means none exists.

## Complexity detail
Each of the $k + 1$ rounds scans all `E` flights, taking $O((k + 1) \cdot E)$ time. The current and next cost arrays each contain `V` entries, for $O(V)$ auxiliary space.

## Alternatives and edge cases
- **Heap over city and flights used:** Dijkstra-style states `(price, city, edges)` can stop at the first valid destination pop, but the edge count must remain part of the state.
- **Two-dimensional dynamic programming:** Store the best price for every city and exact edge count; this uses $O(kV)$ space instead of rolling arrays.
- **Depth-first route enumeration:** Exploring every route up to the stop limit is correct but can grow exponentially in dense graphs.
- **Unrestricted shortest path:** Keeping only one best cost per city without an edge dimension can discard a more expensive prefix that leaves enough stops for the optimal valid route.
- **No stops:** Only direct flights may be used.
- **Unreachable destination:** Return `-1`, not infinity.
- **Cycles:** Positive prices and the explicit edge budget keep the dynamic program finite.
- **Round isolation:** Relaxations must read the old array and write the copy to enforce one additional flight per round.
