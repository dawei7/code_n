## General
**Represent capacity and availability with permits.** Initialize a `slots` semaphore with $c$ permits and an `items` semaphore with zero. An enqueue must acquire one slot before modifying the queue, so the $(c+1)$-st outstanding producer blocks. A dequeue must acquire one item, so a consumer cannot enter the removal step while the queue is empty.

**Protect the deque itself.** A mutex surrounds each append, removal, and size read. After appending at the front, enqueue releases one item permit; after removing from the rear, dequeue releases one slot permit. Publishing the permit only after the protected mutation ensures an awakened thread sees the corresponding queue state.

**Preserve both safety and progress.** Slot permits make the stored count never exceed capacity, item permits prevent removal from an empty deque, and the mutex makes each mutation atomic. Appending at one end and removing at the other preserves FIFO order among operations in the order they acquire the lock. Neither method holds the mutex while waiting for a permit, so a blocked producer cannot prevent a consumer from freeing space and a blocked consumer cannot prevent a producer from publishing an item.

## Complexity detail
Once its required permit is available, each queue method performs a constant number of semaphore, lock, and deque operations, for $O(1)$ work per completed call; scheduler-dependent blocking time is excluded. The deque stores at most $c$ integers, while the synchronization objects occupy constant additional state, so space is $O(c)$.

## Alternatives and edge cases
- **Condition variables:** One mutex with `not_full` and `not_empty` conditions is correct when every wait rechecks its predicate in a loop, but the two counting semaphores encode the bounds directly.
- **Busy waiting:** Repeatedly checking `size()` wastes CPU and does not provide the required atomic handoff or memory visibility.
- **Mutex without conditions:** Mutual exclusion protects the deque but cannot make a full producer or empty consumer sleep until progress becomes possible.
- **Capacity one:** Every successful enqueue must be followed by a dequeue before another producer can publish an element.
- **Consumer arrives first:** It waits on the zero-permit item semaphore without holding the deque mutex, allowing a producer to proceed.
- **Producer arrives at a full queue:** It waits on `slots` without holding the mutex, allowing a consumer to remove an item.
- **Multiple producers:** Their operating-system scheduling order is not predetermined; FIFO applies after their enqueue operations linearize.
- **Final size:** Read it under the same mutex as mutations so it reflects one coherent queue state.
