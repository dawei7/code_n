## General
**Recognize the order of each sign**

Nonnegative nodes already appear in non-decreasing signed order because their
absolute values are their values. Negative nodes appear in the opposite signed
order: as their magnitudes increase, their actual values decrease. Therefore
the negative nodes must be reversed ahead of the nonnegative portion, while
the relative order of nonnegative nodes can remain unchanged.

**Move each encountered negative node to the front**

Keep `current` at a node that remains in the nonnegative chain. Inspect
`current.next`. If that next node is negative, detach it, link it before the
current head, and update the head; do not advance `current`, because its next
link has changed. If the next node is nonnegative, advance normally.

Each later negative node has absolute value at least as large as every earlier
node, so its signed value is no greater than all negative nodes already moved
to the front. Prepending it preserves sorted order within the negative prefix.
Meanwhile, untouched nonnegative nodes retain their original sorted order.

**Join the two orders without extra storage**

Moving nodes to the head automatically leaves the negative prefix connected to
the original nonnegative chain. Every negative node is moved exactly once and
every nonnegative node is passed once. At completion, all negatives precede
zero and positives, both regions are internally non-decreasing, and their
boundary is ordered, proving the full list is sorted.

## Complexity detail
The traversal inspects and relinks each of the $N$ nodes a constant number of
times, for $O(N)$ time. Only node references are retained, so auxiliary space
is $O(1)$.

## Alternatives and edge cases
- **Collect values and sort:** Reading all values and sorting them takes
  $O(N\log N)$ time and $O(N)$ space, and may overwrite rather than relink
  nodes.
- **Linked-list insertion sort:** Inserting each node into a sorted prefix is
  correct but can take $O(N^2)$ time.
- A list with no negative values is returned without structural changes.
- An all-negative input is reversed into increasing signed order.
- A positive node followed by a negative node with the same absolute value
  must be reordered.
- Zero belongs with the nonnegative chain and follows every negative value.
- Duplicate equal values may change node identity order without changing the
  required value sequence.
- A single-node list is already sorted.
