def solve(n: int, cost: list[int]) -> int:
    increments = 0

    for parent in range(n // 2 - 1, -1, -1):
        left = 2 * parent + 1
        right = left + 1
        increments += abs(cost[left] - cost[right])
        cost[parent] += max(cost[left], cost[right])

    return increments
