## General

A critical connection is a bridge in an undirected graph: removing that edge separates vertices that were previously connected. An edge is not a bridge when the child side of a depth-first-search tree has some other route back to the current vertex or one of its ancestors. The exact solution detects that alternative route with Tarjan-style discovery and low-link values.

**Build an undirected adjacency list**

For each connection `[a, b]`, the code appends `b` to `g[a]` and `a` to `g[b]`. Both directions are necessary because the network is undirected. The input has no repeated connections, so each neighbor entry corresponds to one distinct edge.

The arrays `dfn` and `low` both start with zeros. A zero `dfn` means the vertex has not been visited. The variable `now` is a monotonically increasing timestamp shared by the nested DFS through `nonlocal now`.

**Discovery time records DFS order**

When `tarjan(a, fa)` first enters vertex `a`, it increments `now` and assigns that value to both `dfn[a]` and `low[a]`.

`dfn[a]` never changes again. It is the time at which `a` was discovered, so ancestors in the current DFS tree have smaller discovery values.

`low[a]` can decrease. Its eventual meaning is the smallest discovery time reachable from `a`’s DFS subtree by following zero or more tree edges downward and then, if useful, one non-parent edge to an already discovered vertex. Informally, it tells how high that subtree can reconnect without using the tree edge from `a` to its parent.

**Ignore the exact edge back to the parent**

While exploring neighbors `b` of `a`, the check `if b == fa` skips the tree edge that brought the recursion into `a`. In an undirected adjacency list, that same physical edge appears in both endpoint lists. Treating it as an alternate route would falsely make every child appear connected back to its parent.

This simple parent-vertex check is safe because the input forbids repeated parallel connections. With parallel edges between the same endpoints, an edge identifier rather than just the parent vertex would be needed to distinguish the tree edge from another valid back edge.

**Process an unvisited neighbor as a DFS child**

When `dfn[b]` is zero, the edge from `a` to `b` becomes a DFS-tree edge. The recursive call completely explores `b`’s subtree. On return, `low[b]` states how far upward that subtree can reach through some route other than the parent tree edge.

The update

`low[a] = min(low[a], low[b])`

propagates that best reconnection information toward ancestors.

Then the solution tests

`if low[b] > dfn[a]`.

If the smallest discovery time reachable from `b`’s entire subtree is still greater than `a`’s discovery time, the subtree cannot reach `a` or any ancestor without using edge `a-b`. Removing that edge disconnects the child subtree, so `[a, b]` is appended as critical.

If `low[b] <= dfn[a]`, some route from the child subtree reaches `a` or a higher ancestor. Together with the tree edge, that route forms a cycle containing `a-b`. Removing the edge leaves the alternate route, so it is not a bridge.

The comparison must be strict. Equality means the subtree can reconnect exactly to `a`, which is enough to protect the edge.

**Process an already discovered neighbor as a back edge**

If `b` has already been discovered and is not the parent, the code updates

`low[a] = min(low[a], dfn[b])`.

The direct edge reaches vertex `b`, whose discovery time is the relevant ancestral timestamp. Using `dfn[b]` rather than `low[b]` prevents information from unrelated DFS branches from being folded through a non-tree edge in an invalid way.

In an undirected DFS, a visited non-parent neighbor encountered in this context supplies the cycle connection needed to lower the low-link value.

**Following the triangle with a tail**

For connections `[0, 1]`, `[1, 2]`, `[2, 0]`, and `[1, 3]`, vertices zero, one, and two form a cycle. Suppose DFS reaches two through one. The edge from two back to zero lowers `low[2]` to zero’s discovery time. That value propagates to one, showing that the tree edges within the triangle have alternate routes.

Vertex three has no neighbor other than one. Its `low` remains its own later discovery time, which is greater than `dfn[1]`. Therefore edge `[1, 3]` is reported as the only bridge.

**Why every reported edge and only every bridge is returned**

For a DFS-tree edge `a-b`, all paths from the child subtree to the already explored part of the graph either use that parent edge or are represented by a back connection that lowers `low[b]`. If `low[b] > dfn[a]`, no such alternate connection reaches `a` or above, so removing the edge separates the subtree. The reported edge is genuinely critical.

If the inequality fails, the low-link witness supplies a path from the child subtree back to `a` or an ancestor. Combining that path with tree edges creates an alternate route around `a-b`, so the edge is not critical.

Every undirected bridge appears as a DFS-tree edge: a visited-to-visited non-tree edge is itself part of a cycle. The test is applied to every tree edge after its child is fully explored, so no bridge is missed. The network is connected according to the contract, making one call `tarjan(0, -1)` sufficient to visit every server.

## Complexity detail

Let $n$ be the number of servers and $m$ be the number of connections.

Building the adjacency list takes $O(n+m)$ time. DFS discovers each vertex once. Every undirected connection appears twice in the adjacency lists and is examined a constant number of times, so traversal takes $O(n+m)$ time. Overall time complexity is $O(n+m)$.

The adjacency lists store $2m$ neighbor entries. `dfn` and `low` store $n$ integers, and `ans` can contain up to $m$ bridges. The recursive call stack can reach depth $n$ for a chain. Auxiliary and result storage are therefore $O(n+m)$.

The recursive depth is an operational concern in Python at the maximum $n=10^5$. The exact code relies on an execution environment whose recursion allowance can accommodate the DFS, or on surrounding runtime configuration. An iterative Tarjan traversal can avoid that language-stack limit while preserving the same graph complexity.

## Alternatives and edge cases

- **Remove every edge and test connectivity:** Running a graph traversal after each removal can cost $O(m(n+m))$, far too much for $10^5$ edges.
- **Iterative low-link DFS:** Store explicit frames containing vertex, parent, and neighbor position. This avoids Python recursion depth but requires more bookkeeping to perform child-return updates.
- **Union-find in reverse or offline bridge algorithms:** More advanced techniques exist for dynamic settings, but low-link DFS is the direct linear solution for one static graph.
- **Graph is a tree:** Every edge is the sole connection between two components, so every child has `low[child] > dfn[parent]` and all edges are returned.
- **Graph is one cycle:** Every tree child can reconnect to an ancestor, so no edge satisfies the bridge inequality.
- **Two vertices with one edge:** The child has no back edge, and the only connection is correctly reported.
- **Disconnected input:** A general implementation would start DFS from every unvisited vertex. This solution starts only at zero because the local contract states that all servers are mutually reachable.
- **No repeated connections:** Skipping by parent vertex is safe only under this guarantee. Parallel undirected edges would require tracking edge IDs.
- **Strict comparison:** `low[b] == dfn[a]` means a route returns to `a`, so the edge lies on a cycle and is not a bridge.
- **Output orientation and order:** The contract accepts any order and either endpoint orientation, so appending tree direction `[a, b]` is sufficient.
