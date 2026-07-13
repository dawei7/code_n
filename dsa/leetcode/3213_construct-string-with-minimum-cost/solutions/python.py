from collections import defaultdict


def solve(target: str, words: list[str], costs: list[int]) -> int:
    base = 911_382_323
    mask = (1 << 64) - 1
    n = len(target)

    powers = [1] * (n + 1)
    prefix = [0] * (n + 1)
    for i, char in enumerate(target):
        powers[i + 1] = (powers[i] * base) & mask
        prefix[i + 1] = (prefix[i] * base + ord(char)) & mask

    by_length: dict[int, dict[int, int]] = defaultdict(dict)
    for word, cost in zip(words, costs):
        word_hash = 0
        for char in word:
            word_hash = (word_hash * base + ord(char)) & mask
        bucket = by_length[len(word)]
        previous = bucket.get(word_hash)
        if previous is None or cost < previous:
            bucket[word_hash] = cost

    buckets = [(length, by_length[length]) for length in sorted(by_length) if length <= n]
    inf = 10**30
    dp = [inf] * (n + 1)
    dp[0] = 0

    for end in range(1, n + 1):
        best = inf
        for length, bucket in buckets:
            start = end - length
            if start < 0:
                break
            previous = dp[start]
            if previous == inf:
                continue
            segment_hash = (prefix[end] - ((prefix[start] * powers[length]) & mask)) & mask
            cost = bucket.get(segment_hash)
            if cost is not None:
                candidate = previous + cost
                if candidate < best:
                    best = candidate
        dp[end] = best

    return -1 if dp[n] == inf else dp[n]
