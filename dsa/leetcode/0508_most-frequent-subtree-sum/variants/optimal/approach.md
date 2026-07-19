## General
**Process children before their parent**

A node's subtree sum is `node.val + left_sum + right_sum`, so both child sums must be available first. Simulate postorder traversal with stack entries `(node, expanded)`. The first visit schedules the node for a later expanded visit after scheduling its children; the expanded visit performs the sum.

**Store one computed sum per node**

Record each finished sum in a map keyed by the node. Missing children contribute zero. Immediately increment that sum's frequency in a second map and update the largest frequency observed.

**Why every frequency is complete**

Every node receives exactly one expanded visit after both of its child subtrees have been finalized. Its recorded value therefore equals the sum of exactly the nodes in its subtree. Since every subtree is rooted at one unique node, incrementing once per expanded visit counts every subtree sum exactly once. Filtering the frequency map by the recorded maximum returns precisely all tied modes.

## Complexity detail
Each of `n` nodes is pushed and finalized once, and each map operation is expected $O(1)$, for $O(n)$ time. The traversal stack, node-sum map, and frequency map use $O(n)$ space.

## Alternatives and edge cases
- **Recursive postorder:** expresses the recurrence compactly and has $O(n)$ time, but a highly skewed tree can exceed Python's recursion limit.
- **Two-stack postorder:** reverses a root-right-left traversal and has the same asymptotic bounds.
- **Recompute a subtree for every root:** is correct but takes $O(n^2)$ time on a chain.
- **Single node:** its value is the only subtree sum and the only answer.
- **Negative values:** participate in ordinary addition and may produce negative modes.
- **Several maximum-frequency sums:** all must be returned; order is irrelevant.
- **Equal subtree sums at different nodes:** each occurrence contributes separately to frequency.
