## General
**The stack stores pending subtree roots in preorder order**

Return an empty list for a null root. Otherwise push the root, then repeatedly pop the next subtree root and append its value immediately, satisfying preorder's root-first rule.

Because a stack is last-in, first-out, push the right child before the left child. The left child is then processed next, and every descendant scheduled while traversing that left subtree stays ahead of the older pending right subtree. Reading the stack from top to bottom therefore gives exactly the remaining subtree roots in preorder order.

At every iteration, `result` is the completed preorder prefix and the stack represents all unvisited subtrees in the order they must begin. Each child is scheduled only by its parent, so every node appears once and the loop terminates with the complete root-left-right sequence.

## Complexity detail
Every one of the $n$ nodes is pushed, popped, and appended once, giving $O(n)$ time. At most one pending right subtree is retained for each level along the current descent, so the explicit stack uses $O(h)$ auxiliary space for tree height $h$. The returned list itself uses $O(n)$ output space.

## Alternatives and edge cases
- **Recursive depth-first search:** mirrors the preorder definition but uses an $O(h)$ call stack and can hit language recursion limits.
- **Morris preorder traversal:** uses $O(1)$ auxiliary space but temporarily threads tree links and is more intricate.
- **Breadth-first search:** visits nodes by level rather than root-left-right order.
- An empty tree returns `[]`, and a singleton returns its sole value.
- Skewed trees remain linear, while duplicate values are emitted separately because traversal follows node structure rather than value identity.
