"""App-local reference solution for LeetCode 1824."""


def solve(obstacles: list[int]) -> int:
    costs = [1, 0, 1]
    infinity = len(obstacles) + 1

    for obstacle in obstacles[1:]:
        if obstacle:
            costs[obstacle - 1] = infinity
        best = min(costs)
        for lane in range(3):
            if lane != obstacle - 1:
                costs[lane] = min(costs[lane], best + 1)

    return min(costs)
