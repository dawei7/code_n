## General

**Turn the score into a threshold.** For a candidate score $x$, permit only edges whose cost is at least $x$ and only online nodes. A valid path with score at least $x$ exists exactly when the minimum total cost from node 0 to node $n-1$ in this restricted graph is at most `k`. If threshold $x$ is feasible, every smaller threshold is also feasible; increasing it can only remove edges.

**Test one threshold in topological order.** Compute a topological ordering of the original DAG once. For each threshold, initialize the source distance to zero and all others beyond the budget. Scan nodes in topological order and relax permitted outgoing edges from reachable online nodes, discarding updates above `k`. When a node is processed, every path into it has already been considered, so its stored value is the minimum restricted-path cost. The threshold is feasible exactly when the destination distance is within budget.

**Search only meaningful scores.** A nonempty path's minimum edge cost must equal one of the graph's edge costs. Sort the distinct costs and binary-search the greatest feasible value. The monotonic feasibility predicate ensures that all values at or below a successful midpoint remain candidates, while a failed midpoint and every larger value can be discarded. If no distinct cost is feasible, return `-1`.

## Complexity detail

Let $n$ be the node count and $m$ the edge count. Building adjacency and the topological order costs $O(n+m)$. Sorting distinct edge costs costs $O(m\log m)`. Binary search performs $O(\log m)$ feasibility checks, each costing $O(n+m)$ time. The total is $O((n+m)\log m)$ time and $O(n+m)$ space for adjacency, ordering, indegrees, and distances.

The benchmark uses a chain of $m$ distinct-cost edges and enough budget for the entire path. Its score is the smallest edge cost, so a calibrated correct alternative that checks thresholds from largest to smallest rebuilds shortest-path state for every distinct cost, taking $O(m(n+m))$ time.

## Alternatives and edge cases

- **Enumerate all source-to-destination paths:** A DAG can contain exponentially many paths, so direct enumeration is infeasible.
- **Check every distinct score:** It is correct but adds a linear factor in the number of edge costs instead of binary search.
- **Dijkstra for each threshold:** Nonnegative costs make it valid, but a DAG topological pass is linear and avoids a heap.
- **Ignore total recovery cost:** Maximizing only the bottleneck can select a route whose sum exceeds `k`.
- **Offline endpoint of an edge:** That edge cannot participate because every path node must be online; source and destination are guaranteed online.
- **Zero-cost edges:** They can produce a valid score of `0`, distinct from the `-1` no-path result.
- **Budget equality:** A path whose total is exactly `k` is valid.
- **No edges or unreachable destination:** No threshold is feasible, so return `-1`.
- **Node numbers:** Numeric order need not be topological; compute an ordering from the edges.
