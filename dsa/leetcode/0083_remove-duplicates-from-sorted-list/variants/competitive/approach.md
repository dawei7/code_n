## General

**Keep the first node and locate the end of its run**

`cur` points to the node chosen as the retained representative of the current sorted value. A second pointer, `runner`, starts at `cur.next` and advances while its value equals `cur.val`. When it stops, it points to the first node with a different value or to `None` after the list.

Since equal values are contiguous in a sorted list, every node passed by `runner` is an extra copy of `cur`'s value, and no equal copy can occur after `runner` stops at a different value.

**Reconnect the representative directly to the next run**

After the inner loop, `cur.next = runner` bypasses every extra node in the current run at once. If there were no duplicates, `runner` was already the original next node and the assignment changes nothing. If the run reached the tail, `runner` is `None` and the retained representative becomes the new tail.

The source then sets `cur = runner`. This advances to the representative candidate for the next distinct run. Unlike an algorithm that deletes duplicates one at a time, it does not need to hold `cur` and repeatedly compare each newly exposed successor; `runner` has already found the run boundary.

**Trace a long run**

For `1 -> 1 -> 1 -> 2 -> 3 -> 3`, `cur` begins at the first 1 and `runner` walks across the second and third ones to 2. Reconnecting makes the list begin `1 -> 2`, with the skipped copies unreachable from the head. `cur` becomes 2.

The runner for 2 stops immediately at 3 because the values differ, so 2's link remains. At the first 3, runner advances past the final 3 to `None`, and reconnecting makes the first 3 the tail. The result is `1 -> 2 -> 3`.

The retained node for each value is always the run's first node. The problem asks for one value occurrence, so this choice is valid and preserves relative order.

**Why the outer loop needs only `while cur`**

The inner loop checks `runner` before reading its value. A final `cur` with no successor creates `runner = None`; the inner loop is skipped, `cur.next` is assigned `None`, and `cur` becomes `None`. Empty input also skips the outer loop entirely.

This uniform handling means no separate final-node branch is necessary.

**A run-level invariant**

Before each outer iteration, all runs before `cur` have been reduced to one node and linked in original sorted order. `cur` is the first node of the next unprocessed run.

The runner loop finds the first node after that complete run. Linking `cur` to it removes all later copies but keeps `cur`, so the current run now has exactly one representative. Advancing `cur` to `runner` establishes the invariant for the next run.

When `cur` becomes `None`, every original run has been processed. The chain beginning at `head` therefore contains one node for every distinct input value, and because links only skip forward, sorted order remains intact.

**Why returning `head` remains valid**

This contract never removes all copies of a duplicated value; it keeps the first node. The original head, when nonempty, is consequently always retained as the representative of its value. Pointer rewrites happen after it, so the answer head never changes. Returning `head` works for both unique and duplicated head runs.

**The additional recursive method is not the selected path**

The class also contains `deleteDuplicates2`, a recursive alternative. The harness calls `deleteDuplicates`, so the iterative runner method is the selected implementation explained here. If called directly, the recursive method can use linear call-stack space and should not be used as evidence for the selected method's constant-space bound.

Its recursion also retains a representative by recursing through equal neighbors and reconnecting distinct nodes on return. It is functionally related but operationally separate.

**Difference from deleting every repeated value**

The runner deliberately starts after a representative and reconnects from that representative. For `[1,1,2]`, it returns `[1,2]`. A solution to the related problem that removes all repeated values would need a predecessor before the run and would discard both 1 nodes. This source correctly implements the keep-one contract.

## Complexity detail

Let $n$ be the node count. Across all outer iterations, `runner` moves forward over each skipped or next-run node only a constant number of times, and `cur` moves from one run representative to the next. Total time is $O(n)$, matching the manifest.

The selected method stores two pointers and rewires existing nodes. It is iterative and allocates no size-dependent structure, so auxiliary space is $O(1)$, matching the manifest. The module-level `ListNode` is platform/harness structure, not per-input working storage.

## Alternatives and edge cases

- **One-at-a-time bypass:** Compare `cur` with `cur.next`, remove an equal successor, and advance only on a different value. It uses one pointer and is the optimal variant's style.
- **Recursive `deleteDuplicates2`:** It is present but unselected and uses $O(n)$ stack space in the worst case.
- **Copy into a new list:** It avoids modifying original links but violates constant-extra-space intent and needlessly allocates nodes.
- **Empty list:** `cur` is `None`, so the original `None` head is returned.
- **One node:** Runner is `None`, and the node remains the tail.
- **All values equal:** Runner reaches `None` in the first iteration, leaving only the head.
- **No duplicates:** Runner stops immediately at each next node, so the original links are effectively preserved.
- **Tail duplicates:** The final representative is linked to `None`.
- **Multiple long runs:** Each runner crosses one run and cur jumps directly to the next.
- **Value zero and negatives:** The algorithm compares actual node values and has no sentinel-value collision.
- **Head retention:** Keeping one copy makes the original head valid for every nonempty input.
- **Sorted guarantee:** It makes each runner stop the exact moment a value's entire run ends.
- **Input mutation:** Extra nodes become unreachable through pointer rewiring; no new result nodes are created.
