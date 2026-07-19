"""Optimal app-local solution for LeetCode 1406: Stone Game III."""


def solve(stoneValue: list[int]) -> str:
    length = len(stoneValue)
    difference = [0] * (length + 1)

    for index in range(length - 1, -1, -1):
        taken = 0
        best = -float("inf")
        for end in range(index, min(index + 3, length)):
            taken += stoneValue[end]
            best = max(best, taken - difference[end + 1])
        difference[index] = int(best)

    if difference[0] > 0:
        return "Alice"
    if difference[0] < 0:
        return "Bob"
    return "Tie"
