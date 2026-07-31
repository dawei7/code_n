from math import isqrt


def solve(finalSum: int) -> list[int]:
    if finalSum % 2:
        return []

    count = (isqrt(1 + 4 * finalSum) - 1) // 2
    answer = list(range(2, 2 * count + 1, 2))
    answer[-1] += finalSum - count * (count + 1)
    return answer
