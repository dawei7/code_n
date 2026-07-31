from bisect import bisect_right
from itertools import accumulate


def solve(nums: list[int], queries: list[int]) -> list[int]:
    sorted_nums = sorted(nums)
    prefix_sums = list(accumulate(sorted_nums))
    return [
        bisect_right(prefix_sums, query)
        for query in queries
    ]
