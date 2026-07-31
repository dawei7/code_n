class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        if m == 1:
            return max(value * value for value in nums)

        prefix_min = nums[0]
        prefix_max = nums[0]
        answer = -(10**20)

        for last in range(m - 1, len(nums)):
            first_candidate = nums[last - m + 1]
            prefix_min = min(prefix_min, first_candidate)
            prefix_max = max(prefix_max, first_candidate)
            value = nums[last]
            answer = max(answer, value * prefix_min, value * prefix_max)

        return answer
