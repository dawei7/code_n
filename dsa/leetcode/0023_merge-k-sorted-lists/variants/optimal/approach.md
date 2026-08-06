## General
**The heap needs only one exposed node per list**

The first unconsumed value of each sorted list is that list's smallest remaining value. Put those at most `k` candidates into a min-heap. Repeatedly remove the global minimum, append it to the result, and insert the next value from the same source list. Values deeper in a list do not belong in the heap yet because they cannot precede that list's current head.

Each heap entry is `(node.val, i, node)`, where `i` is the source-list position. Attach the popped node directly to the merged tail and push its successor with the same `i`. The source position breaks equal-value ties deterministically, so Python never tries to compare `ListNode` objects.

**Restore the frontier after every extraction**

Before every heap pop, the heap contains exactly the smallest unconsumed value from each nonempty source. Consequently its root is the smallest value not yet emitted across all lists. Replacing it with its same-list successor restores the invariant.

**Trace an uneven merge**

For `[[1, 4, 5], [1, 3, 4], [2, 6]]`, initialize the heap with `1, 1, 2`. Pop the first 1 and expose 4; pop the other 1 and expose 3; then pop 2 and expose 6. Continuing in heap order produces `1, 1, 2, 3, 4, 4, 5, 6`.

**The heap contains the complete merge frontier**

For each nonempty source, its current head is the smallest value not yet emitted from that list. Any hidden node is no smaller than its own head, so no hidden value can be smaller than the minimum among all heads in the heap.

Popping that heap minimum therefore chooses the globally next value. Advancing only its source exposes the sole new value that can enter the frontier; every other source head remains unchanged. Repeating preserves one candidate per nonempty suffix and emits the complete sorted multiset union.

## Complexity detail
Each of the $N$ nodes enters and leaves a heap of at most $k$ entries once. Heap operations cost $O(\log k)$, giving $O(N \log k)$ time; when $k$ is zero or one, the corresponding behavior is constant overhead or a direct list traversal. The heap uses $O(k)$ auxiliary space. Both the app-local and native forms relink and return the existing nodes; the app runner serializes the returned chain only after `solve` finishes.

## Alternatives and edge cases
- **Scan all `k` heads for every output:** uses little storage but requires $O(Nk)$ time.
- **Merge lists one at a time:** can degrade to $O(Nk)$ as the accumulated list is repeatedly scanned.
- **Pairwise divide and conquer:** also achieves $O(N \log k)$ and constant pointer overhead, but the heap exposes the invariant more directly for uneven list sizes.
- Empty source lists contribute no heap entry. If every list is empty, the heap begins empty and so does the result.
- Equal values from different lists must all be retained; the heap tie-breaker orders them but must not deduplicate them.
