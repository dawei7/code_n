from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def build(index: int) -> None:
            if index == len(nums):
                result.append(path[:])
                return
            build(index + 1)
            path.append(nums[index])
            build(index + 1)
            path.pop()

        build(0)
        return result
