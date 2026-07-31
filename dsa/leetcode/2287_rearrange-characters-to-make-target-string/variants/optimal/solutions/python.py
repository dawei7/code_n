from collections import Counter


def solve(s: str, target: str) -> int:
    available = Counter(s)
    required = Counter(target)
    return min(
        available[character] // amount
        for character, amount in required.items()
    )
