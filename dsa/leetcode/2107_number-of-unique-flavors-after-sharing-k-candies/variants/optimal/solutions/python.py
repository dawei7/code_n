from collections import Counter


def solve(candies: list[int], k: int) -> int:
    kept = Counter(candies[k:])
    answer = len(kept)

    for right in range(k, len(candies)):
        kept[candies[right - k]] += 1

        entering_shared = candies[right]
        kept[entering_shared] -= 1
        if kept[entering_shared] == 0:
            del kept[entering_shared]

        answer = max(answer, len(kept))

    return answer
