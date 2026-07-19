## General
**View keys in sorted order.** Record `insertion_time[value - 1]`, the position at which each key entered the BST. An inorder traversal of the final BST is exactly the keys $1,2,\ldots,n$. Its root is the earliest-inserted key; the same rule recursively selects the roots of the key ranges on either side.

**Recognize a Cartesian tree.** These two properties—keys in inorder order and insertion times obeying a min-heap—uniquely define the final BST as the min-Cartesian tree of the insertion-time array. Construct it from left to right with a monotonic stack. Pop later insertion times until the current node can attach beneath an earlier one. The current node's left child is the last popped subtree, while it becomes the right child of the remaining stack top.

Every node is pushed once and popped at most once. After construction, traverse from the stack's bottom root while carrying depths and retain the largest value. The Cartesian tree has the same parent-child relationships as literal BST insertion, so this traversal returns the requested depth.

## Complexity detail
Building insertion times costs $O(n)$. Monotonic-stack construction and the final traversal each process every node a constant number of times, giving $O(n)$ total time. The insertion-time array, child arrays, stack, and traversal worklist use $O(n)$ space.

## Alternatives and edge cases
- **Literal BST insertion:** It is simple and correct but takes $O(n^2)$ time for increasing or decreasing input.
- **Ordered predecessor and successor depths:** A balanced ordered map derives each new depth in $O(\log n)$ time, for $O(n\log n)$ total, but is not needed for this permutation domain.
- **Single key:** The sole node is the root and the answer is one.
- **Monotone order:** Increasing or decreasing input produces the maximum possible depth $n$.
- **Balanced order:** Inserting middle keys before the keys of their subranges can produce logarithmic depth even though the construction still processes all $n$ entries.
- **Permutation guarantee:** There are no duplicate-key insertion rules to resolve, and direct indexing by key is valid.
