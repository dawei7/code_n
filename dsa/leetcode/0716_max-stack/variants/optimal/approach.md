## General

The data structure needs two different orderings over the same elements:

- stack order, so the most recently pushed remaining element is accessible;
- value order, so the largest remaining value is accessible, with the most recently pushed copy chosen among equal maxima.

The exact solution stores each element as one shared node in:

- a doubly linked list ordered by pushes;
- a `SortedList` ordered by `node.val`.

Because both structures hold references to the same node object, removing from one reveals exactly which object must be removed from the other.

**Doubly linked list as the stack**

The list has permanent head and tail sentinels. Real nodes lie between them.

`append` inserts immediately before the tail, making that node the stack top. It updates four links and returns the node reference.

`peek` reads `tail.prev.val`.

`pop` removes `tail.prev` through the general constant-time `remove(node)` helper.

Given a node reference, doubly linked removal needs no search:

`node.prev.next = node.next` and `node.next.prev = node.prev`.

This ability is crucial for `popMax`, which may remove a node from the middle of stack order.

**SortedList as the value ordering**

`self.sl = SortedList(key=lambda x: x.val)` orders node objects by their values.

The final entry `sl[-1]` has maximum value. `peekMax` reads it, and `popMax` removes it.

When equal-valued nodes are added, the sorted container places the newer equal-key node after existing equal-key nodes. Therefore, the final entry among maximum values is the top-most—that is, most recently pushed—maximum occurrence.

This tie behavior is exactly the contract for `popMax`.

**Pushing**

`push(x)` first appends a new node to stack order and receives its reference. It then adds that same reference to the sorted structure.

After both steps:

- the linked-list tail identifies it as newest;
- the sorted list positions it among equal or ordered values.

Neither structure contains a copy with an independent identity.

**Ordinary pop**

`stk.pop()` removes and returns the linked-list top node in constant time.

That node still appears in `sl`, so `sl.remove(node)` removes the exact object from value order. Node equality defaults to object identity because `Node` defines no custom equality.

Returning `node.val` yields stack semantics.

**Top and maximum queries**

`top` reads the last linked-list node and changes nothing.

`peekMax` reads the final sorted node and changes nothing.

Both structures remain synchronized.

**Removing the maximum**

`node = self.sl.pop()` removes the final sorted entry: a maximum-valued node, and among equal maxima the newest one.

`DoubleLinkedList.remove(node)` then splices that exact node out of stack order in constant time, even if it is in the middle.

The value is returned.

**A trace**

Push `5`, then `1`, then `5`.

Stack order is first-`5 -> 1 -> second-5`. Value order ends with the two fives, with the second pushed five last among their equal keys.

- `top()` returns the second `5`.
- `popMax()` chooses that same second `5`, removes it from both structures, and returns five.
- Stack order becomes `5 -> 1`.
- `top()` returns one, while `peekMax()` returns the older five.

This demonstrates why duplicate maxima need node identity and stable equal-key ordering.

**Synchronization invariant**

After every completed public operation:

- every live stack element corresponds to exactly one real linked-list node;
- `sl` contains exactly those same node objects;
- linked-list order is push order after deletions;
- sorted-list order is nondecreasing value, with insertion order resolving equal keys.

Push adds one object to both. Pop removes one object from both starting from stack order. PopMax removes one from both starting from value order. Read operations alter neither.

By induction, the structures never disagree.

**Why one ordinary stack is insufficient**

A stack with running maximums can answer `peekMax` quickly, but removing a maximum below the top would require popping and later restoring all nodes above it. That is linear in the worst case.

The doubly linked list plus an ordered handle structure supports removal at either ordering's endpoint without scanning the other ordering.

## Complexity detail

Let `n` be the current number of elements.

- `push` performs constant-time linked append and `O(\log n)` sorted insertion.
- `pop` performs constant-time linked removal and `O(\log n)` sorted removal.
- `top` reads `tail.prev` in `O(1)`.
- `peekMax` reads the final sorted entry in `O(1)` for the used `SortedList` endpoint access.
- `popMax` removes the final sorted entry in `O(\log n)` and splices its linked node in `O(1)`.

Across `q` operations, a safe aggregate bound is `O(q\log q)`.

Each live value has one node referenced by both structures. Sentinels add constant storage. Total space is

$$
O(n),
$$

or `O(q)` over a sequence that only grows to at most `q` live nodes.

## Alternatives and edge cases

- **Two balanced trees with unique push IDs:** Order one tree by ID and one by `(value, ID)`. It provides the same asymptotic operations without linked nodes.

- **Heap plus lazy deletion:** Keep a stack, max-heap, unique IDs, and a removed-ID set. It offers amortized logarithmic updates but requires cleanup logic.

- **Stack with maximum prefix:** Excellent for `peekMax`, but `popMax` can be linear when the maximum is below the top.

- **Duplicate maxima:** The newest equal maximum must be removed. Equal-key insertion order in the sorted container supplies this tie-break.

- **Negative values:** Value sorting handles them normally.

- **Single element:** Top and maximum are the same node; either pop method empties both structures consistently.

- **Removing a middle node:** Doubly linked pointers make it constant time once `sl` supplies the node reference.

- **Nonempty-operation guarantee:** Pop and peek methods never face only sentinel nodes.

- **Shared identity:** Storing raw duplicate values in both structures would not identify which occurrence to remove; node references solve this.

- **Library dependency:** The complexity relies on `SortedList` providing logarithmic add/remove and efficient endpoint access.

- **Sentinel nodes:** They eliminate special cases when inserting or removing the first or last real node.
