from heapq import heapreplace, heappush
from typing import List


def solve(technique1: List[int], technique2: List[int], k: int) -> int:
    base = sum(technique2)
    positive_gain = 0
    nonnegative_count = 0
    largest_k_gains = []
    for first, second in zip(technique1, technique2):
        gain = first - second
        if gain >= 0:
            nonnegative_count += 1
            positive_gain += gain
        if k == 0:
            continue
        if len(largest_k_gains) < k:
            heappush(largest_k_gains, gain)
        elif gain > largest_k_gains[0]:
            heapreplace(largest_k_gains, gain)
    if nonnegative_count >= k:
        return base + positive_gain
    return base + sum(largest_k_gains)
