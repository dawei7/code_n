## General
**Traverse every depth from right to left.** Process a node's right subtree before its left subtree and retain the identities of nodes already encountered. The defect always points from the invalid node to a same-depth node on its right. Therefore the erroneous target has already been visited when traversal reaches the invalid node.

**Detect the pointer before following it.** For each node, first test whether its current `right` object is in the visited set. If so, this is the unique invalid node: return `null` to its caller, which replaces the parent's link and discards the invalid node's genuine subtree. Crucially, the traversal never follows the erroneous pointer, so the target is neither duplicated nor removed.

**Repair ordinary links recursively.** If the right pointer is not already known, record the current node, recursively repair its right child, then repair its left child, and return the node. The right-first order ensures all nodes on the relevant portion of a level are known in the direction required by the defect guarantee.

**Why the detected node is unique.** A valid child points to the next depth, so it cannot already have been visited by a right-to-left depth-first traversal before its parent examines that edge. The only edge pointing sideways is the promised corrupted right pointer, and its target lies to the right, which has already been traversed. Thus exactly that edge triggers the membership test, and returning `null` removes precisely its source subtree.

## Complexity detail
Each of the $N$ nodes is inserted into and queried against a hash set a constant number of times, giving $O(N)$ time. The visited set and recursion stack can each contain $O(N)$ nodes, so auxiliary space is $O(N)$.

## Alternatives and edge cases
- **Right-to-left breadth-first search:** Process each level from right to left while retaining parent links; detecting an already-seen right target also gives $O(N)$ time and space.
- **List instead of a hash set:** Linear membership checks make a skewed or broad traversal cost $O(N^2)$.
- **Ordinary left-first DFS:** The target to the invalid node's right may not have been visited yet, so the sideways pointer can be followed as though it were a child.
- The invalid node may be a leaf, in which case only that single node is detached.
- The invalid node may have a large genuine left subtree, all of which must be removed with it.
- `toNode` is not part of the removed subtree even though the corrupted pointer reaches it.
- Unique values let the local adapter identify custom-test endpoints, but the repair itself relies on object identity rather than values.
- Extreme positive or negative node values do not affect traversal or pointer detection.
