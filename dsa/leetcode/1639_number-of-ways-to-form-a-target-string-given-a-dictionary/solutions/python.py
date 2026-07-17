from collections import Counter


def solve(words: list[str], target: str) -> int:
    modulus = 1_000_000_007
    column_counts = [Counter(column) for column in zip(*words)]
    ways = [1] + [0] * len(target)

    for column_index, counts in enumerate(column_counts):
        last_target_index = min(len(target) - 1, column_index)
        for target_index in range(last_target_index, -1, -1):
            ways[target_index + 1] += (
                ways[target_index] * counts[target[target_index]]
            )
            ways[target_index + 1] %= modulus

    return ways[-1]
