## General

For a chosen threshold $T$, every edge receives one of two meanings:

- an edge with weight $w\le T$ is light and contributes zero heavy edges;
- an edge with weight $w>T$ is heavy and contributes one heavy edge.

The path requirement can therefore be restated as follows: under threshold $T$, what is the smallest possible sum of these zero-or-one edge costs from `source` to `target`, and is that sum at most `k`? This turns the inner decision problem into a shortest-path problem with only edge costs zero and one.

The complete optimization has two layers. A 0-1 breadth-first search answers whether one threshold is feasible, and binary search finds the smallest feasible threshold.

**The zero-threshold boundary**

If `source == target`, the empty path uses no edges and hence no heavy edges. Threshold zero is already sufficient, so the source returns `0` immediately.

Otherwise, the code builds an undirected adjacency list by placing each input edge in both endpoints' lists. It also collects candidate thresholds in a set initialized with `0`. Every edge weight is added and the set is sorted.

Including zero matters because all edge weights are positive. At $T=0$, every traversed edge is heavy. A path may still be valid when it contains at most $k$ edges. If the smallest valid threshold is below the minimum edge weight, zero is the minimum nonnegative integer threshold and must be available to the binary search.

**Why only zero and edge weights matter**

The light/heavy classification changes only when $T$ reaches an edge weight. Between two consecutive distinct weights, every edge has exactly the same classification, so feasibility cannot change. If some integer threshold between them works, the previous candidate produces the same classifications and also works. Therefore the minimum answer belongs to the sorted list consisting of zero and the distinct edge weights; searching every integer through $10^9$ would be unnecessary.

**Testing one candidate with 0-1 BFS**

Inside `is_possible(threshold)`, `heavy_edges[v]` means the smallest number of heavy edges found so far on a path from `source` to vertex `v`. Every value starts at `k + 1`, which acts as an unreachable sentinel for this decision problem, and the source receives distance zero.

For an adjacency edge, the expression `int(weight > threshold)` produces exactly its decision cost: zero for a light edge and one for a heavy edge. If the current vertex has count `heavy_edges[node]`, traversing this edge proposes

`next_count = heavy_edges[node] + cost`.

The proposal is ignored if it does not improve the neighbor's recorded count. It is also ignored if it exceeds `k`. That pruning is safe because every later edge adds either zero or one; once a partial path already uses more than `k` heavy edges, extending it can never make its count smaller.

When an improvement uses a light edge, the neighbor is placed at the front of the deque with `appendleft`. It can be explored without increasing the current heavy-edge layer. When an improvement uses a heavy edge, the neighbor is placed at the back with `append` because its count is one larger. This ordering is the specialized 0-1 BFS replacement for a priority queue. It processes lower heavy-edge counts before larger ones while taking advantage of the fact that no edge cost is anything other than zero or one.

Relaxation may discover the same vertex more than once, but only a strict improvement changes its stored count and enters it again. At completion, `heavy_edges[target] <= k` says exactly that at least one permitted path exists.

**Why feasibility is monotone**

Suppose a threshold $T$ is feasible. Raising the threshold can only change some edges from heavy to light; it can never change a light edge into a heavy one. The number of heavy edges on every fixed path therefore stays the same or decreases. In particular, the path that worked for $T$ still works for every larger threshold.

This one-way behavior gives a sorted false-then-true predicate over `candidates`. The source first tests the largest edge weight. At that threshold every graph edge is light, so any graph path uses zero heavy edges. If the target is still unreachable, the source and target lie in different connected components and no threshold can help; returning `-1` is correct.

If the largest candidate is feasible, ordinary lower-bound binary search is safe. For midpoint `mid`, a feasible result keeps the left half, including `mid`, because an earlier candidate might also work. An infeasible result discards `mid` and everything below it because monotonicity says none of those candidates can work. When `left == right`, that index is the first feasible candidate and hence the minimum threshold.

**A small way to read the two layers**

It helps to keep the questions separate. Binary search never tries to build the final path itself; it only asks yes-or-no questions. The 0-1 BFS never tries to minimize the threshold; it minimizes the number of heavy edges for one fixed threshold. Their guarantees compose: the inner search answers every predicate exactly, and the outer search selects the first true predicate.

## Complexity detail

Let $n$ be the number of vertices and $m$ the number of edges. Building the undirected adjacency list takes $O(n+m)$ space and $O(n+m)$ time, while collecting and sorting at most $m+1$ threshold candidates takes $O(m\log m)$ time.

For a fixed threshold, 0-1 BFS scans the graph using constant-time deque operations and constant-time relaxations. Its time is $O(n+m)$ and its distance array plus deque use $O(n)$ additional space beyond the graph.

Binary search invokes the feasibility check $O(\log(m+1))$ times. The total time is

$$
O\bigl(m\log m + (n+m)\log(m+1)\bigr),
$$

which is commonly written as $O((n+m)\log m)$ when $m$ is nonzero. This is consistent with the manifest's separated $O(n\log m+m\log m)$ form. The candidate list, graph, distance array, and deque together use $O(n+m)$ space.

The `source == target` return is a constant-time special case. If there are no edges and the endpoints differ, the candidate list contains only zero, the zero-threshold feasibility check fails, and the algorithm returns `-1` without creating any logarithm-related practical issue.

## Alternatives and edge cases

- **Dijkstra's algorithm for each threshold:** Assigning costs zero and one and using a heap is correct, but it adds a logarithmic heap factor to every feasibility test. 0-1 BFS exploits the two-valued costs and is the sharper inner algorithm.
- **Binary search every integer from zero to $10^9$:** This also uses monotonicity, but the classification changes only at actual edge weights. Compressing to distinct weights makes the search depend on $m$, not on the numeric weight range.
- **Sort paths by their largest edges:** The allowance of up to `k` heavy edges means the answer is not simply the minimum bottleneck edge. A path can intentionally tolerate several weights above the chosen threshold, so the heavy-edge count must be modeled explicitly.
- **Plain unweighted BFS:** Counting every edge equally minimizes the number of hops, not the number of weights greater than $T$. A longer path can contain fewer heavy edges and be the only feasible one.
- **Union-find alone:** At the largest threshold, union-find could test ordinary connectivity, but it cannot generally enforce “at most `k` heavy edges” for smaller thresholds because that is a path-cost condition rather than simple connectivity.
- **Source equals target:** The empty path satisfies the budget for threshold zero, independent of edges and of `k`.
- **Disconnected endpoints:** Even when every edge is light at the largest candidate, no path exists. The explicit largest-candidate test turns this into `-1` before binary search.
- **Budget `k = 0`:** Feasibility requires a path made entirely of edges whose weights are at most the threshold. The same 0-1 BFS handles this because all positive-cost relaxations are pruned.
- **Very large `k`:** Threshold zero may be enough if some source-target path has no more than `k` edges. Including zero allows the algorithm to return that minimum.
- **Parallel edges or repeated weights:** The adjacency list safely retains parallel edges. The candidate set removes duplicate weights because equal thresholds induce identical classifications.
- **A light-edge cycle:** Zero-cost cycles cannot cause endless processing because a vertex is enqueued only when its best heavy-edge count strictly improves.
