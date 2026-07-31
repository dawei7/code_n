from collections import defaultdict


def solve(nums: list[int], k: int) -> int:
    frequencies: dict[int, int] = defaultdict(int)
    pairs = 0
    left = 0
    answer = 0

    for right, value in enumerate(nums):
        pairs += frequencies[value]
        frequencies[value] += 1

        while pairs >= k:
            answer += len(nums) - right
            outgoing = nums[left]
            frequencies[outgoing] -= 1
            pairs -= frequencies[outgoing]
            left += 1

    return answer
