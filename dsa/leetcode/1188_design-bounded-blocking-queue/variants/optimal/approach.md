## General

A bounded blocking queue must satisfy several requirements at the same time. It stores elements in first-in, first-out order, never holds more than `capacity` elements, makes a producer wait when no slot is free, makes a consumer wait when no item exists, and remains correct when several threads interleave unpredictably.

The exact solution combines a double-ended queue with two semaphores:

- `s1` counts available storage slots and starts at `capacity`.
- `s2` counts available items and starts at zero.
- `q` stores the actual elements in FIFO order.

A semaphore is a thread-safe counter with an important rule: `acquire()` consumes one permit when a permit is available, but blocks the calling thread when the count is zero. `release()` adds one permit and can wake a waiting thread. The caller does not repeatedly poll in a busy loop; it sleeps under the synchronization primitive until progress becomes possible.

**Enqueue reserves space before modifying the queue**

`enqueue` first calls `self.s1.acquire()`. If the queue has spare capacity, this consumes one available-slot permit and the method continues. If the queue is full, `s1` has no permits and the producer blocks before it can append anything. This ordering is what protects the capacity limit.

After reserving a slot, the method calls `self.q.append(element)`. Appending on the right records this element after all elements that linearized earlier. Finally, `self.s2.release()` publishes one new available-item permit. A consumer waiting for an item may now wake.

The item semaphore is released only after the value is in the deque. Therefore, a consumer can never receive permission to remove an item that has not yet been stored.

**Dequeue reserves an item before removing it**

`dequeue` is the mirror image. It first calls `self.s2.acquire()`. When the queue is empty, no item permit exists, so the consumer blocks before touching the deque. When a permit is available, the consumer has reserved one real queued item.

The method removes `self.q.popleft()`. Producers append on the right and consumers remove on the left, so elements leave in FIFO order according to the order in which the appends take effect. After removal, `self.s1.release()` announces that one storage slot is free. A producer blocked by a full queue may now wake. The removed value is returned.

The slot semaphore is released only after the item has left the deque. A producer therefore cannot treat the capacity as available too early.

**The two semaphore counts encode the queue state**

At a stable point between completed calls, the number of item permits equals the queue length, and the number of slot permits equals `capacity - len(q)`. During the few instructions inside a call, a permit may be temporarily reserved by that call, but this reservation makes the system more conservative rather than unsafe.

For example, after a producer acquires a slot but before it appends, the sum of free-slot permits and stored items is temporarily below capacity. No other producer can steal that reserved slot, so the eventual append still cannot exceed the bound. Similarly, after a consumer acquires an item permit but before `popleft`, that particular item is reserved and cannot be claimed through the semaphore by another consumer.

This establishes the capacity and underflow safety properties. A producer must own a slot permit before appending, and only `capacity` such permits exist. A consumer must own an item permit before removing, and permits are published only for appended items.

**Why blocking does not create a circular wait**

A blocked producer waits only for `s1`. It has not acquired `s2`, and it does not hold a queue-wide lock needed by consumers. When the queue is full, at least one item permit exists, so a consumer can remove an item and release a slot.

A blocked consumer waits only for `s2`. When the queue is empty, slot permits exist, so a producer can append and release an item. No method acquires both semaphores and then waits for the other. This complementary signaling allows the opposite operation to make progress.

Thread scheduling still determines which of several waiting producers or consumers runs first. The contract does not require one scheduler-specific order among concurrent producers. Once appends have linearized, however, `popleft` preserves that established FIFO order.

**Why `size` can be simple here**

`size` returns `len(self.q)`. The reference states that the judge calls it after each test case, when the producer and consumer work for that case has completed. Under that quiescent use, no concurrent mutation competes with the length read, and the value is exactly the number of remaining elements.

If a broader interface required `size` to participate in arbitrary concurrent calls with a strong snapshot guarantee, the synchronization policy would need to state how that read linearizes. The supplied testing contract avoids that extra issue.

The bounded source domain—capacity at most 30 and at most 40 queue-method calls—does not change the algorithm’s synchronization logic. It means validation emphasizes legal interleavings, blocking behavior, FIFO semantics, progress, and final size rather than runtime scaling.

## Complexity detail

Let $c$ be the queue capacity. A completed `enqueue` or `dequeue` performs one semaphore acquisition, one deque operation, and one semaphore release. Semaphore bookkeeping and `deque.append` or `deque.popleft` are constant-time operations, so the active computational work per completed method is $O(1)$.

Blocking time is not bounded by input size. A call may wait until another thread performs the complementary operation, and wall-clock delay depends on scheduling. Complexity notation describes the work once synchronization permits progress; it does not claim that a blocked call returns immediately.

`size` uses the deque’s stored length and takes $O(1)$ time.

The deque holds at most $c$ elements, so payload storage is $O(c)$. The two semaphore objects use constant structural space. Runtime implementations may also maintain wait records for blocked threads; with $T$ participating threads that synchronization bookkeeping can be described as $O(T)$, while the problem’s queue-storage bound is $O(c)$ and the number of producer and consumer threads is itself bounded by the contract.

## Alternatives and edge cases

- **One mutex plus two condition variables:** Protect the deque with a lock, wait on `not_full` in enqueue, and wait on `not_empty` in dequeue. This is a standard design and makes all state predicates explicit, but requires careful use of loops around condition waits.
- **Busy waiting:** Repeatedly checking length until space or data appears wastes CPU and has poor progress behavior. Blocking synchronization primitives are the appropriate tool.
- **One semaphore only:** An item semaphore prevents underflow but not overflow; a slot semaphore prevents overflow but not underflow. The queue needs both resource counts.
- **Capacity one:** The design becomes a synchronized single-slot handoff. A second producer blocks until the stored item is removed, and an empty consumer blocks until a producer appends.
- **Consumer starts first:** `s2` begins at zero, so it waits safely. A later enqueue releases `s2` and enables the removal.
- **Producer reaches a full queue:** `s1` has zero permits, so the producer waits before append. A dequeue releases a slot only after removing an item.
- **Several producers:** Their scheduler order may vary, but each must acquire a distinct slot permit and each atomic append establishes a queue order that consumers then follow.
- **Several consumers:** Each successful item acquisition reserves one published item. No two consumers can remove the same queue entry.
- **FIFO direction:** `append` on the right combined with `popleft` on the left removes the earliest appended element first, matching the required logical queue even though the description names front and rear.
- **Final size:** Each completed enqueue adds one item and each completed dequeue removes one. After all calls finish, `len(q)` equals completed enqueues minus completed dequeues.
- **Exception safety:** In a more general production implementation, an unexpected exception between acquiring and releasing permits would require cleanup to restore semaphore counts. The judge supplies ordinary integer operations for which these deque actions are expected to complete.
- **Built-in bounded queue:** A library queue could provide the behavior directly, but the interview constraint explicitly asks for implementing the coordination rather than using that ready-made abstraction.
