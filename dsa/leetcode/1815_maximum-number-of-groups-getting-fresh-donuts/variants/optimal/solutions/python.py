from functools import lru_cache


def solve(batchSize: int, groups: list[int]) -> int:
    counts = [0] * batchSize
    for group in groups:
        counts[group % batchSize] += 1

    answer = counts[0]
    for remainder in range(1, (batchSize + 1) // 2):
        paired = min(counts[remainder], counts[batchSize - remainder])
        answer += paired
        counts[remainder] -= paired
        counts[batchSize - remainder] -= paired

    if batchSize % 2 == 0:
        middle = batchSize // 2
        answer += counts[middle] // 2
        counts[middle] %= 2

    @lru_cache(None)
    def search(state: tuple[int, ...], leftover: int) -> int:
        best = 0
        for index, count in enumerate(state):
            if count == 0:
                continue
            remainder = index + 1
            next_state = list(state)
            next_state[index] -= 1
            best = max(
                best,
                (1 if leftover == 0 else 0)
                + search(tuple(next_state), (leftover + remainder) % batchSize),
            )
        return best

    return answer + search(tuple(counts[1:]), 0)
