from collections import defaultdict


def solve(n: int, conflictingPairs: list[list[int]]) -> int:
    by_right: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for pair_id, (first, second) in enumerate(conflictingPairs):
        left, right = sorted((first, second))
        by_right[right].append((left, pair_id))

    best_left = 0
    second_left = 0
    best_pair = -1
    total = 0
    gain = defaultdict(int)

    for right in range(1, n + 1):
        for left, pair_id in by_right[right]:
            if left > best_left:
                second_left = best_left
                best_left = left
                best_pair = pair_id
            elif left == best_left:
                second_left = best_left
            elif left > second_left:
                second_left = left

        total += right - best_left
        if best_pair != -1:
            gain[best_pair] += best_left - second_left

    return total + (max(gain.values()) if gain else 0)
