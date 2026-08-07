from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        answer = 0
        for value in nums:
            answer ^= value
        return answer
