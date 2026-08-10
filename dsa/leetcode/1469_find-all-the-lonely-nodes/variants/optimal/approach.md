## General

**Loneliness is determined by a parent, not by the node itself.** A node is lonely exactly when its parent has one child. The traversal therefore examines each current node's two child references and appends the existing child when the other reference is missing.

The root is never appended by this logic because no call examines it as somebody's child. This automatically respects the rule that a parentless root is not lonely.

**Return immediately for absent nodes and leaves.** The condition `root is None` handles a missing child call. The second condition `root.left == root.right` is true for a normal leaf because both references are `None`. Such a node has no children to classify, so recursion can stop.

In an ordinary binary tree, two non-null child references point to different child nodes, so equality does not stop a two-child parent. The compact comparison is effectively a leaf check under the tree model.

**Detect each one-child configuration.** If `root.left is None` after the early return, the node is not a leaf, so its right child must exist. That right child has no sibling, and `root.right.val` is appended.

Similarly, if `root.right is None`, the existing left child is lonely and its value is appended. Exactly one of these two conditions can be true after leaves have returned. A parent with two children satisfies neither, so neither child is labeled lonely.

The code records values rather than node objects because that is the requested result.

**Continue through the complete tree.** After classifying the immediate children, DFS recurses into both references. A missing reference returns immediately. An existing child examines its own children, allowing lonely descendants at any depth to be found.

The result list `ans` belongs to the outer method. Appending from the nested helper mutates that shared list, so no `nonlocal` declaration is needed. `nonlocal` is required for rebinding a variable, not for mutating an existing list object.

**Trace a simple tree.** Suppose root one has children two and three. Neither is lonely because they share a parent, and neither missing-child condition holds at node one. If node two has only right child four, its left reference is missing, so four is appended. The root itself is never considered lonely.

If a node has only a left child, the second condition appends that child before recursion. A chain therefore reports every node except the root: each non-root node is the only child of its parent.

**Why there are no duplicates.** Every non-root node has exactly one parent. Its value can be appended only while that parent is processed, and each parent is visited once. Even if distinct nodes have equal values, the output correctly contains one entry per lonely node, so equal values may appear more than once if the tree permits them.

**The correctness argument.** Whenever the algorithm appends a right child, the left child is absent and the right child exists, so the appended node is genuinely the only child. The left-child case is symmetric. Therefore every reported node is lonely.

Conversely, take any lonely node. Its unique parent has exactly one non-null child reference pointing to it. DFS eventually visits that parent. The early return cannot trigger because the parent is neither absent nor a leaf. The matching missing-side condition appends the lonely node's value. Thus every lonely node is reported.

The traversal order happens to be depth-first and parent-before-descendants, but the problem accepts any order. No sorting is needed.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height. Each node is entered once, and every call performs constant-time child checks and at most one append. Time is `O(N)`.

The recursion stack uses `O(H)` space. The returned list can contain up to `O(N)` values, such as in a one-child chain. Including output, total space is `O(N)`, matching the manifest's worst-case bound.

Excluding output, auxiliary space is `O(H)`: logarithmic for a balanced tree and linear for a skewed tree.

With the stated maximum of one thousand nodes, recursion is near Python's usual default depth limit for a chain. An iterative traversal can avoid environment-dependent stack failure.

## Alternatives and edge cases

- **Pass an is-lonely flag:** Each recursive child call can receive whether its sibling is missing. This classifies the current node rather than inspecting children and is equally correct.
- **Breadth-first search:** A queue can inspect every parent's child pair and append the sole child. It uses space proportional to tree width.
- **Iterative DFS:** An explicit stack avoids recursion-depth limits while preserving linear time.
- **Single-node tree:** The root is a leaf, the helper returns, and the result is empty.
- **Parent with two children:** Neither child is lonely, even if one or both are leaves.
- **Parent with only a right child:** The right child's value is appended.
- **Parent with only a left child:** The left child's value is appended.
- **One-child chain:** Every node except the root is lonely.
- **Leaf:** It has no children to classify and triggers the compact early return.
- **Missing subtree:** Calling DFS on `None` is safe and does nothing.
- **Equal node values:** The result contains values per lonely node; duplicate values can legitimately appear.
- **Any-order contract:** DFS order is acceptable, so no sorting cost is needed.
- **Root rule:** The root is never appended because only children are classified.
- **Shared child object outside a valid tree:** The equality shortcut assumes normal tree structure with distinct child nodes. Such aliasing is outside the contract.
