## General

The path score is its weakest edge. The source binary-searches a proposed minimum edge cost `mid` and asks:

> Using only online nodes and edges with cost at least `mid`, is the cheapest path from node 0 to node `n-1` within budget `k`?

If yes, some valid path has score at least `mid`. If no, no path meeting that threshold can satisfy the budget.

**Filtering offline nodes**

The adjacency list includes edge `u -> v` only when both `online[u]` and `online[v]` are true.

Any path through an offline intermediate node must use one edge entering it or leaving it, so removing all incident edges makes such a path impossible. Nodes 0 and `n-1` are guaranteed online, so valid endpoints remain.

The graph stays directed: only `g[u]` receives `(v,w)`.

**Search bounds**

While constructing the filtered graph, `l` becomes the minimum retained edge cost and `r` the maximum. Any nonempty path score must equal or lie between edge costs in this interval.

The source searches every integer threshold between `l` and `r` rather than only distinct edge weights. Feasibility changes only at actual weights, so searching distinct sorted weights could reduce the logarithmic range, but numeric binary search is still correct.

If no online-to-online edge exists, `l` remains infinity and `r=0`. The loop is skipped and the final feasibility check returns false unless the destination were the start (which cannot happen because `n>=2`), so the method returns `-1`.

**Monotonic feasibility**

If threshold `x` is feasible, the same path is feasible for every `y <= x` because lowering the threshold only allows more edges and does not change the path's total cost.

If `x` is infeasible, raising the threshold removes even more edges and cannot create a budget-feasible path. Therefore, feasible thresholds form a lower prefix, enabling upper-bound binary search.

**Why `check(mid)` computes a shortest path**

Among paths whose every edge costs at least `mid`, only total cost determines whether the budget is met. Edge costs are nonnegative, so Dijkstra's algorithm finds the minimum total cost.

`dist[u]` stores the best discovered cost from node 0 to `u`. The heap begins with `(0,0)`. For an outgoing edge `(v,w)`:

- if `w < mid`, it would lower the path score below the threshold and is ignored;
- otherwise, `dist[u]+w` is a candidate distance to `v`.

A strictly smaller candidate replaces `dist[v]` and is pushed into the heap.

**Stale heap entries**

Python's heap has no decrease-key operation. When a shorter route to a node is found, the older tuple remains. The condition:

`if dist[u] < d: continue`

discards an entry whose distance is no longer current. Only a best-known tuple relaxes outgoing edges.

**Budget early termination**

The heap pops distances in nondecreasing order. If the smallest popped `d` is already greater than `k`, every remaining entry is at least that large. Since all edges have nonnegative cost, no later route can reach the destination within budget. Returning false is safe.

If the destination is popped after passing the budget guard, its distance is the shortest allowed-path cost and is at most `k`, so `check` returns true immediately.

**Binary-search mechanics**

The midpoint is upper-biased:

`mid = (l+r+1) >> 1`.

When feasible, `l=mid` keeps that score and searches higher. When infeasible, `r=mid-1` removes it and every larger threshold. Upper bias prevents an infinite loop when two integers remain.

After the bounds meet, the source runs `check(l)` once more. If feasible, `l` is the greatest feasible score; otherwise, no valid path exists and the answer is `-1`.

This final check is necessary because the initial lower bound is only the minimum edge weight, not proof that any source-to-destination path satisfies the budget.

**Following the second example**

Edges incident to offline node 3 are excluded. At threshold 6, path `0 -> 2 -> 4` remains because both edges cost 6. Its total is 12, within `k=12`, so 6 is feasible.

Any threshold above 6 removes that path. The alternative `0 -> 1 -> 4` contains a weight-5 edge and cannot support a higher score. The maximum feasible threshold is 6.

**Why Dijkstra is valid even though the graph is a DAG**

The DAG property permits a linear topological shortest-path pass, but Dijkstra is also correct because weights are nonnegative. The exact source chooses the heap approach and does not compute a topological order.

**Differences from the manifest**

The manifest describes binary-searching distinct bottleneck thresholds and testing them with topological-order DP, for `O((n+m)\log m)` time. The exact source:

- searches the numeric weight interval;
- runs Dijkstra for every threshold;
- may retain stale heap entries.

Its faithful complexity therefore contains both a heap logarithm and a numeric-range logarithm.

**Exact-source missing names**

The shown file uses `List`, `inf`, `heappop`, and `heappush` without imports or definitions. In an ordinary standalone module, these cause `NameError`. It needs suitable imports from `typing`, `math`, and `heapq`, or a harness that injects them.

The algorithmic explanation describes the behavior once those dependencies are available; it does not claim the file is standalone-executable as written.

## Complexity detail

Let `m` be the number of retained online-to-online edges, `n` the node count, and `U = r-l+1` the searched numeric range.

One Dijkstra check examines at most all retained edges and can push `O(m)` heap entries. With stale entries, the heap can be edge-sized, giving `O((n+m)\log m)` time and `O(n+m)` temporary space.

Numeric binary search performs `O(\log U)` checks, plus the final check. Total time is:

$$
O((n+m)\log m\log U).
$$

Graph construction costs `O(n+m)` and is dominated. Because edge costs are at most `10^9`, `\log U` is at most about 30.

The adjacency list uses `O(n+m)` space. Each check allocates `O(n)` distances and up to `O(m)` heap tuples, so total auxiliary space remains `O(n+m)`.

## Alternatives and edge cases

- **Topological DP per threshold:** Exploit the DAG to test a threshold in `O(n+m)` time, matching the manifest's intended structure.
- **Search distinct edge costs:** Sort unique weights and binary-search their indices, using `O(\log m)` feasibility checks instead of numeric `\log U`.
- **Memoized DFS:** A DAG recursion can compute threshold-restricted shortest costs, but depth up to `n` risks Python recursion limits.
- **Dijkstra without threshold search:** A single scalar distance cannot simultaneously optimize maximum bottleneck and constrained total cost; the decision transformation separates the objectives.
- **No valid path:** The final `check(l)` fails and the method returns `-1`.
- **No retained edges:** `l` remains infinity; the exact control flow still ends at `-1` for `n>=2`.
- **Zero-cost edges:** They are legal. Threshold zero may be feasible, and Dijkstra handles nonnegative zero weights.
- **Budget zero:** Only a total-cost-zero path can qualify.
- **Offline intermediate node:** All incident edges are removed during graph construction.
- **Offline endpoints:** The contract guarantees source and destination online.
- **Edge exactly at threshold:** It is allowed because only `w < mid` is skipped.
- **Path total exactly `k`:** It qualifies; the destination is returned after the `d > k` check.
- **Stale destination tuple:** A stale tuple could only have larger distance; Dijkstra's min ordering pops the current shortest destination first, and stale-node filtering protects ordinary nodes.
- **Large unused weight gaps:** Numeric binary search still spends iterations on them; distinct-weight search avoids this.
- **Missing imports:** Standalone use must define `inf` and import heap operations and `List`.
- **Input preservation:** The source constructs a filtered graph without modifying `edges` or `online`.
