from typing import List


def solve(nums: List[int], k: int) -> List[List[int]]:
    ordered = sorted(nums)
    answer = []

    for start in range(0, len(ordered), 3):
        if ordered[start + 2] - ordered[start] > k:
            return []
        answer.append(ordered[start : start + 3])

    return answer
