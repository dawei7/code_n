from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        answer = 10**9

        for number in nums:
            digit_sum = 0
            while number > 0:
                digit_sum += number % 10
                number //= 10
            answer = min(answer, digit_sum)

        return answer
