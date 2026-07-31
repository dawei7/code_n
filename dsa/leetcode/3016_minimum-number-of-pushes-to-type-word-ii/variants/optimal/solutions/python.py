from collections import Counter


def solve(word: str) -> int:
    frequencies = sorted(Counter(word).values(), reverse=True)
    return sum(frequency * (index // 8 + 1) for index, frequency in enumerate(frequencies))
