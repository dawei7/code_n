from math import isqrt


def solve(ranks: list[int], cars: int) -> int:
    low = 0
    high = min(ranks) * cars * cars

    while low < high:
        time = (low + high) // 2
        repaired = sum(isqrt(time // rank) for rank in ranks)

        if repaired >= cars:
            high = time
        else:
            low = time + 1

    return low
