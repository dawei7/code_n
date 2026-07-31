from bisect import bisect_right
from itertools import accumulate


def solve(w: list[int], random_values: list[float]) -> list[int]:
    prefix_sums = list(accumulate(w))
    total = prefix_sums[-1]
    position = 0

    def random() -> float:
        nonlocal position
        value = random_values[position % len(random_values)]
        position += 1
        return value

    def pickIndex() -> int:
        return bisect_right(prefix_sums, random() * total)

    return [pickIndex() for _ in random_values]
