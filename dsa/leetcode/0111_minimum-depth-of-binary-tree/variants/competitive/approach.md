## General

The competitive solution is a recursive depth-first calculation built around a compact structural rule:

- when both children exist, choose the smaller child depth;
- when at least one child is absent, choose the larger child depth.

Adding one then counts the current node. The switch from `min` to `max` is not a performance trick. It is what preserves the definition of a root-to-leaf path.

**Why zero needs special interpretation**

The base case returns zero for `root is None`. That is the correct answer for an empty input and a convenient value when calculating a leaf. However, a null child of a non-leaf node is not itself a leaf. A path that steps into that null pointer is not a valid root-to-leaf path.

If a node has two real children, each recursive result represents a valid route to some leaf. The shorter route is therefore `min(left_depth, right_depth)`.

If exactly one child exists, the absent side returns zero and the existing side returns a positive depth. Taking `max` discards the invalid zero and selects the only real route. If neither child exists, both recursive calls return zero; `max(0, 0) + 1` correctly gives the leaf depth one.

This explains why the `else` branch handles both one-child nodes and leaves without another condition.

**All structural cases in one expression**

Suppose `root.left` and `root.right` are both truthy. The first branch recursively calculates both depths and returns their smaller value plus one. Both candidates end at real leaves, so choosing the minimum is valid.

Otherwise, one or both child references are absent. The second branch still calls `minDepth` on both. An absent call costs constant time and returns zero. Any real child has minimum depth at least one, so `max` selects it. When both are absent, their tied zeros yield one after adding the current node.

The source tests child references themselves before choosing the operation. It does not try to infer structure from the returned numbers afterward, although that could also be made to work.

**Why the recurrence returns exactly the nearest leaf**

For an empty subtree, zero is correct by contract. For a leaf, the `max` branch returns one. Assume recursive calls return the exact minimum depth of every smaller nonempty subtree.

At a one-child node, every valid path must continue through its sole child, so the child's exact minimum plus one is the current exact minimum. At a two-child node, valid paths split into those beginning left and those beginning right. The best path in each group has the recursively returned depth, and the smaller group minimum is the best overall. This establishes the result at the current node.

Applying that reasoning from leaves upward proves that the root's returned number is precisely the number of nodes on the shortest root-to-leaf path.

**Balanced example**

In `[3,9,20,null,null,15,7]`, each leaf returns one through the `max(0, 0) + 1` case. Node `20` has two children and returns `min(1, 1) + 1 = 2`.

Root `3` also has two children, whose minimum depths are one and two. It returns `min(1, 2) + 1 = 2`, corresponding to the path from `3` to leaf `9`.

**Why a chain does not collapse to depth one**

In `[2,null,3,null,4,null,5,null,6]`, each non-leaf has only a right child. At each such node the left recursion returns zero, while the right recursion returns the positive remaining depth. `max` always selects the right result.

The counts accumulate from leaf `6` upward: one, two, three, four, five. A uniform use of `min` would select zero at the root and incorrectly return one.

**Evaluation behavior and source shape**

In both branches, Python evaluates the two recursive arguments before applying `min` or `max`. The method therefore explores both real subtrees of a two-child node. At a one-child node it also invokes the method on `None`, but that call returns immediately.

Each real node belongs to exactly one recursive subtree, so the compact recurrence does not duplicate substantive work. It uses no cache because a tree node has a unique parent under the contract.

The source defines a conventional `TreeNode`, but `minDepth` only needs objects exposing `left` and `right`. It ignores `val` and performs no mutation.

## Complexity detail

Let $n$ be the number of real nodes. Every node causes one method call and constant local work, while null-child calls are proportional to the number of child positions. Total worst-case time is $O(n)$.

Let $h$ be the tree's maximum root-to-leaf node count. The deepest chain of simultaneous recursive calls is $h$, so auxiliary stack space is $O(h)$. This is $O(\log n)$ for a balanced tree and $O(n)$ for a skewed tree.

The source header correctly states $O(h)$ space. The branch manifest instead states $O(w)$, the maximum-width queue bound associated with BFS. No queue is present here, so $O(w)$ is not the exact selected source's space complexity.

The difference is especially visible for a chain: $w=1$ but recursion holds up to $n$ active frames. The answer itself is one integer and needs constant output space.

## Alternatives and edge cases

- **Explicit missing-child branches:** Check left absence and right absence separately, then use `min` only when both exist. It is longer but makes the invalid-zero issue immediately visible.
- **Breadth-first search:** The first leaf encountered in level order has minimum depth. This can stop before visiting deeper nodes and uses $O(w)$ queue space.
- **Iterative DFS with depths:** Store `(node, depth)` pairs and track the smallest leaf depth. It avoids call-stack overflow but may retain up to $O(h)$ or more explicit entries depending on traversal order.
- **Infinity for nonexistent routes:** Assign infinity to an absent child when the current node is nonempty, allowing `min` to ignore it. Care is needed to return zero for a completely empty tree.
- **Always using `min`:** Incorrect for any node with exactly one real child.
- **Always using `max`:** Correct for chains and leaves but wrong when two children exist and one reaches a nearer leaf.
- **Empty tree:** The initial base case returns zero.
- **Leaf:** Both child calls return zero, and the `max` branch returns one.
- **Only a left child:** `max(positive, 0)` follows the left path.
- **Only a right child:** `max(0, positive)` follows the right path.
- **Both children:** `min` selects the nearer genuine leaf.
- **Tree values:** They never enter the calculation; only child links determine depth.
- **Very deep input:** The $10^5$-node constraint greatly exceeds Python's default recursion limit for a chain, so an iterative method is safer for the full legal domain.
- **No short-circuit between two children:** Both depths must normally be known before their minimum can be selected. BFS is preferable when early discovery of a shallow leaf is valuable.
- **Height versus width:** The source's call stack is governed by $h$, not $w$; keep that distinction when reporting space.
