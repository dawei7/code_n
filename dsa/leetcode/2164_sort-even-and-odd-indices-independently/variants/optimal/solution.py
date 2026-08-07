from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_values = sorted(nums[::2])
        odd_values = sorted(nums[1::2], reverse=True)
        answer = nums[:]
        answer[::2] = even_values
        answer[1::2] = odd_values
        return answer
