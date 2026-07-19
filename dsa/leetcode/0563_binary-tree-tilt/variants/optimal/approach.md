## General
**A parent needs both child subtree sums**

The tilt at a node is `abs(left_sum - right_sum)`. After contributing that value, the node must return `node.val + left_sum + right_sum` so its parent can perform the same calculation.

**Process children before their parent**

Use postorder traversal. An explicit stack frame records which child should be visited next and stores each returned child sum. Once both are available, finalize the node in constant time.

**Accumulate tilt while returning sums**

Keep one running total for the answer. A completed frame adds its local absolute difference, then passes its complete subtree sum into the appropriate field of its parent frame.

**Why every contribution is exact**

By postorder induction, a child frame returns the sum of exactly all values in that child's subtree. Their absolute difference is therefore the current node's defined tilt, and adding the current value produces the exact sum required by the parent. Every node is finalized once, so every tilt is added once and none is omitted.

## Complexity detail
Each of the `n` nodes is pushed, finalized, and removed once, giving $O(n)$ time. The explicit postorder stack contains at most one frame per tree level and uses $O(h)$ space.

## Alternatives and edge cases
- **Recursive postorder:** returns subtree sums naturally in $O(n)$ time, but a skewed tree can exceed recursion limits.
- **Recompute each subtree sum:** is correct but revisits descendants and takes $O(n^2)$ time on a chain.
- **Single node:** has two empty subtrees and tilt zero.
- **Missing child:** contributes subtree sum zero on that side.
- **Zero-valued nodes:** still participate structurally even though they add nothing to a subtree sum.
- **Skewed tree:** every ancestor's tilt includes the complete sum below its one child.
- **Root contribution:** is included just like every other node.
