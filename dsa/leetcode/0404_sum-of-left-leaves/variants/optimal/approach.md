## General
**Carry edge direction with each traversal entry**

Use a stack of pairs `(node, is_left)`. The Boolean records whether the node was reached from its parent's left pointer, information that cannot be inferred from the node value or shape alone. The root starts with `False` because it has no parent.

**Test leaf status before expanding children**

A node is a leaf only when both child pointers are absent. If it is also marked left, add its value. Otherwise push its right child with `False` and its left child with `True`, omitting absent children.

**Why each qualifying value is counted exactly once**

Every non-root node is pushed once from its unique parent with the exact direction of that edge. The leaf test accepts precisely childless nodes, and the direction flag filters those on left edges. Since a tree node has one parent and traversal visits it once, no left leaf is missed or duplicated.

## Complexity detail
Every one of the `n` nodes is processed once, giving $O(n)$ time. The traversal stack holds at most $O(h)$ nodes for tree height `h` in a depth-first traversal, which is $O(n)$ in the worst-case skewed tree.

## Alternatives and edge cases
- **Recursive depth-first search:** passes an `is_left` flag through calls with the same $O(n)$ time and $O(h)$ call-stack space.
- **Breadth-first search:** can inspect each node's left child directly, using $O(w)$ queue space for maximum tree width `w`.
- **Search from the root for each leaf's parent:** is correct but may revisit the tree and take $O(n^2)$ time.
- An empty tree has sum zero.
- The root is not a left leaf even when it has no children.
- A left child with descendants is not a leaf.
- Negative left-leaf values contribute their signed values.
