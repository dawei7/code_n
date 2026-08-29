## General

**A leaf’s value depends on how its parent reaches it**

A leaf is any node with no children, but only a leaf reached through a parent’s left edge contributes. Looking at a node in isolation tells whether it is a leaf, but not whether it is a left child unless parent-side information is carried along.

The exact solution avoids an extra Boolean parameter by making each node inspect its own left child. A parent knows unambiguously that `root.left`, when present, is on a left edge. It can decide immediately whether that child is a leaf and either add its value or recurse into its subtree.

The right subtree is always recursively processed because it may contain left leaves deeper inside, even though its own root is a right child.

**The empty-tree base case**

If `root is None`, the subtree has no leaves and contributes zero. This base case allows the method to call itself on `root.right` without first checking whether the right child exists.

Although the package contract supplies a nonempty tree, supporting `None` makes the recursion complete and simplifies child handling.

**Process the entire right subtree first**

The line

```text
ans = self.sumOfLeftLeaves(root.right)
```

computes the contribution of every left leaf inside the right subtree. It does not add the right child merely because that child might be a leaf. If `root.right` itself is a leaf, its recursive call finds no left child and returns zero, which is correct because it is a right leaf.

Traversal order does not affect a sum. Processing the right subtree before the left is unusual but fully valid.

**Inspect the immediate left child**

If `root.left` exists, there are two cases.

If it has no children, it is a left leaf by definition, so the method adds `root.left.val` directly. It does not recurse into that node because a leaf has no descendants that could contribute.

If it has at least one child, it is not a leaf. Its own value must not be added, but its subtree may contain left leaves, so the method recursively adds `self.sumOfLeftLeaves(root.left)`.

These cases ensure every left edge is classified by its parent.

**Understanding the exact leaf test**

The source tests

```text
root.left.left == root.left.right
```

instead of writing both child comparisons explicitly.

For the platform-provided `TreeNode`, a valid leaf has `left is None` and `right is None`, so the two fields compare equal. A non-leaf in a proper binary tree has at least one non-`None` child; its left and right fields do not compare equal under the ordinary identity-based node semantics.

The intended condition is therefore equivalent to:

```text
root.left.left is None and root.left.right is None
```

The explicit form is generally clearer and safer in production code. The exact shorthand relies on the valid-tree contract and the platform node type not defining structural equality that could make two distinct child subtrees compare equal.

**Tracing the example tree**

For level-order tree `[3,9,20,null,null,15,7]`:

- At root `3`, the method first processes right subtree rooted at `20`.
- At node `20`, the right subtree rooted at leaf `7` contributes zero because `7` is a right child and has no left child.
- Node `20` inspects its left child `15`. Both children of `15` are `None`, so `15` is added.
- Back at root `3`, left child `9` is also a leaf, so `9` is added directly.

The total is `15 + 9 = 24`. Leaf `7` is correctly excluded.

**Why the root is never counted merely for being a leaf**

A one-node tree has a root that is a leaf, but it is not the left child of another node. The method never tests `root` itself as a contribution. It starts with the right-subtree sum and only adds `root.left`, so a lone root returns zero.

This distinction is central: “leaf” alone is not sufficient; the node must also have a parent whose left pointer refers to it.

**Subtree meaning and correctness**

For any node `root`, the method returns the sum of all nodes inside that subtree that are left leaves relative to their parents in the same tree.

The empty subtree returns zero. For a nonempty root, the recursive right call correctly sums all qualifying nodes in the right subtree by induction. If the immediate left child is a leaf, adding it accounts for the only qualifying node at that left edge; it has no deeper nodes. If it is not a leaf, recursion correctly sums all qualifying nodes below it, while not adding the non-leaf child itself.

The left and right regions are disjoint, and every possible left leaf belongs either to the immediate-left-leaf case or to one of the recursively processed subtrees. Therefore each qualifying value is added exactly once and no right leaf or internal node is added.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height.

Every internal node and right leaf is the root of one recursive call. A left leaf may be recognized by its parent without receiving its own call, but it is still inspected once. No node or edge is processed more than a constant number of times, so total time is $O(n)$.

The algorithm allocates no explicit collection. Recursive calls occupy one frame per node along the active traversal path, so auxiliary space is $O(h)$. For a balanced tree, $h=O(\log n)$; for a completely skewed tree, $h=O(n)$. This matches the height-sensitive manifest bound.

The returned sum is a scalar. Node values may be negative, and ordinary addition handles them; initializing empty contributions to zero is still the correct additive identity.

## Alternatives and edge cases

- **Recursive traversal with `is_left` flag:** Pass whether the current node came from a left edge. At a leaf, return its value only when the flag is true. This is more explicit and has the same $O(n)$ time and $O(h)$ stack space.

- **Iterative depth-first search:** Store `(node, is_left)` pairs in a stack. It avoids recursion limits and uses $O(h)$ space in typical depth-first traversal, with $O(n)$ worst-case stack size depending on shape.

- **Breadth-first search:** A queue can inspect every parent’s left child. It is correct but may store an entire wide level, using $O(w)$ space for maximum width.

- **Morris traversal:** Temporary threaded links can achieve $O(1)$ auxiliary space while restoring the tree afterward, but the method is substantially more complex and mutates the tree during traversal.

- **Single-node tree:** The root is a leaf but not a left child, so the result is zero.

- **Only a right leaf:** The recursive right call returns zero, correctly excluding it.

- **Only a left leaf:** The parent recognizes it and adds its value directly.

- **Left child is internal:** Its value is not added; recursion searches its descendants for actual left leaves.

- **Negative left-leaf values:** They decrease the sum as required. The task asks for arithmetic sum, not a nonnegative maximum.

- **Empty root:** The exact base case returns zero even though normal inputs are nonempty.

- **Equality shorthand:** `left.left == left.right` is correct for the supplied ordinary tree nodes and valid tree structure, but explicit `is None` checks communicate the leaf condition more robustly.

- **Deep skewed tree:** Mathematical space is $O(h)$, and a chain near the constraint limit can approach Python’s recursion limit. An iterative stack avoids that runtime concern.
