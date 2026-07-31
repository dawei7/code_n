from typing import List


class Solution:
    def arrayChange(
        self, nums: List[int], operations: List[List[int]]
    ) -> List[int]:
        position = {value: index for index, value in enumerate(nums)}

        for old_value, new_value in operations:
            index = position.pop(old_value)
            nums[index] = new_value
            position[new_value] = index

        return nums
