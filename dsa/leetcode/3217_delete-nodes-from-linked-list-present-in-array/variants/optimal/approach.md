## General

Let $m = \lvert\texttt{nums}\rvert$ and let $n$ be the number of linked-list nodes.

**Make deletion tests independent of the array length.** Put every value from `nums` into a hash set. During the list traversal, each node can then be classified with one expected-$O(1)$ membership lookup instead of searching the array repeatedly.

**Unlink nodes without losing the traversal.** Attach a dummy node before the original head and maintain `previous`, the last node known to be retained, together with `current`, the node being inspected. When `current.val` belongs to the deletion set, redirect `previous.next` to `current.next` but do not advance `previous`. Otherwise, retain `current` and advance `previous` to it. In both cases, advance `current` to the next original node.

The dummy node applies the same update when one or several leading nodes are removed. Every retained node is encountered once and linked after the preceding retained node, so the output contains exactly the allowed nodes in their original order.

## Complexity detail

Building the hash set takes expected $O(m)$ time, and the traversal takes $O(n)$ expected time, for $O(m+n)$ total expected time under standard hash-table behavior. The deletion set stores $m$ values, so the auxiliary space is $O(m)$; pointer updates reuse the existing list nodes.

## Alternatives and edge cases

- **Search `nums` for every node:** This avoids the hash set but requires $O(mn)$ time in the worst case.
- **Build a new linked list:** Copying every retained value is correct but allocates $O(n)$ additional nodes when in-place relinking is sufficient.
- A run of deleted nodes at the beginning is handled through the dummy node, including changes to the returned head.
- Consecutive deleted nodes in the middle must all be skipped without advancing the retained predecessor.
- Repeated list values are judged independently; every occurrence of a forbidden value is removed.
- If no list value belongs to `nums`, all original links and the original head remain valid.
