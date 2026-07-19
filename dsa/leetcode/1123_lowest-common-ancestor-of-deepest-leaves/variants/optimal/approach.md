## General
**Ask each subtree for one complete summary.** A postorder traversal computes two facts for every node: the height of its deepest leaf and the lowest common ancestor of all leaves that reach that height. The empty subtree returns height $0$ and no candidate. A real node combines the already-computed summaries of its left and right children.

**Propagate the uniquely deeper side.** If the left summary has greater height, every deepest leaf below the current node lies in the left subtree. The left candidate therefore remains the answer, and the combined height is one greater. The symmetric rule applies when the right subtree is deeper.

**Join equal-depth sides at the current node.** When the child heights are equal, both sides contain leaves at the same maximum depth. If the height is zero, the current node itself is a leaf; otherwise, deepest leaves occur in both child subtrees. In either case the current node is the deepest node whose subtree contains all of them, so it is exactly their lowest common ancestor. By induction from leaves to the root, the root summary covers every deepest leaf in the whole tree.

## Complexity detail
Each of the $n$ nodes is visited once and performs constant work, giving $O(n)$ time. Postorder recursion holds at most one root-to-leaf path, so auxiliary space is $O(h)$; this is $O(n)$ for a skewed tree and $O(\log n)$ for a height-balanced tree.

## Alternatives and edge cases
- **Breadth-first search plus parent links:** BFS can identify the deepest level, then repeatedly move those nodes to their parents until they meet, but it stores $O(n)$ parent and frontier data.
- **Repeated height computation:** Descending toward the deeper child while recomputing subtree heights is correct, but a skewed tree makes it $O(n^2)$.
- **Singleton tree:** Its root has no children and is both the only deepest leaf and the returned ancestor.
- **One uniquely deepest leaf:** The candidate propagates unchanged from that leaf to the root, so the returned subtree is just that leaf.
- **Deepest leaves on both root sides:** Equal child heights make the root the answer even when shallower leaves occur elsewhere.
