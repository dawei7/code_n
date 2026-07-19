def solve(n: int, edges: list[list[int]]) -> int:
    connected = [[False] * (n + 1) for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for first, second in edges:
        connected[first][second] = True
        connected[second][first] = True
        degree[first] += 1
        degree[second] += 1

    best = float("inf")
    for first in range(1, n + 1):
        for second in range(first + 1, n + 1):
            if not connected[first][second]:
                continue
            for third in range(second + 1, n + 1):
                if connected[first][third] and connected[second][third]:
                    best = min(
                        best,
                        degree[first] + degree[second] + degree[third] - 6,
                    )

    return -1 if best == float("inf") else int(best)
