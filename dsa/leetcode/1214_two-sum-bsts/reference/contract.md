## Function Contract

**Inputs**

- `root1`: The root of the first nonempty binary search tree.
- `root2`: The root of the second nonempty binary search tree.
- `target`: The integer sum to test.

Let $n$ and $m$ be the respective numbers of nodes in the two trees. Each node has an integer value and optional left and right children. The examples serialize trees in level order, using `null` where an absent child must be shown.

**Return value**

Return `true` when one node from `root1` and one node from `root2` have values summing to `target`. Return `false` when no cross-tree pair has that sum.
