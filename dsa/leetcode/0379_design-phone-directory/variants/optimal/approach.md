## General
**Keep an explicit pool of numbers ready to allocate**

Initialize a queue with every number in the directory and a Boolean availability array. A get removes one queue front, marks that number unavailable, and returns it. If the queue is empty, no number can be allocated and the result is `-1`.

**Use the Boolean array for checks and safe releases**

A check reads the availability flag directly. To release a number, first inspect its flag. If it is currently allocated, mark it available and append it to the queue. If it is already available, do nothing; this prevents duplicate queue entries that could allocate the same number twice.

**Why the queue and flags stay synchronized**

Initially every number appears once in the queue and every flag is true. A get removes exactly one queued available number and flips exactly its flag. A valid release performs the inverse transition, while a redundant release changes neither structure. By induction, the queue contains each available number exactly once and no allocated number, so both allocation and checks remain correct.

**Allow any allocation order**

The contract does not require the smallest available number. Queue order is deterministic for the reference, but a stack or another constant-time pool is also valid. Validation simulates the operation stream against the returned choices rather than enforcing one number sequence.

## Complexity detail
Each queue operation and Boolean lookup or update is $O(1)$, so every public operation has constant time. The queue and availability array each store at most `maxNumbers` entries, using $O(maxNumbers)$ space.

## Alternatives and edge cases
- **Stack of available numbers:** has the same bounds and returns a different valid allocation order.
- **Scan an availability array on every get:** makes checks simple but can require $O(maxNumbers)$ time per allocation.
- **Hash set only:** supports checks and release but selecting an arbitrary element may have language-specific behavior and iteration costs.
- Getting from an exhausted directory returns `-1`.
- Releasing an allocated number makes it available again.
- Releasing an already available number must not duplicate it in the pool.
- A one-number directory exercises both exhaustion and reuse boundaries.
