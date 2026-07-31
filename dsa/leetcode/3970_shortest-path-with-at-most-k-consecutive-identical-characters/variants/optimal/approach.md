## General

A node number alone does not contain enough information to decide whether the next edge is legal. Two routes can reach the same node with different lengths for the trailing run of that node's label. If the next node has the same label, one arrival may still extend the run while the other may already be at the limit.

Represent each search state as `(node, run_length)`, where `run_length` is the number of equal labels at the end of the route so far. The initial state is `(0, 1)`. For a directed edge from `node` to `neighbor`, the new run length is `run_length + 1` when their labels match and `1` otherwise. Discard the transition if that value exceeds `k`.

These states form an expanded directed graph with the original positive edge weights. Run Dijkstra's algorithm from `(0, 1)`, storing a separate best cost for every node and legal run length. A heap entry whose cost no longer equals the stored distance is stale and can be skipped. Because all weights are positive, the first state removed from the heap at node `n - 1` has the minimum cost among every destination state and can be returned immediately.

Every accepted transition appends exactly one graph edge and computes exactly the resulting trailing run, so each path explored in the expanded graph corresponds to a valid route in the original graph. Conversely, every valid route has a legal run length after each node and therefore traces the same sequence of expanded states. Dijkstra minimizes cost over all such state paths, which proves that the returned destination cost is the required minimum. If no destination state is reached, no valid route exists.

## Complexity detail

Let $m = \lvert\texttt{edges}\rvert$. There are at most $nk$ expanded states and at most $mk$ legal state transitions. Binary-heap Dijkstra therefore takes $O(k(n+m)\log(nk))$ time. The adjacency list, distance table, and heap together use $O(k(n+m))$ space.

## Alternatives and edge cases

- **Dijkstra by node only:** Keeping one distance per node loses the trailing run length. A cheaper arrival that has exhausted the run limit can incorrectly suppress a costlier arrival from which a same-label edge remains legal.
- **Bellman-Ford on expanded states:** Repeated relaxation is correct and can use the same state definition, but its worst-case time is far larger than necessary for positive edge weights.
- **Explicitly materialized state graph:** Prebuilding every `(node, run_length)` transition makes the reduction visible but can consume $O(mk)$ additional storage; generating transitions from the original adjacency list is simpler.
- **Single node:** When `n = 1`, the initial state is already the destination and its cost is zero.
- **`k = 1`:** Every traversed edge must change the current label; an edge joining equal labels is immediately unusable.
- **Label changes:** Moving to a different label resets the run to one rather than zero because the destination node starts the new run.
- **Directed and parallel edges:** Only the recorded direction may be followed, and multiple edges between the same ordered pair remain distinct weighted choices.
- **Unreachable destination:** An empty heap without a destination state means every possible directed route is absent or violates the label rule, so the answer is `-1`.
- **Large path costs:** A legal route through expanded states can cost more than a 32-bit integer; fixed-width implementations should store distances in a 64-bit type.
