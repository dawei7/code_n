## General

**Turn money into a monotone edge prefix**

If a repair threshold works, every larger threshold also works because it only adds usable edges.

The source sorts `edges` by repair cost. For prefix ending at index `idx`, `check(idx)` builds the graph using those first `idx+1` edges.

This prefix may stop inside a group of equal-weight edges and therefore need not correspond exactly to “repair every edge of that money.” That does not harm the returned threshold: the first feasible prefix has some weight `w`, and paying `w` repairs at least that prefix. No smaller distinct weight could be feasible, or an earlier prefix would already succeed.

Sorting also guarantees every prefix edge costs at most its last edge, so that last weight is a valid repair threshold for the whole prefix.

**Use BFS to enforce the edge-count limit**

All usable edges count as one route step regardless of repair cost. BFS therefore finds the minimum number of edges from node zero to every reachable node.

`q` contains the current distance layer and `nq` the next. `dist` is the number of edges used to reach nodes in `q`.

When target `n-1` is encountered, its BFS distance is minimal. The check returns whether that distance is at most `k`.

`vis` marks a node when first discovered. Revisiting it through a longer or equal route cannot improve the edge count.

At the start of a BFS layer, all nodes in `q` are exactly `dist` edges from the source. Their newly discovered neighbors form the next layer. Therefore a target encountered with distance above `k` cannot later receive a shorter path.

**Why continuing beyond `k` is harmless**

The exact source does not stop expansion once `dist>k`. It may explore unnecessary deeper layers, but BFS still cannot later find the target at a smaller distance. If it encounters the target too deep, it returns false.

An early depth cutoff would improve concrete work but not correctness or worst-case asymptotics.

**Binary-search the first feasible prefix**

With edges sorted, `check(idx)` is monotone: adding edges cannot destroy an existing short route.

The binary search keeps candidate interval `[l,r]`. If middle prefix works, the first feasible index is at or before `mid`, so `r=mid`. Otherwise it must be later, so `l=mid+1`.

When they meet, `l` is the only possible first feasible prefix index. A final `check(l)` distinguishes true feasibility from the case where even all edges fail.

If feasible, `edges[l][2]` is the minimum money threshold. Otherwise the method returns `-1`.

**Trace the one-edge constraint**

In the first example, low-cost edges 0–1 and 1–2 create a two-edge path but `k=1`, so their prefix check fails.

Adding direct edge 0–2 of cost 100 creates a one-edge path. Its prefix is the first feasible one, and binary search returns threshold 100.

**Why disconnected or too-long cases return `-1`**

The final check uses every sorted edge. If BFS still cannot reach the target within `k` edges, no money amount can help because there are no additional graph edges to repair.

This covers both physical disconnection and connection only through paths longer than the allowed edge count.

**Repair threshold is a bottleneck, not a path sum**

Paying `money` repairs every edge with cost at most that value simultaneously. Traversing several repaired edges does not add their repair costs. A route's required money is its maximum edge cost, while BFS separately controls its number of edges.

**Each check owns a fresh graph**

`check` rebuilds adjacency from exactly its candidate prefix. Edges from a previous larger check cannot leak into a smaller threshold. This repeated construction is included in the per-check linear cost.

## Complexity detail

Let $M$ be the edge count. Sorting costs $O(M\log M)$.

One check builds an adjacency list and runs BFS in $O(N+M)$ worst-case time and space. Binary search performs $O(\log M)$ checks plus one final check.

Total time is $O(M\log M+(N+M)\log M)=O((N+M)\log M)$. The adjacency list, visited array, and BFS layers use $O(N+M)$ space.

The source sorts `edges` in place, mutating their input order.

## Alternatives and edge cases

- **Try every distinct threshold:** Repeating BFS for all weights can cost $O(M(N+M))$.
- **Dijkstra by repair cost sum:** Money is a maximum edge threshold, not a sum along the path.
- **Ignore `k`:** Connectivity alone may use too many edges.
- **Use DFS:** It does not directly guarantee the fewest-edge route; BFS does.
- **Stop equal-weight prefix early:** Intermediate checks may omit peers, but the returned weight still repairs all peers and remains minimal.
- **Direct source-target edge:** It satisfies every `k>=1` when repaired.
- **Graph disconnected after all repairs:** Return `-1`.
- **Shortest route longer than `k`:** Return `-1` even if connected.
- **Duplicate repair costs:** Sorted occurrences remain separate, and returned threshold semantics stay correct.
- **Final feasibility check:** Required because binary search interval convergence alone does not prove any prefix works.
- **Input mutation:** Sorting changes the edge array order.
- **Threshold versus sum:** Money is a global cutoff, not accumulated path cost.
- **Fresh graph:** Every check isolates its own edge prefix.
- **BFS invariant:** First discovery gives minimum hop distance.
