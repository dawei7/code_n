# Design Circular Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 622 |
| Difficulty | Medium |
| Topics | Array, Linked List, Design, Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/design-circular-queue/) |

## Problem Description
### Goal
Design a circular queue, also called a ring buffer: a fixed-capacity FIFO data structure in which the position after the final storage slot wraps back to the first slot. Reusing freed positions at the front allows later insertions without shifting the remaining values.

Implement construction with capacity `k`, `enQueue(value)`, `deQueue()`, `Front()`, `Rear()`, `isEmpty()`, and `isFull()`. Insertion and deletion report whether they succeed, endpoint queries return `-1` when the queue is empty, and failed operations leave the state unchanged. All operations should run in constant time without using a built-in queue implementation.

### Function Contract
**Inputs**

- `MyCircularQueue(k)`: construct an empty queue with positive capacity `k`
- `enQueue(value)`: append a value and report whether insertion succeeds
- `deQueue()`: remove the front value and report whether removal succeeds
- `Front()` / `Rear()`: return the corresponding value, or `-1` when empty
- `isEmpty()` / `isFull()`: report the current state

**Return value**

- The operation trace returns null for construction and the documented result for every later call
- Failed insertion or removal leaves the queue unchanged

### Examples
**Example 1**

- Operations: construct capacity 3; enqueue 1, 2, 3, then 4; query rear and full; dequeue; enqueue 4; query rear
- Output: `null, true, true, true, false, 3, true, true, true, 4`

**Example 2**

- Operations: construct capacity 1; query front; enqueue 7; query front and rear
- Output: `null, -1, true, 7, 7`
