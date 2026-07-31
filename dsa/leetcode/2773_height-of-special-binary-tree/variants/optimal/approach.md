## General

A normal traversal cannot blindly follow every non-null `left` and `right` pointer: the original leaves use those pointers to form a cycle, so treating them as descendants would revisit nodes and would not measure the underlying tree's height.

**Recognizing an original leaf**

When the special tree has multiple leaves, a leaf's `left` pointer refers to its predecessor in the cyclic order. That predecessor's `right` pointer points back to the current node. Thus `node.left.right is node` identifies a linked leaf. If the tree has only one original leaf, the example contract leaves both of its pointers null, so that case is recognized separately.

An internal node cannot satisfy the back-link test: its left child is connected to it by an original downward edge, and that child's right pointer is either another original child or, if the child is a leaf, the next leaf in the cycle rather than the parent.

**Iterative depth-first traversal**

Store `(node, depth)` pairs in a stack, beginning with `(root, 0)`. Update the greatest depth whenever a pair is removed. If the node is either kind of original leaf, do not follow its neighbor pointers. Otherwise, push each non-null original child with depth increased by one.

Every internal node is reached through exactly one original parent edge, and every leaf ends a traversal branch. Consequently, the recorded maximum considers every root-to-node path in the underlying tree and excludes every artificial leaf-cycle edge, which is exactly the requested height.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Each original node is pushed and removed once, so the time complexity is $O(n)$. A depth-first stack holds at most one pending branch per level, giving $O(h)$ auxiliary space.

## Alternatives and edge cases

- **Recursive depth-first search:** The same leaf test gives a concise $O(n)$ traversal, but a tree of height close to $10^4$ can exceed Python's recursion limit.
- **Breadth-first search:** Level-order traversal also runs in $O(n)$ time, but its queue can hold $O(n)$ nodes on a wide level rather than $O(h)$ depth-first state.
- **Visited-set graph traversal:** Marking nodes prevents an infinite loop, but following leaf-neighbor links still treats artificial edges as tree edges and can report the wrong height.
- **Iterative deepening:** Repeatedly searching from the root for the next depth uses only $O(h)$ space but can take $O(nh)$ time on a skewed tree.
- A tree with one original leaf has no cyclic neighbor pointers, so the ordinary null-child leaf case must be handled.
- An internal node may have only one child; a single null pointer does not by itself identify an original leaf.
- Height counts edges, so the root starts at depth $0$ and a two-node tree has height $1$.
