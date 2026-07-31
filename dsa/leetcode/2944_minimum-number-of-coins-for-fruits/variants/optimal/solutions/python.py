from collections import deque


def solve(prices: list[int]) -> int:
    fruit_count = len(prices)
    cost = [0] * (fruit_count + 1)
    candidates = deque([fruit_count])

    for index in range(fruit_count - 1, -1, -1):
        right = min(fruit_count, 2 * index + 2)
        while candidates[0] > right:
            candidates.popleft()

        cost[index] = prices[index] + cost[candidates[0]]

        while candidates and cost[candidates[-1]] >= cost[index]:
            candidates.pop()
        candidates.append(index)

    return cost[0]
