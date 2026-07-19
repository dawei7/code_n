from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        first_index = {0: -1}
        remainder = 0
        for index, value in enumerate(nums):
            remainder = (remainder + value) % k
            if remainder in first_index:
                if index - first_index[remainder] >= 2:
                    return True
            else:
                first_index[remainder] = index
        return False
