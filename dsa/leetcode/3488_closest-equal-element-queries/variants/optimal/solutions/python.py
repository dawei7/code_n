from bisect import bisect_left
from collections import defaultdict


def solve(nums: list[int], queries: list[int]) -> list[int]:
    n = len(nums)
    positions: dict[int, list[int]] = defaultdict(list)
    for index, value in enumerate(nums):
        positions[value].append(index)

    answer: list[int] = []
    for query in queries:
        same = positions[nums[query]]
        if len(same) == 1:
            answer.append(-1)
            continue
        pos = bisect_left(same, query)
        previous_index = same[pos - 1]
        next_index = same[(pos + 1) % len(same)]
        previous_distance = abs(query - previous_index)
        next_distance = abs(next_index - query)
        answer.append(
            min(
                previous_distance,
                n - previous_distance,
                next_distance,
                n - next_distance,
            )
        )
    return answer
