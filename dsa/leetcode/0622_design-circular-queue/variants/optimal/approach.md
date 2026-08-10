## General

**Create a logical circle on top of a fixed array.** An array is physically linear, but index arithmetic can wrap its last position back to position 0. The class stores four pieces of state:

- `q` is an array of exactly `k` slots;
- `capacity` is the fixed value `k`;
- `front` is the physical index of the current first element;
- `size` is the number of logical queue elements.

The central invariant is that for every offset `t` from 0 through `size - 1`, the queue's logical element at position `t` lives at

$$
(\texttt{front}+t)\bmod \texttt{capacity}.
$$

Modulo is what turns a physical array into a ring. If the computed index reaches `capacity`, it wraps to 0.

**Why `size` is needed.** In a circular representation, `front` can be 0 when the queue is empty, partially filled, or full. The front index alone cannot distinguish those states. Tracking the exact size makes the boundary conditions unambiguous:

- empty means `size == 0`;
- full means `size == capacity`.

The constructor begins with `front = 0` and `size = 0`. The zeroes initially placed in `q` are merely unused storage; they are not queue elements because the size is zero.

**Enqueue at the first slot after the logical rear.** When `size` elements are present, they occupy offsets 0 through `size - 1`. The next free logical offset is therefore `size`, whose physical location is

`(front + size) % capacity`.

`enQueue` first calls `isFull()`. If all slots are live, writing would overwrite the oldest element, so it returns `False` without changing any state. Otherwise it writes the value at the formula's index, increases `size` by one, and returns `True`. Increasing size after the write expands the live logical range to include precisely that slot.

**Dequeue by moving the logical boundary.** FIFO removal always removes the element at `q[front]`. The method does not need to erase that physical cell. Instead, it advances

`front = (front + 1) % capacity`

and decreases `size`. The old value may remain in memory, but it lies outside the live offset range and cannot be observed through `Front` or `Rear`. A later enqueue may safely overwrite it after indices wrap.

If the queue is empty, `deQueue` returns `False` and leaves state unchanged. This guard also prevents size from becoming negative.

**Read the front and rear from the invariant.** When nonempty, the first element is directly `q[front]`. The last logical element has offset `size - 1`, so `Rear` uses

`q[(front + size - 1) % capacity]`.

Both accessors return `-1` on an empty queue. The input values are constrained to 0 through 1000, so `-1` cannot be confused with a valid stored value.

**Walk through wraparound.** With capacity 3, enqueueing 1, 2, and 3 stores them at indices 0, 1, and 2. The queue is full. Dequeue removes logical value 1 by moving `front` to 1 and reducing size to 2; the stale 1 remains physically at index 0 but is no longer live. Enqueueing 4 computes

`(1 + 2) % 3 = 0`,

so it reuses the free position at the beginning of the array. Logical order is now indices 1, 2, 0, containing 2, 3, 4. `Rear` computes the same wrapped index 0 and returns 4.

**Why every operation preserves correctness.** Assume the invariant holds before an operation. A successful enqueue writes at offset `size`, immediately after every existing element, and then extends the live range by one. A successful dequeue removes offset 0 by advancing the front to the old offset 1 and shortening the range; all remaining elements retain their relative order. Read operations use the exact offset formulas without changing state. Failed operations change nothing. By induction over the call sequence, the array segment viewed through modular offsets always equals the required FIFO queue.

The implementation intentionally avoids a built-in queue. The plain array is only storage; the class itself implements all queue semantics and circular reuse.

## Complexity detail

Every public operation performs a fixed number of comparisons, arithmetic operations, array accesses, or assignments. `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull` are each $O(1)$ time.

If $Q$ method calls are made, their total time is $O(Q)$, which is the manifest's sequence-level time bound. Initialization allocates an array of length $k$, taking $O(k)$ time and space. The persistent queue storage remains $O(k)$ for the object's lifetime, while all scalar metadata uses $O(1)$ space.

Modulo by `capacity` is safe because the constraint guarantees $k\ge1$. The implementation is not thread-safe: a check and its following mutation are multiple steps, so concurrent unsynchronized calls could violate `size` or overwrite slots. Thread safety is outside the challenge contract and would require locking.

## Alternatives and edge cases

- **Head and tail indices with one unused slot:** Reserve one physical slot so equal indices mean empty and the next tail equaling head means full. This removes `size` but requires an array of capacity `k + 1`.
- **Head, tail, and size:** Store the next insertion index explicitly. This makes enqueue slightly more direct but adds redundant state that must remain synchronized.
- **Singly linked list:** Keep head and tail node references plus a count. Operations remain constant time and allocation grows with occupancy, but every enqueue allocates a node and the representation is not a physical ring.
- **Capacity one:** Front and rear use the same slot. After one enqueue the queue is full; after dequeue it is empty; modulo arithmetic still works.
- **Empty access:** `Front` and `Rear` return `-1`, while `deQueue` returns `False`, and no state changes.
- **Full enqueue:** It returns `False` before writing, preventing loss of the oldest element.
- **Stale array values:** Dequeue need not clear a slot because `size` defines which positions are live.
- **Repeated wraparound:** Modulo makes any number of enqueue/dequeue cycles reuse all slots correctly.
- **Allowed value zero:** Initial zero-filled slots do not create ambiguity because occupancy is determined only by `size`.
- **Invalid zero capacity:** The official constraint excludes it; otherwise modulo operations would divide by zero and no value could be stored.
- **Concurrent callers:** The class requires external synchronization if used across threads; constant-time logic alone does not make compound state updates atomic.
