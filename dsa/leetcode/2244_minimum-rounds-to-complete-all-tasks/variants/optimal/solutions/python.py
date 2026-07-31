from collections import Counter


def solve(tasks: list[int]) -> int:
    rounds = 0
    for frequency in Counter(tasks).values():
        if frequency == 1:
            return -1
        rounds += (frequency + 2) // 3
    return rounds
