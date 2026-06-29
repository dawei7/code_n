import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    _r, _c, n = (data[0], data[1], data[2])
    cells = [(data[i], data[i + 1]) for i in range(3, 3 + 2 * n, 2)]
    planted = set(cells)
    visited = set()
    best = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for start in cells:
        if start in visited:
            continue
        queue = deque([start])
        visited.add(start)
        perimeter = 0
        while queue:
            x, y = queue.popleft()
            perimeter += 4
            for dx, dy in directions:
                nxt = (x + dx, y + dy)
                if nxt in planted:
                    perimeter -= 1
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        best = max(best, perimeter)
    print(best)


if __name__ == "__main__":
    solve()
