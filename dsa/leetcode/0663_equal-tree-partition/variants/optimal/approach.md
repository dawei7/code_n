## General

**Every removable edge identifies one subtree**

Removing an edge between a parent and child separates the original tree into:

- the complete subtree rooted at that child;
- all remaining nodes outside that subtree.

If the total tree sum is `S` and the child-subtree sum is `T`, the other component has sum `S - T`. The two components are equal exactly when:

`T = S - T`,

which is equivalent to `T = S / 2`.

Therefore, the problem reduces to computing every subtree sum and asking whether any proper subtree has half the total sum.

**Compute subtree sums with postorder traversal**

The nested function named `sum` returns the sum of the subtree rooted at its argument.

For a null child, it returns zero. For a real node, it first computes:

- `l`, the sum of the left subtree;
- `r`, the sum of the right subtree.

It then adds `l + r + root.val` to `seen` and returns that newly appended value.

Children are processed before the parent, so the traversal is postorder. This is exactly the order needed because a parent sum depends on both child sums.

The helper name shadows Python's built-in `sum` inside the method, but the implementation never needs the built-in there. A name such as `subtree_sum` would be clearer without changing behavior.

**Why the total must be even**

The first call returns the complete tree sum `s`. If a valid cut created two equal integer sums `q`, then `s = q + q = 2q`, which must be even.

If `s` is odd, no integer subtree can equal half of it, so the method returns `False` immediately.

The exact condition is `s % 2 == 1`. In Python, this also detects negative odd integers because, for example, `-3 % 2` is one. A more language-portable expression is `s % 2 != 0`.

**Why the root's total is removed**

Postorder appends the root's subtree sum last, and that value is the total `s`. The code executes `seen.pop()` to remove it before searching for `s // 2`.

This is essential because the root does not correspond to a removable parent edge. Choosing the whole tree as one “subtree” would mean removing no edge and leaving an empty other component, which violates the requirement to remove exactly one existing edge.

The issue is especially visible when `s = 0`. The target half is also zero, so leaving the root total in `seen` would make every zero-sum tree appear splittable, even a one-node tree with no edge. Removing the last entry prevents that false positive.

**Search all proper subtree sums**

After excluding the root, the expression `s // 2 in seen` checks whether any remaining node roots a subtree with the required half sum.

If such a subtree exists, remove the edge from its parent. Its sum is half the total, and the complement is also half, so the cut is valid.

If no proper subtree has that sum, no edge can work because every possible removed edge selects exactly one proper child subtree.

**A positive example**

Suppose the tree has root five, a left leaf ten, and a right subtree with values ten, two, and three. The complete sum is thirty.

The left subtree sum is ten. The right subtree sum is fifteen. The target is fifteen, so the right-subtree total occurs in `seen`. Cutting the edge from root five to that right child produces components of fifteen and fifteen.

**Why negative values do not break the method**

Subtree sums need not be positive, and neither does the total. The algebra `T = S - T` remains valid for negative and zero values.

For a total of negative eight, the target is negative four. Python's exact integer division gives `-8 // 2 = -4`. The membership test works like any other integer lookup.

**Why the method is correct**

Every non-root node has exactly one parent edge. Removing that edge separates precisely the node's subtree from the rest of the tree. The traversal records the sum of every such subtree.

If the algorithm finds target `S / 2` among proper subtree sums, the associated edge produces components with sums `S / 2` and `S - S / 2 = S / 2`, so returning `True` is sound.

Conversely, if any valid cut exists, its child component is a proper subtree whose sum must satisfy `T = S / 2`. That value was appended to `seen` and was not the removed root entry, so membership succeeds. Thus the algorithm finds every valid cut.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height.

The postorder traversal visits each node exactly once and performs constant arithmetic, taking `O(N)` time. The final list-membership test scans at most `N - 1` values, also `O(N)`. Total running time remains `O(N)`.

The `seen` list stores one subtree sum per node before the root is removed, using `O(N)` space. Recursive call depth is `O(H)` and can be `O(N)` for a skewed tree. Combined auxiliary space is `O(N)`.

Using a set instead of a list would make the final lookup expected constant time, but the traversal already costs linear time, so the overall asymptotic bound would not change. A list also preserves the useful fact that the root sum is last and can be popped directly.

With up to ten thousand nodes, a highly skewed tree can exceed Python's default recursion depth. An iterative postorder traversal would address that practical limitation.

## Alternatives and edge cases

- **Use a set of proper subtree sums:** Compute the total separately or remove the root value before lookup. This provides expected constant-time membership but still uses `O(N)` memory.

- **Two-pass traversal:** First compute the total, then traverse again and return as soon as a non-root subtree reaches half. This can avoid storing all sums but performs two traversals and still uses recursion stack space.

- **Recompute every subtree for every edge:** This repeats work and can take `O(N^2)` time. Postorder computes each subtree sum once.

- **Total sum is odd:** Equal integer components are impossible, so immediate rejection is correct.

- **Total sum is zero:** A proper zero-sum subtree is required. The whole root sum must not count.

- **Single-node tree:** After popping the root total, `seen` is empty, so the result is `False` because there is no edge to remove.

- **Root with one zero-sum child:** The child's zero appears after the root total is removed, so cutting that edge can correctly return `True` when the complement also sums to zero.

- **Negative values:** Evenness and half-sum reasoning remain valid; do not use positivity-based pruning.

- **Duplicate subtree sums:** Only existence matters. A list may contain the same target several times, but one valid edge is enough.

- **Removing a node instead of an edge:** The node remains part of its subtree component. The algorithm partitions by parent-child edge, exactly as required.

- **Leaving the root sum in `seen`:** This causes false positives, particularly for total zero. `seen.pop()` is a correctness step, not an optimization.

- **Deeply skewed tree:** Recursion depth may require an iterative traversal in production Python despite the correct asymptotic analysis.
