## General

**Avoid all rewiring when the input is already sorted**

The competitive source begins with two early exits. An empty list returns immediately, and `isSorted` scans adjacent pairs to determine whether the whole list is already non-decreasing.

If so, the original head is returned without allocating a dummy or changing any link. This guarantees $O(n)$ best-case time for sorted input.

If an inversion exists, the method performs insertion sort with:

- `sorted_tail`: the final node of the sorted prefix;
- `cur`: the first node outside that prefix;
- `dummy`: a permanent predecessor before the real head.

Initially the prefix contains only `head`, so `sorted_tail = head` and `cur = head.next`.

**Search for the first value not smaller than `cur`**

For each current node, `prev` starts at `dummy` and advances while:

`prev.next.val < cur.val`

When the loop stops, `prev.next` is the first sorted-prefix node whose value is greater than or equal to `cur.val`, unless `prev` has reached `sorted_tail`.

There is no explicit `prev.next is not None` guard. It is safe because `cur` currently follows `sorted_tail`. At worst the search reaches `sorted_tail`, whose `next` is `cur`, and `cur.val < cur.val` is false.

The dummy value `-2147483648` is below the Reference’s minimum node value, but the search actually compares `prev.next.val`; the dummy mainly supplies a predecessor for insertion before the head.

**Recognize when no relocation is needed**

If `prev == sorted_tail`, every value in the sorted prefix is strictly less than `cur.val`. The current node already follows that tail and belongs there.

The method advances both pointers:

- `cur` moves to the next unprocessed node;
- `sorted_tail` becomes the current node.

This is the append fast path.

**Relocate the current node with simultaneous assignment**

Otherwise, `cur` must be inserted after `prev` and before `prev.next`. The compact assignment:

`cur.next, prev.next, sorted_tail.next = prev.next, cur, cur.next`

first evaluates all three old right-hand references. It then:

- points `cur` to the old successor of `prev`;
- points `prev` to `cur`;
- points `sorted_tail` to `cur`’s old successor, removing `cur` from its former position.

Afterward, `cur = sorted_tail.next` selects the next unprocessed node. `sorted_tail` remains the same object because the moved node was inserted earlier in the prefix.

Rewriting this assignment as naive sequential statements could lose `cur.next` before it is used to reconnect the unsorted remainder. Explicit temporary variables are required in languages without Python’s tuple-assignment semantics.

**Why the prefix invariant proves sorted output**

The append branch adds a value larger than every prefix value. The relocation branch inserts before the first value greater than or equal to it, so values before are smaller and values after are at least as large. Existing prefix order is otherwise unchanged.

Each iteration incorporates exactly one node, and `cur` advances through the original unprocessed order. When `cur` becomes null, every node is in the sorted prefix, and `dummy.next` is its head.

The use of `<` means a moved node is inserted before earlier equal values. The result is correctly non-decreasing but not stable: equal-valued node identities may reverse relative order. Stability is not required by the Reference.

## Complexity detail

Let $n$ be the list length.

`isSorted` costs $O(n)$ in the worst case. If it succeeds, that is the complete runtime.

Otherwise, the outer insertion loop processes $O(n)$ nodes, and each search can inspect $O(n)$ prefix nodes. Overall worst-case time is $O(n^2)$; the preliminary linear scan is absorbed by that bound.

One dummy node and a fixed number of pointers are allocated, so auxiliary space is $O(1)$. All original nodes are reused and only their links change.

## Alternatives and edge cases

- **Stable insertion scan:** Use `<=` rather than `<` to insert a later equal value after prior equals. This preserves node order while keeping the same bounds.
- **No preliminary sortedness scan:** The main algorithm already has an append path, so correctness does not require `isSorted`; removing it avoids a duplicate pass on inputs that become unsorted late.
- **Merge sort:** It offers $O(n\log n)$ worst-case time for linked lists but is a different sorting algorithm from the requested insertion sort.
- **Empty or one-node list:** The first condition returns immediately.
- **Already sorted:** `isSorted` returns true and no node is relinked.
- **Equal-valued nodes:** Output values are correct, but the `<` insertion rule can change their identity order.
- **New minimum:** Search stops with `prev = dummy`, making the node the new real head.
- **Current maximum:** Search reaches `sorted_tail`, and the fast path leaves the node in place.
- **Sentinel range:** The chosen dummy value is below all allowed values, though correctness mainly relies on its pointer role.
- **Object equality:** `prev == sorted_tail` uses default identity behavior for `ListNode`; identity comparison would be clearer if node equality were ever overloaded.
- **Recursive representation:** The helper’s `__repr__` follows the full list and could recurse deeply, but sorting never calls it.
