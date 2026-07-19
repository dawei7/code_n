## General
**Evaluate a node only after its children**

Whether a node should be deleted depends on the state of both child subtrees after their own deletions. Traverse the tree in postorder. An explicit stack stores each node together with its parent, which side links it to that parent, and whether its children have already been scheduled.

On the postorder visit, both child pointers already describe the fully processed subtrees. If they are both null and the node value is `target`, detach the node from its parent. When the node is the original root, replace the result root with null instead. Because parents are visited later, they immediately observe that deletion and can be removed in the same single postorder pass.

Every deletion required by the repeated process occurs when its node is visited: its descendants have reached their final forms, so it is a leaf exactly when the repeated bottom-up process would eventually expose it. Nodes that fail either the value or leaf condition must remain.

## Complexity detail
Each of the $n$ nodes is pushed and processed a constant number of times, for $O(n)$ time. The explicit postorder stack can contain $O(n)$ entries on a skewed tree, giving $O(n)$ auxiliary space without relying on the language recursion limit.

## Alternatives and edge cases
- **Recursive postorder:** Returning null for a qualifying processed node is concise and also $O(n)$, but a 3000-node skewed tree can exceed Python's recursion limit.
- **Repeated whole-tree passes:** Removing only the current leaves and rescanning until stable is correct but can take $O(n^2)$ time on a target-valued chain.
- **Root deletion:** If the final root is a target-valued leaf, the result is empty.
- **Non-target leaf:** It remains even when its parent equals `target`, preventing that parent from becoming a leaf.
- **Cascade through one child:** A parent can become a leaf after its only surviving child is removed.
- **No matching values:** The tree structure remains unchanged.
