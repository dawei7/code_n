from collections import Counter


def solve(s: str, k: int) -> str:
    frequency = Counter(s)
    return "".join(character for character in s if frequency[character] < k)
