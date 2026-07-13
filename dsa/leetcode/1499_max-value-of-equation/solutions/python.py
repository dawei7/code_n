from collections import deque


def solve(points, k):
    normalized = []
    for index, point in enumerate(points):
        if isinstance(point, list) and len(point) >= 2:
            normalized.append((point[0], point[1]))
        else:
            normalized.append((index, point))
    normalized.sort()
    queue = deque()
    best = -10**18
    for x, y in normalized:
        while queue and x - queue[0][1] > k:
            queue.popleft()
        if queue:
            best = max(best, x + y + queue[0][0])
        value = y - x
        while queue and queue[-1][0] <= value:
            queue.pop()
        queue.append((value, x))
    return 0 if best == -10**18 else best
