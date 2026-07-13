from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        path = []
        result = []

        def arrange() -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return
            for index, value in enumerate(nums):
                if used[index]:
                    continue
                if index > 0 and value == nums[index - 1] and not used[index - 1]:
                    continue
                used[index] = True
                path.append(value)
                arrange()
                path.pop()
                used[index] = False

        arrange()
        return result
