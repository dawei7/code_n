## General
**Carry each node's parent through a level traversal:** Begin a breadth-first traversal with the root paired with no parent. All entries processed in one outer iteration have the same depth. For that level, record the parent whenever a node's value equals `x` or `y`, and enqueue every child together with its current node.

**Decide as soon as a relevant level ends:** If both values were found in the same level, they are cousins exactly when their recorded parent objects differ. If only one was found, the other node must occur at another depth, so the answer is immediately `false`. If neither appears, continue to the next level.

Because both selected values are guaranteed to exist and node values are unique, encountering both nodes at one level with distinct parents is sufficient and no later tree structure can change the result.

## Complexity detail
Each of the $N$ nodes enters and leaves the queue at most once, giving $O(N)$ time. The widest tree level can contain $O(N)$ nodes, so the queue uses $O(N)$ space.

## Alternatives and edge cases
- **Depth-first search with parent and depth records:** One traversal can locate both nodes and compare the same two attributes; recursion may use $O(N)$ call-stack space in a skewed tree.
- **Materialize every root-to-node path:** Comparing paths reveals depth and parent information, but repeatedly copying long paths can take $O(N^2)$ time on deep trees.
- **Siblings:** Nodes at the same depth are not cousins when their parent is identical.
- **Different depths:** Different parents alone are insufficient; both nodes must also share a depth.
- **Root selected:** The root cannot be a cousin of another node because no other node has depth $0$.
