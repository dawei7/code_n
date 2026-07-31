## General

The graph node alone is not a complete shortest-path state. Reaching the same node after using different numbers of hops leaves different future options. Represent a state as `(node, used)`, where $0 \le \texttt{used} \le K$.

For every original edge from $u$ to $v$ with weight $w$, the layered graph has two possible transitions from `(u, used)`: pay $w$ and remain in the same layer, or, when `used < K`, pay zero and move to `(v, used + 1)`. The undirected edge supplies both directions. These transitions can be generated from the original adjacency list without materializing a separate layered graph.

Run Dijkstra from `(s, 0)`, storing a distance for every node and hop count. Paid relaxations add the edge weight; hopped relaxations preserve the current distance. All transition weights are nonnegative. Therefore, when any state whose node is `d` is removed from the heap with its current best distance, it is the cheapest destination state across every layer and can be returned immediately.

This state graph represents every permitted path exactly: the layer records how many traversals were made free, while ordinary transitions leave that count unchanged. Conversely, every layered path projects to an original graph path using no more than $K$ hops. Dijkstra thus returns precisely the minimum legal cost.

## Complexity detail

Let $E$ be the number of original edges and $K=k$. There are $n(K+1)$ states and $O(E(K+1))$ implicit directed transitions up to constant factors. Heap operations give $O(E(K+1)\log(n(K+1)))$ time. The adjacency list, distance table, and heap occupy $O((n+E)(K+1))$ space in the worst case. The benchmark fixes $K=1$ and uses `size` as $E$.

## Alternatives and edge cases

- **Layered Bellman-Ford:** Repeated relaxation is correct even with nonnegative weights, but it can require many complete passes and becomes polynomially slower.
- **Choose hops after ordinary Dijkstra:** Making edges free can change which route is optimal, so discounting a fixed ordinary shortest path is not valid.
- **One distance per node:** This loses how many hops remain and can discard a more useful state with a larger current cost.
- With $K=0$, the algorithm reduces to ordinary Dijkstra.
- A direct source-to-destination edge costs zero when at least one hop is available.
- The budget is at most $K$; reaching the destination never requires consuming unused hops through a detour.
- Several zero-cost layered transitions are safe because Dijkstra permits nonnegative edge weights.
- The source and destination may be any distinct node labels.

