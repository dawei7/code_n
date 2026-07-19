## General
**Generate leaves in their structural order**

Perform a depth-first traversal of each tree that always explores the left child before the right child. A node is a leaf only when both of its children are absent; yield its value at that moment and ignore the values of internal nodes. An explicit stack can preserve the required order by pushing the right child before the left child.

**Compare the two streams without storing either sequence**

Advance the two leaf generators together. Corresponding yielded values must be equal, and the generators must finish at the same time. A private sentinel supplied to a zip-with-padding operation distinguishes exhaustion from every legal node value, including `0`.

Every leaf is emitted in left-to-right order because depth-first traversal completely visits a node's left subtree before its right subtree. Therefore each generator produces exactly its tree's leaf value sequence. Pairwise equality plus simultaneous exhaustion is precisely the definition of leaf similarity, so the returned result is correct.

## Complexity detail
Each node of both trees is pushed and removed once, so the total time is $O(n_1+n_2)$. Each traversal stack holds at most a root-to-leaf frontier, requiring $O(h_1)$ and $O(h_2)$ space respectively; the two lazy generators therefore use $O(h_1+h_2)$ auxiliary space.

## Alternatives and edge cases
- **Materialize both sequences:** Collecting two leaf arrays and comparing them is simple and still uses linear time, but it requires $O(n_1+n_2)$ space instead of space proportional to tree height.
- **Recursive depth-first search:** Recursion yields leaves naturally in left-to-right order, with the same asymptotic bounds, but a highly skewed tree consumes one call-stack frame per level.
- **Compare node-by-node traversals:** Internal structure and values are irrelevant, so ordinary preorder or inorder sequences can disagree even when the leaves match.
- **Single-node trees:** The root is also the only leaf, so the answer depends solely on the two root values.
- **Equal prefix with different lengths:** Matching yielded values are insufficient if one tree has an additional leaf; simultaneous exhaustion is required.
- **Repeated and zero values:** Values are compared by position, and the exhaustion sentinel must not collide with any valid value.
