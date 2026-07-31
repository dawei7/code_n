class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        best = -1
        length = 1
        expected = 1

        for index in range(1, len(nums)):
            difference = nums[index] - nums[index - 1]

            if difference == expected:
                length += 1
                expected = -expected
            elif difference == 1:
                length = 2
                expected = -1
            else:
                length = 1
                expected = 1

            if length >= 2:
                best = max(best, length)

        return best
