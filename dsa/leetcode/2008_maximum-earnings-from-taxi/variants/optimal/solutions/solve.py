def solve(n: int, rides: list[list[int]]) -> int:
    rides_by_end: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for start, end, tip in rides:
        rides_by_end[end].append((start, end - start + tip))

    best = [0] * (n + 1)
    for point in range(1, n + 1):
        best[point] = best[point - 1]
        for start, earnings in rides_by_end[point]:
            best[point] = max(best[point], best[start] + earnings)

    return best[n]
