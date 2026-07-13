from math import comb


def solve(nums):
    mod = 10**9 + 7

    def count_orders(values):
        if len(values) <= 2:
            return 1
        root = values[0]
        left = [value for value in values[1:] if value < root]
        right = [value for value in values[1:] if value >= root]
        ways = comb(len(left) + len(right), len(left))
        return ways * count_orders(left) * count_orders(right) % mod

    if not nums:
        return 0
    return (count_orders(nums) - 1) % mod
