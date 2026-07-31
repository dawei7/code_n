from collections import defaultdict


def solve(nums: list[int], k: int) -> int:
    frequencies = defaultdict(int)
    distinct_sum = 0
    left = 0
    best = len(nums) + 1

    for right, value in enumerate(nums):
        if frequencies[value] == 0:
            distinct_sum += value
        frequencies[value] += 1

        while distinct_sum >= k:
            best = min(best, right - left + 1)
            outgoing = nums[left]
            frequencies[outgoing] -= 1
            if frequencies[outgoing] == 0:
                distinct_sum -= outgoing
                del frequencies[outgoing]
            left += 1

    return best if best <= len(nums) else -1
