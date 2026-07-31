class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        right_sum = nums[-1]
        right_count = 1
        answer = 0

        for index in range(len(nums) - 2, -1, -1):
            if nums[index] * right_count > right_sum:
                answer += 1
            right_sum += nums[index]
            right_count += 1

        return answer
