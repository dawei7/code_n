from collections import defaultdict


def solve(target: str, words: list[str], costs: list[int]) -> int:
    base = 911_382_323
    mask = (1 << 64) - 1
    target_length = len(target)

    powers = [1] * (target_length + 1)
    prefix_hash = [0] * (target_length + 1)
    for index, character in enumerate(target):
        powers[index + 1] = (powers[index] * base) & mask
        prefix_hash[index + 1] = (prefix_hash[index] * base + ord(character)) & mask

    costs_by_length: dict[int, dict[int, int]] = defaultdict(dict)
    for word, cost in zip(words, costs):
        word_hash = 0
        for character in word:
            word_hash = (word_hash * base + ord(character)) & mask
        bucket = costs_by_length[len(word)]
        previous_cost = bucket.get(word_hash)
        if previous_cost is None or cost < previous_cost:
            bucket[word_hash] = cost

    buckets = [(length, costs_by_length[length]) for length in sorted(costs_by_length) if length <= target_length]
    infinity = 10**30
    minimum_cost = [infinity] * (target_length + 1)
    minimum_cost[0] = 0

    for end in range(1, target_length + 1):
        best = infinity
        for length, bucket in buckets:
            start = end - length
            if start < 0:
                break
            previous = minimum_cost[start]
            if previous == infinity:
                continue
            segment_hash = (prefix_hash[end] - (prefix_hash[start] * powers[length] & mask)) & mask
            word_cost = bucket.get(segment_hash)
            if word_cost is not None:
                best = min(best, previous + word_cost)
        minimum_cost[end] = best

    return -1 if minimum_cost[-1] == infinity else minimum_cost[-1]
