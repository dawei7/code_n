## General

Every pair's distance equals the number of edges on its path. Instead of finding every path, count how many valid same-group paths cross each edge.

Root the tree at node `0`. Removing the edge from a non-root node `u` to its parent separates `u`'s subtree from the rest of the tree. For a group label `g`, let `subtree[u][g]` contain $c$ nodes and let the whole tree contain $T_g$ nodes of that group. Exactly $c(T_g-c)$ unordered same-group pairs have one endpoint on each side, so exactly that many valid paths use this edge.

Build parent and traversal arrays iteratively, then process nodes in reverse order. Each node begins with one count for its own label. Its completed counts contribute $c(T_g-c)$ for its parent edge and are added into its parent's counts. Summing these contributions over all labels and all edges counts each pair once per edge on its unique path, which is precisely its interaction cost.

## Complexity detail

There are at most 20 labels. Processing all labels for each node therefore takes $O(20N)=O(N)$ time. The adjacency lists, traversal arrays, and fixed 21-entry count array per node use $O(N)$ auxiliary space.

## Alternatives and edge cases

- **All-pairs searches:** Run a tree search from every node and add matching-label distances. This is correct but takes $O(N^2)$ time.
- **Per-group virtual trees:** Compress each group's relevant paths and sum distances. This is useful for a large label domain but is unnecessarily complex when labels are bounded by 20.
- **Singleton:** With no unordered pair, the answer is `0`.
- **Unique labels:** Groups containing one node contribute nothing.
- **Pairs across branches:** Their path crosses the parent-side edges of both branches, so edge contributions recover the complete distance.
- **Large total:** A group containing every node on a path yields a cubic-size sum, so the result can exceed 32-bit range.
