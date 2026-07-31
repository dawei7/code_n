from collections import Counter


def solve(arr, k):
    frequencies = sorted(Counter(arr).values())
    remaining = len(frequencies)

    for frequency in frequencies:
        if frequency > k:
            break
        k -= frequency
        remaining -= 1

    return remaining
