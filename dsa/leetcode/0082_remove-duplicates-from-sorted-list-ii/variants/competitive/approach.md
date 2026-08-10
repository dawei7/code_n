## General

**Build the retained chain behind a sentinel**

`dummy` is a new node whose `next` will become the answer head. `pre` is the last node in the retained output chain, initially the dummy. `cur` is the first unclassified input node.

The dummy makes deletion of a repeated value at the original head identical to deletion anywhere else. There is always a predecessor link, `pre.next`, that can be aimed at the next retained candidate. The dummy's numeric value zero is never used in comparisons, so it cannot conflict with a legitimate zero-valued input node.

The module-level `ListNode` is harness structure; the task's core logic remains inside `Solution.deleteDuplicates`.

**Detect a repeated run from its first two nodes**

Because the input is sorted, a value occurs more than once exactly when the current node has a next node with the same value. The test `cur.next and cur.next.val == cur.val` recognizes the beginning of such a run.

When the test is true, the source stores `val = cur.val` before moving. It then advances `cur` while nodes still have that value. The loop stops at the first node with a different value or at `None`, so every node in the repeated run has been skipped—including the first copy.

This complete removal is essential. Keeping the first node and skipping only later copies would solve a different duplicate-removal problem.

**Reconnect without advancing the retained predecessor**

After skipping a repeated run, `pre.next = cur` connects the last retained node directly to the first different value, or to `None` when the repeated run reached the tail. `pre` itself does not advance because the algorithm retained nothing from the run.

If the next run is also repeated, the same predecessor link is simply updated again. This supports consecutive deleted runs and an arbitrary number of deleted values at the head.

The skipped nodes may retain their old internal `next` references, but no node reachable from `dummy.next` points to the run's first node. They are excluded from the returned list.

**Retain a singleton and advance both roles**

If the current node has no equal successor, sorted order proves its value occurs exactly once: any earlier equal node would have been adjacent in the same run, and no later equal node can appear after a different value.

The source links `pre.next = cur`, advances `pre = cur`, and then moves `cur = cur.next`. The retained node becomes the new tail of the output chain. Its original next link currently points to the next unclassified node; a later duplicate branch will repair that link if the next run must be deleted.

Explicitly assigning `pre.next = cur` even when it already has that link keeps the construction uniform. It is necessary after one or more preceding duplicate runs because `pre` may be the dummy or a much earlier singleton.

**Trace a head duplicate and following singleton**

For `[1,1,1,2,3]`, the first two nodes prove that value 1 is repeated. The inner loop advances `cur` across all three ones and stops at 2. `pre` is still the dummy, so `pre.next = cur` makes 2 the tentative answer head.

The 2 node has a different successor and is a singleton. It is linked, becomes `pre`, and `cur` moves to 3. The 3 is also retained. Returning `dummy.next` yields `[2,3]`.

For `[1,2,3,3]`, 1 and 2 are successively retained. When the 3 run is detected, `cur` advances to `None` and `pre.next = None` severs the retained 2 from the deleted tail.

**A precise invariant**

Before every outer iteration, the chain from `dummy.next` through `pre` contains exactly the singleton-value nodes in all fully processed runs, in sorted order. `cur` points to the first node of the next run, and `pre.next` either already points there or is ready to be rewritten.

For a repeated run, advancing past all equal nodes and linking `pre` to the remainder adds no forbidden value and preserves all prior singleton nodes. For a singleton run, linking and advancing `pre` adds exactly the one allowed node. These are the only run types.

At termination, no unprocessed run remains. The sentinel's next link therefore begins exactly the required list of original values that appeared once.

**Why the board-style “visited” issue does not arise**

Pointer rewiring is permanent because duplicate nodes must be removed from the returned structure. There is no backtracking or need to restore input links to their original shape. The method intentionally mutates the linked list, reusing its singleton nodes as the answer.

## Complexity detail

Let $n$ be the original node count. `cur` advances monotonically and passes each node once, whether in the outer loop or the duplicate-skipping inner loop. Total time is $O(n)$, matching the manifest.

Only one dummy node, two pointers, and one temporary run value are stored. Auxiliary space is $O(1)$, also matching the manifest. The returned nodes are reused from the input rather than copied.

## Alternatives and edge cases

- **First-versus-last node identity:** Advance to a run's final node and compare it with the predecessor's original next pointer. This avoids storing `val` and is the optimal variant's style.
- **Frequency counting:** It can handle unsorted data but requires a map and often a second pass.
- **Recursive solution:** Recurse past a repeated run or retain one singleton. It uses call-stack space proportional to list length.
- **Empty list:** The outer loop is skipped and `dummy.next` remains `None`.
- **Single node:** It follows the singleton branch and is returned.
- **All nodes repeated:** Every run is bypassed and the answer is empty.
- **Repeated head:** The dummy's next link is redirected without a head special case.
- **Repeated tail:** Linking `pre.next` to `None` correctly terminates the result.
- **Several deleted runs in sequence:** `pre` remains the last retained node while `cur` skips each run.
- **Singleton between duplicate runs:** It advances `pre`, after which the later run is bypassed from that singleton.
- **Value zero:** It cannot be confused with the dummy because only real node relationships and run values are examined.
- **Sorted-order dependency:** Equal values must be contiguous for the inner loop to classify total frequency.
- **Input mutation:** The returned list reuses nodes and intentionally changes `next` links.
