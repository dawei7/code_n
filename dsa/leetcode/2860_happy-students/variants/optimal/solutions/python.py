from typing import List


def solve(nums: List[int]) -> int:
    ordered = sorted(nums)
    n = len(ordered)
    answer = int(ordered[0] > 0)

    for selected in range(1, n):
        if ordered[selected - 1] < selected < ordered[selected]:
            answer += 1

    if ordered[-1] < n:
        answer += 1

    return answer
