# Circular Queue (Array Based)

| | |
|---|---|
| **ID** | `queue_05` |
| **Category** | queue |
| **Complexity (required)** | $O(1)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) |

## Problem statement

Design your implementation of the circular queue.
A circular queue is a linear data structure following FIFO principles, but the last position is connected back to the first position to make a circle. It is also called a "Ring Buffer".
This completely eliminates the fundamental flaw of a standard array-based queue: empty spaces left at the front of the array by dequeued elements cannot be reused.

Implement the `MyCircularQueue` class:
- `MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`.
- `Front()` Gets the front item. Return -1 if empty.
- `Rear()` Gets the last item. Return -1 if empty.
- `enQueue(value)` Inserts an element. Return True if successful.
- `deQueue()` Deletes an element from the queue. Return True if successful.
- `isEmpty()` Checks whether the queue is empty.
- `isFull()` Checks whether the queue is full.

**Input:** A sequence of Circular Queue operations.
**Output:** Booleans and integers depending on the method.

## When to use it

- To understand low-level memory architecture. Almost all hardware buffers (like keyboard input buffers or streaming video memory) use this exact physical structure.

## Approach

We use a fixed-size array `arr` of size K.
We maintain two pointers:
- `head`: Points to the oldest element.
- `tail`: Points to the newest element (or the next empty slot, depending on implementation).
We also maintain a `size` counter to easily track if we are empty or full.

**The "Circle" Math:**
Whenever we increment `head` or `tail`, we don't just do `+ 1`. We do `(head + 1) % K`.
The modulo operator mathematically "wraps" the pointer back to index 0 the moment it hits the end of the array `K`.

**Operations:**
- `enQueue`: If not full, put the element at the `tail` index. Move `tail` forward using modulo. Increment `size`.
- `deQueue`: If not empty, we don't need to actually erase the memory. Just move `head` forward using modulo. Decrement `size`. The old memory will just get overwritten eventually!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for queue_05: Circular Queue (Array-based).

Implement a fixed-capacity circular queue using
"""


def solve(operations, capacity, n):
    """Fixed-capacity circular queue. Returns list of dequeued values."""
    if capacity <= 0:
        return []
    queue = [None] * capacity
    front = 0
    rear = -1
    size = 0
    dequeued = []
    for op in operations:
        name = op[0]
        if name == "enqueue":
            if size == capacity:
                continue  # overflow: silently skip
            rear = (rear + 1) % capacity
            queue[rear] = op[1]
            size += 1
        elif name == "dequeue":
            if size == 0:
                continue  # underflow: silently skip
            dequeued.append(queue[front])
            front = (front + 1) % capacity
            size -= 1
        elif name == "front":
            pass  # we don't return this
        elif name == "rear":
            pass
        elif name == "isEmpty":
            pass
        elif name == "isFull":
            pass
    return dequeued
```

</details>

## Walk-through

`q = MyCircularQueue(3)`
`capacity = 3`, `queue = [0, 0, 0]`, `head = 0`, `tail = 0`, `size = 0`.

1. `enQueue(1)`: `queue[0]=1`. `tail = (0+1)%3 = 1`. `size=1`.
2. `enQueue(2)`: `queue[1]=2`. `tail = (1+1)%3 = 2`. `size=2`.
3. `enQueue(3)`: `queue[2]=3`. `tail = (2+1)%3 = 0`. `size=3`.
4. `enQueue(4)`: `isFull` is True. Returns `False`.
5. `Rear()`: `(0 - 1 + 3) % 3 = 2`. `queue[2] = 3`. Returns `3`.
6. `deQueue()`: `head = (0+1)%3 = 1`. `size=2`. (The `1` at index 0 is "deleted").
7. `enQueue(4)`: `queue[0]=4`. `tail = (0+1)%3 = 1`. `size=3`. (It wrapped around and overwrote index 0!).
8. `Front()`: `queue[head] = queue[1] = 2`. Returns `2`.

Correctly models a dynamic circle! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(K)$ |
| **Average** | $O(1)$ | $O(K)$ |
| **Worst** | $O(1)$ | $O(K)$ |

Absolutely every operation utilizes mathematically instant array indexing and integer arithmetic. Time complexity is strictly $O(1)$.
Space complexity is strictly bounded to $O(K)$, as we pre-allocate the array precisely once and completely reuse the memory without any garbage collection or reallocation.

## Variants & optimizations

- **No Size Variable:** You can implement this without the `size` integer! To do this, you make the array size `K + 1`. The queue is Empty when `head == tail`. The queue is Full when `(tail + 1) % (K + 1) == head`. This is how hardcore low-level C ring buffers are implemented to avoid concurrent read/write locks on a shared `size` variable.

## Real-world applications

- **Network Interface Cards (NIC):** Hardware buffers that hold incoming TCP packets use Ring Buffers. If the CPU doesn't `deQueue` the packets fast enough, the NIC simply `enQueue` wraps around and overwrites the oldest packets, resulting in "packet drop".

## Related algorithms in cOde(n)

- **[queue_01 - Implement Queue using Stacks](queue_01_implement-queue-using-stacks.md)** — The higher-level programmatic abstraction of a queue.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
