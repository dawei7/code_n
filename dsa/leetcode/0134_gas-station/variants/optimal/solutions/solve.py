def solve(gas: list[int], cost: list[int]) -> int:
    total = 0
    tank = 0
    start = 0
    for index, (available, required) in enumerate(zip(gas, cost)):
        difference = available - required
        total += difference
        tank += difference
        if tank < 0:
            start = index + 1
            tank = 0
    return start if total >= 0 else -1
