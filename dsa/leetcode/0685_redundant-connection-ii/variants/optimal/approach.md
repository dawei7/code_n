## General

This problem looks similar to the undirected redundant-edge problem, but edge direction creates an additional failure mode. A valid rooted tree must satisfy both of these structural rules:

- exactly one node, the root, has no parent;
- every other node has exactly one parent and is reachable from the root.

The graph began as such a rooted tree and received one extra directed edge. That extra edge can cause a directed cycle, give one node two parents, or do both at once. The exact solution first determines whether any node has two parents and then uses disjoint set union to decide which candidate edge must be removed.

**Why there are only two incoming-edge candidates**

The array `ind` counts incoming edges. For every directed edge `u -> v`, the code increments `ind[v - 1]`. Node labels are one-based, while list indices are zero-based.

The original rooted tree gave every non-root node one incoming edge and the root none. Adding one edge increases the indegree of exactly one destination. Therefore, if some node has indegree two, exactly two input edges point to that child. One is its original tree-parent edge and the other is the added edge, although the input does not reveal which is which.

The comprehension that builds `dup` records the indices of all edges whose destination has final indegree two. Under the source contract, `dup` is either empty or contains exactly two indices in increasing input order:

- `dup[0]` is the earlier incoming edge to that child;
- `dup[1]` is the later incoming edge to the same child.

This reduces the two-parent case to deciding which of those two edges is incompatible with a rooted tree.

**What union-find tests**

The parent array `p` represents connected components of the edges currently being considered. The nested `find` follows parent pointers to a representative and performs path compression:

`p[x] = find(p[x])`.

Although the source edges are directed, union-find intentionally examines their underlying undirected connectivity. If endpoints `u` and `v` already share a representative, an undirected path between them already exists. Adding another edge between them closes a cycle. If their representatives differ, `p[pu] = pv` merges the two components.

The direction used for the union-find parent pointer is unrelated to the graph's parent-child direction. The array `p` is merely a connectivity data structure; it is not trying to reproduce the rooted tree's directed parent relation.

**Case 1: no node has two parents**

If `dup` is empty, every node has indegree at most one. Because the graph has `n` nodes and `n` edges, the extra edge must have produced a cycle. The solution scans edges in their original order and unions their endpoints.

When an edge `[u, v]` has `find(u - 1) == find(v - 1)`, its endpoints were already connected by earlier edges. That edge is the one that closes the cycle in input order, so it is returned.

Returning the first cycle-closing edge also satisfies the “last answer in the input” rule. Among the edges belonging to the unique cycle, all earlier cycle edges must already be present before the final cycle edge can find an alternative path between its endpoints. Thus the first edge detected by forward union-find is the last-listed edge on that cycle.

**Case 2: one node has two parents**

The solution temporarily ignores the later incoming edge `edges[dup[1]]` and runs union-find on every other edge.

This experiment asks a precise question:

> If the later parent edge is removed, do the remaining edges still contain a cycle?

If union-find encounters a cycle even after skipping the later edge, the later edge cannot be the cycle's cause because it is not present. The earlier incoming edge `edges[dup[0]]` must be the problematic edge. It participates in the surviving cycle, while the skipped later edge is the parent connection that should remain. The method returns the earlier candidate immediately.

If no cycle appears, removing the later incoming edge fixes the graph. The remaining `n-1` edges have no undirected cycle and every node has indegree at most one. An acyclic graph of `n` nodes with `n-1` edges is connected, so its underlying graph is a tree. Its indegree pattern then supplies exactly one root and one parent for every other node. The solution returns `edges[dup[1]]`.

**Why the three apparent situations are covered**

It helps to separate the possible damage caused by the extra edge.

First, the extra edge can point into an ancestor and create a cycle without making any node have two parents. This happens when the destination was the original root. The `dup` list is empty, and the final union-find scan returns the cycle-closing edge.

Second, the extra edge can give a node a second parent without creating a cycle. Skipping the later incoming edge leaves an ordinary tree, so no union-find collision occurs and the later candidate is returned. Because both incoming edges might be plausible from indegree alone, trying the later one first is what enforces the input-order tie rule.

