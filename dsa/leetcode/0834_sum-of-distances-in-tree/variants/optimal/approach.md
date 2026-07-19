## General
**Root once to expose reusable information**

Choose node `0` as a temporary root and build an adjacency list. An iterative traversal records each node's parent, depth, and a parent-before-child order. The sum of all recorded depths is already `answer[0]`, because a node's depth is exactly its distance from root `0`.

Process that order backward to compute a subtree size $c_v$ for every node $v$. Each size starts at one, then a child's completed count is added to its parent. The reverse order guarantees that all descendants of a node have contributed before that node contributes upward.

**Reroot instead of traversing again**

Suppose $v$ is a child of $u$ in the temporary rooting. Moving the distance-sum viewpoint from $u$ to $v$ makes each of the $c_v$ nodes in $v$'s subtree one edge closer. The other $n-c_v$ nodes become one edge farther away. Therefore

$$
\texttt{answer}[v]
= \texttt{answer}[u] - c_v + (n-c_v)
= \texttt{answer}[u] + n - 2c_v.
$$

A final forward pass applies this relation from each parent to its children. `answer[0]` is correct from the depth sum. If a parent's answer is correct, the relation accounts once for the distance change to every node when crossing that parent-child edge, so its child's answer is also correct. Following the traversal order proves every returned entry correct.

## Complexity detail
Building the adjacency list touches `n - 1` edges. The rooting traversal, reverse subtree pass, and forward reroot pass each visit every node or edge only a constant number of times, giving $O(n)$ time. The adjacency list, parent/order/depth arrays, subtree counts, and answers use $O(n)$ space.

## Alternatives and edge cases
- **Traversal from every node:** Breadth-first or depth-first search computes each sum correctly, but repeating a linear traversal for all roots costs $O(n^2)$ time.
- **Recursive two-pass rerooting:** The same dynamic program can be concise recursively, but a path-shaped tree can have depth $n$ and exceed Python's recursion limit; iterative orders avoid that runtime hazard.
- **Single node:** With no edges and no other nodes, the only distance sum is zero.
- **Path-shaped tree:** Subtree sizes can be highly unbalanced, and endpoint sums are largest; the reroot relation still applies unchanged.
- **Edge orientation:** Each input pair is undirected, so both adjacency directions must be stored regardless of the pair's listed order.
- **Integer range:** Distance sums may be quadratic in $n$, even though the algorithm is linear; the stored values must not be confused with operation counts.
