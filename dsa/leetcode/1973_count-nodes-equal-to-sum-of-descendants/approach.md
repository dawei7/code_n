## General

**Compute information from children before judging a parent**

For each node, the condition asks for the sum of all its descendants. Rewalking the entire subtree separately for every node would repeat a great deal of work: a leaf's value could be added once for each ancestor above it.

Postorder traversal avoids that repetition. "Postorder" means that the recursive search completely processes the left child and right child before processing the current node. Once both child calls return, their results already summarize everything below the current node.

The helper `dfs(root)` returns the sum of the complete subtree rooted at `root`, including `root` itself. This return meaning is the key contract of the helper. It is slightly different from the value needed for the comparison, which excludes the current node.

**Base case: an absent subtree contributes zero**

If `root is None`, the helper returns zero. An absent child contains no nodes, so zero is its correct subtree sum. This base case also lets every real node use the same formula without separately checking whether its left or right child exists.

For a leaf, both recursive calls therefore return zero. Its descendants sum to zero. A leaf is counted exactly when its own value is zero, matching the definition in the statement.

**Combine the two child summaries**

For a real node, the exact source evaluates

`l, r = dfs(root.left), dfs(root.right)`.

Here, `l` is the total value of every node in the left subtree, and `r` is the corresponding total for the right subtree. Every descendant of the current node belongs to exactly one of those two subtrees, and neither subtotal includes the current node. Consequently, the descendant sum is precisely `l + r`.

The test `l + r == root.val` therefore checks the required property directly. When it succeeds, `ans` increases by one.

After the comparison, the helper returns `root.val + l + r`. The parent needs the whole current subtree as one of its child summaries, so including `root.val` at this point establishes the helper contract for the next stack frame.

**Why `nonlocal ans` is present**

`ans` is initialized to zero in `equalToDescendants`, outside the nested helper. The helper must update that same variable rather than create a new local variable. Python's `nonlocal ans` declaration tells the language exactly that.

In the source, the declaration appears inside the successful `if` block. A `nonlocal` statement is handled when Python compiles the function, so its lexical effect is not conditional even though its line is indented there. Placing it near the top of `dfs` would often be easier for a beginner to notice, but the exact placement is valid.

**Trace a small tree**

Consider a node with value 3 whose children are leaves 2 and 1. Each leaf receives zero from both missing children. Neither positive leaf equals zero, and the calls return 2 and 1.

At node 3, `l + r` is 3, so the node is counted. It then returns the full subtree sum 6 to its parent. Notice why returning only the descendant sum 3 would be wrong: from the parent's perspective, node 3 itself is also a descendant and must contribute its value.

For a larger root of value 10 above that subtree and another subtree totaling 4, the returned values are 6 and 4. Their sum equals 10, so the root is counted as well.

**Why every answer is found exactly once**

The recursion reaches every node because it follows both child references from the root. A node is evaluated only after both of its subtrees have supplied correct sums.

The base case gives the correct sum for an empty tree. Assuming the left and right recursive calls return correct subtree sums, `l + r` is the exact descendant sum, so the node is counted exactly when it should be. Adding the node's own value then returns the correct current subtree sum. By this bottom-up argument, the claim holds for every node.

Each real node executes the equality test once, so no qualifying node is missed or counted twice. After the initial call completes, `ans` is the requested total.

**Why postorder is essential**

Preorder could visit the parent first, but the necessary descendant total would not yet be available. One could postpone the decision or perform another traversal, which recreates complexity. Postorder aligns the direction of computation with the dependency: a parent's answer depends on completed child summaries.

The tree values are nonnegative, but the algorithm does not rely on that fact for its aggregation. Python integers also grow as needed, so even a subtree total larger than a fixed 32-bit integer remains exact.

## Complexity detail

Let $N$ be the number of nodes and $H$ be the tree height. Every real node is entered once, performs constant work besides its two recursive calls, and every missing-child reference is handled in constant time. Total time is $O(N)$.

The recursion stack holds at most one frame per level, so auxiliary space is $O(H)$. A balanced tree has $H=O(\log N)$, while a completely skewed tree has $H=O(N)$. The manifest states the worst-case bound, $O(N)$. The solution stores no per-node array or map.

## Alternatives and edge cases

- **Recompute every descendant sum independently:** This is conceptually direct but can take $O(N^2)$ time on a chain because the same lower subtrees are scanned repeatedly.
- **Iterative postorder:** A stack plus visitation state can compute the same sums without Python recursion, but it needs a way to retain each child's subtotal.
- **Two-stack traversal:** It gives a clear reverse-preorder/postorder sequence at the cost of explicit $O(N)$ storage.
- **Leaf with value zero:** Its descendant sum is zero, so it must be counted.
- **Positive-valued leaf:** Its descendant sum is zero and it is not counted.
- **Only one child:** The missing side contributes zero, so the same `l + r` formula remains correct.
- **Single-node tree:** The result is one when that node is zero and zero otherwise.
- **Skewed tree:** The algorithmic bound stays linear, but a depth near $10^5$ can exceed Python's recursion limit.
- **Large subtree sum:** Python's arbitrary-precision integers prevent fixed-width overflow.
- **Do not include the node in its own descendant sum:** Compare `l + r`, then include `root.val` only in the value returned upward.
- **Shared counter:** `nonlocal ans` is necessary; otherwise assignment would target a new local name and fail to update the outer result.
- **Input preservation:** The traversal reads node values and child links without modifying the tree.
