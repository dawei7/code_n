## General
**Carry the only history a child needs**

Whether a path continues at a node depends only on its parent's value and the valid length ending at that parent.
During depth-first traversal, carry those two pieces of state. If `node.val == parent_value + 1`, extend the length;
otherwise start a new path of length one at the node. The candidate's local `TreeNode` annotation makes this stack
state explicit without changing the traversal.

Every node may be the endpoint of the global answer, so update a running maximum after computing its local length.
Then pass the new value and length to both children. An explicit stack avoids recursion-depth limits while holding at
most one pending sibling per level.

**Direction and adjacency are strict**

The path must move from parent to child; a child with value one less does not form a reverse sequence. Values also
cannot skip: `3 -> 5` resets even though it is increasing. Branches are evaluated independently, because a path
cannot travel up from one child and down into its sibling.

For `[3,2,4,1,null,null,5]`, the left edges decrease and reset. The right branch follows `3 -> 4 -> 5`, so the answer is three.

**Why one traversal finds every candidate**

At each node, the carried length is exactly the longest valid consecutive path ending there: there is only one parent,
so it either extends that unique incoming path or begins anew. Taking the maximum of these endpoint lengths considers
every possible downward path, since every such path has a final node.

## Complexity detail
Let $n$ be the number of nodes and $h$ the tree height. Every node is pushed, examined, and popped once, giving
$O(n)$ time. Because the depth-first stack holds at most one pending sibling for each level plus the active branch,
it uses $O(h)$ auxiliary space: $O(n)$ for a skewed tree and $O(\log n)$ for a balanced tree.

## Alternatives and edge cases
- **Start a fresh search from every node:** is correct but revisits long descendant paths and can take $O(n^2)$ on a chain.
- **Inorder or sorted values:** lose parent-child adjacency and cannot establish a valid path.
- **Empty adapter input:** returns zero defensively, although the source contract contains at least one node.
- **Resetting edges:** duplicate, decreasing, or skipped values all start a new length-one path at the child.
