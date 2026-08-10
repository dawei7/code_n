## General

The exact Optimal solution looks downward from a node's parent relationship rather than asking each current node for both ancestors. Its helper `dfs(root, x)` receives:

- `root`, the current node, and
- `x`, the value of the current node's parent.

After recursively processing the current subtree, if `x` is even, the method adds the values of `root`'s children. Those children have `x`'s node as their grandparent: `x` belongs to the parent of `root`, and `root` is their parent.

This is a shifted but valid way to count every node with an even-valued grandparent.

**The empty-subtree base case**

If `root is None`, the subtree contains no nodes and contributes zero. This also lets the parent call recurse on missing children without separate checks around the recursive calls.

The later direct child additions do check `if root.left` and `if root.right` because the code must read a child value only when that child exists.

**Passing the parent value downward**

The recursive calls are:

`dfs(root.left, root.val)` and `dfs(root.right, root.val)`.

For either child, the current `root` becomes its parent, so passing `root.val` preserves the helper's stated meaning.

Suppose the helper is currently at node $P$ with argument `x` equal to $G$'s value, where $G$ is $P$'s parent. Then each child $C$ of $P$ has $G$ as its grandparent. Checking whether `x` is even and adding $C$'s value is exactly the required test for $C$.

**Why the method adds children instead of the current node**

A more common DFS passes both parent and grandparent values and decides whether to add the current node. This exact source passes only the parent value. At the current frame, that is enough to decide the status of the current node's children.

The code first obtains the complete sums from the left and right subtrees:

`ans = dfs(root.left, root.val) + dfs(root.right, root.val)`.

Then, if `x % 2 == 0`, it adds the immediate child values. These child nodes were not already counted by their own recursive frames for this same grandparent condition. Their own frames are responsible for deciding whether to add their children, one generation lower.

Thus, each qualifying node is added exactly once: in the frame belonging to its parent.

**The odd sentinel at the root**

The public method calls `dfs(root, 1)`. The root has no real parent, so the argument is a sentinel rather than an actual tree value.

Choosing odd value one prevents the root frame from adding the root's children. Those children have no grandparent and must not qualify. If an even sentinel were used, the code would incorrectly count them as though a nonexistent grandparent were even.

The root itself is never directly added by any parent frame because it has no parent. That is also correct: it has no grandparent.

**Walking through three generations**

Consider a node $G$ with even value, its child $P$, and $P$'s child $C$.

When recursion enters `dfs(P, G.val)`, the argument `x` is even. After processing deeper descendants, that frame sees child $C$ and adds `C.val`. This matches the fact that $C$'s grandparent is $G$.

If $P$ also has another child, both child values are added. If either child is absent, its check contributes nothing.

If $G$ is odd, the same frame skips both children. Their deeper descendants may still qualify because their own grandparents can have different values; recursive subtree totals remain included regardless of the current parity check.

**Why postorder placement does not double count**

The recursive calls occur before the direct child additions, giving a postorder-style evaluation. This order is not required for the numerical sum because additions commute, but it makes the returned `ans` clearly represent all qualifying nodes below plus any qualifying immediate children.

Subtree calls add nodes based on grandparents within those subtrees. The current frame adds only its own immediate children based on `x`. These responsibility sets do not overlap.

**Why the final sum is correct**

For any non-root node $C$ that has a grandparent $G$, let $P$ be its parent. The call for $P$ receives `x = G.val` by construction. That call adds $C$ exactly when `x` is even, which is exactly when $G$ has an even value.

Nodes without grandparents are the root and its children. The root has no parent frame, and the odd sentinel prevents root children from being added. Therefore, no ineligible top-level node is counted.

Every eligible node is counted once and every ineligible node zero times, so the returned sum is exact.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height.

Every real node is visited once. Its frame performs two recursive calls, one parity test, and at most two child-value additions, all constant work. Time complexity is $O(n)$.

The algorithm allocates no collection proportional to the tree. Its extra storage is the recursion stack, whose depth is $O(h)$. In a balanced tree this is $O(\log n)$; in a completely skewed tree it is $O(n)$. The manifest states the valid worst-case bound $O(n)$.

The constraint allows up to $10^4$ nodes. A skewed tree can exceed Python's default recursion depth even though the asymptotic algorithm is correct. An iterative traversal is safer for full worst-case robustness.

## Alternatives and edge cases

- **Pass parent and grandparent values:** At each node, add its own value when the passed grandparent is even. This is often easier to understand, though it carries one extra scalar argument.
- **BFS and inspect grandchildren:** For every even-valued node, add its existing four possible grandchildren, while a queue visits all nodes. It is iterative and remains $O(n)$.
- **Stack with ancestor values:** An explicit stack storing node, parent value, and grandparent value avoids recursion-limit risk.
- **Single-node tree:** The odd sentinel prevents any addition, recursive child calls return zero, and the answer is zero.
- **Tree with only root and children:** No node has a grandparent, so the answer remains zero.
- **Even-valued root:** Its grandchildren qualify, not its direct children. The root's value is passed into calls for its children, and those frames add the grandchildren.
- **Odd-valued root:** Its grandchildren do not qualify because the child frames receive an odd `x`.
- **Missing child:** Null recursion returns zero, and direct child access is guarded.
- **A node with two even-valued grandparents is impossible:** Every tree node has at most one parent and therefore at most one grandparent, so no duplicate eligibility arises.
- **Positive node values:** The parity test works directly. An arbitrary odd root sentinel is safe because real root-parent data does not exist.
- **Recursion depth:** A skewed tree near 10,000 nodes can fail in Python despite $O(n)$ theoretical stack space; iterative traversal avoids that implementation limit.
- **Postorder versus preorder:** The additions could occur before recursive calls without changing the sum, provided each frame keeps the same responsibility for its children.
