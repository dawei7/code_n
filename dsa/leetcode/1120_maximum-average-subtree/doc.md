# Maximum Average Subtree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1120 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-average-subtree/) |

## Problem Description

### Goal

You are given the root of a nonempty binary tree whose node values are nonnegative. For any node, its subtree consists of that node together with every descendant reachable through its left and right children.

The average value of a subtree is the sum of all values in that subtree divided by its number of nodes. Consider the subtree rooted at every node and return the greatest of those averages. The answer is accepted within the platform's floating-point tolerance.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ nodes; cOde(n) fixtures serialize it in level order with `null` for absent children.

**Return value**

- The maximum arithmetic mean among all $N$ rooted subtrees, as a floating-point number.

### Examples

**Example 1**

- Input: `root = [5,6,1]`
- Output: `6.0`

The leaf containing `6` has average 6, while the entire tree has average 4.

**Example 2**

- Input: `root = [0,null,1]`
- Output: `1.0`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**A parent needs two summaries from each child:** Process the tree in postorder. For each node, obtain `(left_sum, left_count)` and `(right_sum, right_count)`. Its own subtree summary is then computed with `total = node.val + left_sum + right_sum` and `count = 1 + left_count + right_count`.

**Evaluate each rooted subtree when its summary becomes complete:** Compute `total / count` at that node and update a shared best average. Return only the sum and count upward; the best is already recorded and does not need to be recomputed by ancestors.

Every possible subtree in this problem is rooted at exactly one node. Postorder computes the exact sum and node count for that root because its children's disjoint summaries contain all and only the descendants. The algorithm evaluates the corresponding average once. Taking the maximum across all visited roots therefore returns the maximum over the complete candidate set.

#### Complexity detail

Each of the $N$ nodes is entered once and performs constant arithmetic after its children, for $O(N)$ time. Recursion depth is the tree height $h$, bounded by $N$, so worst-case auxiliary space is $O(N)$ and is $O(h)$ more precisely.

#### Alternatives and edge cases

- **Recompute every subtree independently:** Starting a fresh sum/count traversal at each node is correct but takes $O(N^2)$ time on a chain.
- **Iterative postorder:** An explicit stack avoids recursion limits while retaining $O(N)$ time and space.
- **Store all descendant values:** It can derive averages but duplicates data and may require quadratic storage.
- **Single node:** Its one-node subtree is the only candidate, so its value is returned as a float.
- **Leaf maximum:** A high-valued leaf can beat every larger subtree because adding smaller descendants lowers an average.
- **Internal maximum:** A parent and selected descendant structure may average higher than either the full tree or other leaves; every root must be evaluated.
- **All equal values:** Every subtree has the same average, so that shared value is returned.
- **Zero values:** Initializing the best to `0.0` is valid because node values and all subtree averages are nonnegative.

</details>
