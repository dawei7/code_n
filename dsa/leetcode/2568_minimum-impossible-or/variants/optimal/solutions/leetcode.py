class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        present_powers = 0

        for value in nums:
            if value & (value - 1) == 0:
                present_powers |= value

        answer = 1
        while present_powers & answer:
            answer <<= 1

        return answer
