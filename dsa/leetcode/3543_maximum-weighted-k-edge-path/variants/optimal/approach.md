## General

For a fixed number of used edges, the future only needs to know the current endpoint and which totals below `t` are reachable. Encode the reachable totals for endpoint `v` in an integer `states[v]`: bit $s$ is set exactly when some path ending at `v` uses the current number of edges and has weight $s$.

Before using any edge, a zero-edge path of weight zero may start at every node, so every state is initialized to bitset `1`. To add one edge `[source, target, weight]`, shift `states[source]` left by `weight`. Each old bit $s$ moves to $s + \texttt{weight}$, exactly representing extension through that edge. OR the shifted bits into the next-layer state for `target`. A mask containing only bits $0$ through $t-1$ discards totals at least `t`; positive weights mean a discarded total can never become valid later.

Build a fresh state array for each of the `k` rounds. This replacement is what enforces exactly one additional edge per round rather than allowing paths with fewer edges. By induction, after round $j$, the states contain precisely all valid weights of paths with exactly $j$ edges at each endpoint. After round `k`, the highest set bit across all endpoints is therefore the requested maximum. If every state is zero, its maximum has bit length zero and the returned value is `-1`.

## Complexity detail

Let $m$ be the number of edges. A language-neutral Boolean dynamic program processes $k$ layers, $m$ edges, and up to $t$ sums, taking $O(kmt)$ time. Rolling the current and next layers uses $O(nt)$ state space.

Python packs each node's Boolean sum row into one integer. Its shift, mask, and OR operate on $\lceil t / w \rceil$ machine words, where $w$ is the machine-word bit width, so the implemented work is $O(km\lceil t/w\rceil)$ word operations and the packed state occupies $O(n\lceil t/w\rceil)$ words. The manifest states the portable Boolean-DP bounds.

## Alternatives and edge cases

- **Explicit Boolean table:** Stores the same endpoint, edge-count, and sum states but loops over all $t$ totals for every edge instead of using packed bit operations.
- **Enumerate every path:** A DAG may still contain exponentially many paths, so DFS or breadth-first path expansion can time out even with only 300 edges.
- **Keep only the best sum per endpoint:** A larger partial sum may block a later extension at `t`, while a smaller sum can remain feasible; multiple sums must be retained.
- **Topological longest path:** Optimizing without the sum dimension cannot enforce the exclusive threshold, and optimizing without the layer dimension cannot enforce exactly `k` edges.
- **Zero edges:** A path may start at any node with total $0$, so `k = 0` returns `0` because $t \ge 1$.
- **Strict threshold:** Bit `t` is masked out; a total equal to `t` is invalid.
- **No sufficiently long path:** An empty state layer propagates as empty through all later rounds and yields `-1`.
- **Non-topological labels:** Transitions use the directed edge list and do not assume node numbers follow a topological order.
