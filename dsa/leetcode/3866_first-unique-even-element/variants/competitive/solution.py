class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counts = [0] * 101
        for value in nums:
            counts[value] += 1

        for value in nums:
            if value % 2 == 0 and counts[value] == 1:
                return value

        return -1
