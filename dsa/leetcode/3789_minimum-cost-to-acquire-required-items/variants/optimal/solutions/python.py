def solve(cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
    shared_units = min(need1, need2)
    answer = shared_units * min(costBoth, cost1 + cost2)
    if need1 > need2:
        answer += (need1 - need2) * min(cost1, costBoth)
    else:
        answer += (need2 - need1) * min(cost2, costBoth)
    return answer
