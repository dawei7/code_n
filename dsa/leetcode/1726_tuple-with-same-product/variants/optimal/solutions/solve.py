from collections import defaultdict


def solve(nums: list[int]) -> int:
    pair_count: dict[int, int] = defaultdict(int)
    answer = 0

    for right in range(len(nums)):
        for left in range(right):
            product = nums[left] * nums[right]
            answer += 8 * pair_count[product]
            pair_count[product] += 1

    return answer
