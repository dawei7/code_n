### 1. Description

Implement a thread-safe bounded blocking queue that has the following methods:

- `BoundedBlockingQueue(int capacity)` The constructor initializes the queue with a maximum `capacity`.

- `void enqueue(int element)` Adds an `element` to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.

- `int dequeue()` Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.

- `int size()` Returns the number of elements currently in the queue.

Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread that only makes calls to the `enqueue` method or a consumer thread that only makes calls to the `dequeue` method. The `size` method will be called after every test case.

Please do not use built-in implementations of bounded blocking queue as this will not be accepted in an interview.

### 2. Function Contract

**Class interface**

- `BoundedBlockingQueue(int capacity)`: Initialize an empty queue whose maximum number of stored elements is `capacity`.
- `void enqueue(int element)`: Add `element` at the front. If the queue is full, wait until space becomes available before completing the insertion.
- `int dequeue()`: Remove and return the element at the rear. If the queue is empty, wait until an element becomes available before completing the removal.
- `int size()`: Return the queue's current number of stored elements.

**Threading semantics**

Multiple threads can invoke the instance concurrently. Each producer thread calls only `enqueue`, and each consumer thread calls only `dequeue`. The implementation must keep its capacity bound under every legal interleaving, return elements in the FIFO order established when enqueues linearize, and allow an opposite operation to make progress while another thread is blocked.

After each test case, the judge calls `size()`. Enqueue has no return value; dequeue returns the removed integer; and size returns an integer from $0$ through `capacity`. When multiple producers or consumers are runnable together, the operating system may choose their relative order.

### 3. Examples

#### Example 1

- **Input:** ``
1
1
["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
[[2],[1],[],[],[0],[2],[3],[4],[]]
- **Output:** ``
[1,0,2,2]
- **Explanation:** Number of producer threads = 1
Number of consumer threads = 1
BoundedBlockingQueue queue = new BoundedBlockingQueue(2);   // initialize the queue with capacity = 2.
queue.enqueue(1);   // The producer thread enqueues 1 to the queue.
queue.dequeue();    // The consumer thread calls dequeue and returns 1 from the queue.
queue.dequeue();    // Since the queue is empty, the consumer thread is blocked.
queue.enqueue(0);   // The producer thread enqueues 0 to the queue. The consumer thread is unblocked and returns 0 from the queue.
queue.enqueue(2);   // The producer thread enqueues 2 to the queue.
queue.enqueue(3);   // The producer thread enqueues 3 to the queue.
queue.enqueue(4);   // The producer thread is blocked because the queue's capacity (2) is reached.
queue.dequeue();    // The consumer thread returns 2 from the queue. The producer thread is unblocked and enqueues 4 to the queue.
queue.size();       // 2 elements remaining in the queue. size() is always called at the end of each test case.

#### Example 2

- **Input:** ``
3
4
["BoundedBlockingQueue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","enqueue"]
[[3],[1],[0],[2],[],[],[],[3]]
- **Output:** ``
[1,0,2,1]
- **Explanation:** Number of producer threads = 3
Number of consumer threads = 4
BoundedBlockingQueue queue = new BoundedBlockingQueue(3);   // initialize the queue with capacity = 3.
queue.enqueue(1);   // Producer thread P1 enqueues 1 to the queue.
queue.enqueue(0);   // Producer thread P2 enqueues 0 to the queue.
queue.enqueue(2);   // Producer thread P3 enqueues 2 to the queue.
queue.dequeue();    // Consumer thread C1 calls dequeue.
queue.dequeue();    // Consumer thread C2 calls dequeue.
queue.dequeue();    // Consumer thread C3 calls dequeue.
queue.enqueue(3);   // One of the producer threads enqueues 3 to the queue.
queue.size();       // 1 element remaining in the queue.
Since the number of threads for producer/consumer is greater than 1, we do not know how the threads will be scheduled in the operating system, even though the input seems to imply the ordering. Therefore, any of the output [1,0,2] or [1,2,0] or [0,1,2] or [0,2,1] or [2,0,1] or [2,1,0] will be accepted.

### 4. Constraints

- $1 \le Number of Prdoucers \le 8$

- $1 \le Number of Consumers \le 8$

- $1 \le size \le 30$

- $0 \le element \le 20$

- The number of calls to `enqueue` is **greater than or equal to** the number of calls to `dequeue`.

- At most `40` calls will be made to `enque`, `deque`, and `size`.
