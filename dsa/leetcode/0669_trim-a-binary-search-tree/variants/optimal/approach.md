## General

**Use the ordering guarantee to discard whole regions**

In a binary search tree, every value in a node's left subtree is smaller than the node's value, and every value in its right subtree is larger. That ordering lets the algorithm decide that an entire side cannot contain any valid answer.

The helper `dfs(root)` returns the correctly trimmed version of the subtree rooted at `root`. Its return value may be:

- the same root after its children are trimmed;
- a descendant that replaces an out-of-range root;
- `None` when no value in that subtree survives.

**Empty subtree**

If `root is None`, there is nothing to keep or trim, so the helper returns `None`. The exact code returns `root` itself, which is the same null value.

**Root is above the upper boundary**

If `root.val > high`, the root must be removed.

Every node in its right subtree is even larger than `root.val`, so every one of those nodes is also above `high`. The right subtree can be discarded without visiting it.

Only the left subtree might contain values within `[low, high]`. The trimmed result for the current subtree is therefore:

`dfs(root.left)`.

Returning that recursive result directly also allows a valid left descendant to become the new subtree root.

**Root is below the lower boundary**

If `root.val < low`, the symmetric argument applies. The root and its entire left subtree are too small. Only the right subtree may contain valid values, so the helper returns:

`dfs(root.right)`.

**Root lies inside the interval**

When `low <= root.val <= high`, the root must remain. Its left and right subtrees may still contain out-of-range nodes, so both are trimmed recursively:

- replace `root.left` with `dfs(root.left)`;
- replace `root.right` with `dfs(root.right)`.

Then return `root`.

These assignments reconnect surviving descendants around nodes that were removed. No new TreeNode objects are necessary.

**Why relative descendant structure is preserved**

The method never moves a node from one original branch to another. When an out-of-range node is removed, it returns the only side that could contain valid nodes. That surviving side was already a descendant of the removed node.

When an in-range node remains, its trimmed left and right results come from its original left and right subtrees. Thus every retained ancestor-descendant relationship remains consistent with the original tree.

**A root-replacement example**

Suppose the root value is zero and `low = 1`. Zero is too small. The entire left subtree is smaller still and cannot survive, so the method trims the right subtree and returns its result.

The returned root may be the original right child or a deeper right descendant if that child is also below one. This is why the public method returns the helper result rather than assuming the original root remains.

**Why boundaries are inclusive**

A node equal to `low` or `high` enters the in-range branch because the rejection tests use strict `<` and `>`. It remains in the tree, as required by the closed interval.

Its ordering can still prune descendants naturally. For example, a node equal to `low` cannot have a valid smaller left descendant, but the recursive call will remove those nodes.

**Why the recursion is correct**

Use structural induction on the subtree.

The null case is correct. For a node above `high`, BST ordering proves the root and entire right subtree are invalid, so the unique possible answer lies in the left subtree; the recursive result is correct by induction. The below-`low` case is symmetric.

For an in-range root, correctness requires keeping it and independently trimming both child subtrees. The induction assumption makes each returned child correct, and reconnecting them to the retained root yields exactly all valid nodes in their original relative structure.

These cases cover every node value, so the top-level return is the unique trimmed BST.

**The operation mutates surviving nodes**

The exact implementation rewrites `left` and `right` pointers on nodes that remain. Removed nodes become unreachable from the returned root, but they are not explicitly destroyed.

This is appropriate for the judge. A caller holding separate references to original nodes may observe changed child links.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height.

Each visited node performs constant work. No node is visited more than once, so worst-case time is `O(N)`. BST pruning may skip large invalid subtrees and make actual work smaller.

The recursive call stack follows one tree path at a time, using `O(H)` space. A balanced BST has `H = O(log N)`, while a skewed BST can have `H = O(N)`.

No new tree proportional to input size is allocated; the existing nodes are relinked. With up to ten thousand nodes, a skewed tree can exceed Python's default recursion depth despite the correct asymptotic bound.

## Alternatives and edge cases

- **Iterative trimming:** First move the root into range, then repair left and right boundary chains with loops. This avoids recursion limits but requires careful pointer updates.

- **Traverse every node without BST pruning:** It can still filter values in `O(N)` time, but it misses the main ordering advantage and complicates valid reconnection.

- **Build a new tree:** Copy retained nodes into new objects to preserve the original tree. This uses `O(N)` additional allocation.

- **Treat the tree as a sorted list:** Inorder filtering loses the original relative tree structure unless a reconstruction rule is added, which would not necessarily produce the required unique result.

- **All nodes inside the interval:** Every node is visited, child pointers are reassigned to equivalent results, and the original root is returned.

- **All nodes below `low`:** Recursion follows rightward possibilities until no valid node remains, returning `None`.

- **All nodes above `high`:** The symmetric leftward search returns `None`.

- **Original root removed:** A valid descendant can become the new root, so callers must use the returned value.

- **Value equals a boundary:** It is retained because the interval is inclusive.

- **Single-node tree:** It is returned if in range and `None` otherwise.

- **Unique values:** The contract avoids duplicate-key ordering ambiguity. The pruning reasoning relies on the BST's strict ordering.

- **Deeply skewed tree:** An iterative version may be necessary to avoid Python recursion failure at the maximum node count.

- **External references:** The method mutates child links in place. References outside the returned root may still point to removed or modified nodes.
