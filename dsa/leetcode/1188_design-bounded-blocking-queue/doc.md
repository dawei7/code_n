# Design Bounded Blocking Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1188 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| Official Link | [design-bounded-blocking-queue](https://leetcode.com/problems/design-bounded-blocking-queue/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-bounded-blocking-queue/).

### Goal
Design a thread-safe bounded blocking queue. `enqueue` waits while the queue is full, `dequeue` waits while the queue is empty, and `size` reports the current number of queued elements.

### Concurrency Contract
**Operations**

- `BoundedBlockingQueue(capacity)`: Initialize the queue with a maximum size.
- `enqueue(element)`: Add an element, blocking until space is available.
- `dequeue()`: Remove and return the oldest element, blocking until an element is available.
- `size()`: Return the number of elements currently in the queue.

**Return value**

Operation-specific return values as described above.

### Examples
**Example 1**

- Scenario: capacity `2`; call `enqueue(1)`, `enqueue(2)`, `size()`, `dequeue()`, `size()`.
- Output: `size()` returns `2`, `dequeue()` returns `1`, final `size()` returns `1`.

**Example 2**

- Scenario: capacity `1`; one thread calls `enqueue(1)`, then another `enqueue(2)` before any dequeue.
- Output: the second enqueue waits until a dequeue frees space.

**Example 3**

- Scenario: an empty queue receives a `dequeue()` call before any enqueue.
- Output: the dequeue waits until an element is enqueued, then returns it.

---

## Solution
### Approach
Protect the underlying FIFO queue with a mutex. Use condition variables or semaphores to coordinate capacity:

- Producers wait on a "not full" condition before appending.
- Consumers wait on a "not empty" condition before removing.
- Each successful enqueue signals consumers, and each successful dequeue signals producers.

### Complexity Analysis
- **Time Complexity**: `O(1)` per queue operation, excluding time spent blocked.
- **Space Complexity**: `O(capacity)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
