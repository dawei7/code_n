from collections import defaultdict


def solve(nums: list[int]) -> int:
    positions: dict[int, list[int]] = defaultdict(list)
    for index, value in enumerate(nums):
        positions[value].append(index)

    n = len(nums)
    answer = n
    for indices in positions.values():
        largest_gap = n + indices[0] - indices[-1]
        for left, right in zip(indices, indices[1:]):
            largest_gap = max(largest_gap, right - left)
        answer = min(answer, largest_gap // 2)

    return answer
