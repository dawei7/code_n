## General

**One maximum is not enough for a subtree.**

Whether a child may be robbed depends on whether its parent is robbed. If a recursive helper returned only the single best amount from a subtree, the parent would not know whether that amount included the child root. It could accidentally combine two directly linked robbed houses.

The exact source solves this by returning two values for every node. For a subtree rooted at `root`, `dfs(root)` returns

$$
(\text{take},\text{skip}),
$$

where:

- `take` is the maximum money obtainable from the complete subtree when `root` itself is robbed;
- `skip` is the maximum money obtainable from the complete subtree when `root` itself is not robbed.

These are conditional optima. Keeping both lets the parent request exactly the state that is compatible with its own decision.

**Use postorder because a parent depends on child states.**

The helper first evaluates `dfs(root.left)` and `dfs(root.right)`. Their returned pairs are unpacked as `(la, lb)` and `(ra, rb)`. In this naming, `la` and `ra` are take-values, while `lb` and `rb` are skip-values.

Only after both children are solved can the current node combine their results. This left-right-root order is postorder dynamic programming on the tree.

No explicit memoization dictionary is needed. A binary tree has one parent for every non-root node, so each subtree is reached by exactly one recursive parent call. There are no shared subtrees that would cause repeated state computation.

**State one: rob the current node.**

If `root` is robbed, neither directly connected child may be robbed. The left subtree is therefore forced to use its `skip` value `lb`, and the right subtree is forced to use `rb`. The best total under this condition is

$$
\text{take}
=\text{root.val}+lb+rb.
$$

Skipping each child root does not mean skipping the entire child subtree. Its `skip` value is already the best plan that excludes that child but may include grandchildren or deeper descendants. This is how the recursion handles the common idea of robbing a node and then possibly robbing its grandchildren without directly reaching down two levels in the current formula.

**State two: skip the current node.**

If `root` is not robbed, there is no direct-link restriction between it and either child. For the left subtree, the thief may choose whichever of `la` and `lb` is larger. The right subtree independently chooses the larger of `ra` and `rb`. Thus

$$
\text{skip}
=\max(la,lb)+\max(ra,rb).
$$

The choices are independent because there is no edge connecting a node in the left subtree directly to a node in the right subtree. Their only connection passes through the skipped root. Combining each side's optimum therefore cannot create a forbidden parent-child pair across sides.

It is not always best to rob both children when the parent is skipped. A child's own skip-state may enable several valuable grandchildren and exceed the child's take-state. Taking the maximum separately for each child captures that possibility.

**The empty-subtree base case.**

For `root is None`, the helper returns `(0, 0)`. An absent house contributes no money whether it is conceptually required to be taken or skipped; in practice, both neutral values let leaf formulas work without special branches.

For a leaf of value $v$, both child calls return `(0, 0)`. Its result is therefore

$$
(v,0).
$$

Robbing the leaf earns $v$; skipping it earns zero.

**Walk through the first example.**

The tree has root `3`. Its left child is `2` with a right child `3`, and its right child is `3` with a right child `1`.

The leaf `3` returns `(3,0)`. Its parent `2` then computes:

$$
\text{take}=2+0=2,
\qquad
\text{skip}=\max(3,0)=3.
$$

So the left subtree returns `(2,3)`.

The leaf `1` returns `(1,0)`. Its parent `3` computes a result of `(3,1)`: taking that parent earns `3`, while skipping it permits taking the child worth `1`.

At the root:

$$
\text{take}=3+3+1=7,
$$

because taking the root forces both child roots to be skipped but uses their profitable skip-plans. The alternative is

$$
\text{skip}=\max(2,3)+\max(3,1)=3+3=6.
$$

The larger amount is seven, corresponding to the root plus the two eligible grandchildren.

**Choose the root's better state.**

The root has no parent, so nothing forces it to be robbed or skipped. The public method returns `max(dfs(root))`, selecting the better of the complete tree's two conditional optima.

This final maximum is also correct for a missing root: `dfs(None)` returns `(0,0)`, whose maximum is zero. Although the stated tree contains at least one node, the helper remains naturally robust to an empty tree.

**Why both returned values are correct.**

Use induction on subtree height. The empty subtree's two zero values are correct. Assume both child pairs give the optimal totals under their stated take/skip conditions.

If the current root is taken, every valid plan must skip both child roots. By the induction hypothesis, `lb` and `rb` are the greatest totals under exactly those restrictions. Adding the current value gives the optimal take-state.

If the root is skipped, each child may independently be taken or skipped. The better child state on each side is optimal by induction, and their sums are compatible. Therefore the computed skip-state is optimal.

The two states cover every valid plan according to whether it contains the current root. Their maximum at the top is consequently the global optimum.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Each node is visited exactly once and performs constant-time arithmetic and comparisons after its two child calls. Total time complexity is $O(n)$.

The recursive call stack contains at most one frame per tree level, so it uses $O(h)$ space. This is $O(n)$ in the worst case of a skewed tree and $O(\log n)$ for a balanced tree. Apart from these frames and constant-size return pairs, no data structure proportional to the tree is allocated.

The manifest's $O(n)$ worst-case space bound matches the source, but its summary says iterative postorder. The checked-in optimal solution uses recursive postorder, so its working storage is the call stack rather than an explicit stack or table.

## Alternatives and edge cases

- **Iterative postorder:** Use an explicit stack and store each node's take/skip pair after its children are processed. This avoids recursion limits and matches the manifest wording, but typically keeps an $O(n)$ map or stack.

- **Pass a `parent_robbed` flag:** Recursively solve each node under whether its parent was taken. Without memoization, overlapping state calls repeat work. Memoization restores $O(n)$ time but uses explicit caches; returning both states at once is cleaner on a tree.

- **Recurse directly to grandchildren:** A take-branch can add results from four grandchildren, while a skip-branch calls both children. This duplicates subproblems unless memoized and is more error-prone than the two-state recurrence.

- **Single node:** Its pair is `(value, 0)`, and the public maximum returns its nonnegative value.

- **Zero-valued houses:** Taking or skipping may tie. Either plan is valid, and the numeric optimum is unaffected.

- **A skipped parent does not force taken children:** Each child uses `max(take, skip)`. Forcing take could lose a better combination among grandchildren.

- **Subtrees are independent after fixing the root state:** There are no cross-edges in a tree, so adding the independently optimal left and right totals is safe.

- **Recursion depth:** The tree may contain `10000` nodes. A highly skewed tree can exceed Python's default recursion limit; iterative postorder would preserve the same recurrence without that implementation-level risk.
