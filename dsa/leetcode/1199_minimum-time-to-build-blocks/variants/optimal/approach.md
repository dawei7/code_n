## General
**Reverse splitting into merging.** View every block time as the completion time of a one-block plan. To place two plans beneath one earlier worker, that worker first spends `split` time creating two workers, after which the plans run in parallel. If their completion times are $a\le b$, the combined plan finishes in `split + b`; the smaller time affects neither the maximum nor the merged value.

**Delay expensive plans from gaining depth.** Every merge adds `split` to the larger of its two children. Combining a long plan early risks charging it this cost repeatedly. An exchange argument shows that two smallest available completion times can be made siblings at the deepest remaining merge without worsening the final maximum: replacing a deeper larger child by a smaller one never increases any ancestor completion time.

**Implement the greedy merge order.** Store all completion times in a min-heap. Remove the two smallest values; discard the smaller and insert `larger + split`, which is their combined completion time. Repeat until one plan remains. The exchange argument makes each merge safe, and the last heap value is the minimum elapsed time for the full worker-splitting tree.

## Complexity detail
Heap construction takes $O(n)$. The algorithm performs $n-1$ merges, each with two removals and one insertion costing $O(\log n)$, for $O(n\log n)$ total time. The heap contains at most $n$ completion times and therefore uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Explicit two-minimum scan:** Finding the two smallest plans by a full scan before every merge is correct but takes $O(n^2)$ time.
- **Forward worker scheduling:** Deciding which active worker should split and which block it should build creates a large scheduling state space and obscures the greedy structure.
- **Single block:** No split is useful, so its build time is returned directly.
- **Two blocks:** Exactly one split is necessary, producing `split + max(blocks)`.
- **Equal block times:** A balanced merge tree minimizes how often any one completion time receives the split cost.
- **One very long block:** Greedy merging leaves it until late so shorter blocks can be prepared in parallel without repeatedly delaying it.
- **Parallel splits:** Separate workers may split simultaneously; elapsed time follows the maximum branch depth, not the sum over all split operations.
- **Positive costs:** Every build and split time is positive, so unnecessary splits cannot improve a completed plan.
