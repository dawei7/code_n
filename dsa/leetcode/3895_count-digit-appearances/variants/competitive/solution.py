class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        occurrences = 0
        for value in nums:
            while value:
                if value % 10 == digit:
                    occurrences += 1
                value //= 10
        return occurrences
