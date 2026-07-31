## General

Fix a candidate threshold $T$ and assign every edge a traversal cost: $0$ when its weight is at most $T$, and $1$ when its weight is greater than $T$. The total cost of a path is then exactly its number of heavy edges. A 0-1 BFS from `source` computes the minimum such count to every node, so $T$ is feasible precisely when the value at `target` is at most `k`.

The feasibility predicate is monotone. Raising $T$ can only turn heavy edges into light ones; it can never increase the minimum number of heavy edges on a path. This permits binary search for the first feasible threshold.

Only the value $0$ and weights that occur in `edges` need to be searched. Between two consecutive edge weights, every edge keeps the same light-or-heavy classification, so feasibility cannot change. The explicit $0$ candidate is essential because all edge weights are positive: a path using at most `k` edges can be valid even when every one of those edges is heavy. If `source == target`, the empty path immediately gives the same answer.

Build and sort those candidates. First test the largest one; at that threshold every edge is light, so failure proves that `source` and `target` lie in different connected components and the answer is `-1`. Otherwise, binary-search the candidates and run 0-1 BFS for each midpoint. Every rejected candidate is below the answer by monotonicity, while every accepted candidate remains a valid upper bound. When the search converges, it is therefore the smallest feasible integer threshold.

## Complexity detail

Let $n$ be the number of nodes and $m$ the number of edges. Building the adjacency list takes $O(n+m)$ time, and sorting at most $m+1$ candidates takes $O(m \log m)$ time. Each of the $O(\log m)$ feasibility checks costs $O(n+m)$ with 0-1 BFS, giving $O(n\log m + m\log m)$ total time. The adjacency list, candidate list, distance array, and deque use $O(n+m)$ space. When $m=0$, the direct checks take constant time beyond the $n$-node adjacency list.

## Alternatives and edge cases

- **Linear threshold scan:** Testing candidate weights in increasing order with the same 0-1 BFS is correct, but it can take $O(m(n+m))$ time instead of exploiting monotonicity.
- **Dijkstra with a heap:** The heavy-edge costs are only zero or one, so ordinary Dijkstra is correct but adds an unnecessary logarithmic factor to each feasibility check.
- **Depth-first enumeration of paths:** Enumerating simple paths can establish feasibility on tiny graphs, but the number of paths may be exponential.
- **Threshold zero:** Positive edge weights do not imply a positive answer; when `k` covers every edge on some path, all of those edges may remain heavy and the answer is `0`.
- **Identical endpoints:** The empty path uses zero heavy edges, so `source == target` returns `0` even with no edges and `k = 0`.
- **Disconnected endpoints:** Even an arbitrarily large threshold cannot create a missing connection; testing the largest candidate distinguishes this case and returns `-1`.
- **Cycles, parallel edges, and self-loops:** Relaxing only a strictly better heavy-edge count makes 0-1 BFS terminate and naturally ignores transitions that cannot improve a node.
