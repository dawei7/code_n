class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suffix = [0] * (n + 1)
        for index in range(n - 1, -1, -1):
            suffix[index] = suffix[index + 1] | nums[index]

        answer = 0
        prefix = 0
        for index, value in enumerate(nums):
            answer = max(answer, prefix | (value << k) | suffix[index + 1])
            prefix |= value
        return answer
