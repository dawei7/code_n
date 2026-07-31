## Function Contract

`solve(n, edges, power, cost, source, target) -> list[int]`

Let $m = \lvert\texttt{edges}\rvert$ and $P = \texttt{power}$.

**Inputs**

- `n`: The number of graph nodes, labeled from `0` through `n - 1`.
- `edges`: Directed weighted edges. Each entry `[u, v, travel_time]` permits travel only from `u` to `v` and contributes `travel_time` seconds.
- `power`: The signal's initial power $P$.
- `cost`: A length-`n` array in which `cost[u]` is the power consumed whenever the signal leaves node `u` through any outgoing edge.
- `source`: The node at which the signal starts at time zero with all $P$ power units.
- `target`: The destination node.

**Output**

Return `[minimum_time, maximum_remaining_power]`. The first component is the least travel time over all legal paths from `source` to `target`; the second is the greatest remaining power among only the paths attaining that least time. If no legal path reaches `target`, return `[-1, -1]`.

A departure from `u` is legal exactly when the current power is at least `cost[u]`; that cost is subtracted once for the departure, independently of which outgoing edge is selected. Arrival does not consume power. In particular, when `source == target`, the result is `[0, power]` without paying any departure cost.
