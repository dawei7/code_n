def solve(
    n: int,
    k: int,
    stayScore: list[list[int]],
    travelScore: list[list[int]],
) -> int:
    best = [0] * n

    for day in range(k):
        next_best = [0] * n
        for destination in range(n):
            score = best[destination] + stayScore[day][destination]
            for source in range(n):
                if source == destination:
                    continue
                candidate = best[source] + travelScore[source][destination]
                if candidate > score:
                    score = candidate
            next_best[destination] = score
        best = next_best

    return max(best)
