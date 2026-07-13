# Design Circular Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 622 |
| Difficulty | Medium |
| Topics | Array, Linked List, Design, Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/design-circular-queue/) |

## Problem Description
### Goal
Design a circular queue, also called a ring buffer: a fixed-capacity FIFO data structure in which the position after the final storage slot wraps back to the first slot. Reusing freed positions at the front allows later insertions without shifting the remaining values.

Implement construction with capacity `k`, `enQueue(value)`, `deQueue()`, `Front()`, `Rear()`, `isEmpty()`, and `isFull()`. Insertion and deletion report whether they succeed, endpoint queries return `-1` when the queue is empty, and failed operations leave the state unchanged. All operations should run in constant time without using a built-in queue implementation.

### Function Contract
**Inputs**

- `MyCircularQueue(k)`: construct an empty queue with positive capacity `k`
- `enQueue(value)`: append a value and report whether insertion succeeds
- `deQueue()`: remove the front value and report whether removal succeeds
- `Front()` / `Rear()`: return the corresponding value, or `-1` when empty
- `isEmpty()` / `isFull()`: report the current state

**Return value**

- The operation trace returns null for construction and the documented result for every later call
- Failed insertion or removal leaves the queue unchanged

### Examples
**Example 1**

- Operations: construct capacity 3; enqueue 1, 2, 3, then 4; query rear and full; dequeue; enqueue 4; query rear
- Output: `null, true, true, true, false, 3, true, true, true, 4`

**Example 2**

- Operations: construct capacity 1; query front; enqueue 7; query front and rear
- Output: `null, -1, true, 7, 7`

### Required Complexity

- **Time:** $O(Q)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Represent state with a head and count**

Allocate exactly `k` array slots. Store the index of the current front in `head` and the number of occupied slots in `count`. The queue is empty exactly when `count == 0` and full exactly when `count == k`, so the two states remain unambiguous even when indices wrap.

**Derive insertion and rear positions**

The next free slot is `(head + count) % k`. On a successful enqueue, write there and increment `count`. When nonempty, the rear is one position before the next insertion slot: `(head + count - 1) % k`.

**Remove by advancing rather than shifting**

A successful dequeue moves `head` to `(head + 1) % k` and decrements `count`; no stored elements move. Old values outside the occupied circular range are irrelevant and may remain in the array.

**Why FIFO order survives wrap-around**

The occupied queue always consists of `count` consecutive circular positions starting at `head`. Enqueue extends that range at its end, while dequeue removes exactly its first position. Both operations preserve the invariant, so `Front` and `Rear` always address the oldest and newest live values respectively.

#### Complexity detail

For `Q` operations, each method performs a constant number of arithmetic, indexing, or state operations, giving $O(Q)$ total time and $O(1)$ time per call. The fixed backing array occupies $O(k)$ space.

#### Alternatives and edge cases

- **Linked list with head and tail:** supports the same $O(1)$ operations and tracks capacity with a count, but allocates one node per live value.
- **Linked list without a tail pointer:** remains correct but searches from the head for every enqueue, costing $O(k)$ per insertion and $O(Qk)$ over a trace.
- **Array with one deliberately unused slot:** distinguishes full from empty using indices alone, but must allocate $k + 1$ positions to provide capacity `k`.
- Capacity one must distinguish its empty and full states even though head and rear share an index.
- `Front` and `Rear` return `-1` on an empty queue.
- Enqueue on full and dequeue on empty return false without changing state.
- Repeated dequeue/enqueue cycles must wrap indices and reuse freed slots.

</details>
