# Design Bounded Blocking Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1188 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Python |
| Official Link | [LeetCode](https://leetcode.com/problems/design-bounded-blocking-queue/) |

## Problem Description

### Goal

Implement a thread-safe bounded blocking queue with a fixed maximum `capacity`. Producers add an integer at the front through `enqueue(element)`, while consumers remove and return the integer at the rear through `dequeue()`, giving the queue first-in, first-out behavior.

An enqueue call made while the queue is full must block until another thread removes an element. A dequeue call made while it is empty must block until a producer adds an element. Multiple producer and consumer threads operate on the same instance concurrently, and `size()` reports the number of currently stored elements after the test. Do not delegate the design to a built-in bounded blocking queue.

### Function Contract

**Inputs**

- `BoundedBlockingQueue(capacity)`: Constructs an empty queue whose maximum size $c$ satisfies $1\le c\le30$.
- `enqueue(element)`: Adds `element` at the front after waiting for free capacity; $0\le\texttt{element}\le20$.
- `dequeue()`: Waits for a stored element, then removes and returns the element at the rear.
- `size()`: Returns the current number of stored elements.
- Each test uses from $1$ through $8$ producer threads and from $1$ through $8$ consumer threads. A producer calls only `enqueue` and a consumer calls only `dequeue`. At most $40$ total queue-method calls occur, and the number of enqueue calls is at least the number of dequeue calls.

**Return value**

- `enqueue` returns `None`, `dequeue` returns the oldest queued integer, and `size` returns an integer from $0$ through $c$. The observable dequeue order must be FIFO, while the order in which simultaneous producers reach the queue may vary with scheduling.

### Examples

**Example 1**

- Input: one producer, one consumer, `capacity = 2`, operations `enqueue(1), dequeue(), dequeue(), enqueue(0), enqueue(2), enqueue(3), enqueue(4), dequeue()`
- Output: dequeues return `[1,0,2]` and the final size is `2`

The empty dequeue waits for `0`. Later, `enqueue(4)` waits while two elements occupy the queue and continues after the consumer removes `2`.

**Example 2**

- Input: three producers, four consumers, `capacity = 3`, enqueues of `1`, `0`, and `2` followed by three dequeues and an enqueue of `3`
- Output: the dequeues contain `0`, `1`, and `2` in whichever producer-arrival order the scheduler created; the final size is `1`
