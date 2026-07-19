## General
**Record how every node reaches the root**

Traverse the tree once. For each unique node value, store its parent's value and its depth from the root. The root has no parent and depth zero. An explicit stack keeps this traversal safe even when the tree is a long chain.

**Raise the deeper target first**

Start from values `p` and `q`. If one target is deeper, repeatedly replace it with its parent and count each traversed edge until both current nodes have equal depth. Every shortest route between the original targets must include those upward edges because the shallower node cannot occur below its own depth.

**Climb together to the meeting point**

If the equal-depth values differ, move both to their respective parents and add two edges to the distance. Their first shared value is their lowest common ancestor: below it the two ancestor chains are disjoint, while from it upward they coincide. The edges counted before and during this joint climb are therefore exactly the unique path between the targets. When `p == q`, no climb occurs and the result is zero.

## Complexity detail
The traversal visits all $N$ nodes once, and the two ancestor chains contain at most $N$ edges in total. The time is $O(N)$. Parent and depth maps plus the explicit traversal stack store $O(N)$ entries.

## Alternatives and edge cases
- **Recursive lowest common ancestor:** Find the common ancestor and target depths with depth-first search; this is also $O(N)$ but a skewed legal tree can exceed Python's recursion limit.
- **Undirected adjacency plus breadth-first search:** Convert every parent-child edge into two graph edges and search from one target. It is correct but stores a larger graph than the parent/depth representation.
- **Repeated parent searches:** Finding each next ancestor by rescanning from the root can degrade to $O(N^2)$ on a chain.
- **Equal targets:** When `p == q`, the unique path has no edges.
- **Ancestor target:** If one target is an ancestor of the other, depth alignment reaches it directly.
- **Targets in opposite root subtrees:** Their meeting point is the root.
- **Single-node tree:** Both target values identify the root and the answer is zero.
