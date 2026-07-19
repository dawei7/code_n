## General
**The edge count reduces the remaining question to cycles**

An undirected tree on `n` nodes must have exactly $n - 1$ edges. Reject any other count, then use disjoint sets to ensure those edges do not create a cycle.

Each disjoint-set root represents one connected component of all edges processed so far. Unioning different roots merges components; encountering equal roots means the new edge closes a cycle.

**Successful unions prove both acyclicity and connectivity**

An edge whose endpoints already share a root closes a path into a cycle, so rejecting it is necessary. If all $n - 1$ edges instead join different components, each union reduces the component count by one: starting from `n`, exactly $n - 1$ successful unions leave one component. The graph is therefore connected and acyclic, which is precisely a tree.

## Complexity detail
Union by size with path compression takes $O((n + e) \alpha(n))$, conventionally written $O(n + e)$. Parent and size arrays use $O(n)$ space.

## Alternatives and edge cases
- **DFS/BFS:** also achieves $O(n + e)$ by checking connectivity while ignoring each node's parent edge.
- **Search for a path before every insertion:** can take $O(ne)$.
- One isolated node is a tree; zero nodes are outside the native constraints.
