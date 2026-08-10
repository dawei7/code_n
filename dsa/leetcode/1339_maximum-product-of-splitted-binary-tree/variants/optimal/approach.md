## General

Removing one edge from a tree produces exactly two components. If the lower endpoint of the removed edge roots a subtree with sum `t` and the sum of the entire original tree is `s`, then the other component contains every remaining node and has sum `s - t`. The product for that cut is therefore

$$
t(s-t).
$$

Every removable edge corresponds to one non-root node: choose that node as the root of the component below the edge to its parent. This reduces the task to finding every non-root subtree sum and maximizing the formula above.

The checked-in implementation performs two postorder depth-first traversals. The first obtains the fixed total `s`. The second recomputes subtree sums and evaluates the possible cut above each non-root subtree.

**First traversal: obtain the whole-tree sum**

The nested function named `sum` returns zero for a missing child. For a real node, it recursively obtains the left and right subtree sums and returns
`root.val + sum(root.left) + sum(root.right)`.

This is postorder evaluation: children are completely summed before their parent. By induction from the null-child base case, the value returned at every node is exactly the sum of all nodes in that node’s subtree. Calling `sum(root)` therefore assigns the entire tree’s sum to `s`.

The helper’s name shadows Python’s built-in `sum` only inside `maxProduct`. Recursive calls resolve to the nested helper, which is intentional.

**Second traversal: treat every child subtree as a cut**

The function `dfs` has the same postorder shape. Once both recursive calls return, `t = root.val + dfs(root.left) + dfs(root.right)` is the exact sum of the subtree rooted at the current node.

For every proper subtree, cutting its incoming parent edge creates components with sums `t` and `s - t`. The line `ans = max(ans, t * (s - t))` compares that cut’s product with the best product seen earlier. `ans` and `s` belong to the enclosing function, so `nonlocal ans, s` permits the helper to read the total and update the running maximum.

The condition `if t < s` excludes the full tree. The original root has `t == s` and has no parent edge to remove, so treating it as a candidate would describe an illegal cut with an empty second component. All node values are strictly positive. Therefore, every proper subtree omits at least one positive-valued node and has `t < s`, so the condition excludes only the root and keeps every legal cut.

This establishes complete coverage. Each non-root node contributes the cut above it exactly once when its `dfs` call finishes. No other cut exists in a tree, because each edge connects one child-rooted subtree to the rest. For that cut, `s - t` is exactly the complementary component sum. Taking the maximum over these products therefore yields the required unmodded optimum.

**Delay the modulus until selection is finished**

The method computes all products as ordinary Python integers and applies `ans % mod` only at the return, where `mod = 10**9 + 7`. This order is mandatory. Modular reduction does not preserve numerical ordering: a larger product can have a smaller remainder than a smaller product. Reducing each candidate before comparing could select the wrong edge.

Python integers expand to hold the needed product, so multiplication does not overflow. In a fixed-width language, the total fits within ordinary bounds described by the constraints, but the product needs a sufficiently wide integer type.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height.

The `sum` traversal visits every real node once and performs constant work per node, so it takes $O(n)$ time. The `dfs` traversal independently visits every node once and also performs constant work per node. Two linear passes still total $O(n)$ time.

Each traversal uses recursion frames proportional to the current root-to-leaf path, so auxiliary space is $O(h)$. The first traversal’s frames are gone before the second begins; their storage does not add across passes. A balanced tree has $h = O(\log n)$, while a completely skewed tree has $h = O(n)$. The worst-case auxiliary-space bound is therefore $O(n)$.

The solution does not store all subtree sums in a list. Apart from recursion, it keeps only `s`, `ans`, `mod`, and per-call scalar totals. Python’s arbitrary-precision integers can use more than constant machine words as values grow, but standard algorithm analysis treats arithmetic on the constraint-bounded values as constant-time.

The source is recursive, and the constraints allow a highly skewed tree with up to fifty thousand nodes. A Python runtime with its usual recursion limit may raise `RecursionError` before reaching that depth. The asymptotic algorithm remains linear, but exact runtime robustness on the maximum-height input depends on the harness increasing the recursion limit or replacing recursion with an explicit stack.

## Alternatives and edge cases

- **One traversal plus stored sums:** A single postorder pass can append every subtree sum to a list, after which a linear scan evaluates products using the returned total. It has the same $O(n)$ time and $O(n)$ space but stores all sums explicitly.
- **Iterative postorder:** Use an explicit stack and a map or visitation state to compute subtree sums without Python recursion. It preserves $O(n)$ time and handles a height-$n$ tree without relying on the interpreter’s recursion limit.
- **Searching for the sum nearest half:** For fixed `s`, the product `t(s - t)` is largest when `t` is closest to `s / 2`. This viewpoint is valid, but every subtree sum still has to be generated, so it does not improve the linear time bound.
- **Recomputing the complement directly:** Physically removing each edge and summing both resulting trees would revisit nodes for many cuts and can become quadratic. Using `s - t` makes every complement calculation constant-time.
- **Modulo during comparison:** This is incorrect because remainder order can differ from original product order. Maximize first and reduce only the final `ans`.
- **Original root:** Its subtree is the entire tree and no edge exists above it. The `t < s` test prevents considering that illegal split.
- **Positive node values:** Strict positivity guarantees every proper subtree has sum below `s`. If zero or negative values were allowed, `t < s` would no longer be a reliable root test.
- **Two-node tree:** There is exactly one edge and therefore one legal product. The child subtree is evaluated, while the root is skipped.
- **Balanced tree:** Recursion consumes $O(\log n)$ frames even though the reported worst-case space is $O(n)$.
- **Skewed tree:** The logical algorithm still visits each node twice, but recursion depth becomes $n$ and may exceed Python’s configured limit.
- **Large product:** Python avoids overflow automatically. Fixed-width implementations should multiply using a type wide enough for the unmodded product.
- **Null child:** Both helpers return zero, which is the additive identity and lets leaves be handled by the same recurrence as internal nodes.
