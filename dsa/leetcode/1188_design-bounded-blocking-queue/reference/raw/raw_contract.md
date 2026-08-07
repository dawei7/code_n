## Function Contract

**Class interface**

- `BoundedBlockingQueue(int capacity)`: Initialize an empty queue whose maximum number of stored elements is `capacity`.
- `void enqueue(int element)`: Add `element` at the front. If the queue is full, wait until space becomes available before completing the insertion.
- `int dequeue()`: Remove and return the element at the rear. If the queue is empty, wait until an element becomes available before completing the removal.
- `int size()`: Return the queue's current number of stored elements.

**Threading semantics**

Multiple threads can invoke the instance concurrently. Each producer thread calls only `enqueue`, and each consumer thread calls only `dequeue`. The implementation must keep its capacity bound under every legal interleaving, return elements in the FIFO order established when enqueues linearize, and allow an opposite operation to make progress while another thread is blocked.

After each test case, the judge calls `size()`. Enqueue has no return value; dequeue returns the removed integer; and size returns an integer from $0$ through `capacity`. When multiple producers or consumers are runnable together, the operating system may choose their relative order.
