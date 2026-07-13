"""Patience-sorting tails solution for LeetCode 300."""

def solve(nums: list[int]) -> int:
    tails: list[int] = []
    for value in nums:
        left = 0
        right = len(tails)
        while left < right:
            middle = (left + right) // 2
            if tails[middle] < value:
                left = middle + 1
            else:
                right = middle
        if left == len(tails):
            tails.append(value)
        else:
            tails[left] = value
    return len(tails)
