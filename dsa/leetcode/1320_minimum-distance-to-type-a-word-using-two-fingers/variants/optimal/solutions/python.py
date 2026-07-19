"""Optimal app-local solution for LeetCode 1320."""


def solve(word):
    def distance(first, second):
        if first == 26 or second == 26:
            return 0
        return abs(first // 6 - second // 6) + abs(first % 6 - second % 6)

    letters = [ord(character) - ord("A") for character in word]
    costs = [float("inf")] * 27
    costs[26] = 0
    previous = letters[0]

    for target in letters[1:]:
        next_costs = [float("inf")] * 27
        for other, cost in enumerate(costs):
            next_costs[other] = min(
                next_costs[other], cost + distance(previous, target)
            )
            next_costs[previous] = min(
                next_costs[previous], cost + distance(other, target)
            )
        costs = next_costs
        previous = target

    return min(costs)
