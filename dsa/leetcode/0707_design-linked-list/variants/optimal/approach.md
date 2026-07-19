## General
**Use sentinels at both ends**

Keep dummy head and tail nodes permanently linked around the real elements. Inserting or deleting beside either sentinel then uses the same pointer rewiring as an interior change, without special null-neighbor cases.

**Track size and choose the nearer direction**

Reject invalid indices using the stored size. To locate a valid element, walk forward from the head when the index is in the first half and backward from the tail otherwise. This takes $O(\min(index + 1, n - index))$ steps.

**Insert between known neighbors**

A helper links a new node between a predecessor and successor. Head and tail additions call it directly in $O(1)$. Indexed insertion normalizes a negative index to zero, rejects an index greater than the size, and inserts immediately before the node currently at that index; index `size` inserts before the tail.

**Delete by reconnecting neighbors**

After locating a valid indexed node, link its predecessor directly to its successor and decrement the size. Sentinel nodes are never valid deletion targets.

**Why the structure remains consistent**

Every insertion establishes both forward and backward links for the two affected boundaries, and every deletion repairs both directions across the removed node. The sentinels remain the unique outer nodes, while the size changes exactly once per successful mutation, so index validation and traversal continue to describe the stored sequence.

## Complexity detail
Head and tail insertion take $O(1)$ time. Lookup, indexed insertion, and deletion take $O(n)$ time in the worst case and $O(\min(i, n - i))$ traversal time for index `i`. The list stores one node per element plus two sentinels, using $O(n)$ space.

## Alternatives and edge cases
- **Singly linked list with a tail pointer:** endpoint insertion stays constant time, but predecessor-based deletion and some indexed operations can only traverse forward.
- **Singly linked list without a tail pointer:** it is correct but every tail insertion may scan the full list, making a sequence of tail additions quadratic.
- **Dynamic array:** indexed lookup is constant time, while interior insertion or deletion shifts later elements and takes linear time.
- Getting or deleting a negative or out-of-range index returns `-1` or does nothing, respectively.
- `addAtIndex` treats a negative index as zero and ignores an index greater than the current size.
- Inserting at index `size` is exactly a tail insertion.
- Deleting the only element reconnects the two sentinels and restores an empty list.
