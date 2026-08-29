## General

**Return presence upward while recording the answer**

The ordinary LCA problem assumes both targets exist. Here, returning one found target is not enough: if the other is absent, the required result is null.

The source makes `dfs` return a Boolean rather than a candidate node. For any subtree, true means that subtree contains at least one of the two target values. The nonlocal variable `ans` is set only when the traversal sees evidence that both distinct targets have been found in the required LCA pattern.

If `root is None`, the subtree contains neither target, so `dfs` returns false.

For a real node, the function recursively evaluates both children first. `l` says whether the left subtree contains a target, and `r` says the same for the right subtree. The postorder order is important because the current node needs complete information from both sides.

**Two ways a node can be the LCA**

The first condition is `l and r`. One target appears in the left subtree and one in the right. Since target values are unique and `p != q`, the current node is their first meeting point and therefore their lowest common ancestor. The source assigns `ans = root`.

The second condition is:

`(l or r) and (root.val == p.val or root.val == q.val)`.

Here, the current node itself is one target and at least one child subtree contains the other. A node is allowed to be its own descendant for LCA purposes, so the current target node is the LCA.

If the current node is a target but neither child contains the other, `ans` is not set. The function still returns true upward, allowing an ancestor or another branch to combine that evidence later.

**What is returned to the parent**

The final Boolean is true when any of these holds:

- the left subtree contains a target,
- the right subtree contains a target,
- the current node's value equals `p.val`,
- the current node's value equals `q.val`.

Thus the presence signal propagates all the way toward the root.

The code compares values rather than object identity. The contract guarantees all tree values are unique, so finding an equal value identifies the intended node unambiguously.

**Why a missing target leaves `ans` null**

If neither target exists, every call returns false and neither assignment condition can hold.

If exactly one target exists, true signals propagate from it through one child at each ancestor. No node has both `l` and `r` true, and no target node has another target in a child. Therefore `ans` remains its initial `None`.

Only evidence of both distinct targets can set the answer, which integrates existence checking into the same traversal.

**Why a deeper answer is not overwritten incorrectly**

Suppose both targets lie in one child subtree. That recursive call discovers their LCA and stores it in `ans`. At every ancestor, only one of `l` and `r` is true, and the ancestor is not a target because both unique targets are below it. Neither assignment condition fires, so the deeper answer remains unchanged.

If targets lie on opposite sides of a node, that node sets `ans`. Higher ancestors again receive presence from only one child and do not overwrite it.


For every subtree, the returned Boolean is true exactly when it contains at least one target, by induction over the postorder traversal.

When both child signals are true, uniqueness means the two targets are separated across the children, so the current node is their LCA. When the current node is a target and a child signal is true, that child contains the other target, so the current node is the LCA. These cover every possible relationship when both targets exist.

The lowest node satisfying one of those patterns sets `ans`, and ancestors cannot replace it. If both targets do not exist, no pattern can occur. Returning `ans` therefore gives the LCA exactly when both nodes are present and null otherwise.

## Complexity detail

Let $n$ be the number of tree nodes and $h$ its height. The traversal visits every node once and performs constant work there, so time complexity is $O(n)$.

The recursive stack follows one root-to-leaf path and uses $O(h)$ space. A balanced tree has $h=O(\log n)$; a skewed tree has $h=O(n)$. Apart from recursion, only constant state and the nonlocal answer reference are stored.

The source deliberately traverses both children even after an answer may have been found because existence evidence is integrated into full postorder processing. This does not change the linear bound.

## Alternatives and edge cases

- **Ordinary LCA plus separate existence checks:** Find a candidate, then search for missing targets as needed. It remains $O(n)$ but may traverse parts of the tree more than once.
- **Return a count and candidate pair:** Each recursion can return how many targets were found and the LCA candidate. This avoids nonlocal state and makes the two-target proof explicit.
- **Parent maps:** Traverse once to record parents and confirm both targets, then walk ancestors. This uses $O(n)$ extra storage rather than $O(h)$ recursion alone.
- **One target is ancestor of the other:** The target node sees the other in a child subtree and becomes `ans`.
- **Targets in opposite subtrees:** Their first split node is assigned.
- **Only one target exists:** Presence propagates, but no two-evidence condition fires, so null is returned.
- **Neither target exists:** Every presence result is false.
- **Root is one target:** If the other exists below, the root satisfies the node-plus-child condition.
- **Unique values:** Value comparison is safe only because duplicates are forbidden.
- **Skewed tree:** Time remains linear, but recursion depth can reach $n$ and may challenge Python's recursion limit at the maximum constraint.
