## General
**A parent needs a complete summary of both children**

Process nodes in postorder. For each subtree, record whether it is a BST, its minimum and maximum values, its node count when valid, and the largest BST size found anywhere below it.

An empty child is a valid BST of size zero with minimum $+\infty$ and maximum $-\infty$. Those sentinels make the same strict comparison work for missing and nonmissing children.

**Combine summaries with strict boundary tests**

A node roots a BST exactly when both child subtrees are BSTs and `left.maximum < node.value < right.minimum`. When this holds, its size is one plus both child sizes, and its new bounds include the node and both children. The entire valid subtree is at least as large as either valid descendant, so its size becomes the best value for that summary.

If either child is invalid or a boundary comparison fails, the current subtree cannot be a BST. Its best answer is still the larger best value reported by its children; no cross-root candidate is possible because any subtree containing the current root must contain all descendants beneath that root.

**Iterative postorder keeps deep trees safe**

Use a stack of `(node, expanded)` pairs. The first visit schedules the node after its children; the expanded visit combines summaries that are now available. This has the same dependency order as recursive postorder without relying on the language call-stack limit.

For `[10,5,15,1,8,null,7]`, the subtree rooted at five summarizes as a three-node BST. The subtree rooted at fifteen is invalid because seven is on its right but is smaller than fifteen, so the root ten is also invalid. The best child summary correctly preserves answer three.

Each summary is correct by induction from empty children upward. The strict min/max conditions are exactly the global BST constraints for joining two already valid children, and invalid joins retain the best complete subtree wholly contained on one side. Thus the root summary contains the global optimum.

## Complexity detail
Every node is pushed a constant number of times and summarized once, giving $O(n)$ time. The explicit postorder stack and summary table hold at most $O(n)$ nodes, using $O(n)$ space.

## Alternatives and edge cases
- **Validate and count every rooted subtree independently:** repeats descendant traversal and can take $O(n^2)$ time on a skewed tree.
- **Check only immediate child values:** misses violations deeper inside a child subtree.
- **Inorder traversal alone:** identifies whether the entire tree is a BST but does not directly isolate the largest valid rooted subtree.
- Duplicate boundary values invalidate a strict BST. An empty tree returns zero; every single node is a BST of size one.
