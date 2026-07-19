## General
**Compute the ordering key from the destination**

The restriction compares every visited node's shortest distance to node `n`, so run Dijkstra's algorithm from `n`. Positive edge weights guarantee that the min-heap finalizes correct distances. Store the undirected graph as adjacency lists.

Running from the destination computes all required values in one shortest-path pass. Running separately from each node would repeat work and is unnecessary.

**Orient the graph by strictly decreasing distance**

Once distances are known, conceptually direct every edge from its larger-distance endpoint toward its smaller-distance endpoint. Ignore edges whose endpoint distances are equal. Along every directed edge the distance strictly decreases, so a directed cycle is impossible.

This turns the restricted-path relation into a directed acyclic graph, even though the original graph is undirected and may contain cycles.

**Count paths in distance order**

Set the number of ways at node `n` to one. Process nodes from smallest to largest distance. When processing `node`, its count already represents every restricted suffix from that node to `n`. For each neighbor with a larger distance, add `ways[node]` to that neighbor because taking the edge from the neighbor to `node` is a valid first descending step.

Apply the modulus after every addition. By increasing-distance order, all smaller-distance successors of a node have been completed before that node receives its final count.

Dijkstra supplies the exact values used by the definition. The orientation retains exactly those edge traversals that satisfy the strict inequality, and the dynamic program counts every directed path to `n` once by its first edge. Therefore `ways[1]` is precisely the number of restricted paths.

## Complexity detail
Building adjacency lists takes $O(n+E)$ space and $O(E)$ time. Dijkstra with a binary heap takes $O((n+E)\log n)$ time. Sorting the nodes by distance costs $O(n\log n)$, and the dynamic program inspects both directions of every edge in $O(n+E)$ time. The total remains $O((n+E)\log n)$.

The graph, distance array, heap, ordering, and path counts use $O(n+E)$ space.

## Alternatives and edge cases
- **Memoized depth-first search after Dijkstra:** Recursing only to smaller-distance neighbors computes the same DAG recurrence in $O(n+E)$ after distances are known, but a long restricted chain can exceed a language's recursion limit.
- **Integrate counting with Dijkstra finalization:** Counts can be propagated in finalized-distance order, but separating shortest paths from the DAG recurrence makes stale heap entries and equal-distance edges easier to handle correctly.
- **Bellman–Ford distances:** Positive weights do not require repeated relaxation; this increases shortest-path work to $O(nE)$.
- **Path enumeration:** Explicitly constructing every restricted path can be exponential even though the dynamic program has only one state per node.
- **Restricted is not shortest:** A traversed edge may be heavier than an alternative route; only the endpoint distance values must strictly decrease.
- **Equal distances:** An edge between equal-distance nodes cannot be used in either direction because the comparison is strict.
- **Single node:** When `n = 1`, the empty path from node `1` to itself contributes one.
- **Large path counts:** Reduce each accumulated count modulo $10^9+7$.
