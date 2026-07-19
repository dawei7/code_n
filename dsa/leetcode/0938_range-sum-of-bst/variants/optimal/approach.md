## General
**Traverse while exploiting BST order.** Keep a stack of nodes still to inspect. For a node whose value is below `low`, its entire left subtree is also below the range, so only push the right child. Symmetrically, when the value is above `high`, only its left subtree can contain qualifying values.

**Include both boundaries.** When `low <= node.val <= high`, add the value and push both children. The inclusive comparisons ensure values equal to either limit contribute. Every skipped subtree is proved irrelevant by BST ordering, while every subtree that could contain an in-range value remains reachable.

**Finish after all relevant nodes are resolved.** Each node enters the stack at most once. The running total therefore contains every qualifying value exactly once when the stack empties. An iterative traversal avoids recursion-depth failures on a highly unbalanced tree. Pruning can make many inputs faster, although a range covering the whole tree still requires visiting all $N$ nodes.

## Complexity detail
The traversal visits the $v$ in-range nodes plus at most the boundary search paths around them, taking $O(h+v)$ time. A depth-first stack holds $O(h)$ nodes. Either $h$ or $v$ can equal $N$, so the time bound still becomes $O(N)$ in the worst case.

## Alternatives and edge cases
- **Recursive pruned DFS:** Apply the same comparisons recursively. It has the same $O(h+v)$ time and $O(h)$ call-stack bounds but may exceed the language recursion limit on a skewed tree.
- **Full inorder traversal:** Visit every node and filter values. This always takes $O(N)$ time and misses beneficial pruning on narrow ranges.
- **Scan the tree once per candidate value:** Searching the entire tree separately for every integer in the range is correct but can require $O(N^2)$ time when the range width scales with $N$.
- **Boundary equality:** Values exactly equal to `low` or `high` are included.
- **Range outside most tree values:** BST pruning may reduce the work to a single root-to-leaf path.
