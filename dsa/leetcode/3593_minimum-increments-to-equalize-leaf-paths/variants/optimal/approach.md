## General

Root the undirected tree at node `0`. For each node $u$, define `best_path[u]` as the greatest original score of any path starting at $u$ and ending at a leaf in $u$'s rooted subtree, including `cost[u]`.

Suppose an internal node has child-subtree scores $s_1, s_2, \ldots$, and let $T = \max_i s_i$. Every child subtree below $T$ must receive additional cost before its paths can match the locally longest subtree. One increment at that child's root is sufficient: adding $T-s_i$ there raises every leaf path in that entire child subtree by the required common amount.

That changed node is also unavoidable. A shorter child subtree needs a positive increase somewhere below its edge from the parent, while changing the parent would raise the already-longest sibling paths as well and would not close the gap. Thus each child with $s_i<T$ contributes exactly one changed node after all imbalances internal to that child have already been resolved.

Process nodes in reverse root-to-node traversal order. Leaves report their own cost. Each internal node counts its lagging children and reports `cost[u] + T` upward. The resulting increments make all paths match the original global maximum root-to-leaf score; choosing a still larger target cannot remove any forced subtree difference and therefore cannot use fewer nodes.

An iterative traversal avoids recursion-depth failure on a chain containing up to $10^5$ nodes.

## Complexity detail

Let $n$ be the number of nodes. Building the adjacency list, rooting the tree, and processing every child edge bottom-up each take $O(n)$ time because a tree has exactly $n-1$ edges. The total time is therefore $O(n)$.

The adjacency list, parent/children structure, traversal order, and `best_path` table use $O(n)$ space. Path sums may reach $10^{14}$, so fixed-width implementations need 64-bit integers even though the returned node count is at most $n-1$.

## Alternatives and edge cases

- **Recursive postorder DFS:** It expresses the same recurrence compactly, but a legal chain can have depth $10^5$ and overflow the language call stack.
- **Recomputing each subtree maximum:** Running a fresh traversal from every node produces the same decisions but can take $O(n^2)$ time on a deep tree.
- **Adjusting leaves independently:** Increasing every short leaf is valid but can change many more nodes than increasing their shared ancestor once.
- **Raising the global target:** Choosing a value above the original maximum also requires raising the longest paths and cannot eliminate any existing difference between sibling subtrees.
- **Unary nodes:** A node with one child introduces no choice and never adds an operation by itself.
- **Tied child maxima:** Every child already equal to the local maximum needs no new increment; only strictly smaller child scores are counted.
- **Undirected edge order:** Parent-child direction must be derived from root `0`; input edge orientation and ordering carry no meaning.
