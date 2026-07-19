## General
**Classifying a child from its parent**

Loneliness is determined completely by a node's parent and sibling position. When visiting a parent, inspect `left` and `right` together. If exactly one is present, append that existing child's value. If both are present, the children are siblings and neither is lonely. If neither is present, the parent contributes no child at all.

This parent-centered test is simpler than carrying parent pointers or asking each node to search for its sibling. The exclusive condition can be written conceptually as “one child exists and the other does not,” and it treats left-only and right-only parents symmetrically.

**Traversing every possible parent**

Use an explicit stack beginning with `root`. Pop one node, perform the child-pair test, and push each existing child so it can later be examined as a possible parent. Depth-first and breadth-first traversal are both valid because the output has no ordering requirement.

The root itself is never appended. It enters the stack only so its children can be classified. If the root has exactly one child, that child is lonely and is correctly appended while processing the root.

**Why each lonely node is found exactly once**

Every non-root node in a tree has exactly one parent. The traversal visits that parent exactly once and examines both of its child fields together. A node is appended during this unique examination precisely when the opposite child field is empty. That condition is exactly the definition of having no sibling.

Conversely, every appended value comes from an existing child of a parent whose other child is absent, so no non-lonely node can enter the result. Because the root is never considered as someone else's child, it cannot be appended. The collected values are therefore exactly the lonely nodes.

**A small structural trace**

For `[1,2,3,null,4]`, processing node `1` finds two children and appends neither. Processing node `2` finds no left child and right child `4`, so it appends `4`. Nodes `3` and `4` have no children and add nothing. The result is `[4]`.

## Complexity detail
Every one of the $N$ nodes is pushed and popped once, and each visit performs constant work, so time is $O(N)$. The explicit stack can hold $O(N)$ nodes in the worst case, and the returned list can itself contain $O(N)$ values. Auxiliary traversal space is therefore $O(N)$ under the stated bound.

## Alternatives and edge cases
- **Recursive depth-first search:** The same parent-local check can be expressed recursively with $O(N)$ time and $O(H)$ call-stack space for tree height $H$, but an iterative traversal avoids recursion-limit concerns.
- **Breadth-first search:** A queue visits nodes level by level and has the same correctness and $O(N)$ worst-case space; it merely produces a different valid output order.
- **Pass an `is_lonely` flag:** A parent can enqueue each child with a boolean indicating whether the sibling is absent. This is correct but stores state that can be consumed immediately while examining the parent.
- **Search for every node's parent:** Repeatedly traversing the tree to locate each parent and sibling can take $O(N^2)$ time and ignores the parent-child relationship already available during one traversal.
- **Single-node tree:** Return an empty array because the root has no parent.
- **Root with one child:** The child is lonely even though its parent is the root; only the root itself is excluded by definition.
- **Parent with two children:** Neither child is lonely, regardless of whether either child is a leaf.
- **Long one-sided chain:** Every node except the root is lonely. An iterative stack handles this shape without deep recursion.
- **Output order:** Do not sort unless desired for presentation. Any traversal order is accepted, and sorting adds unnecessary work.
