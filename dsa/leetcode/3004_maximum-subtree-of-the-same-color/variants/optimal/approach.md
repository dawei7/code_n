## General

**Root the undirected tree.** Starting from node 0, record each node's parent
and a traversal order. Reversing that order guarantees that every child is
processed before its parent without relying on recursion depth.

**Propagate two subtree facts.** For each node, maintain its full rooted
subtree size and whether that subtree is monochromatic. Begin every node as a
valid size-one subtree. Add each child's size to its parent. The parent's
subtree remains uniform exactly when every child subtree is uniform and every
child has the same color as the parent.

Whenever a completed node is uniform, use its accumulated size to update the
answer. This condition is necessary because any invalid child or color change
appears inside the parent's subtree, and sufficient because the parent and all
uniform child subtrees then share one color.

## Complexity detail

Building the adjacency lists, rooting the tree, and processing the postorder
each touch every node and edge a constant number of times. The algorithm uses
$O(N)$ time and $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Recursive depth-first search:** It expresses the same recurrence but may overflow the call stack on a 50,000-node chain.
- **Rescan every candidate subtree:** Gathering descendants and colors independently for every root is correct but costs $O(N^2)$ time on a chain.
- **Leaf nodes:** Every leaf is a valid monochromatic subtree of size one.
- **Matching parent and child colors:** This is not enough when the child's own subtree already contains another color.
- **Single node:** With no edges, the root itself gives answer one.
- **Large color identifiers:** Only equality matters; colors need no compression.
