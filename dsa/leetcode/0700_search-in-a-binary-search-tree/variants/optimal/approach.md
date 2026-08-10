## General

A binary search tree provides more information than an arbitrary binary tree:

- every value in a node's left subtree is smaller than that node's value;
- every value in its right subtree is larger.

The exact recursive solution uses this ordering to choose only one child at each node. It returns the actual node whose value matches `val`, which is also the root reference of the requested subtree.

**The recursive stopping conditions**

The first condition is:

`if root is None or root.val == val: return root`.

If `root is None`, the chosen search path has fallen beyond a leaf. No node with the target value exists on that path, and because BST ordering ruled out every unchosen branch, the value is absent from the whole tree. Returning `None` matches the required null result.

If `root.val == val`, the search is complete. Returning `root` rather than `root.val` is important: the caller needs the entire subtree rooted at that node, including its existing left and right descendants.

**Choosing the only possible branch**

If the target is smaller than `root.val`, the BST property guarantees that every value in the right subtree is greater than `root.val` and therefore also greater than the target. The target, if present, can only be in the left subtree.

If the target is greater than `root.val`, every value in the left subtree is smaller than `root.val` and cannot equal the target. Only the right subtree remains possible.

The conditional expression implements exactly this choice:

`self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)`.

Rewriting `root.val > val` as `val < root.val` gives the familiar BST comparison. Equality was already handled by the base case, so the `else` branch means strictly greater target.

**Why the discarded subtree never needs exploration**

At each node, the BST invariant applies to every descendant in each subtree, not just the immediate child.

When `val < root.val`, no node anywhere in the right subtree can equal `val`. Searching it would be provably useless. The same symmetric argument holds for the left subtree when `val > root.val`.

This is what makes BST search different from a general binary-tree traversal, which might need to inspect both children.

**A successful trace**

For a tree rooted at `4` with children `2` and `7`, searching for `2` proceeds as follows:

- At `4`, the target is smaller, so recurse only into the left subtree.
- At `2`, `root.val == val`, so return that node.
- The returned object is the root of the subtree containing `2` and its descendants, such as `1` and `3`.

No copy of the subtree is built. The original node reference is returned.

**An unsuccessful trace**

Using the same tree, search for `5`:

- `5 > 4`, so move right to `7`.
- `5 < 7`, so move left.
- If `7` has no left child, the next call receives `None` and returns it.

The left subtree of `4` and right subtree of `7` are skipped because their value ranges cannot contain `5`.

**The recursive invariant**

At the beginning of `searchBST(root, val)`:

> If a node with value `val` exists in the original tree, it lies inside the subtree rooted at `root`.

The invariant is true for the initial call because `root` is the full tree.

At a nonmatching node, the comparison and BST ordering identify the only child subtree that could contain `val`. Recursing into that child preserves the invariant. Returning `None` at an empty subtree proves no candidate remains; returning a matching node gives the required object.

**Why the method terminates**

Each recursive call moves from a node to one of its children, strictly one level lower. A finite tree cannot contain an infinite downward path. The search must therefore reach either a matching node or `None`.

**Why the returned result is correct**

If the method returns a non-null node, it did so only after checking `root.val == val`, so that node is a valid answer and its reference exposes exactly the rooted subtree requested.

If it returns null, the recursive path ended without a match. At every earlier comparison, the discarded subtree's entire value range excluded `val`. Therefore, no unsearched node could match, and null is correct.

This proves both successful and unsuccessful outcomes.

## Complexity detail

Let `H` be the height of the BST, measured as the maximum number of nodes on a root-to-leaf search path.

The algorithm visits at most one node per level, performing constant work at each. Its time complexity is

$$
O(H).
$$

For a balanced BST, `H = O(\log N)`, so search is logarithmic. For a completely skewed BST, `H = O(N)` and the worst-case time is linear.

The exact implementation is recursive. It keeps one stack frame per visited level until the result returns, so its auxiliary space is

$$
O(H).
$$

An iterative version can perform the same one-branch walk with `O(1)` auxiliary space. The constant-space bound does not apply to this literal recursive source.

## Alternatives and edge cases

- **Iterative BST search:** Keep a current node in a loop and replace it with the left or right child after each comparison. It retains `O(H)` time and reduces auxiliary space to `O(1)`.

- **General DFS:** Searching both children works even without BST ordering but can visit `O(N)` nodes unnecessarily.

- **Balanced tree:** Search follows only `O(\log N)` levels.

- **Skewed tree:** The tree behaves like a linked list, giving `O(N)` time and recursion depth.

- **Target at the root:** The first base-case check returns immediately.

- **Target at a leaf:** Comparisons guide the search down to the leaf, which is returned with null children as its subtree.

- **Missing target:** The selected path ends at `None` and returns null.

- **Return node, not value:** Returning `root.val` would violate the contract because descendants of the matching node must remain accessible.

- **No subtree copy:** The returned node belongs to the original tree. Mutating it later would mutate that tree.

- **Strict BST ordering:** The branch proof assumes left values are smaller and right values larger. An arbitrary binary tree would require a different search.

- **One-node tree:** A matching target returns the root; any other target recurses once to a null child and returns null.

- **Recursion depth risk:** A highly skewed tree with thousands of nodes can exceed Python's recursion limit. The iterative alternative is operationally safer while preserving the algorithm.
