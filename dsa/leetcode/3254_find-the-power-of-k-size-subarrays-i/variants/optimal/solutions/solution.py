from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        consecutive_length = 0

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1] + 1:
                consecutive_length += 1
            else:
                consecutive_length = 1

            if index >= k - 1:
                result.append(value if consecutive_length >= k else -1)

        return result
