## General

**Infection travels along undirected adjacency**

A binary-tree node normally exposes only its left and right children. Infection can also move from a child to its parent, so starting from an arbitrary node requires upward edges that the original representation does not directly provide.

The exact solution first converts the tree into an undirected adjacency list keyed by unique node values. It then runs a second depth-first search from `start` to find the greatest number of edges from the start to any node.

That greatest distance is the infection time because infection expands across one edge per minute and all infected nodes spread simultaneously.

**Build the undirected tree**

The first helper receives the current node and its parent `fa`. For every real parent-child relationship, it records both directions:

```python
g[node.val].append(fa.val)
g[fa.val].append(node.val)
```

It then recurses into the left and right children, passing the current node as their parent. A null child returns immediately.

The root has no parent, so the `if fa` guard skips adding a nonexistent edge. Tree nodes are objects and therefore truthy, so this condition distinguishes the root call from child calls.

Unique node values make them safe graph identifiers. If values could repeat, a value-keyed graph would merge distinct nodes incorrectly; the contract rules that out.

**Find the farthest node from the infection source**

`dfs2(node, fa)` returns the maximum distance from `node` to any node reachable without stepping back through `fa`. It begins with zero, representing the current node itself.

For every adjacency neighbor other than the parent, it computes:

```python
1 + dfs2(nxt, node)
```

The added one counts the edge from `node` to `nxt`. Taking the maximum selects the deepest route.

Although the graph is now undirected, it is still a tree. Passing the immediate parent is enough to prevent cycles: the only way to reach an already visited part from a node is through the edge just used to enter it. A general graph would require a full visited set.

**Relate farthest distance to simultaneous infection**

At minute zero, only `start` is infected. After one minute, exactly nodes at graph distance one can be infected. More generally, after $t$ minutes, every node whose shortest distance from `start` is at most $t$ is infected.

This follows by induction. Infection can traverse at most one new edge per minute, so no node farther than $t$ can be infected by then. Every node at distance $t$ has a neighbor at distance $t-1$, which was infected one minute earlier and transmits to it.

Therefore, all nodes are infected precisely when time reaches:

$$
\max_v \operatorname{dist}(\texttt{start},v).
$$

The second DFS computes this maximum distance directly.

**Trace movement above and below the start**

If infection begins at an internal node, one DFS branch may go down into its children, while another moves through its recorded parent and then into the parent's other subtree. The undirected graph treats all three directions uniformly.

In the first example, starting from node `3` reaches nodes `1`, `10`, and `6` after one edge. The farthest nodes `9` and `2` lie four edges away through `1`, `5`, and `4`. `dfs2` returns four, matching the final infection minute.

**Why both DFS passes are correct**

The first pass visits every original tree edge once as a parent-child relation and inserts its two directed adjacency entries. It inserts no edge absent from the tree. Thus, paths in `g` correspond exactly to legal parent-or-child infection paths.

The second pass recursively evaluates all branches from `start` without revisiting the parent. For a leaf relative to that traversal, it returns zero. For an internal node, the farthest reachable node is either itself or lies through one neighbor, so the maximum of one plus child results is exact. Induction on the traversal subtree proves the returned value is the farthest distance.

Combining this with the distance-time equivalence proves the final answer.

**Exact source versus the manifest wording**

The manifest summary mentions recording parents and running breadth-first search. The source instead builds a full adjacency list and runs a recursive longest-distance DFS. Both are linear and return the same eccentricity in a tree, but the data flow and practical stack behavior differ. This document follows the actual two-DFS code.

## Complexity detail

Let $n$ be the number of tree nodes. The graph-building DFS visits every node and original edge once, taking $O(n)$ time. The distance DFS likewise visits every graph node and scans both adjacency entries of every edge, taking $O(n)$ time. Total time is $O(n)$.

The adjacency lists store $2(n-1)$ neighbor values, requiring $O(n)$ space. Either recursive pass can reach depth $O(n)$ in a skewed tree, so the call stack also uses $O(n)$ space. Total auxiliary space is $O(n)$.

With up to $10^5$ nodes, a path-shaped tree can exceed Python's default recursion limit. The mathematical algorithm is correct, but iterative traversal is operationally safer.

## Alternatives and edge cases

- **Parent map plus BFS:** Record each node's parent, then breadth-first search from `start` across parent, left child, and right child. Queue levels directly count minutes and avoid deep recursion.
- **One-pass DFS:** Propagate distances to the start while computing subtree heights. It avoids a separate graph but requires more intricate state reasoning.
- **Single-node tree:** The graph has no edges and `dfs2` returns zero.
- **Start at the root:** All movement is downward, and the answer is the ordinary tree height in edges.
- **Start at a leaf:** The farthest node may lie in a different branch reached through several parents.
- **Skewed tree:** The answer can be `n - 1`, while recursive depth becomes a practical concern.
- **Unique values:** They are essential for using integers as graph node identities.
- **No visited set in `dfs2`:** Parent exclusion is sufficient only because the converted graph is a tree.
- **Minute zero:** The starting node is already infected, so a distance of zero requires no elapsed minute.
