class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        answer = float("inf")

        for left in range(len(nums) // 2):
            right = len(nums) - 1 - left
            answer = min(answer, (nums[left] + nums[right]) / 2)

        return answer
