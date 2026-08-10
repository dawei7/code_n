## General

**Use the ordering information, not just the tree shape**

A plain binary-tree traversal could visit every node, check whether its value lies in the inclusive range, and add qualifying values. That is correct, but it ignores the defining property of a binary search tree:

- every value in a node's left subtree is smaller than the node's value;
- every value in its right subtree is larger than the node's value.

All node values are unique, so these inequalities are strict. They tell the recursion when an entire branch cannot possibly contain an in-range value.

**What each recursive call returns**

The helper `dfs(root)` returns the sum of all values in the subtree rooted at `root` that lie in `[low, high]`.

If `root is None`, the subtree has no values and contributes zero. This base case also handles missing left or right children without separate checks at the caller.

For a real node, the code stores `x = root.val`. It initializes the local result as `x` when `low <= x <= high` and as zero otherwise. Both endpoints are included, so equality with `low` or `high` must contribute the node's value.

The helper then decides independently whether the left and right subtrees can contain useful values.

**Why the left recursion uses `x > low`**

Every value in the left subtree is strictly smaller than `x`.

If `x <= low`, every left-subtree value is smaller than or equal to the lower-bound side and, because values are unique, is actually smaller than `low` when `x = low`. None can belong to the inclusive range. The entire left subtree can be skipped.

If `x > low`, the left subtree may contain values at least `low`, so the code adds `dfs(root.left)`. Some of that subtree may still be outside the range, but recursive calls apply the same pruning at their own roots.

The strict condition is important. At `x = low`, the current node is included, but its left descendants are all below `low` and should not be visited.

**Why the right recursion uses `x < high`**

Every value in the right subtree is strictly larger than `x`.

If `x >= high`, every right-subtree value is greater than the upper bound, so the branch cannot contribute. If `x < high`, useful values may exist on the right and the helper explores it.

Again, equality is handled precisely. At `x = high`, the current node contributes, but every right descendant exceeds `high` and is safely pruned.

**How both decisions interact**

There are three useful positional cases:

- If `x < low`, the node contributes zero, the left subtree is pruned, and only the right subtree might reach the range.
- If `low <= x <= high`, the node contributes `x`. The left side is explored unless `x = low`, and the right side is explored unless `x = high`.
- If `x > high`, the node contributes zero, the right subtree is pruned, and only the left subtree might reach the range.

This resembles binary search when the current value is outside the interval, because only one direction can move toward it. Inside the interval, both branches may contain additional qualifying nodes.

**A trace**

For a root value `10` with range `[7, 15]`, ten is added. Because `10 > 7`, the left subtree may contain values in range. Because `10 < 15`, the right subtree may also contain them.

At a left child `5`, five is below the range. Its left subtree contains only values below five and is discarded; only its right subtree can approach seven. If that right path reaches `7`, seven is added, its left subtree is pruned because `7 = low`, and its right side may still contain values up to fifteen.

At a node `15`, fifteen is added. Its right subtree is pruned immediately because every right value exceeds the inclusive upper endpoint.

**Why the sum is correct**

Prove the helper's contract by induction on subtree size. The empty subtree returns the correct sum zero. For a nonempty subtree, the current value is included exactly when it satisfies both inclusive bounds.

If the left recursive call is skipped, `x <= low` and every left value is strictly below `x`, so every one is below `low`; the skipped branch contributes zero to the desired sum. If it is explored, the inductive hypothesis gives exactly its in-range sum. The same argument applies symmetrically to the right branch using `x >= high`.

The current contribution and the two subtree contributions cover disjoint node sets. Adding them gives exactly the in-range sum for the current subtree. Applying this result at the original root proves the returned answer.

## Complexity detail

Let `h` be the tree height and `v` the number of values that fall in the requested range and are therefore reported into the sum.

In a binary search tree, the pruned range traversal visits the qualifying region plus boundary search paths needed to reach it. Its output-sensitive time is `O(h + v)`. Each visited node performs constant work. In the worst case, the range covers the entire tree or the tree is highly skewed, so this becomes `O(N)` for `N` total nodes.

The recursion stack follows one root-to-leaf path at a time, so auxiliary space is `O(h)`. A balanced tree has `h = O(log N)`, while a chain-shaped tree has `h = O(N)`.

The function does not allocate a collection of qualifying values; it accumulates their sum directly. Therefore `v` affects traversal time but does not create `O(v)` result storage.

## Alternatives and edge cases

- **Traverse every node:** A generic DFS or BFS with a range check is correct in `O(N)` time, but it wastes the BST ordering and may inspect large branches known to be irrelevant.
- **Iterative pruned DFS:** Use an explicit stack and apply the same left and right conditions. This preserves `O(h + v)` time and `O(h)` typical stack space while avoiding Python recursion-limit failures.
- **In-order traversal:** It visits values in sorted order and can stop after exceeding `high`, but a naive version may still descend unnecessarily below `low`. Adding the same pruning makes it equivalent in asymptotic behavior.
- **Prefix sums over a static BST:** If many range-sum queries were made against an unchanging tree, an ordered array plus prefix sums could answer later queries quickly after preprocessing. For one query, building that structure adds unnecessary `O(N)` work and storage.
- **Endpoint equality:** The current node is included when `x = low` or `x = high`. The corresponding outward subtree is pruned with a strict recursive condition because unique descendants lie strictly beyond that endpoint.
- **Range containing every value:** Both branches are explored throughout and the result is the sum of the entire tree. The worst-case running time is `O(N)`.
- **Range containing one existing value:** Search paths toward that value are visited, while impossible branches are pruned. The result is that value alone.
- **Range containing no node value:** The traversal still follows boundary-directed paths but adds nothing and returns zero.
- **Missing children:** The `None` base case contributes zero, so leaf nodes and one-child nodes require no special handling.
- **Skewed tree:** The mathematical space bound becomes `O(N)`, and a tree with up to twenty thousand nodes can exceed Python's default recursion depth. An iterative stack is safer if such shapes are expected.
- **Unique-value guarantee:** The strict BST comparisons and pruning conditions rely on the stated uniqueness. A duplicate policy would need to specify which subtree may contain equal values, although the inclusive range check itself would still be straightforward.
