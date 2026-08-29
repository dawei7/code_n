## General

The class implements a singly linked list with two permanent pieces of metadata:

- `dummy`, a sentinel node placed before the first real node;
- `cnt`, the number of real nodes.

The sentinel eliminates special pointer logic at the head. Inserting or deleting real index zero becomes the same predecessor-based operation used for every other index.

**The structural invariant**

After every operation:

- `dummy.next` points to the first real node or `None` when empty;
- following `next` links visits exactly `cnt` real nodes;
- the final real node points to `None`.

The dummy node is never counted and its value is irrelevant.

**Getting a value**

`get(index)` first rejects `index < 0` or `index >= cnt`. This prevents traversal beyond the real list.

For a valid index, `cur` starts at `dummy.next`, which is real index zero. Moving `index` times reaches the requested node:

- zero moves for index zero;
- one move for index one;
- and so forth.

The method returns `cur.val` without modifying any link.

**One insertion primitive**

Both convenience methods delegate:

- `addAtHead(val)` calls `addAtIndex(0, val)`;
- `addAtTail(val)` calls `addAtIndex(cnt, val)`.

This prevents three insertion implementations from drifting apart.

`addAtIndex(index, val)` rejects only `index > cnt`. The source's indices are nonnegative. An index equal to `cnt` is valid and means append.

The pointer `pre` begins at `dummy`. Moving it `index` times reaches the predecessor of the insertion position. For index zero it remains the sentinel; for index `cnt` it reaches the last real node.

**The insertion link change**

The statement

`pre.next = ListNode(val, pre.next)`

must be read from the inside outward:

1. create a node whose `next` is the old `pre.next`;
2. change `pre.next` to the new node.

This places the new value between `pre` and the former successor without losing the remainder of the list.

Then `cnt` increases by one.

**Deleting by predecessor**

`deleteAtIndex(index)` does nothing when `index >= cnt`. Under the nonnegative-index contract, all remaining indices are valid.

As in insertion, `pre` starts at the dummy and advances `index` times, ending immediately before the target.

`t = pre.next` saves the target node. `pre.next = t.next` bypasses it, reconnecting the predecessor directly to the successor.

`t.next = None` detaches the removed node from the list. Python garbage collection does not require this for correctness, but it makes the removed node no longer reference the live suffix and expresses the deletion cleanly.

Finally, `cnt` decreases.

**Why the dummy node matters**

Without a sentinel, insertion at the head would need to replace a separate `head` variable, and deletion at index zero would need a separate branch. With the dummy, every real node—including the first—has a predecessor.

For head insertion, that predecessor is `dummy`. For head deletion, bypassing `dummy.next` uses exactly the normal link change.

**A trace**

Start empty with `dummy.next = None` and `cnt = 0`.

- `addAtHead(1)` inserts after dummy: list is `1`, count one.
- `addAtTail(3)` uses index one, reaches node `1` as predecessor, and appends `3`.
- `addAtIndex(1, 2)` reaches node `1` and inserts `2` before old successor `3`, forming `1 -> 2 -> 3`.
- `get(1)` starts at `1`, moves once, and returns `2`.
- `deleteAtIndex(1)` again finds predecessor `1` and changes its next link from `2` to `3`.

All operations preserve count and link structure.

**Why operations are correct**

For insertion, traversal finds exactly the node preceding the requested zero-based position. The new node points to the old successor before the predecessor is redirected, so no existing node is lost. Count grows by one.

For deletion, traversal finds the predecessor of exactly the indexed node. Bypassing one link removes precisely that node and preserves the order of every other node. Count falls by one.

Get performs the corresponding number of steps from the first real node. Invalid operations return or do nothing before touching links.

By induction, the structural invariant and all interface results remain correct after any valid operation sequence.

## Complexity detail

Let `n` be the current number of real nodes and `i` a valid operation index.

- `get(i)` takes `O(i)` time.
- `addAtIndex(i, val)` takes `O(i)` time.
- `deleteAtIndex(i)` takes `O(i)` time.
- `addAtHead` delegates with index zero and takes `O(1)`.
- `addAtTail` delegates with index `n` and takes `O(n)`.

Each operation changes or creates only a constant number of nodes beyond traversal.

The list's persistent storage is

$$
O(n)
$$

for `n` real nodes plus one sentinel. Auxiliary working space per operation is `O(1)` because traversal is iterative.

## Alternatives and edge cases

- **Doubly linked list with head and tail sentinels:** It supports `O(1)` tail insertion and can reach an index from the closer end, at the cost of a previous pointer per node and more link updates.

- **Store a tail pointer:** This alone makes `addAtTail` constant time but requires careful maintenance when deleting the last node.

- **Empty-list get:** Count validation returns `-1` without dereferencing `None`.

- **Insert into empty list:** Only index zero is valid; the dummy becomes the new node's predecessor.

- **Append:** `index == cnt` is allowed, and traversal ends at the last node.

- **Index above length:** Insertion does nothing and count stays unchanged.

- **Invalid get or delete:** The contract's indices are nonnegative; out-of-range high indices are rejected.

- **Delete the head:** The predecessor is dummy, so its next link skips the first real node.

- **Delete the tail:** The predecessor's next becomes `None`.

- **Single-node deletion:** Dummy's next becomes `None` and count becomes zero.

- **Count consistency:** Increment and decrement occur only after a real structural change.

- **External `ListNode` helper:** Node construction and fields come from the platform-provided harness; the user implements only list operations.
