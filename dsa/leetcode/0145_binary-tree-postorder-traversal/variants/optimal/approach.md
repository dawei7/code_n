## General
**The stack defers each ancestor until both subtrees are complete**

Follow `current` down the left spine, pushing every node because postorder cannot emit it before its descendants. When `current` becomes null, inspect the stack top without immediately removing it.

If that node has a right child other than `last_visited`, set `current` to the right child and perform the same left descent there. Otherwise its right subtree is absent or has just completed, while its left subtree completed before this inspection; the node is ready to pop and append. Record the popped node in `last_visited` so its parent can recognize the completed right subtree instead of entering it again.

At every step, `result` contains complete subtrees in postorder, the stack holds ancestors whose own visits are pending, and `last_visited` identifies the most recently finished subtree. A node is appended only after both children, and every child transition is taken once, so the final sequence is exactly left-right-root order.

## Complexity detail
Each of the $n$ nodes is pushed and popped once and inspected only a constant number of times, giving $O(n)$ time. The stack contains at most one root-to-leaf path, so auxiliary space is $O(h)$ for tree height $h$. The returned list uses $O(n)$ output space.

## Alternatives and edge cases
- **Recursive depth-first search:** is shorter but uses an $O(h)$ call stack and can hit recursion limits.
- **Two stacks or reversed root-right-left:** is simple but can retain $O(n)$ nodes rather than $O(h)$.
- **Morris postorder traversal:** achieves $O(1)$ auxiliary space but temporarily threads links and reverses paths.
- An empty tree returns `[]`, and a singleton is emitted immediately after its null left descent.
- Skewed trees remain linear in either direction.
- Right-subtree completion must use node identity, not value equality, because distinct nodes may store equal values.
