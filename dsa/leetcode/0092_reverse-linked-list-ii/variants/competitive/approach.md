## General

The competitive implementation reverses exactly the requested links in place and reconnects the reversed block to the surrounding list. Its variable names describe the final boundary roles:

- `last_unswapped` is the node immediately before the reversed interval;
- `first_swapped` is the interval's original first node, which becomes its last node;
- `prev` becomes the front of the reversed portion; and
- `cur` advances to the first node not yet reversed.

The length of the interval is computed once as `diff = n - m + 1`, using the source's parameter names `m` and `n` for the Reference's `left` and `right`.

**Establishing a uniform predecessor**

A dummy node is linked to `head`, then `last_unswapped` begins at that dummy. The first `while` loop advances `cur` and `last_unswapped` together until `m == 1`. At that point, `cur` is the original node at position `m`, and `last_unswapped` is its predecessor.

When the interval begins at position one, the loop runs zero times. `last_unswapped` remains the dummy and `cur` remains the original head, so the exact same later reconnection updates the head through `dummy.next`. This avoids a special case.

The loop condition includes `cur` defensively, although the contract guarantees that `m` is a valid node position. Decrementing `m` changes only a local integer; `diff` already preserved the original inclusive segment length.

**Reversing with simultaneous assignment**

The algorithm sets `prev = last_unswapped` and `first_swapped = cur`. Then, while there is a current node and `diff > 0`, it executes:

`cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1`

Python evaluates every expression on the right-hand side before assigning any target on the left. That semantic guarantee is crucial. In particular, the old `cur.next` is captured before `cur.next` is overwritten. The statement is equivalent to saving the next node, reversing the current link, advancing `prev`, advancing `cur`, and decreasing the remaining length—but without an explicit temporary variable.

After one iteration, the processed node points backward to the previous node. After `diff` iterations:

- `prev` points to the original node at position `n`, the new first node of the interval;
- `first_swapped` still points to the original node at position `m`, now the interval tail; and
- `cur` points to position `n + 1`, or `None` if the interval reached the list tail.

**Why starting `prev` at the predecessor works**

The first reversed node points to `last_unswapped`, temporarily making a backward connection to the prefix. Meanwhile, `last_unswapped.next` still points to `first_swapped`, so a short cycle exists during the operation. This is deliberate and safe because the reversal loop follows the separately saved `cur` reference, never the prefix's forward link.

The final simultaneous assignment

`last_unswapped.next, first_swapped.next = prev, cur`

repairs both boundaries. As with the earlier tuple assignment, the right-hand references are collected before mutation. The first target connects the untouched prefix to the new segment head. The second target connects the new segment tail to the untouched suffix, replacing its temporary backward pointer and removing the cycle.

**Trace for reversing positions 2 through 4**

For `1 -> 2 -> 3 -> 4 -> 5`, `diff` is three. The positioning loop leaves `last_unswapped` at `1` and `cur` at `2`; `first_swapped` is saved as `2`.

1. Processing `2` makes it point to `1`; `prev` becomes `2`, and `cur` becomes `3`.
2. Processing `3` makes it point to `2`; `prev` becomes `3`, and `cur` becomes `4`.
3. Processing `4` makes it point to `3`; `prev` becomes `4`, and `cur` becomes `5`.

The final reconnection makes `1.next` point to `4` and `2.next` point to `5`, yielding `1 -> 4 -> 3 -> 2 -> 5`.

**Why all unaffected nodes remain in order**

The positioning loop never edits a link. The reversal loop edits only the `next` field of the `diff` segment nodes. The prefix retains its internal links and changes only its last outgoing link during reconnection. The suffix is never modified; only the new segment tail is pointed at its first node. Therefore nodes outside the inclusive interval remain in their original relative order.

## Complexity detail

Let $N$ be the total number of nodes and $k=n-m+1$ the interval length, using the original parameter values. The first loop advances $m-1$ nodes, and the second processes $k$ nodes. Since the interval is valid, their combined work is at most $N$. Thus time is $O(N)$, and the algorithm satisfies the one-pass follow-up: no node is revisited through a second full traversal.

The dummy node plus a fixed set of references and counters occupy $O(1)$ auxiliary space. Reversal reuses existing nodes and allocates no collection or recursion stack. The top-level `ListNode` class definition is part of the source environment; the only runtime node allocation within the method is the single dummy.

## Alternatives and edge cases

- **Explicit temporary pointer:** Replace the dense tuple assignment with separate `next_node`, link reversal, and pointer-advance statements. It has identical complexity and is often easier for beginners to debug.
- **Head-insertion method:** Repeatedly move the node after the segment's original first node to the segment front. It preserves the predecessor pointer throughout and also uses $O(1)$ space.
- **Recursion:** A recursive partial reversal can work but consumes linear call-stack space and does not improve time.
- **Do not change tuple-assignment semantics casually:** Converting the simultaneous assignment into sequential assignments in the same textual order would read the already changed `cur.next` and lose the suffix. An explicit temporary is required when expanding it.
- **Segment begins at position one:** `last_unswapped` is the dummy, so updating its `next` automatically installs the new head.
- **Segment ends at the tail:** `cur` becomes `None`, and `first_swapped.next = cur` correctly terminates the reversed list.
- **Single-node segment:** `diff` is one. The loop briefly points the node backward, and the two final links restore the same visible list. It is correct even without an early return.
- **Whole list:** The dummy supplies the left connection and `None` supplies the right connection, producing an ordinary complete reversal.
- **Nonempty valid input:** The Reference guarantees a real head and valid positions. The defensive `cur` conditions do not define a reliable contract for invalid indices; callers should not depend on out-of-range behavior.
- **Node identity:** Links, not values, are reversed. External references to nodes therefore observe the requested structural reorder rather than merely seeing exchanged payloads.
