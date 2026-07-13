"""Linear circular distance transforms for LeetCode 514."""


def solve(ring: str, key: str) -> int:
    size = len(ring)
    infinity = 10**9
    costs = [infinity] * size
    costs[0] = 0

    for character in key:
        transformed = costs + costs
        for index in range(1, 2 * size):
            transformed[index] = min(transformed[index], transformed[index - 1] + 1)
        for index in range(2 * size - 2, -1, -1):
            transformed[index] = min(transformed[index], transformed[index + 1] + 1)
        costs = [
            min(transformed[index], transformed[index + size]) if ring[index] == character else infinity
            for index in range(size)
        ]

    return min(costs) + len(key)
