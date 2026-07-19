## General
**Serialize each complete eating transaction.** Store one mutex in the shared `DiningPhilosophers` object. An invocation acquires that mutex before touching either fork and holds it until both forks have been put down. At most one philosopher can therefore be inside the callback sequence at a time.

**Invoke callbacks in physical order.** While holding the mutex, call `pickLeftFork`, then `pickRightFork`, then `eat`, followed by `putRightFork` and `putLeftFork`. Both acquisitions precede eating, and both releases follow it. The `with` scope releases the mutex even if control leaves the block unexpectedly.

**Why circular wait is impossible.** A philosopher never waits for a fork while another philosopher owns the transaction mutex: all other invocations wait before performing their first pick callback. The active invocation acquires both logical forks, eats, releases them, and exits the mutex scope in finite callback work. Thus no cycle of philosophers can each hold one fork while waiting for another. Under the judge's progressing thread scheduler, queued invocations successively enter the finite critical section, so every request completes.

The discipline sacrifices parallel eating by nonadjacent philosophers, but the contract asks for a correct starvation-free discipline rather than maximum concurrency.

## Complexity detail
There are always five philosophers and five callbacks per invocation. Excluding scheduler-dependent waiting time, an invocation performs $O(1)$ work. The shared object stores one mutex, so its space use is $O(1)$.

## Alternatives and edge cases
- **One lock per fork plus a four-seat semaphore:** Allowing at most four contenders prevents all five from holding one fork in a cycle and permits nonadjacent parallelism, but it requires more synchronization state.
- **Asymmetric fork order:** Making one philosopher acquire forks in the opposite order breaks circular wait, though starvation and reasoning about repeated concurrent calls require care.
- **Unrestricted left-then-right locking:** All five philosophers may hold their left fork and wait forever for the right, producing the classic deadlock.
- **Callback order:** `eat` must occur after both picks, and neither put callback may occur before eating.
- **Repeated same-philosopher calls:** They are separate transactions and are safely serialized by the shared mutex.
- **Exceptions:** A callback exception is outside the judge's normal contract, but the mutex scope itself is still released.
- **Throughput tradeoff:** Global serialization is intentionally conservative; correctness does not require simultaneous nonadjacent meals.
