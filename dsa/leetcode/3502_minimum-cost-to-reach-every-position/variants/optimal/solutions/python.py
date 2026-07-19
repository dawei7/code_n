def solve(cost: list[int]) -> list[int]:
    answer = []
    best = 10**9
    for value in cost:
        best = min(best, value)
        answer.append(best)
    return answer
