## General
**Visit nodes in the required order**

An in-order traversal of a binary search tree visits values in increasing order: traverse the left subtree, visit the node, and then traverse the right subtree. Use an explicit stack to perform this traversal without losing access to pending ancestors.

**Rewire one node at a time**

Keep a dummy node and a `tail` pointer to the last node placed in the result. When a node is popped from the traversal stack, save its original right child before changing links. Set its left child to `None`, connect `tail.right` to this node, advance `tail`, and continue the traversal from the saved right child. Finally set the last right pointer to `None` and return `dummy.right`.

After each visited node, the chain beginning at `dummy.right` contains exactly the already visited in-order prefix, with no left children and with `tail` at its final node. The next stack pop is the next node in in-order sequence, so appending it preserves this property. Once traversal ends, every original node appears exactly once. Because a binary search tree's in-order sequence is increasing, the completed rightward chain has precisely the required order and shape.

## Complexity detail
Each of the $n$ nodes is pushed onto and popped from the traversal stack once, giving $O(n)$ time. The stack holds at most one root-to-leaf path, so it uses $O(h)$ auxiliary space. Rewiring reuses the existing nodes and does not allocate an $O(n)$ output copy.

## Alternatives and edge cases
- **Recursive in-order traversal:** Carrying a shared tail pointer gives the same $O(n)$ time and $O(h)$ call-stack space, but recursion hides the rewiring order.
- **Collect values and build new nodes:** An in-order value list followed by reconstruction is simple, but it uses $O(n)$ extra storage and discards reusable nodes.
- **Sort all values first:** A general traversal plus sorting is correct for a binary search tree, but costs $O(n \log n)$ time and ignores the in-order ordering guarantee.
- **Repeated minimum selection:** Selecting the next smallest remaining value by scanning all candidates can take $O(n^2)$ time.
- **One node:** Clear its left and right pointers and return the same node.
- **Already right-skewed tree:** The traversal preserves the increasing order while ensuring every left pointer is empty.
- **Left-skewed tree:** The deepest left node becomes the new root, and every former ancestor is appended to its right.
- **Saved right child:** Preserve `current.right` before assigning links, or rewiring can lose the unvisited right subtree.
