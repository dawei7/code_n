"""Optimal solution for queue_03: Generate Binary Numbers (1 to n).

Generate the binary representations of 1, 2, ..., n
"""


def solve(n):
    """Generate binary strings '1', '10', '11', '100', ... up to n."""
    from collections import deque
    if n <= 0:
        return []
    result = []
    q = deque(["1"])
    for _ in range(n):
        s = q.popleft()
        result.append(s)
        q.append(s + "0")
        q.append(s + "1")
    return result
