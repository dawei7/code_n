## General
**Visit a node before its descendants**

Preorder emits the current node as soon as it is reached, then processes each child subtree in the stored left-to-right order. An explicit stack avoids dependence on recursion depth.

**Reverse children when pushing**

A stack removes its most recently added item first. Push the current node's children from right to left so the leftmost child becomes the next node removed and visited. Each later sibling remains below the complete subtree of the sibling to its left.

**Why the produced order is preorder**

The root is the only initial stack item and is emitted first. After any node is emitted, its children are arranged so its first child is processed next; descendants pushed by that child sit above the remaining siblings, so the entire child subtree completes before the next sibling. Induction over the tree therefore matches recursive root-then-children preorder exactly.

## Complexity detail
Every one of the `n` nodes is pushed, popped, and appended once, taking $O(n)$ time. The explicit stack may hold $O(n)$ nodes in a wide tree, and the returned traversal also stores `n` values, so total auxiliary and output space is $O(n)$.

## Alternatives and edge cases
- **Recursive traversal with one shared output list:** is also $O(n)$, but a very deep tree may exceed the recursion limit.
- **Recursive list concatenation:** is correct, yet repeatedly copying descendant results on a deep chain can take $O(n^2)$ time.
- **Queue traversal:** produces breadth-first order and is incorrect for preorder.
- **Empty tree:** returns an empty list.
- **Leaf node:** contributes its value and no children.
- **Wide root:** sibling order must be preserved.
- **Deep chain:** an explicit stack avoids call-stack overflow.
- **Child push direction:** pushing left to right reverses the requested traversal order.
- **Repeated values:** do not identify nodes; visit every node occurrence.
