## General
**Record discovery ancestry.** Build an adjacency list and run depth-first search from server `0`, which reaches the entire connected network. Assign `discovery[u]` when `u` is first visited. For each server, maintain `low[u]`, the smallest discovery time reachable from its DFS subtree by following tree edges and then at most one non-parent edge to an already discovered vertex.

**Propagate alternate routes upward.** After recursively exploring a previously unseen neighbor `v`, update `low[u] = min(low[u], low[v])`. An edge to an already discovered neighbor other than the DFS parent is a back edge, so update with that neighbor's discovery time instead. Ignoring only the parent edge prevents the immediate undirected return from being mistaken for an alternate route.

**Identify exactly the bridges.** For a DFS tree edge from `u` to `v`, the condition $\textit{low}[v]>\textit{discovery}[u]$ means no vertex in `v`'s subtree can reach `u` or an ancestor without that edge. Removing it therefore separates the subtree, so it is critical. If the inequality does not hold, a back edge supplies another route around the tree edge, and removing the edge cannot disconnect that subtree from the rest of the network.

## Complexity detail
Let $m$ be the number of connections. Building the adjacency list takes $O(n+m)$ space and $O(m)$ time. DFS visits each server once and examines each undirected edge from both endpoints, for $O(n+m)$ total time. The adjacency list, discovery and low arrays, result, and recursion stack occupy $O(n+m)$ space.

## Alternatives and edge cases
- **Remove every edge and retest connectivity:** A BFS or DFS after each removal is correct but costs $O(m(n+m))$ time.
- **Disjoint-set union per omitted edge:** Rebuilding connectivity for every candidate has the same prohibitive repeated-work pattern.
- **Single edge:** With two servers and one connection, that connection is a bridge.
- **Tree network:** Every edge is critical because a tree has no alternate route around any edge.
- **Cycle:** No edge on a cycle is critical; the remaining direction around the cycle preserves connectivity.
- **Cycle with a tail:** Cycle edges are protected by alternate routes, while every edge in the attached acyclic tail is critical.
- **Output order:** DFS discovery order need not match the input order, and either endpoint orientation represents the same undirected critical connection.
- **Recursion depth:** A chain may contain $10^5$ servers, so recursive implementations must provide enough call-stack capacity or use an explicit stack.
