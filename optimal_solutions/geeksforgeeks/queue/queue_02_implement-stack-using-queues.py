"""Optimal solution for queue_02: Implement Stack using Queues.

Implement a LIFO stack using only FIFO queues
"""


def solve(operations, n):
    """Implement LIFO stack using one FIFO queue."""
    from collections import deque
    q = deque()
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            q.append(op[1])
            # Rotate: dequeue and re-enqueue (len(q) - 1) times
            # so the new element ends up at the front.
            for _ in range(len(q) - 1):
                q.append(q.popleft())
        elif name == "pop":
            if q:
                q.popleft()
        elif name == "top":
            if q:
                results.append(q[0])
        elif name == "empty":
            pass
    return results
