## General

An ordinary shortest-path table indexed only by node is insufficient. Reaching the same node sooner with little power can prevent a later departure, while another arrival at that node may take longer but preserve enough power to finish. Treat `(node, remaining)` as the complete state instead.

Build the directed adjacency list and let `best_time[u][p]` be the least known arrival time at node `u` with exactly `p` power remaining. Initially only `(source, P)` has time zero. When Dijkstra removes `(u, p)` at its current best time, it may leave `u` only if `p >= cost[u]`. Every outgoing edge then reaches its endpoint with the common next power `p - cost[u]` and with the edge's positive travel time added.

These transitions reproduce every legal signal path: each departure checks and subtracts precisely the cost of the node being left, and each edge follows its recorded direction and time. Conversely, every generated transition is a legal departure, so every reachable state represents a legal path. All edge times are positive, allowing Dijkstra's extraction order to finalize the minimum time for each expanded state.

The destination is not one state but the family `(target, p)` for $0 \le p \le P$. Scan that row after Dijkstra finishes. Its smallest finite time is the globally minimum arrival time; among entries equal to that time, select the largest `p`. The unchanged initial state naturally gives `[0, P]` when `source == target`, and if every target entry is infinite the target is unreachable.

## Complexity detail

Let $n$ be the node count, $m = \lvert\texttt{edges}\rvert$, and $P = \texttt{power}$. There are at most $n(P+1) = O(nP)$ expanded states. Across all power levels, at most $O(mP)$ directed transitions are examined, and each successful relaxation performs a heap operation costing $O(\log(nP))$. The running time is therefore $O(P(n + m)\log(nP))$.

The distance table contains $O(nP)$ entries, the adjacency list uses $O(n + m)$ storage, and the heap can hold $O(nP)$ pending states. Because $P \ge 1$, the total auxiliary space is $O(nP + m)$.

## Alternatives and edge cases

- **One shortest time per node:** This discards distinct remaining-power states. A fastest arrival may be unable to pay the next departure cost even though a slower arrival can still reach the target.
- **Bellman-Ford over expanded states:** Repeated relaxation is correct, but it scans the state graph many times and can require quadratic work in the number of power levels instead of using positive edge times through Dijkstra.
- **Stop at the first target heap entry:** The first target extraction establishes the minimum time but does not automatically establish the greatest remaining power among every target state tied at that time.
- **Source equals target:** Return time zero and all initial power; no departure cost is paid.
- **Target departure cost:** The target's `cost` is irrelevant unless a path leaves the target and later returns. Simply arriving there consumes no power.
- **Exact remaining power:** A departure is permitted when `remaining == cost[u]`, producing a next state with zero power.
- **Cycles and self-loops:** Every traversal has positive time and every departure consumes positive power, so cycles cannot create infinitely many reachable states or improve a fixed expanded state.
- **Wide travel times:** A legal path may accumulate times beyond 32-bit range, so fixed-width implementations should store distances in 64-bit integers.
