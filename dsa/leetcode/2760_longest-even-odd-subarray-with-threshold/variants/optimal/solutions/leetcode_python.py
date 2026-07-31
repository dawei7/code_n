class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        best = 0
        length = 0

        for index, value in enumerate(nums):
            if value > threshold:
                length = 0
            elif length == 0:
                length = 1 if value % 2 == 0 else 0
            elif nums[index - 1] % 2 != value % 2:
                length += 1
            else:
                length = 1 if value % 2 == 0 else 0

            best = max(best, length)

        return best

