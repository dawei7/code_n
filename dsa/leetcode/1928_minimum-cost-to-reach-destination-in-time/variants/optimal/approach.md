## General
**Keep time as part of the state**

A cheapest arrival at one city may have used too much time to finish, while a more expensive but faster arrival can remain useful. A single best cost per city therefore loses necessary information.

Define `cost[t][v]` as the minimum fee of a route that reaches city `v` in exactly `t` minutes. Initialize `cost[0][0]` with the source fee and every other state to infinity.

**Relax from earlier time layers**

Process elapsed times from one through `maxTime`. For every undirected road `(u, v, d)` with `d <= t`, a finite state at `cost[t - d][u]` can reach `v` by paying `passingFees[v]`; the reverse direction is symmetric.

All road times are positive, so every transition comes from a strictly earlier layer that is already final. Induction on `t` shows that each table entry is the cheapest exact-time route: the final edge of any such route supplies one considered predecessor, and every relaxation constructs a legal route with the recorded time and fee.

Take the minimum destination cost over every layer from zero through `maxTime`. If all are infinite, no route meets the budget.

## Complexity detail
There are `maxTime` layers and each scans all $E$ roads with constant work per direction, giving $O(\texttt{maxTime}\,E)$ time. The table stores $V$ costs for each layer, using $O(\texttt{maxTime}\,V)$ space.

## Alternatives and edge cases
- **Dijkstra by fee per city only:** Discarding a faster, costlier arrival can make the destination appear unreachable.
- **Dijkstra over `(city, time)`:** This is also correct, using a heap over the expanded state graph.
- **Enumerate all routes:** Cycles and branching make the number of walks exponential.
- **Exact budget:** Arrival at exactly `maxTime` is allowed.
- **Source and destination fees:** Both must be included once when visited.
- **Parallel roads:** Different travel times create distinct transitions and may change feasibility.
- **No feasible route:** Connectedness alone does not guarantee arrival within the time limit.
