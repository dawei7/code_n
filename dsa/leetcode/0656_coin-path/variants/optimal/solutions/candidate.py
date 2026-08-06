def solve(coins: list[int], maxJump: int) -> list[int]:
    size = len(coins)
    unreachable = float("inf")
    cost = [unreachable] * size
    successor = [-1] * size
    if coins[-1] != -1:
        cost[-1] = coins[-1]

    for position in range(size - 2, -1, -1):
        if coins[position] == -1:
            continue
        stop = min(size, position + maxJump + 1)
        for following in range(position + 1, stop):
            candidate_cost = coins[position] + cost[following]
            if candidate_cost < cost[position]:
                cost[position] = candidate_cost
                successor[position] = following

    if cost[0] == unreachable:
        return []
    path = []
    position = 0
    while position != -1:
        path.append(position + 1)
        position = successor[position]
    return path
