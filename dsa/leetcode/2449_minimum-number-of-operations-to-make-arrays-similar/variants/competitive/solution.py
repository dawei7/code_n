from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_even = sorted(value for value in nums if value % 2 == 0)
        nums_odd = sorted(value for value in nums if value % 2 == 1)
        target_even = sorted(value for value in target if value % 2 == 0)
        target_odd = sorted(value for value in target if value % 2 == 1)

        operations = 0
        for source, destination in zip(nums_even, target_even):
            if source > destination:
                operations += (source - destination) // 2
        for source, destination in zip(nums_odd, target_odd):
            if source > destination:
                operations += (source - destination) // 2

        return operations
