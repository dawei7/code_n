def solve(n: int, roads: list[list[int]]) -> int:
    degree = [0] * n
    connected = [[False] * n for _ in range(n)]

    for first, second in roads:
        degree[first] += 1
        degree[second] += 1
        connected[first][second] = True
        connected[second][first] = True

    maximum = 0
    for first in range(n):
        for second in range(first + 1, n):
            rank = degree[first] + degree[second] - connected[first][second]
            maximum = max(maximum, rank)

    return maximum
