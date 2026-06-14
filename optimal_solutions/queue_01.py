"""Optimal solution for queue_01: Implement Queue using Stacks.

Implement a FIFO queue using only two LIFO stacks.
"""


def solve(operations, n):
    """Implement FIFO queue with two LIFO stacks."""
    inbox = []
    outbox = []
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            inbox.append(op[1])
        elif name == "pop":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                outbox.pop()
        elif name == "peek":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                results.append(outbox[-1])
        elif name == "empty":
            pass
    return results
