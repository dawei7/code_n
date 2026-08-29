## General

**A parent needs a compact summary of each child subtree**

To decide whether a subtree rooted at one node is a binary search tree, inspecting only the two child values is insufficient. Every value in the left subtree must be smaller than the root, and every value in the right subtree must be greater. A postorder DFS solves the children first and returns four facts about each entire subtree:

1. Whether it is a BST.
2. Its minimum value.
3. Its maximum value.
4. The sum of all its node values.

The exact tuple order is `(is_bst, minimum, maximum, sum)`. Once both child tuples are known, the parent can validate, total, and summarize its own subtree in constant time.

**Why the empty-subtree tuple uses infinities**

For `None`, the helper returns `(1, inf, -inf, 0)`. An empty tree is treated as a valid BST and has sum zero. Its boundary values are deliberately reversed neutral sentinels.

If there is no left child, its maximum is negative infinity, so `lmx < root.val` is automatically true. If there is no right child, its minimum is positive infinity, so `root.val < rmi` is automatically true. This lets leaf nodes pass the same condition as all other nodes without separate cases.

For a leaf, both children are empty. The test becomes negative infinity less than the leaf value less than positive infinity. Its sum is its own value, and its returned minimum and maximum both become that value.

**The exact BST test**

After recursively obtaining both summaries, the current subtree is valid only when:

- `lbst` says the complete left subtree is a BST.
- `rbst` says the complete right subtree is a BST.
- `lmx < root.val` says every left value is strictly smaller.
- `root.val < rmi` says every right value is strictly greater.

The inequalities are strict, so duplicate keys on either side invalidate the current subtree, exactly matching the stated BST definition. Checking only the immediate child values would miss a deeper violation, such as a large value hidden inside the left subtree. The returned extrema prevent that error.

**What happens for a valid subtree**

Its total is `s = ls + rs + root.val`. The global `ans` is updated with this candidate because every valid BST subtree is eligible. The helper then returns a valid flag, the new minimum, the new maximum, and `s`.

`min(lmi, root.val)` handles an empty left child whose minimum is positive infinity and otherwise preserves the left subtree's smallest value. `max(rmx, root.val)` symmetrically handles the right side. Since validity already proves the ordering, these expressions summarize the complete current subtree correctly.

**What happens for an invalid subtree**

The helper returns `(0, 0, 0, 0)`. The numeric fields are meaningless placeholders. This is safe because a parent first requires the child BST flag. If it is false, short-circuit evaluation prevents that invalid child's extrema from making the combined condition succeed.

An invalid larger subtree may still contain a valid descendant BST. That descendant was processed earlier in postorder and already updated `ans`, so discarding the invalid subtree's sum does not lose a candidate.

**Why the answer begins at zero**

Node values may be negative. The problem's expected convention allows the empty BST with sum zero, so a negative valid subtree should not force a negative answer. Initializing `ans = 0` and applying `max` ensures all-negative trees return zero, while any positive-sum BST replaces it.

**Why the algorithm is correct**

By induction on subtree size, the empty tuple correctly summarizes an empty BST. Assume both child calls return correct summaries. The current test requires valid child BSTs and exactly the boundary inequalities needed for all left keys to be below the root and all right keys above it; therefore it accepts exactly the BST subtrees. When accepted, adding the child sums and root value gives the exact sum, and the returned extrema are correct. When rejected, the false flag correctly prevents ancestors from treating this subtree as a BST.

Every subtree is evaluated once at its root. Every valid one updates `ans` with its exact sum, while no invalid one does. Starting from zero also considers the allowed empty choice. Consequently, the final maximum is exactly the requested maximum BST-subtree sum.

## Complexity detail

Let $N$ be the number of nodes and $H$ the tree height. Each node is visited once, combines two fixed-size tuples, and performs constant arithmetic and comparisons. Time is $O(N)$.

The active recursion stack is $O(H)$. No table is retained after child summaries are combined. The manifest states $O(N)$ space, which is a correct worst-case bound because a skewed tree has $H=N$; the sharper shape-sensitive bound is $O(H)$.

## Alternatives and edge cases

- **Validate every subtree independently:** Run a BST check and sum traversal from every node. It is conceptually direct but repeats descendants and can cost $O(N^2)$.
- **Inorder-only reasoning:** An inorder traversal identifies whether one whole tree is a BST, but finding the best among all overlapping subtrees still needs boundary and sum information per subtree.
- **Iterative postorder:** Explicitly store traversal state and computed summaries. It avoids recursion limits but requires a map from nodes to tuples.
- **Leaf node:** Empty-child sentinels make it a valid one-node BST automatically.
- **All negative values:** `ans` stays zero, representing the allowed empty BST.
- **Duplicate value:** Strict inequalities reject a duplicate on either side.
- **Deep boundary violation:** Returned subtree minima and maxima expose it even when immediate parent-child values look valid.
- **Invalid child:** Its false flag blocks the parent; placeholder zeros are never trusted as real boundaries.
- **Valid descendant inside invalid parent:** Postorder updates the answer before the invalid parent is rejected.
- **Null root outside the contract:** The DFS returns the empty summary and the answer remains zero.
- **Recursion depth:** Up to 40,000 nodes can form a skewed tree and exceed Python's default recursion limit; iterative postorder avoids that runtime risk.
- **Infinity names:** The execution environment must provide `inf`, commonly from `math`.
