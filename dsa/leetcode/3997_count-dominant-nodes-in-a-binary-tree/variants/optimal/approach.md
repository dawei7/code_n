## General

Whether a node is dominant depends on information below it: the largest value in its entire left subtree and the largest value in its entire right subtree. This makes postorder traversal the natural direction, because both child summaries are available before their parent is examined.

For each non-null node, recursively obtain the maximum value returned by each child. A missing child contributes negative infinity, so it can never prevent a real node from being dominant. The current node is dominant exactly when its value is at least both child-subtree maxima. Equality must count: the definition asks whether the node's value equals the maximum in its subtree, not whether it is the unique maximum.

After making that decision, return the maximum of the current value and the two child summaries. By induction from the leaves upward, every call returns the true maximum of precisely its own subtree. The same fact proves the count: leaves are counted automatically, and every internal node is counted exactly when no descendant has a larger value.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Each node is visited once and performs constant work, so the running time is $O(n)$. The recursive call stack contains at most one root-to-leaf path and therefore uses $O(h)$ auxiliary space. Because the input is a complete binary tree, $h=O(\log n)$, giving the manifest's $O(\log n)$ auxiliary-space bound.

## Alternatives and edge cases

- **Recompute every subtree maximum:** Starting a fresh traversal at every node is correct but revisits descendants and takes $O(n\log n)$ time on a complete tree instead of linear time.
- **Iterative postorder:** A stack plus a map of computed subtree maxima avoids recursion, but it needs $O(n)$ explicit auxiliary storage rather than exploiting the complete tree's logarithmic height.
- **Leaf nodes:** A leaf has no larger descendant, so it is always dominant.
- **Equal descendant values:** A node still counts when a descendant ties its value; only a strictly larger descendant disqualifies it.
- **Incomplete last level:** Completeness allows the last level to stop early from the right, but postorder reasoning does not require both children to exist.
