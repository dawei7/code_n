## General

**Insertion changes edges, not merely node values.** At target depth `depth`, every existing node one level above must receive two new children with value `val`. The old left subtree must remain on the left side, below the new left node. The old right subtree must remain on the right side, below the new right node. The exact recursive solution navigates to those parent nodes and rewires their child references in place.

**Handle depth 1 before ordinary traversal.** There is no parent at depth 0. When `depth == 1`, the method creates `TreeNode(val, root)` and returns it immediately. Under the platform's constructor order, the second argument is the new node's left child, so the original root becomes the left subtree. The right child keeps its default `None` value. This exactly follows the special root rule.

This branch must be separate. The helper begins at the existing root at depth 1 and searches for nodes at `depth - 1`. If the requested depth itself is 1, that parent depth would be 0 and cannot be reached by descending the tree.

**Give the helper a precise meaning.** `dfs(root, d)` means: process the non-null node referenced by `root`, knowing that its current depth is `d`. The initial call `dfs(root, 1)` is correct because the statement defines the original root's depth as 1.

If `root is None`, there is no node and no descendant branch to process, so the helper returns. Otherwise it asks whether `d == depth - 1`. This is the only level whose outgoing edges must change.

**Rewire the left side correctly.** At an insertion parent, the assignment

`root.left = TreeNode(val, root.left, None)`

creates a new node whose value is `val`, whose left child is the parent's original left subtree, and whose right child is `None`. Python evaluates the entire right-hand side before assigning it to `root.left`. Therefore, the `root.left` passed into the constructor is still the original child; it is not the new node being assigned.

**Rewire the right side symmetrically but with the opposite child slot.** The assignment

`root.right = TreeNode(val, None, root.right)`

creates the new right child. Its left pointer is `None`, while its right pointer receives the parent's original right subtree. The asymmetry is intentional: old left content stays below a left edge, and old right content stays below a right edge.

After both assignments, the helper returns immediately. It must not recurse into the new nodes. The requested row has already been installed, and descending through it could insert extra rows or interpret newly shifted subtrees at the wrong depth.

**Continue only while above the parent level.** If the current depth is less than `depth - 1`, the helper calls itself for `root.left` and `root.right` with `d + 1`. Depth-first order does not affect the result because each insertion parent is changed independently.

For Example 1, `depth = 2`. The root is already at depth 1, which equals `depth - 1`. Two new value-1 nodes become its children. The original subtree rooted at 2 becomes the left child of the new left node, and the original subtree rooted at 6 becomes the right child of the new right node.

For `depth = 3`, traversal first visits the depth-1 root, then descends to every existing node at depth 2. Each such node gets two new children. If one original child is missing, the corresponding new node is still created; its preserved child pointer is simply `None`. Thus “add one row” creates both new positions below every non-null parent at the preceding depth.

**Why the result is correct.** For depth 1, the special branch directly constructs the required new root. For a larger target, the DFS reaches every non-null node at depth `depth - 1` because it explores both child branches from the root. At each such node, it creates exactly two value-`val` children and places the old left and right subtrees in precisely the required outer positions. It changes no other edge above that level and stops before altering descendants. Therefore, every required new node is present, every original subtree is retained, and no extra insertion occurs.

## Complexity detail

Let $N$ be the original number of nodes, let $V$ be the number of nodes visited through depth `depth - 1`, let $P$ be the number of non-null parents at that insertion level, and let $H$ be the greatest recursion depth reached. The helper processes each visited node once and creates two nodes for each of the $P$ parents, so time is $O(V+P)$, which is $O(N)$ in the worst case.

The exact Python source is recursive DFS. Its active call stack is $O(H)$: $O(\log N)$ for a balanced traversal to a moderate depth and $O(N)$ for a skewed tree. It also allocates $2P$ required output nodes. The manifest lists $O(W)$ auxiliary space, where $W$ is a level width; that bound describes the editorial's BFS queue, not this exact DFS. The honest live auxiliary bound for this source is $O(H)$, excluding the required output nodes.

With a possible tree depth of $10^4$, Python's default recursion limit can be exceeded on a skewed input. An iterative traversal avoids that runtime risk while preserving the same asymptotic time.

## Alternatives and edge cases

- **Breadth-first search:** Advance a queue level by level and stop at `depth - 1`. It mirrors the row concept directly and uses $O(W)$ queue space, matching the manifest's stated auxiliary symbol.
- **Iterative DFS stack:** Store each node with its depth. This avoids recursion-limit failure and uses space proportional to the explicit frontier.
- **Depth 1:** Return a new root with the complete original tree as its left child; do not run ordinary insertion logic.
- **Target depth 2:** Only the original root is modified, and two new children are created immediately.
- **Target one beyond the tree depth:** The deepest leaves are the insertion parents, so each receives two new leaf children.
- **Missing original left child:** A new left node is still created with `None` as its left subtree.
- **Missing original right child:** A new right node is still created with `None` as its right subtree.
- **Negative `val`:** Node construction is unchanged; the insertion logic depends only on structure.
- **Stop after insertion:** Recursing below a modified parent would process the new row and can produce incorrect duplicate insertion.
- **RHS evaluation order:** The old child reference is captured while constructing the new node before the assignment overwrites `root.left` or `root.right`.
- **Very deep skewed tree:** The algorithm is logically correct but recursive Python may raise `RecursionError`; an explicit stack is safer at the maximum constraint.
