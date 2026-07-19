## General
**The root supplies the global minimum**

Every internal node equals the minimum of its children. Repeating this relation down the tree shows that no descendant can be smaller than an ancestor, so the root value is the minimum of the entire tree. The target is therefore the smallest value encountered that differs from this root value.

**Prune as soon as a larger value appears**

When a node value is greater than the root minimum, that node is already the smallest value in its subtree: every descendant is at least its ancestor under the special-tree rule. Return the node value immediately without inspecting its children. A node equal to the minimum cannot itself be the answer, so recursively request candidates from both children.

**Combine subtree candidates without confusing absence**

A leaf equal to the minimum has no candidate and returns `-1`. When both child calls produce candidates, keep their smaller value; when only one does, propagate it. Each subtree result is consequently its smallest value above the global minimum or `-1` if none exists. Applying that statement at the root gives exactly the second smallest distinct value.

## Complexity detail
Each node is visited at most once, and candidate subtrees can be pruned at their roots, for $O(N)$ worst-case time. Recursion stores at most one frame per tree level, using $O(H)$ space for height `H`. A balanced tree has logarithmic height, while a legal comb-shaped tree can have linear height.

## Alternatives and edge cases
- **Full traversal with two running minima:** ignores the special pruning opportunity but still finds the answer in $O(N)$ time and $O(H)$ stack space.
- **Pairwise candidate validation:** collect all nodes, then test every larger value against every other value to determine whether a smaller candidate exists; it is correct but takes $O(N^2)$ time.
- **Enumerate every root-to-leaf path:** is correct because every node occurs on some path, but copying shared prefixes can take $O(NH)$ time and space.
- **Collect distinct values in a set and sort:** is straightforward, but uses $O(N)$ extra space and $O(N \log N)$ sorting time.
- The second minimum must be distinct from the root value; repeated minimum nodes do not qualify.
- A single-node tree has no second distinct value and returns `-1`.
- Large candidate values must be compared normally rather than replaced by a narrow numeric sentinel.
