from collections import defaultdict


def solve(nums: list[int], target: int) -> int:
    ways = {0: 1}
    for value in nums:
        next_ways = defaultdict(int)
        for current_sum, count in ways.items():
            next_ways[current_sum + value] += count
            next_ways[current_sum - value] += count
        ways = next_ways
    return ways.get(target, 0)
