import heapq
import urllib.request


def solve() -> int:
    """Find minimal path sum from top-left to bottom-right moving LEFT, RIGHT, UP, DOWN using Dijkstra's algorithm.
    
    Time Complexity: O(V log V)
    Space Complexity: O(V)
    """
    url = "https://projecteuler.net/resources/documents/0083_matrix.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    grid = [[int(x) for x in line.strip().split(",")] for line in text.strip().splitlines() if line.strip()]
    rows, cols = len(grid), len(grid[0])

    dist = {}
    pq = [(grid[0][0], 0, 0)]
    dist[(0, 0)] = grid[0][0]

    while pq:
        d, r, c = heapq.heappop(pq)
        if (r, c) == (rows - 1, cols - 1):
            return d

        if d > dist.get((r, c), float('inf')):
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_d = d + grid[nr][nc]
                if new_d < dist.get((nr, nc), float('inf')):
                    dist[(nr, nc)] = new_d
                    heapq.heappush(pq, (new_d, nr, nc))

    return -1
