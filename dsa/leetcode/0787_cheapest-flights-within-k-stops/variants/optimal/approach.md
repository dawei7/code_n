## General

**Convert the stop limit into an edge limit**

A route with zero intermediate stops is one direct flight, so it uses one edge. In general, a route with at most `k` stops uses at most `k + 1` flight edges.

The task is therefore to find the cheapest source-to-destination path using no more than `k + 1` edges. Ordinary single-distance shortest-path reasoning is not enough by itself because reaching a city cheaply with many edges may leave no edge budget, while a slightly more expensive arrival with fewer edges may still lead to the best legal destination route.

The solution uses the edge-bounded form of Bellman–Ford dynamic programming.

**Define what the distance array means after each round**

Before any relaxation round, `dist[src] = 0` and every other entry is a large sentinel `INF`. This represents cheapest costs using at most zero edges: only the source is reachable.

After one complete round, `dist[v]` should mean the cheapest cost from `src` to `v` using at most one edge. After two rounds it should mean at most two edges, and so on.

Running exactly `k + 1` rounds therefore produces the cheapest costs among all routes allowed by the stop constraint.

**Freeze the previous round with a snapshot**

At the beginning of each round, the method creates `backup = dist.copy()`. Every flight relaxation reads its starting-city cost from `backup`:

`dist[t] = min(dist[t], backup[f] + p)`.

This separation is essential. `backup[f]` represents a path using at most the previous round's edge count. Adding flight `f -> t` creates a candidate using at most one more edge.

The destination update is written to `dist`, but no later flight in the same round is allowed to use that fresh update because all reads still come from `backup`. Thus one round can add at most one flight edge, regardless of the order in which flights appear.

Without the copy, a chain of several flights could propagate through `dist` during one scan. That would silently exceed the intended edge budget and make results depend on input edge order.

**Carry forward routes that use fewer edges**

The algorithm does not reset `dist` to infinity in each round. It begins the round with the previous best values and takes a minimum against new one-edge extensions.

Consequently, after round `r`, `dist[v]` covers paths using at most `r` edges, not exactly `r` edges. A cheap direct route remains available in every later round even if no equally cheap route uses more edges.

This matches the problem's “at most `k` stops” wording.

**Understand the relaxation**

For flight `[f, t, p]`:

- `backup[f]` is the cheapest cost to reach departure city `f` within the previous edge allowance.
- Adding price `p` gives a legal candidate cost to reach `t` with one more edge.
- Taking the minimum preserves either the prior best route to `t` or this newly extended route, whichever is cheaper.

All prices are positive. `INF = 0x3F3F3F3F` is much larger than any legal answer under the constraints. If `f` is unreachable, `backup[f] + p` is larger than `INF`, so the minimum leaves `dist[t]` unchanged. The code therefore does not need a separate reachability branch.

**Trace a route whose extra stop saves money**

Suppose flights are `0 -> 1` for 100, `1 -> 2` for 100, and `0 -> 2` for 500.

Initially, only `dist[0] = 0`.

After the first round, the snapshot permits both direct outgoing flights from city zero. The costs become 100 to city one and 500 to city two. The fresh 100 at city one cannot yet feed the flight to city two in that same round.

After the second round, the new snapshot contains city one's cost 100. Relaxing `1 -> 2` produces 200, improving the prior 500. With one allowed stop, two edges are permitted, so 200 is the correct answer.

**The round invariant**

After `r` completed rounds, `dist[v]` equals the minimum price of every path from `src` to `v` containing at most `r` edges, or `INF` if no such path exists.

The invariant is true for `r = 0` by initialization.

Assume it holds before the next round. Any path with at most `r + 1` edges either already has at most `r` edges, in which case its best cost is retained in `dist`, or ends with some flight `f -> t` appended to a path of at most `r` edges. By the induction hypothesis, `backup[f]` holds the cheapest such prefix. Scanning every flight considers every possible final edge and takes the minimum. No candidate uses more than `r + 1` edges because reads come only from `backup`.

The invariant therefore holds after the round.

**Why the returned result is correct**

After `k + 1` rounds, the invariant covers exactly all routes with at most `k + 1` edges, equivalent to at most `k` intermediate stops.

If `dist[dst]` remains `INF`, no legal route reached the destination, so the method returns `-1`. Otherwise it returns the minimum price among every legal route.

Cycles require no special handling. Prices are positive, and the explicit edge limit already bounds all considered walks. The dynamic program evaluates them safely without assuming an unrestricted shortest path must be simple.

## Complexity detail

Let $V$ be the number of cities and $E$ the number of flights. There are `k + 1` rounds. Each round copies a $V$-entry distance array in $O(V)$ time and scans all $E$ flights in $O(E)$ time.

The exact implementation therefore takes

$$
O((k + 1)(V + E))
$$

time, plus the already included initialization. The manifest's $O((k + 1)E)$ expression describes the edge-relaxation work but omits the explicit Python list copy in every round. When $E$ dominates $V$, the expressions coincide asymptotically; for a sparse or empty flight set, the copy cost remains real.

`dist` and `backup` each store $V$ numbers. Rebinding `backup` each round releases the prior snapshot, so peak auxiliary space is $O(V)$.

## Alternatives and edge cases

- **Two-row dynamic programming:** Explicitly compute costs for each exact or bounded edge count. It expresses the same recurrence and also uses $O(V)$ rolling space.

- **State-expanded Dijkstra:** Treat `(city, edges_used)` as a state and use a heap. It can return early but requires more elaborate dominance handling.

- **Ordinary Dijkstra with one distance per city:** It can discard a more expensive but lower-edge state that is necessary under the stop constraint.

- **In-place relaxation without `backup`:** Incorrect because one round could chain multiple edges and violate the budget.

- **Zero allowed stops:** One round considers only direct flights.

- **No flights:** Every non-source city stays at `INF` and the destination returns `-1`.

- **Destination unreachable within the limit:** A route that exists only with extra edges is deliberately excluded.

- **Cheaper route with fewer than the maximum edges:** Previous values are retained, so “at most” is handled correctly.

- **Flight order:** Snapshot reads make the answer independent of how the flight list is arranged.
