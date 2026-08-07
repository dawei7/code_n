class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for number in nums for digit in str(number)]
