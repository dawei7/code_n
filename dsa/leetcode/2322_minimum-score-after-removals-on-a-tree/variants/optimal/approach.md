## General

Root the tree at node `0`. Every edge can then be identified by its non-root
endpoint: removing the parent edge of node `u` detaches exactly the subtree of
`u`. An iterative depth-first traversal records each node's parent and a
contiguous entry/exit interval. It also supplies a parent-before-child order;
processing that order backward computes the XOR of every subtree.

**Why ancestry determines the three values**

Consider the two non-root endpoints `u` and `v` associated with the removed
edges. If neither is an ancestor of the other, their subtrees are disjoint.
Two component XORs are therefore `subtree_xor[u]` and `subtree_xor[v]`, while
the remaining component has
`total ^ subtree_xor[u] ^ subtree_xor[v]`.

If `u` is an ancestor of `v`, the subtree of `v` forms one component, the part
of `u`'s subtree outside `v` forms another, and everything outside `u` forms
the third. Their XORs are respectively `subtree_xor[v]`,
`subtree_xor[u] ^ subtree_xor[v]`, and `total ^ subtree_xor[u]`. The symmetric
formula handles the case where `v` is the ancestor.

The DFS intervals answer either ancestry question in constant time. Thus every
pair of removed edges yields its exact three component XORs without rebuilding
the forest. Evaluating the spread for all pairs necessarily considers the
optimal cut pair.

## Complexity detail

Let $n$ be the number of nodes. Building and traversing the adjacency list and
combining subtree XORs take $O(n)$ time. There are
$\binom{n-1}{2}=O(n^2)$ pairs of removable parent edges, and each pair is
evaluated in $O(1)$ time, so the total time is $O(n^2)$. The adjacency list,
traversal arrays, subtree XORs, and explicit DFS stack use $O(n)$ space.

## Alternatives and edge cases

- **Rebuild the forest for every cut pair:** This is straightforward and
  correct, but traversing the tree again for each of $O(n^2)$ pairs costs
  $O(n^3)$ time.
- **Recursive DFS:** It computes the same subtree information, but a legal
  1000-node path can approach or exceed Python's default recursion depth; an
  explicit stack avoids that runtime dependency.
- **Nested cuts:** XORing the inner subtree out of the outer subtree is
  essential; treating both detached subtrees as disjoint double-counts nodes.
- **Disjoint cuts:** The untouched component is obtained by XORing both
  detached subtree XORs out of the total tree XOR.
- **Minimum tree:** With three nodes there is only one pair of edges to remove,
  and the formulas still produce the XOR of each singleton component.
