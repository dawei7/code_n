## General

The tilt of a node depends on the **sum of every value** in each child subtree, not merely on the immediate child values. A postorder depth-first traversal computes those subtree sums from the bottom upward while accumulating each node's tilt.

The helper `dfs(root)` returns the sum of all values in the subtree rooted at `root`.

If `root is None`, the subtree contains no nodes and its sum is zero. This exactly matches the rule that a missing left or right child contributes subtree sum zero.

**Compute child sums before the current tilt.** The calls:

`l, r = dfs(root.left), dfs(root.right)`

fully process both child subtrees. Their returned values are the complete left and right sums needed at the current node.

Because the children are processed first, their own node tilts have already been added to the shared answer before the current node contributes.

**Add the current node's tilt once.** The definition is the absolute difference between the two child-subtree sums:

$$
\lvert l-r\rvert.
$$

The code performs `ans += abs(l - r)`. Absolute value is necessary because either subtree may have the larger sum, and node values may be negative.

**Return the complete subtree sum upward.** After recording tilt, the helper returns:

`l + r + root.val`.

This includes every value in the left subtree, every value in the right subtree, and the current node exactly once. The parent can therefore use this single integer instead of traversing the subtree again.

For tree `[1,2,3]`, leaves two and three each receive left and right sums zero, add tilt zero, and return sums two and three. The root adds `abs(2 - 3) = 1` and returns total sum six. The final tilt answer is one.

For the larger tree rooted at four, subtree rooted at two returns ten after including values two, three, and five. Subtree rooted at nine returns sixteen after including nine and seven. The root's own tilt is six. That is added to tilts two and seven from its children, producing fifteen.

**Why subtree sum and subtree tilt are different quantities.** The value returned by DFS is a sum of node values, because that is what the parent needs. The global `ans` separately accumulates tilt contributions. Returning the total tilt instead would give the parent the wrong inputs for its absolute difference.

**Why one traversal is enough.** A naive method might compute the left and right sums afresh at every node. Nodes near the bottom would then be revisited for many ancestors. Postorder DP summarizes each subtree once and immediately passes its sum upward.

**Why every node contributes exactly once.** DFS is invoked once from its parent for every real node. The update occurs in that node's unique call after both children return. A valid tree has no shared child or cycle, so no node can be reached twice.

**Why the returned answer is complete.** The helper reaches all nodes. At each, `l` and `r` are exact by induction: null subtrees return zero, and a real subtree returns its child sums plus its root value. Therefore each absolute difference is the defined tilt. Summing those one-per-node contributions yields the required total.

Variable `ans` is declared `nonlocal` so every recursive frame updates the same accumulator. It begins at zero, the correct total for an empty tree or before any node is visited.

The tree is read-only. Neither values nor child references are modified.

This separation of returned subtree sum and side-effected total tilt is deliberate and exact.

## Complexity detail

Let $n$ be the node count and $h$ the tree height. Every node is visited once and performs constant arithmetic after its child calls, so time is $O(n)$.

The recursion stack holds at most one frame per level, using $O(h)$ auxiliary space, matching the manifest. A balanced tree uses $O(\log n)$ depth; a skewed tree may use $O(n)$.

Only scalar sums and the shared answer are stored beyond the call stack.

## Alternatives and edge cases

- **Recompute subtree sums per node:** It is correct but can take $O(n^2)$ time on a skewed tree.
- **Store all subtree sums in a map:** It avoids recomputation but uses unnecessary $O(n)$ storage; postorder returns each sum directly.
- **Return tilt instead of value sum:** The parent needs child value totals, so this breaks the recurrence.
- **Empty tree:** DFS returns zero and the answer remains zero.
- **Single node:** Both subtree sums are zero, so its tilt is zero.
- **One missing child:** Its side contributes zero exactly as required.
- **Negative values:** Subtree sums may be negative; `abs` still gives the defined difference.
- **Equal subtree sums:** The current node contributes zero.
- **Skewed tree:** Each node compares zero with its only child-subtree sum.
- **Input immutability:** The computation uses summaries without changing nodes.
- **Recursion limit:** A 10,000-node chain may require an iterative postorder traversal in Python environments with a default recursion limit.
