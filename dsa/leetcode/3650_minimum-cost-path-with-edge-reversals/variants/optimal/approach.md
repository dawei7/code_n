## General

**Why switch history does not enlarge the state.** Every traversal has positive cost. If a route revisits a node, removing the closed segment between two visits produces a strictly cheaper route and cannot create a new switch conflict. Hence an optimal route can be chosen simple: it visits every node at most once and therefore can use each node's switch at most once automatically.

**Encode both ways to traverse an edge.** An original edge `u -> v` of weight `w` provides an ordinary transformed arc `u -> v` costing `w`. When standing at `v`, the same original edge is incoming, so `v` may use its switch to traverse temporarily backward to `u` at cost `2 * w`; add transformed arc `v -> u` with that cost. Every valid simple route maps to a transformed route of equal cost, and a simple shortest path in the transformed graph maps back to valid switch operations.

All transformed costs are positive, so run Dijkstra from node 0. Return as soon as node `n - 1` is removed from the heap with its final distance. If the heap empties first, the destination is outside node 0's component even after reverse traversals.

## Complexity detail

Let $V=n$ and let $E$ be the number of original edges. The transformed adjacency list has $2E$ arcs. Binary-heap Dijkstra takes $O((V+E)\log V)$ time and stores $O(V+E)$ distances, heap entries, and arcs.

The benchmark sets size $N=V$, uses a chain with $E=N-1$, and writes its edges in reverse relaxation order. Tiers 16, 64, and 256 span 16x. Dijkstra takes $O(N\log N)$ time. Correct Bellman–Ford relaxation needs $N-1$ passes on that ordering and takes $O(N^2)$ time, so it must complete all tiers but fail scaling.

## Alternatives and edge cases

- **Bellman–Ford:** It handles the positive transformed graph correctly but costs $O(VE)$ and is unnecessary without negative edges.
- **Switch-mask shortest path:** Tracking a used-switch bit for every node is exponential and redundant because a positive-cost shortest path is simple.
- **No reversal needed:** Ordinary arcs retain their original costs, so Dijkstra naturally chooses a directed path when it is cheapest.
- **Several reversals:** A simple path may reverse edges at several different nodes; each uses a distinct switch and is valid.
- **Parallel edges:** Keep every arc because different weights or directions may change the optimum.
- **Disconnected underlying graph:** Reverse traversal cannot cross a missing undirected connection, so return `-1`.
