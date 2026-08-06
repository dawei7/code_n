## General
**Visit every structural decision once**

Begin an explicit depth-first traversal with the root. Whenever a node is removed from the stack, exchange its left and right references, then schedule the children that now occupy those positions.

The traversal order is irrelevant: a node's local swap does not depend on whether its parent, children, or nodes on another branch were processed first.

**Local swaps compose into the global mirror**

After a node is processed, its two outgoing edges have their final mirrored orientation. Both original subtrees are still reachable—the swap changes only which side points to each one—and every reachable child is scheduled exactly once.

Applying this local transformation at every node exchanges the left and right subtrees recursively throughout the entire tree. The returned root therefore heads the complete mirror image.

## Complexity detail
Every node is processed once for $O(n)$ time. The explicit stack can hold $O(n)$ nodes in the worst case.

## Alternatives and edge cases
- **Recursive DFS:** It is concise but uses call-stack depth and can approach the recursion limit on a skewed tree.
- **Level-order queue:** It has the same time and worst-case auxiliary-space bounds.
- **Value-only exchange:** Swapping stored values does not invert the tree's structure.
- **Empty or singleton tree:** It is unchanged.
- **Missing child:** A lone child simply moves to the opposite side, so asymmetric trees need no special branch.
