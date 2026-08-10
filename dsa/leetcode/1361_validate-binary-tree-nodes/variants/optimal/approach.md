## General

A valid tree over all `n` nodes needs three structural properties: no node has more than one parent, no directed edge creates a cycle, and all nodes belong to one connected component. The checked-in solution verifies those properties while processing every parent-child edge with a disjoint-set structure.

**Represent current components**

`p = list(range(n))` initially makes every node the representative of its own component. The helper `find(x)` follows parent links until it reaches a representative and applies path compression on the way back:
`p[x] = find(p[x])`.

After compression, later lookups for the same node reach the component representative more quickly.

The variable named `n` begins as the number of components as well as the number of nodes. Each accepted edge joins two components and decrements `n`. By the final return, `n` is being used as a component counter rather than as the original node count.

**Reject a second parent**

`vis[j]` records whether node `j` has already appeared as a nonnegative child in any left or right slot. Before accepting a new edge `i -> j`, the method checks `vis[j]`.

If it is already true, two parent positions point to the same child. Those positions could belong to different nodes or even be both child slots of one node. Either way, a binary tree node other than the root must have exactly one parent, so the structure is invalid.

The child is marked only after the edge passes all checks.

**Reject an edge inside one component**

If `find(i) == find(j)`, the proposed parent and child are already connected by previously accepted edges. Adding another edge between them closes an undirected cycle in that component. Given the one-parent checks on accepted directed edges, this also means the directed structure cannot be a valid tree.

The method immediately returns false instead of performing the union.

**Merge an accepted parent-child connection**

For a valid edge, `p[find(i)] = find(j)` joins the two disjoint components. This orientation points the representative of `i`’s component at the representative of `j`’s component. Union-find does not require a particular representative to remain root; it only needs both sets to acquire one common representative.

The source then marks `vis[j] = True` and decrements the component count.

The loops examine `leftChild[i]` and `rightChild[i]`. A value of negative one means no edge and is ignored.

**Use the final component count for connectivity**

If all accepted edges avoid multiple parents and cycles but the nodes form several separate trees, the component count remains greater than one. `return n == 1` rejects that forest.

If the count is one, all nodes are connected. A connected acyclic graph of `n` nodes has `n - 1` accepted edges. The multiple-parent check ensures the connected directed structure has one root and every other node has one incoming edge. Because each input node provides at most a left and right child, the result is exactly one valid binary tree.

This combination covers every failure mode:

- A repeated child is caught by `vis`.
- A cycle is caught before union.
- Multiple disconnected roots remain as multiple components.
- A valid tree performs exactly enough unions to leave one component.

## Complexity detail

There are at most $2n$ child slots. Each nonnegative child causes a constant number of `find` operations and at most one union assignment. With path compression, disjoint-set operations are near constant amortized time; the conventional bound is $O(n\alpha(n))$, reported as $O(n)$ because the inverse Ackermann function grows extremely slowly.

The implementation does not use union by rank or size. Path compression still prevents repeated long traversals in normal amortized use, but a conservative general union-find analysis is weaker than for the full two-optimization structure.

The arrays `p` and `vis` each contain $n$ entries, so auxiliary space is $O(n)$. `find` is recursive. An adversarial long parent chain followed by a lookup near its beginning can require $O(n)$ call depth before compression, potentially exceeding Python’s recursion limit for `n = 10^4`. An iterative `find` would remove that runtime robustness concern.

## Alternatives and edge cases

- **Root plus DFS:** Compute which node has no parent, traverse from it, reject revisits, and verify that all `n` nodes were reached. This is also $O(n)$ time and space.
- **Breadth-first traversal:** The same root and revisit checks can use a queue instead of a stack.
- **Indegree counting:** Require exactly one zero-indegree node and every other node to have indegree one, then verify connectivity or acyclicity.
- **Repeated child in both slots:** `vis` rejects a node named as both left and right child, even when the parent is the same.
- **Self-child:** `find(i) == find(j)` immediately detects `i -> i` as a cycle.
- **Disconnected forest:** Each component may individually be a tree, but the final count exceeds one and returns false.
- **One node with no children:** No union occurs, the component count remains one, and the answer is true.
- **No root because of a cycle:** The cycle is detected during edge processing before the final count.
- **Negative-one child:** It means absence and must not be passed to `find` or marked visited.
- **Recursive find depth:** A long chain can stress Python’s call stack; iterative path compression is safer for adversarial maximum-size input.
- **Union orientation:** Pointing the parent component’s representative to the child component’s representative looks reversed compared with some DSU examples but does not affect component membership correctness.
