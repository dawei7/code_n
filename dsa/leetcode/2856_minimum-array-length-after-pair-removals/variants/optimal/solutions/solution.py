class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        max_frequency = 1
        run_length = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                run_length += 1
            else:
                run_length = 1
            max_frequency = max(max_frequency, run_length)

        return max(n % 2, 2 * max_frequency - n)
