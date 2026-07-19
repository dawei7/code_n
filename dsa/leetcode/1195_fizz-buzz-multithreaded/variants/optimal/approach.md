## General
**Share one guarded position.** Store `current = 1` and protect it with a condition variable. Each worker owns a predicate describing exactly the positions for its callback. While the sequence is unfinished but the predicate is false, that worker waits and releases the condition lock so the responsible worker can proceed.

**Emit and transfer ownership atomically.** The worker whose predicate matches invokes its callback while holding the condition lock, increments `current`, and wakes every waiting worker. Keeping the callback and increment in one critical section prevents another thread from printing the next token first. The four predicates are mutually exclusive and collectively exhaustive, so exactly one worker can advance each position.

**Terminate every waiter.** After the final callback changes `current` to `n + 1`, it notifies all workers. Each awakened loop checks the bound before testing its predicate or printing, allowing all four methods to return even when their final owned positions occurred much earlier.

## Complexity detail
Exactly one callback and one increment occur for each of the $n$ sequence positions, giving $O(n)$ total productive work. Condition waits do not busy-spin. The shared counter, condition variable, and fixed set of four worker states use $O(1)$ auxiliary space, excluding the platform's output collection.

## Alternatives and edge cases
- **Four routing semaphores:** A number coordinator can release the semaphore for the appropriate callback and wait for completion; this is correct but needs more explicit handoff state.
- **Busy waiting:** Repeatedly reading an unguarded counter wastes CPU and risks data races or visibility errors.
- **Independent loops without synchronization:** Even correct per-thread divisibility tests cannot preserve global output order under arbitrary scheduling.
- **Predicate overlap:** The fizz and buzz predicates must exclude multiples of 15 so only `fizzbuzz` owns those positions.
- **Small `n`:** Some worker predicates may never match, but the final notification must still let those threads terminate.
- **Spurious wakeups:** Every wait is enclosed in a loop that rechecks both the bound and its predicate.
- **Callback ordering:** Invoking a callback outside the guarded handoff could let later output overtake it.
- **Completion:** Advancing past `n` and notifying all waiters prevents a thread from remaining blocked after the sequence ends.
