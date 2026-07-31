from bisect import bisect_right
from itertools import accumulate


def solve(nums: list[int], queries: list[int]) -> list[int]:
    nums.sort()
    prefix_sums = list(accumulate(nums))
    return [bisect_right(prefix_sums, query) for query in queries]
