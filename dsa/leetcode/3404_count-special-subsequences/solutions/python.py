from collections import defaultdict
from math import gcd


def solve(nums):
    n = len(nums)
    pair_ratios = defaultdict(int)
    answer = 0

    for r in range(4, n - 2):
        q = r - 2
        for p in range(q - 1):
            divisor = gcd(nums[p], nums[q])
            pair_ratios[(nums[p] // divisor, nums[q] // divisor)] += 1

        for s in range(r + 2, n):
            divisor = gcd(nums[s], nums[r])
            answer += pair_ratios[(nums[s] // divisor, nums[r] // divisor)]

    return answer
