def solve(cost: list[int]) -> list[int]:
    answer = []
    best = cost[0]

    for value in cost:
        best = min(best, value)
        answer.append(best)

    return answer
