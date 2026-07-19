## General
**A parent needs two summaries from each child:** Process the tree in postorder. For each node, obtain `(left_sum, left_count)` and `(right_sum, right_count)`. Its own subtree summary is then computed with `total = node.val + left_sum + right_sum` and `count = 1 + left_count + right_count`.

**Evaluate each rooted subtree when its summary becomes complete:** Compute `total / count` at that node and update a shared best average. Return only the sum and count upward; the best is already recorded and does not need to be recomputed by ancestors.

Every possible subtree in this problem is rooted at exactly one node. Postorder computes the exact sum and node count for that root because its children's disjoint summaries contain all and only the descendants. The algorithm evaluates the corresponding average once. Taking the maximum across all visited roots therefore returns the maximum over the complete candidate set.

## Complexity detail
Each of the $N$ nodes is entered once and performs constant arithmetic after its children, for $O(N)$ time. Recursion depth is the tree height $h$, bounded by $N$, so worst-case auxiliary space is $O(N)$ and is $O(h)$ more precisely.

## Alternatives and edge cases
- **Recompute every subtree independently:** Starting a fresh sum/count traversal at each node is correct but takes $O(N^2)$ time on a chain.
- **Iterative postorder:** An explicit stack avoids recursion limits while retaining $O(N)$ time and space.
- **Store all descendant values:** It can derive averages but duplicates data and may require quadratic storage.
- **Single node:** Its one-node subtree is the only candidate, so its value is returned as a float.
- **Leaf maximum:** A high-valued leaf can beat every larger subtree because adding smaller descendants lowers an average.
- **Internal maximum:** A parent and selected descendant structure may average higher than either the full tree or other leaves; every root must be evaluated.
- **All equal values:** Every subtree has the same average, so that shared value is returned.
- **Zero values:** Initializing the best to `0.0` is valid because node values and all subtree averages are nonnegative.
