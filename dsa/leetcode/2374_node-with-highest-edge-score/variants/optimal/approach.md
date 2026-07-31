## General

Each array position `source` describes one edge to `edges[source]`. Its contribution to the target's edge score is the source label itself, so all scores can be accumulated independently in an array indexed by target node.

**Aggregate every edge once.** Initialize all scores to zero. For every `(source, target)` pair from `enumerate(edges)`, add `source` to `scores[target]`. This accounts for every directed edge exactly once, including the zero contribution from source node `0`.

**Make the tie rule part of the scan.** Start with node `0` as the answer and inspect candidate nodes in ascending order. Replace the answer only when a candidate's score is strictly greater. Equal scores never replace an earlier index, so the final node is automatically the smallest index attaining the maximum.

The accumulation gives each node exactly the sum in the definition. The second pass compares all completed scores and preserves the earliest maximum, proving both the primary and tie-breaking requirements.

## Complexity detail

Let $n = \lvert\texttt{edges}\rvert$. Accumulating the $n$ edges and scanning the $n$ scores take $O(n)$ time. The score array uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Hash map of target scores:** A dictionary can store only nodes with incoming contributions, but all target labels already lie in the dense range from `0` through `n - 1`, so an array is simpler.
- **Rescan sources per target:** Computing each target's score by inspecting every edge is correct but requires $O(n^2)$ time.
- **Indegree counting:** Counting incoming edges is insufficient because a high-labeled source contributes more than a low-labeled source.
- **Score ties:** Comparison must retain the smallest target index.
- **Source zero:** Its edge contributes `0`, though the target still has an incoming edge.
- **No incoming edges:** Such a node has score zero and still participates in tie comparisons.
