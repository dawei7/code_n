# Binary Tree Tilt

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 563 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-tilt/) |

## Problem Description
### Goal
Given the root of a binary tree, define the tilt of a node as the absolute difference between the sum of all values in its left subtree and the sum of all values in its right subtree. An empty subtree has sum `0`, so a leaf has tilt `0`.

Return the sum of the tilts of every node in the tree. Each subtree sum includes all descendants on that side, not only the node's immediate children, and every node's individual tilt contributes once to the final total.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

- The sum of every node's tilt

### Examples
**Example 1**

- Input tree: `[1, 2, 3]`
- Output: `1`

**Example 2**

- Input tree: `[4, 2, 9, 3, 5, null, 7]`
- Output: `15`

**Example 3**

- Input tree: `[21, 7, 14, 1, 1, 2, 2, 3, 3]`
- Output: `9`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**A parent needs both child subtree sums**

The tilt at a node is `abs(left_sum - right_sum)`. After contributing that value, the node must return `node.val + left_sum + right_sum` so its parent can perform the same calculation.

**Process children before their parent**

Use postorder traversal. An explicit stack frame records which child should be visited next and stores each returned child sum. Once both are available, finalize the node in constant time.

**Accumulate tilt while returning sums**

Keep one running total for the answer. A completed frame adds its local absolute difference, then passes its complete subtree sum into the appropriate field of its parent frame.

**Why every contribution is exact**

By postorder induction, a child frame returns the sum of exactly all values in that child's subtree. Their absolute difference is therefore the current node's defined tilt, and adding the current value produces the exact sum required by the parent. Every node is finalized once, so every tilt is added once and none is omitted.

#### Complexity detail

Each of the `n` nodes is pushed, finalized, and removed once, giving $O(n)$ time. The explicit postorder stack contains at most one frame per tree level and uses $O(h)$ space.

#### Alternatives and edge cases

- **Recursive postorder:** returns subtree sums naturally in $O(n)$ time, but a skewed tree can exceed recursion limits.
- **Recompute each subtree sum:** is correct but revisits descendants and takes $O(n^2)$ time on a chain.
- **Single node:** has two empty subtrees and tilt zero.
- **Missing child:** contributes subtree sum zero on that side.
- **Zero-valued nodes:** still participate structurally even though they add nothing to a subtree sum.
- **Skewed tree:** every ancestor's tilt includes the complete sum below its one child.
- **Root contribution:** is included just like every other node.

</details>
