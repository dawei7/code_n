def solve(s: str, t: str, nextCost: list[int], prevCost: list[int]) -> int:
    n = 26
    dist = [[10**30] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        dist[i][(i + 1) % n] = min(dist[i][(i + 1) % n], nextCost[i])
        dist[i][(i - 1) % n] = min(dist[i][(i - 1) % n], prevCost[i])

    for mid in range(n):
        for start in range(n):
            via_mid = dist[start][mid]
            for end in range(n):
                candidate = via_mid + dist[mid][end]
                if candidate < dist[start][end]:
                    dist[start][end] = candidate

    return sum(dist[ord(source) - 97][ord(target) - 97] for source, target in zip(s, t))
