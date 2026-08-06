## General
**The edge count reduces the remaining question to cycles**

An undirected tree on `n` nodes must have exactly $n - 1$ edges. Reject any other count, then use disjoint sets to ensure those edges do not create a cycle.

Each disjoint-set root represents one connected component of all edges processed so far. Unioning different roots merges components; encountering equal roots means the new edge closes a cycle.

**Successful unions prove both acyclicity and connectivity**

An edge whose endpoints already share a root closes a path into a cycle, so rejecting it is necessary. If all $n - 1$ edges instead join different components, each union reduces the component count by one: starting from `n`, exactly $n - 1$ successful unions leave one component. The graph is therefore connected and acyclic, which is precisely a tree.

## Complexity detail

The edge-count check takes $O(1)$. Across all $e$ edges, union by size with path compression takes
$O(e\alpha(n))$ time. Because the only inputs that reach the union loop have $e = n - 1$, this is within the
required $O(n + e)$ bound. The `parent` and `size` arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **DFS/BFS:** also achieves $O(n + e)$ by checking connectivity while ignoring each node's parent edge.
- **Search for a path before every insertion:** can take $O(ne)$.
- **One node:** with no edges, the edge-count check accepts the graph and there is no cycle to reject.
- **Invalid edge count:** fewer than $n - 1$ edges cannot connect every node, while more than $n - 1$ edges cannot form a tree.
