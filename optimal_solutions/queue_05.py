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
