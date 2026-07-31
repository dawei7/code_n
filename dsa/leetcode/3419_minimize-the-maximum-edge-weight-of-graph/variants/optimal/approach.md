## General

Reverse every edge. A path from some node `u` to node `0` in the original graph then becomes a path from `0` to `u`. For each node, seek a reversed path whose cost is the largest edge on that path, minimized over all possible paths. The answer is the largest of these per-node minimax costs; if any node remains unreachable, no edge removal can repair the graph.

Use Dijkstra's algorithm with a bottleneck cost instead of an additive distance. Set node `0` to cost zero. When a settled node with cost `cost` traverses an edge of weight `weight`, the candidate for its neighbor is `max(cost, weight)`. A min-heap always selects the smallest outstanding bottleneck. If a supposedly better route to a settled node existed, every prefix of that route would have no larger bottleneck and would have been processed first, so the usual Dijkstra ordering proves the settled value minimal.

The outgoing-degree restriction does not require a separate state. Because `threshold` is at least one, choose for every nonzero node the original edge corresponding to the predecessor that established its minimax route. Those chosen edges lead through discovered predecessors to node `0`, and each nonzero node contributes only one outgoing edge. Thus every feasible reachability solution can be reduced to one that satisfies even `threshold = 1`, without increasing its maximum weight.

## Complexity detail

Let $n$ be the number of nodes and $m$ the number of edges. Building the reversed adjacency lists takes $O(n+m)$ time and space. Each successful relaxation adds one heap entry, and heap operations cost $O(\log n)$, giving $O((n+m)\log n)$ time. The adjacency lists, bottleneck array, and heap use $O(n+m)$ space.

The benchmark defines `size` as $n$ and uses sparse graphs with $m=2(n-1)$, so $n+m=\Theta(n)$. A correct repeated-relaxation method may need $\Theta(n)$ full edge scans on the adversarial chain, yielding $\Theta(nm)$ time; the accepted heap-based minimax traversal must scale near linearly apart from its logarithmic factor.

## Alternatives and edge cases

- **Binary search plus reverse reachability:** Testing whether all nodes are reachable under a weight cap is correct and runs in $O((n+m)\log W)$ time, where $W$ is the weight range, but minimax Dijkstra computes all critical caps in one traversal.
- **Repeated full-edge relaxation:** Bellman-Ford-style bottleneck relaxation is correct but can require $n-1$ passes and therefore $O(nm)$ time.
- **Use ordinary additive shortest paths:** Summing weights optimizes a different objective; only the largest edge on each path matters here.
- **Treat `threshold` as a flow capacity:** Since it is always positive and one selected outgoing edge per nonzero node suffices, this introduces unnecessary machinery.
- **Edges directed away from node `0`:** Such edges become incoming to `0` only after reversal when they truly represent an original path toward `0`; preserving the direction reversal is essential.
- **Parallel edges:** Distinct parallel weights are handled independently, and relaxation naturally keeps the better bottleneck.
- **Disconnected component or closed cycle:** If it has no directed route to node `0`, its nodes remain at infinite cost and the answer is `-1`.
- **Heavier direct edge versus lighter detour:** The minimax relaxation correctly prefers a longer route when its largest edge is smaller.
