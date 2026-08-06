## Examples

**Example 1**

- Input: `1, 1, ["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"], [[2],[1],[],[],[0],[2],[3],[4],[]]`
- Output: `[1,0,2,2]`
- Explanation: There is one producer, one consumer, and a queue of capacity `2`. The producer first enqueues `1`, so the first dequeue returns `1`. The next dequeue reaches an empty queue and blocks. Enqueuing `0` makes that consumer runnable, and it returns `0`.

The producer then enqueues `2` and `3`, filling the queue. Its attempt to enqueue `4` blocks until the next dequeue removes `2`; the insertion of `4` can then finish. Two elements remain, so the final size is `2`.

**Example 2**

- Input: `3, 4, ["BoundedBlockingQueue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","enqueue"], [[3],[1],[0],[2],[],[],[],[3]]`
- Output: `[1,0,2,1]`
- Explanation: Three producer threads enqueue `1`, `0`, and `2` into a queue of capacity `3`. Three of the four consumer threads then dequeue those elements, and a producer enqueues `3`, leaving a final size of `1`.

Because several producers and consumers are scheduled by the operating system, the first three output positions may be any permutation of the three dequeued values: `[1,0,2]`, `[1,2,0]`, `[0,1,2]`, `[0,2,1]`, `[2,1,0]`, or `[2,0,1]`. The shown output is one valid schedule.
