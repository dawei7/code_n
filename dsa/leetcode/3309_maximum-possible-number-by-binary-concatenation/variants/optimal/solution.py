from itertools import permutations


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        answer = 0

        for ordering in permutations(nums):
            value = 0
            for number in ordering:
                value = (value << number.bit_length()) | number
            answer = max(answer, value)

        return answer
