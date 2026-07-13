from collections import Counter


def solve(words, chars):
    available = Counter(chars)
    total = 0
    for word in words:
        counts = Counter(word)
        if all(counts[ch] <= available[ch] for ch in counts):
            total += len(word)
    return total
