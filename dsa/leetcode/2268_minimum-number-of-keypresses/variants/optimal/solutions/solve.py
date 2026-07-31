from collections import Counter


def solve(s: str) -> int:
    frequencies = sorted(Counter(s).values(), reverse=True)
    return sum(frequency * (index // 9 + 1) for index, frequency in enumerate(frequencies))
