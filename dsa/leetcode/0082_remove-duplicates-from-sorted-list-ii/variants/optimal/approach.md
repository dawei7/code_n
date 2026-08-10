## General

**Remove an entire repeated run, not merely extra copies**

This problem differs from the simpler task that keeps one copy of every value. If a value occurs more than once, every node with that value must disappear. Because the list is sorted, equal values form one contiguous run. The algorithm can inspect and either keep or bypass one complete run at a time.

`cur` begins at the first node of the next unclassified run. `pre` is the last node already retained in the output list—or the dummy node when no real node has been retained. Most importantly, `pre.next` points to the first node of the run currently under examination.

**Use a dummy node so the result head is ordinary pointer work**

A duplicate run may begin at the original `head`. Without a predecessor before that run, deleting it would require a special update to the head variable. `ListNode(next=head)` creates a sentinel whose `next` field behaves as the predecessor link for the first real run.

`dummy = pre = ...` gives both names the same sentinel object initially. The sentinel's value is irrelevant; it is never compared with input values and is not part of the returned list. Returning `dummy.next` works whether the original head survives, is replaced by a later node, or the entire list is removed.

The repository's linked-list template supplies `ListNode`; the commented definition in the solution indicates platform-provided structure rather than work the user must recreate.

**Advance `cur` to the end of its equal-value run**

The inner loop continues while a next node exists and has the same value as `cur`. Every iteration sets `cur = cur.next`. Since all equal values are adjacent, the loop stops with `cur` at the final node of the current value's run.

For a singleton run, the loop performs zero iterations and `cur` remains the first node. For a repeated run, `cur` moves at least once. The source uses this movement itself as the duplicate signal rather than maintaining a counter or saving the value separately.

**Use node identity to distinguish singleton and repeated runs**

After the inner loop, `pre.next` still points to the run's first node. The expression `pre.next == cur` compares node references. It is true exactly when the first and last nodes of the run are the same object, which means the run contains one node.

For a singleton, the value is distinct and must remain. Assigning `pre = cur` promotes that node to the last retained output node. Its `next` link already points to the next unclassified run.

For a repeated run, `pre.next` and `cur` are different nodes. `pre.next = cur.next` bypasses the entire run from its first node through its last node. `pre` deliberately stays where it is, because no node from the repeated run was retained. It remains the predecessor for the next run.

The test must use node identity rather than value equality: all nodes in a repeated run have equal values, so values cannot reveal whether `cur` moved from the first object to a later object.

**Move to the next run after the decision**

`cur = cur.next` occurs after either keeping or deleting the run. Since `cur` currently points to that run's final node, its `next` is the first node of the next value or `None` at the list end.

In the repeated case, pointer bypass happens before this movement. Although the removed nodes may still point to one another internally, no retained predecessor points to their first node, so they are unreachable from `dummy.next` and are logically deleted.

**Trace duplicates at both ends**

For `[1,1,1,2,3,3]`, `pre.next` starts at the first 1 while `cur` advances to the third 1. The objects differ, so the sentinel is linked directly to 2. `pre` remains the sentinel. The 2 run is a singleton, so `pre.next == cur`; 2 is retained and becomes `pre`.

The final 3 run contains two nodes. `cur` advances to the second, and `pre.next` still points to the first. Bypassing with `pre.next = cur.next` sets the retained 2's next link to `None`. The result is `[2]` with no special head or tail case.

**A run-level invariant proves correctness**

Before each outer iteration, the list reachable from `dummy.next` through `pre` contains exactly the already processed values that occurred once, in original sorted order. `pre.next` points to the first unprocessed run.

The inner loop finds that run's exact end. If first and last are the same object, the value occurs once and moving `pre` retains precisely that node. Otherwise the value occurs at least twice and bypassing the entire run removes precisely all of its nodes. Both choices preserve the invariant.

When `cur` becomes `None`, every run has been classified. `dummy.next` therefore begins a sorted list containing exactly values with original frequency one.

## Complexity detail

Let $n$ be the number of nodes. Although there are nested loops, `cur` only moves forward and visits each node at most once. Pointer comparisons and rewiring are constant time, so total time is $O(n)$, matching the manifest.

The algorithm allocates one dummy node and stores two pointer variables. It uses no recursion, array, set, or map, so auxiliary space is $O(1)$, also matching the manifest. Removed nodes are reused input objects that merely become unreachable from the returned head.

## Alternatives and edge cases

- **Saved run value:** Detect a duplicate pair, store its value, advance beyond all equal nodes, and connect the predecessor to the first different node. This is the competitive variant's style.
- **Frequency map:** Count values and build links only for frequency-one nodes. It ignores sorted grouping and uses extra space.
- **Recursive run removal:** Process the first run and recurse on the remainder. It is concise but uses $O(n)$ stack space in the worst case.
- **Empty list:** `cur` is `None`, the loop is skipped, and `dummy.next` is `None`.
- **One node:** First and last run nodes are identical, so the node is retained.
- **All nodes equal:** The sentinel bypasses the complete run and the result is empty.
- **Duplicate run at the head:** The dummy supplies the predecessor needed to remove it.
- **Duplicate run at the tail:** `cur.next` is `None`, so bypass terminates the retained list correctly.
- **Adjacent duplicate runs:** `pre` stays fixed after each deletion and reconnects directly to the next candidate run.
- **Negative values:** Only equality and sorted adjacency matter.
- **Node identity:** `pre.next == cur` asks whether they are the same node, not merely whether values match.
- **Sorted guarantee:** Without it, equal values could occur in separate runs and this local classification would be insufficient.
