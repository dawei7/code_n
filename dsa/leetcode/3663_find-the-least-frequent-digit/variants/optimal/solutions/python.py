from collections import Counter


def solve(n: int) -> int:
    frequency = Counter(str(n))
    return int(min(frequency, key=lambda digit: (frequency[digit], digit)))
