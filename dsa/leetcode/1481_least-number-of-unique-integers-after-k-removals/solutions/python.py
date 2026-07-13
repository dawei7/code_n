from collections import Counter


def solve(arr, k):
    freq = Counter(arr)
    counts = sorted(freq[value] for value in freq)
    remaining = len(counts)
    for count in counts:
        if k < count:
            break
        k -= count
        remaining -= 1
    return remaining
