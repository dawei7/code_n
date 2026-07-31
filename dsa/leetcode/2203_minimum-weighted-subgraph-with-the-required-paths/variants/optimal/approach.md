## General

**Reduce a shared subgraph to a meeting node**

Because all edge weights are positive, an optimal qualifying subgraph needs no directed cycle or redundant branch. Its two source routes can be viewed as separate prefixes that meet at some node $v$, followed by one shared suffix from $v$ to `dest`. For a fixed meeting node, the least possible total is

$$
d_1(v)+d_2(v)+d_D(v),
$$

where $d_1(v)$ and $d_2(v)$ are shortest-path distances from the two sources and $d_D(v)$ is the shortest distance from $v$ to the destination.

Any optimal subgraph has such a meeting point and cannot cost less than these three shortest distances. Conversely, combining shortest paths for the three terms creates a valid pair of routes; if those paths overlap even more, their union only removes duplicate edge cost. Taking the minimum over all $v$ therefore yields the optimum.

**Compute every required distance with three searches**

Run Dijkstra on the original adjacency list from `src1` and from `src2`. To obtain every distance *to* `dest` in one more run, reverse every edge and run Dijkstra from `dest`; a reversed route from `dest` to $v$ has the same weight as the original route from $v$ to `dest`.

For each node, add the three distances. Nodes unreachable in any one search contribute infinity and cannot be meeting points. If every sum is infinite, return `-1`.

## Complexity detail

Each binary-heap Dijkstra run costs $O((n+m)\log n)$ with adjacency lists. Three runs and one linear meeting-node scan preserve the bound $O((n+m)\log n)$.

The forward and reverse adjacency lists, three distance arrays, and priority queue use $O(n+m)$ space.

## Alternatives and edge cases

- **Bellman-Ford from all three endpoints:** It handles negative weights, but weights here are positive and its $O(nm)$ time is unnecessary.
- **All-pairs shortest paths:** Floyd-Warshall makes meeting-node evaluation easy but requires $O(n^3)$ time and $O(n^2)$ space.
- **Meet at the destination:** Choosing `dest` is valid and represents two routes with no earlier shared suffix.
- **Meet at a source:** One source may reach the other, after which both can share the remaining route.
- **Parallel edges:** Dijkstra naturally relaxes each edge and keeps the cheaper resulting distance.
- **Unreachable nodes:** A finite path from only one source is insufficient; all three distance terms must be finite.
