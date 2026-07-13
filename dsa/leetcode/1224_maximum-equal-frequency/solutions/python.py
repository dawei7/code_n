from collections import Counter


def solve(nums):
    counts = Counter()
    freq = Counter()
    answer = 0
    max_freq = 0

    for i, value in enumerate(nums, 1):
        old = counts[value]
        if old:
            freq[old] -= 1
        counts[value] = old + 1
        freq[old + 1] += 1
        max_freq = max(max_freq, old + 1)

        if (
            max_freq == 1
            or max_freq * freq[max_freq] + 1 == i
            or (max_freq - 1) * (freq[max_freq - 1] + 1) + 1 == i
        ):
            answer = i
    return answer
