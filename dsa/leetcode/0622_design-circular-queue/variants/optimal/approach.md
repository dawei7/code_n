## General
**Represent state with a head and count**

Allocate exactly `k` array slots. Store the index of the current front in `head` and the number of occupied slots in `count`. The queue is empty exactly when `count == 0` and full exactly when `count == k`, so the two states remain unambiguous even when indices wrap.

**Derive insertion and rear positions**

The next free slot is `(head + count) % k`. On a successful enqueue, write there and increment `count`. When nonempty, the rear is one position before the next insertion slot: `(head + count - 1) % k`.

**Remove by advancing rather than shifting**

A successful dequeue moves `head` to `(head + 1) % k` and decrements `count`; no stored elements move. Old values outside the occupied circular range are irrelevant and may remain in the array.

**Why FIFO order survives wrap-around**

The occupied queue always consists of `count` consecutive circular positions starting at `head`. Enqueue extends that range at its end, while dequeue removes exactly its first position. Both operations preserve the invariant, so `Front` and `Rear` always address the oldest and newest live values respectively.

## Complexity detail
For `Q` operations, each method performs a constant number of arithmetic, indexing, or state operations, giving $O(Q)$ total time and $O(1)$ time per call. The fixed backing array occupies $O(k)$ space.

## Alternatives and edge cases
- **Linked list with head and tail:** supports the same $O(1)$ operations and tracks capacity with a count, but allocates one node per live value.
- **Linked list without a tail pointer:** remains correct but searches from the head for every enqueue, costing $O(k)$ per insertion and $O(Qk)$ over a trace.
- **Array with one deliberately unused slot:** distinguishes full from empty using indices alone, but must allocate $k + 1$ positions to provide capacity `k`.
- Capacity one must distinguish its empty and full states even though head and rear share an index.
- `Front` and `Rear` return `-1` on an empty queue.
- Enqueue on full and dequeue on empty return false without changing state.
- Repeated dequeue/enqueue cycles must wrap indices and reuse freed slots.
