def solve(customers: list[int], boardingCost: int, runningCost: int) -> int:
    waiting = 0
    profit = 0
    best_profit = 0
    best_rotation = -1
    rotation = 0

    while rotation < len(customers) or waiting:
        if rotation < len(customers):
            waiting += customers[rotation]
        boarded = min(4, waiting)
        waiting -= boarded
        rotation += 1
        profit += boarded * boardingCost - runningCost
        if profit > best_profit:
            best_profit = profit
            best_rotation = rotation

    return best_rotation
