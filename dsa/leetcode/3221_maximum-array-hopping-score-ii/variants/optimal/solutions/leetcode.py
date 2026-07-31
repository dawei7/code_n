class Solution:
    def maxScore(self, nums: List[int]) -> int:
        best_destination = nums[-1]
        score = best_destination

        for index in range(len(nums) - 2, 0, -1):
            best_destination = max(best_destination, nums[index])
            score += best_destination

        return score
