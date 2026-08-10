## General

**Split so the reversed side is never shorter**

The competitive source also finds a midpoint, reverses the suffix, and alternates the two chains. Its split convention differs from the optimal variant.

`fast`, `slow`, and `prev` begin at the head, head, and `None`. Every loop iteration moves fast by two, slow by one, and records slow’s previous node in `prev`.

When traversal stops:

- for an even-length list, `slow` begins a second half of equal length;
- for an odd-length list, `slow` is the middle node, so the second half contains one more node than the first.

The simultaneous assignment:

`current, prev.next, prev = slow, None, None`

saves `slow` as the second-half start, cuts the first half after the old `prev`, and resets `prev` for reversal. Python evaluates all right-hand values before performing the assignments, so the old predecessor is still available as the `prev.next` target when the cut occurs.

Lists of length zero or one return early, so `prev` is a real node whenever this split assignment is reached.

**Reverse the complete second half**

Starting with `current = slow` and `prev = None`, the reversal statement:

`current.next, prev, current = prev, current, current.next`

also relies on simultaneous right-hand evaluation. It saves the old successor before overwriting `current.next`, points the current node backward, and advances both state pointers.

At completion, `prev` is the original tail and heads the reversed suffix.

For five nodes, the original halves are `1->2` and `3->4->5`; reversal makes the second half `5->4->3`. For four nodes, the halves are `1->2` and `3->4`, with reversed suffix `4->3`.

**Alternate through a dummy head**

The source names the two chains `l1` and `l2`. A new dummy node is used only as a merge anchor; it is not part of the final list.

While both chains are nonempty, the loop first appends one `l1` node and then one `l2` node. Each tuple assignment:

- attaches the selected node after `current`;
- moves `current` to that attached node;
- advances the selected list to its saved old successor.

The order is therefore first-front, first-back, second-front, second-back, and so on.

For four nodes, the pairs consume both halves completely and yield `1->4->2->3`.

For five nodes, the merge consumes `1,5,2,4`, after which `l1` is empty and `l2` still references `3`. The loop does not explicitly append that remainder. It remains connected because node `4` was followed by node `3` in the reversed second half, and the append operation did not overwrite `4.next` afterward. The final order is `1->5->2->4->3`.

This detail works because the split guarantees that `l2` has either the same length as `l1` or exactly one extra node. There can never be an unconnected remainder in `l1`.

**Why no stale link creates a cycle**

Cutting `prev.next = None` terminates the first half before reversal. Reversal terminates its old first node by pointing it to `None`. During merge, every selected first-half node is linked to a reversed node, and each selected reversed node already points toward the next remaining reversed node until it is redirected on a subsequent alternation.

All links progress through nodes not yet output or end at `None`; no node points back into the completed prefix. The final result contains every original node exactly once.

The source returns `dummy.next`, which is the original `head` for lists of length at least two. The Reference says to return nothing, so this return value is unnecessary but does not interfere with the in-place mutation. For length zero or one it similarly returns `head`.

## Complexity detail

Let $n$ be the list length.

The midpoint pass, reversal pass, and alternating merge each process at most $n$ nodes and together take $O(n)$ time.

The implementation uses a fixed number of pointers and allocates one dummy node. One node is constant storage, so auxiliary space is $O(1)$, matching the manifest.

It allocates no replacement nodes for the actual list and does not copy values.

## Alternatives and edge cases

- **Split with the center in the first half:** This is the optimal variant’s convention. It makes the second half never longer and merges while the reversed half exists.
- **Node-reference array:** Indexing from the front and back makes the target order obvious but requires $O(n)$ memory.
- **Tail extraction per round:** It avoids an array but repeatedly scans for the last node, producing $O(n^2)$ time.
- **Empty list outside the Reference constraint:** The early return handles it without dereference.
- **One node:** The early return preserves the list.
- **Two nodes:** The halves each contain one node; alternating them reproduces the original order.
- **Odd length:** The middle belongs to the reversed second half and survives as its one-node remainder after paired merging.
- **Even length:** Both halves are exhausted together.
- **Tuple-assignment semantics:** Rewriting the compact assignments sequentially requires explicit temporaries; otherwise old successors or the old `prev` can be lost.
- **Return-contract mismatch:** The function mutates correctly but returns a head node even though the native contract expects no meaningful return value.
- **Dummy allocation:** Constant auxiliary space allows a fixed one-node helper; the dummy is not linked into the returned real chain.
- **Recursive `__repr__` caveat:** Printing a cyclic or extremely long malformed list through the helper’s recursive representation could recurse indefinitely or deeply, but `reorderList` does not call it.
