from heapq import nlargest


class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        selected = nlargest(k, nums)
        multiplied = min(k, mul - 1)

        total = 0
        for index in range(multiplied):
            total += selected[index] * (mul - index)
        return total + sum(selected[multiplied:])
