"""Optimal app-local solution for LeetCode 992."""


def solve(nums, k):
    def at_most(limit):
        frequencies = [0] * (len(nums) + 1)
        left = 0
        distinct = 0
        total = 0

        for right, value in enumerate(nums):
            if frequencies[value] == 0:
                distinct += 1
            frequencies[value] += 1

            while distinct > limit:
                outgoing = nums[left]
                frequencies[outgoing] -= 1
                if frequencies[outgoing] == 0:
                    distinct -= 1
                left += 1

            total += right - left + 1

        return total

    return at_most(k) - at_most(k - 1)
