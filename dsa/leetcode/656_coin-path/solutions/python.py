def solve(coins: list[int], maxJump: int) -> list[int]:
    size = len(coins)
    unreachable = float("inf")
    cost = [unreachable] * size
    next_index = [-1] * size
    if coins[-1] != -1:
        cost[-1] = coins[-1]

    for index in range(size - 2, -1, -1):
        if coins[index] == -1:
            continue
        stop = min(size, index + maxJump + 1)
        for following in range(index + 1, stop):
            candidate = coins[index] + cost[following]
            if candidate < cost[index]:
                cost[index] = candidate
                next_index[index] = following

    if cost[0] == unreachable:
        return []
    path = []
    index = 0
    while index != -1:
        path.append(index + 1)
        index = next_index[index]
    return path
