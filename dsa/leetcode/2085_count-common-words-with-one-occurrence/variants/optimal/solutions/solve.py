from collections import Counter


def solve(words1: list[str], words2: list[str]) -> int:
    counts1 = Counter(words1)
    counts2 = Counter(words2)
    return sum(counts1[word] == 1 and counts2[word] == 1 for word in counts1)
