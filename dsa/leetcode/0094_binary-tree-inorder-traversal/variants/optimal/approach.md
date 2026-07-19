## General
**The stack stores visits deferred by a left descent**

Keep `current` and an explicit stack of ancestors. While `current` exists, push it and move to its left child. Each pushed node is deferred: its own visit and right subtree must wait until every node reachable down its left side has been handled.

**A pop marks the exact inorder visit moment**

When no further left child exists, pop the nearest waiting ancestor. Its left subtree is now complete, so append its value and set `current` to its right child. The outer loop then descends that right subtree's left spine before any later ancestor is visited.

**Result, stack, and current divide completed and pending work**

The result contains precisely the nodes whose inorder visit is complete. The stack is a root-to-current path of nodes awaiting their own visit after left-side work. `current` begins the next subtree whose left spine has not yet been pushed. These three regions contain all reached nodes without duplication.

**Trace a right child with its own left subtree**

For `[1, null, 2, 3]`, visit `1`, move right to `2`, push `2`, and descend left to `3`. Pop and visit `3`, then pop and visit `2`, producing `[1, 3, 2]`.

**The stack suspends nodes between their left and right visits**

Descending left pushes each node whose own visit must wait until its left subtree is exhausted. Popping then visits that node, and moving to its right child begins the final part of inorder processing for that subtree.

Every node is reached once from its parent, pushed during the unique left descent that discovers it, and popped once before its right subtree. The emitted order is therefore left subtree, node, right subtree for every node, exactly inorder traversal.

## Complexity detail
Each of the `n` nodes is pushed and popped once, giving $O(n)$ time. The stack holds at most one root-to-leaf path, so auxiliary space is $O(h)$, where `h` is the tree height; the returned list is excluded.

## Alternatives and edge cases
- **Recursive depth-first search:** has the same asymptotic bounds but can exceed the language recursion limit on a highly skewed tree.
- **Repeatedly rescan subtrees:** can revisit nodes and degrade to $O(n^2)$ time.
- **Morris traversal:** achieves $O(1)$ auxiliary space by temporarily modifying pointers, but is more delicate and mutates the tree during traversal.
- Empty input leaves both `current` and the stack empty and returns an empty list.
- In a balanced tree, stack depth is $O(\log n)$; in a completely skewed tree, the $O(h)$ bound becomes $O(n)$.
