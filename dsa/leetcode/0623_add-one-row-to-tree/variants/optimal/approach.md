## General
**Handle a new root separately**

When `depth = 1`, create a node with `val`, attach the old root as its left child, and return it. No existing edge inside the old tree changes.

**Stop at the parent level**

For deeper insertion, traverse level by level with a deque until it contains exactly the nodes at depth `depth - 1`. There is no reason to visit their descendants before rewiring, because those descendants remain intact as whole subtrees.

**Preserve each old child on its side**

For every target parent, save its old left and right children. Set the parent's left child to `TreeNode(val, left = old_left)` and its right child to `TreeNode(val, right = old_right)`. Thus the old left subtree remains below the new left node and the old right subtree remains below the new right node.

**Why the transformation is exact**

The traversal reaches every and only parent at depth `depth - 1`. Each receives exactly two new children, so the requested row is complete across all available parent positions. Saving and reattaching the old children preserves every original node and edge below that boundary, while nodes above it are untouched.

## Complexity detail
Let `N` be the number of nodes at or above the insertion parent level and `W` the maximum width reached there. Each visited node enters and leaves the deque once, giving $O(N)$ time and $O(W)$ auxiliary space. The output adds exactly two nodes per parent at the boundary.

## Alternatives and edge cases
- **Depth-first traversal:** carry the current depth and stop descending after rewiring a target parent; it has the same $O(N)$ time and uses $O(H)$ stack space for height `H`.
- **Rescan for every level:** repeatedly traverse the whole tree to rediscover each successive level; it is correct but can take $O(NH)$ time and become quadratic on a chain.
- **Recursive insertion without a depth-one guard:** cannot attach the old root correctly because no parent exists above it.
- At depth one, the previous root becomes only the new root's left child.
- Null old children still receive new nodes; their corresponding side below the new row remains null.
- Existing left and right subtrees must stay on their original sides.
- Inserted values may equal, cancel, or differ from neighboring values without affecting structure.
