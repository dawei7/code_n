from collections import defaultdict
from math import gcd


def solve(nums: list[int]) -> int:
    length = len(nums)
    left_ratios = defaultdict(int)
    answer = 0

    for r in range(4, length - 2):
        q = r - 2
        for p in range(q - 1):
            divisor = gcd(nums[p], nums[q])
            ratio = (nums[p] // divisor, nums[q] // divisor)
            left_ratios[ratio] += 1

        for s in range(r + 2, length):
            divisor = gcd(nums[s], nums[r])
            ratio = (nums[s] // divisor, nums[r] // divisor)
            answer += left_ratios[ratio]

    return answer
