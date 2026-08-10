## General

**A node can be decided only after its descendants are known.**  A node `x` is dominant when its own value equals the maximum value anywhere in the subtree rooted at `x`. That subtree contains:

- the node itself;
- every node in its left subtree;
- every node in its right subtree.

Consequently, the information needed at `x` is just the maximum from each child subtree. Once those two numbers are available, the subtree maximum at `x` is

`max(left_max, right_max, node.val)`.

This naturally calls for a postorder traversal: process the left child, process the right child, and process the current node last.

**Give the recursive function one precise responsibility.**  The nested `dfs(node)` function returns the maximum value in the subtree rooted at `node`. While producing that return value, it also decides whether `node` itself is dominant and, if so, increments the shared counter `ans`.

For a missing child, there is no real node value to contribute. The intended base case returns negative infinity. That sentinel is smaller than every legal `Node.val`, so a missing child can never incorrectly become the maximum of a nonempty subtree.

For a real node, the source performs these steps:

1. recursively obtain `l`, the left-subtree maximum;
2. recursively obtain `r`, the right-subtree maximum;
3. compute `mx = max(l, r, node.val)`;
4. if `mx == node.val`, increment `ans`;
5. return `mx` to the parent.

The comparison deliberately uses equality, not a strict greater-than test. If a descendant has the same maximum value as the current node, then the current node's value is still equal to the maximum in its subtree, so the current node is dominant.

**Why the returned summary is sufficient.**  A parent does not need the complete list of values below either child. It needs only the largest value in each child subtree. The recursive return value discards everything else, but loses no information relevant to the parent's decision.

At a leaf, both recursive child calls reach the missing-child base case. The maximum of negative infinity, negative infinity, and the leaf value is the leaf value itself. Therefore every leaf is counted, as expected: a leaf is the only node in its subtree.

Now consider any internal node after both child calls finish. By the recursive contract, `l` and `r` are the true maxima of the complete left and right subtrees. Taking the maximum of those values and `node.val` therefore gives the true maximum of the current subtree. The equality check counts the node exactly when its value equals that maximum, and the returned `mx` gives the parent the same valid summary. Processing nodes from the leaves upward extends this reasoning to the root.

**Walk through the first example.**  In `[5, 3, 8, 2, 4, 7, 1]`, the leaves `2`, `4`, `7`, and `1` are immediately counted.

- Node `3` receives child maxima `2` and `4`. Its subtree maximum is `4`, so `3` is not counted and returns `4`.
- Node `8` receives `7` and `1`. Its subtree maximum is `8`, so it is counted and returns `8`.
- Root `5` receives `4` and `8`. Its subtree maximum is `8`, so it is not counted.

The four leaves plus node `8` give the answer `5`.

**The complete-tree guarantee controls recursion depth, not the decision rule.**  Completeness does not imply binary-search-tree ordering. A descendant may be larger than its ancestors on either side, so the traversal still must inspect every node. The useful consequence is that a complete tree with `n` nodes has height `O(\log n)`, keeping the recursive call stack shallow.

The outer method initializes `ans = 0`, calls `dfs(root)`, and returns the counter. The nested function declares `nonlocal ans` before changing that outer variable. Although the declaration appears inside the conditional block in the exact source, Python treats `nonlocal` as a declaration for the nested function's scope; the code parses successfully.

**Important defect in the exact stored source.**  The algorithm intends the missing-child branch to return `-inf`, but the file neither imports `inf` from `math` nor defines it. With the platform-provided `TreeNode` type available, calling the method on even a one-node tree reaches a missing child and raises:

`NameError: name 'inf' is not defined`.

Thus the stored source is not independently executable unless its environment injects a name called `inf`. The intended traversal would work if negative infinity were explicitly supplied, for example by importing `inf` or using `float("-inf")`. This approach documents that dependency rather than pretending the exact file already contains the required definition. The commented `TreeNode` declaration is different: that class is intentionally supplied by the LeetCode-style platform harness.

## Complexity detail

Let `n` be the number of nodes. Every real node is visited exactly once. At that visit, the algorithm performs two already-returned recursive calls, one maximum over three values, one comparison, and at most one counter increment.

- Time complexity is `O(n)`.
- Auxiliary space complexity is `O(\log n)` under the stated complete-tree guarantee.

The space bound comes from the recursion stack. A complete binary tree has height `O(\log n)`, so at most that many unfinished calls lie on one root-to-leaf path. No array, map, or per-node result table is retained.

If the same traversal were applied to an arbitrary skewed binary tree, its worst-case recursion depth would be `O(n)`. That does not change the `O(n)` time, but it would change the auxiliary-space bound and could exceed Python's recursion limit. The completeness constraint is therefore material to the manifest's `O(\log n)` space claim.

## Alternatives and edge cases

- **Recompute every subtree separately:** Scanning a node's entire subtree to find its maximum and repeating that work at every node is correct but redundant. On a complete tree it can take `O(n \log n)` time, whereas postorder reuses each child maximum and takes `O(n)`.
- **Return both maximum and count:** Instead of a `nonlocal` counter, `dfs` could return a pair containing the subtree maximum and number of dominant nodes. That is equally asymptotic and can make the data flow more explicit, but it is not the structure used by the exact source.
- **Iterative postorder traversal:** An explicit stack can avoid recursion. It needs a visited marker or another way to recognize when both children have been processed, so it is more verbose while retaining `O(n)` time.
- **Breadth-first traversal:** Level order visits nodes before their descendants' maxima are known. It would need stored per-node information and a later reverse pass, while postorder produces the needed summaries directly.
- **Leaf nodes:** Every leaf is dominant because its subtree contains only itself. The negative-infinity child sentinel makes this fall out of the ordinary logic.
- **Single-node tree:** The answer should be `1`. The intended recurrence obtains that result, but the exact stored file currently raises `NameError` first because `inf` is undefined.
- **Duplicate maximum values:** A node tied with a descendant maximum is dominant. The `mx == node.val` comparison handles ties correctly.
- **Root node:** The root is dominant exactly when its value equals the maximum value in the whole tree.
- **Positive-value constraint:** All values are at least `1`, so a sentinel such as `0` would also be below every legal value. Negative infinity expresses the general intent more clearly, but it must actually be defined.
- **Missing children near the last level:** A complete tree may have absent children only at the end of its last level. The same base case handles all of them without special completeness logic.
- **Not a binary search tree:** Completeness describes shape, not value order. Neither the left nor right subtree can be skipped based on the current value.
- **Undefined `inf` dependency:** The solution explanation and complexity describe the intended Optimal algorithm. They do not erase the exact source defect; a valid execution environment must provide `inf` or the source must be corrected separately.
- **Platform-provided `TreeNode`:** The annotation and child fields rely on the standard harness type. Users are not expected to recreate that helper inside the solution method.