Third, the extra edge can give a node two parents while a cycle also exists. If the later candidate is skipped and the cycle survives, the earlier incoming edge is the one on the cycle and must be removed. The collision during the trial reveals exactly this condition.

No fourth structural pattern is possible when one edge is added to a valid rooted tree.

**A trace of the two-parent-only case**

For `edges = [[1, 2], [1, 3], [2, 3]]`, node `3` has indegree two, so `dup` contains the indices of `[1, 3]` and `[2, 3]`.

The later edge `[2, 3]` is skipped. Union-find processes `[1, 2]` and `[1, 3]` without finding a cycle. Therefore, deleting the later candidate leaves the rooted tree with root `1`, and the answer is `[2, 3]`.

**A trace where the earlier candidate must be removed**

Suppose the earlier incoming edge to a two-parent node belongs to a cycle. Skipping the later incoming edge does not break that cycle. During the trial scan, an edge eventually connects two vertices that union-find already places in one component. At that moment, the algorithm does not return the edge currently being scanned; it returns `edges[dup[0]]`. The collision is evidence that the earlier parent candidate is incompatible, not necessarily that the currently scanned edge is the required last-listed answer.

This distinction is central to the directed version.

## Complexity detail

Let `n` be the number of nodes. The source guarantees `len(edges) == n`.

Counting indegrees and collecting the two-parent edge indices each take `O(n)` time. The algorithm then performs at most one scan of all edges, with two `find` calls and at most one union per processed edge.

The exact code uses path compression but does not use union by rank or union by size. With both optimizations, the standard disjoint-set bound is `O(n\alpha(n))`, where `\alpha` is the inverse Ackermann function. For this literal implementation, a conservative worst-case bound is

$$
O(n\log n),
$$

because arbitrary root linking without a balancing rule does not justify the usual inverse-Ackermann guarantee. In practice, path compression makes the scans very close to linear. Adding rank or size would establish the tighter `O(n\alpha(n))` amortized bound.

The `ind` and `p` arrays each contain `n` integers, while `dup` has at most two entries. Data-structure space is `O(n)`. Recursive `find` can use stack space proportional to an uncompressed parent-chain depth, at worst `O(n)` without balanced union, so the complete auxiliary-space bound remains

$$
O(n).
$$

## Alternatives and edge cases

- **Explicit validation of each candidate:** Identify the two incoming edges, remove candidates from later to earlier, and run a directed traversal to test whether all nodes form one rooted tree. This is easier to visualize but can require more graph construction and repeated work.

- **Directed parent-map and cycle traversal:** One can follow parent pointers to locate a directed cycle and combine that information with the indegree-two candidates. It can also be linear, but the case analysis is easier to implement incorrectly.

- **Union-find with rank or size:** A rank or component-size array makes the asymptotic guarantee match the standard `O(n\alpha(n))` claim while preserving all decisions in this solution.

- **The original root receives the extra edge:** Every node then has indegree one, so `dup` is empty. The no-duplicate-parent branch correctly finds the cycle.

- **Two parents but no cycle:** Skipping `dup[1]` produces no collision, so the later candidate is returned as required.

- **Two parents and a cycle:** A collision remains after the later candidate is skipped, so `dup[0]` is returned.

- **Input ordering:** `dup` is built by scanning `edges` from left to right. Its positions therefore encode the earlier and later candidates without an extra sort.

- **One-based graph labels:** Calls to `find` subtract one, but returned edges keep their original one-based values.

- **Union direction:** `p[pu] = pv` does not mean `v` is the graph parent of `u`. Reversing that assignment would not alter connectivity correctness.

- **No general malformed-input fallback:** The code relies on the promise that the graph is a rooted tree plus exactly one new edge. Arbitrary directed graphs could violate the assumptions that `dup` has zero or two entries and that one of the described cases must yield an answer.

- **Recursive parent chains:** With `n <= 1000` the stated input bound limits the practical risk, but balanced or iterative union-find would be more robust under much larger constraints.
