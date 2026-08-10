## General

**Convert “everyone reaches node 0” into a search outward from node 0.** Original edges point from a node toward the nodes it can reach. To determine, in one search, how every node can eventually reach node $0$, the source reverses each edge:

`source -> destination` with weight `weight`

becomes an adjacency entry `(source, weight)` in `reverse_graph[destination]`.

Now a path from node $0$ to node $v$ in the reversed graph corresponds exactly to a path from $v$ to node $0$ in the original graph, using the same edge weights.

**The path cost is its largest edge, not its sum.** For each node $v$, `best[v]` stores the smallest possible maximum edge weight among all original paths from $v$ to $0$. This is often called a minimax or bottleneck path value.

The source initializes `best[0] = 0` because node $0$ reaches itself without an edge. Other nodes begin at infinity. A min-heap contains `(cost, node)` pairs, starting with `(0, 0)`.

Suppose the heap finalizes a reversed path to `node` whose bottleneck is `cost`. Extending that path through a reversed edge of weight `weight` to `predecessor` corresponds to prepending the original edge `predecessor -> node`. The extended path's largest edge is

`candidate = max(cost, weight)`.

If this candidate is smaller than `best[predecessor]`, it improves the predecessor's best-known route to node $0$, so the source updates the array and pushes the new heap entry.

**Why Dijkstra's greedy order still works.** Ordinary Dijkstra uses addition because path sums never decrease when an edge is appended. The bottleneck operation `max` has the same monotonic property: extending a path cannot make its maximum edge smaller. Therefore, the smallest heap cost can be finalized with the standard argument. Any alternative path reaching that node through an unprocessed state already has a bottleneck at least as large as that state's heap key. The stale-entry check `cost != best[node]` ignores older heap records after a better route has been pushed.

After the search, every finite `best[v]` is the minimum bottleneck needed for that node to reach $0$. One global edge-weight limit must work for every node, so the smallest possible limit is

$$
\max_v\texttt{best}[v].
$$

If any value remains infinite, that node has no path to $0$ even when all edges are allowed. The task is impossible and the source returns `-1`.

**Why the outgoing-edge threshold does not appear in the code.** The source accepts `threshold` but never reads it. This is correct under the guaranteed constraint `threshold >= 1`.

Once every node has some path to $0$ using edges no heavier than a limit $W$, those paths contain a directed structure from which one outgoing edge per nonzero node can be retained. For example, use the predecessor choices made by the reversed search, or choose for each reachable node an edge that moves it one step closer to $0$ in a rooted reachability tree. Removing all other edges leaves every node able to reach $0$ and gives each node at most one outgoing edge. Since one is no greater than any allowed `threshold`, the cap creates no additional restriction.

Conversely, any valid remaining graph gives each node a path to $0$, and every edge on those paths is at most its maximum retained weight. Thus that maximum must be at least every node's minimum bottleneck, and hence at least `max(best)`. The search's chosen paths demonstrate that `max(best)` is achievable. This proves optimality and explains the otherwise surprising unused parameter.

For the third example, reversed exploration from $0$ first reaches node $4$ with bottleneck $1$, then node $3$ through weight $2$ with bottleneck $2$, node $2$ with bottleneck $2$, and node $1$ with bottleneck $2$. The maximum per-node requirement is $2$.

Parallel original edges are harmless. Each reversed adjacency entry is relaxed independently, and only the path yielding the smallest bottleneck survives in `best`.

## Complexity detail

Let $m=\lvert\texttt{edges}\rvert$. Building the reversed adjacency list costs $O(n+m)$ time and space. Each successful relaxation pushes one heap entry; with a binary heap, the standard bound is $O((n+m)\log n)$ time, or equivalently $O(m\log n)$ when the graph is connected enough for all vertices to matter. Stale entries may be popped but are charged to prior pushes.

The reversed graph stores $m$ edge pairs, `best` stores $n$ values, and the heap can hold $O(m)$ pending entries in the usual bound. Total auxiliary space is $O(n+m)$, matching the manifest.

## Alternatives and edge cases

- **Binary search a weight limit:** For each candidate $W$, keep edges of weight at most $W$ and test reverse reachability from zero. This works in $O((n+m)\log W)$ but repeats graph scans; minimax Dijkstra finds all thresholds at once.
- **Ordinary shortest-path sums:** Adding edge weights solves a different objective. A path with a large total but small maximum edge can be preferable here.
- **Search the original graph from zero:** That tests whether zero can reach other nodes, the reverse of the required direction. Reversing edges is essential.
- **Threshold equal to one:** A rooted choice of one outgoing edge per nonzero node is enough, so the minimum allowed threshold does not change the answer.
- **Hypothetical threshold zero:** Then no nonzero node could have an outgoing path. The source relies on the statement's guarantee that threshold is at least one.
- **Disconnected node:** Its `best` remains infinity, making `max(best)` infinite and causing the required `-1` result.
- **Node zero:** Its bottleneck is zero because it already reaches itself; no self-loop is required.
- **Multiple equal-cost routes:** Any may define the retained reachability tree. Only the minimum bottleneck value affects the answer.
- **Cycles:** The heap algorithm handles cycles through improvement checks. The final retained edges can be chosen acyclically toward zero even if the input contains cycles.
- **Multiple edges between nodes:** Unique weights are not needed by the algorithm; each edge competes through the same `max` relaxation.
