def solve(numWays: list[int]) -> list[int]:
    n = len(numWays)
    ways = [0] * (n + 1)
    ways[0] = 1
    denominations = []

    for amount, target in enumerate(numWays, 1):
        if ways[amount] == target:
            continue

        if ways[amount] + 1 != target:
            return []

        denominations.append(amount)

        for total in range(amount, n + 1):
            ways[total] += ways[total - amount]

    return denominations
