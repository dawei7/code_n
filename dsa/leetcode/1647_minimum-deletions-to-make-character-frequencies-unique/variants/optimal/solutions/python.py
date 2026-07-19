from collections import Counter


def solve(s: str) -> int:
    used: set[int] = set()
    deletions = 0
    for frequency in Counter(s).values():
        while frequency > 0 and frequency in used:
            frequency -= 1
            deletions += 1
        if frequency > 0:
            used.add(frequency)
    return deletions
