## General
**Expose the missing parent edges**

A binary-tree node directly references only its children, but a shortest path from the target may need to move upward. Traverse the entire tree once and record each node's parent. During the app-local traversal, also locate the node whose unique value equals the serialized `target`; the native artifact already receives that node object.

After this pass, treat every node as a vertex with up to three neighbors: `left`, `right`, and its recorded parent. These undirected connections represent exactly the legal one-edge steps in the original tree.

**Expand breadth-first from the target**

Begin a breadth-first search with only the target in layer zero. For each layer, add every unvisited child or parent to the next layer. A visited set prevents immediately walking back across an edge and ensures each node enters at most once.

Breadth-first layers are defined by shortest-path length: the initial layer is at distance zero, and every expansion adds one edge. Because a tree has one unique path between any pair of nodes, all nodes first reached in layer `d` are exactly distance $d$ from the target. After `k` expansions, return the values in the current layer. If the frontier becomes empty sooner, no qualifying nodes exist.

## Complexity detail
Building parent links visits all $n$ nodes once. The breadth-first search also visits each node at most once and inspects at most three neighbors per node, so total time is $O(n)$. The parent map, visited set, traversal stack, and breadth-first frontiers together use $O(n)$ space.

## Alternatives and edge cases
- **Rebuild a full adjacency matrix:** It supports breadth-first search but spends $O(n^2)$ time and space discovering edges that the tree already exposes.
- **Run a fresh root search for every candidate node:** Computing each candidate's path to the target separately is correct but can take $O(n^2)$ total time.
- **Recursive distance propagation:** A depth-first solution can return distances while collecting opposite subtrees, but its control flow and boundary calculations are more intricate.
- **Distance zero:** The answer contains only the target value.
- **`k` exceeds the tree diameter:** The frontier becomes empty and the result is `[]`.
- **Target is the root:** There is no parent neighbor, but downward breadth-first layers work unchanged.
- **Target is a leaf:** Parent edges allow the search to reach siblings, ancestors, and other branches.
- **Output order:** Any permutation of the qualifying unique values is valid.
