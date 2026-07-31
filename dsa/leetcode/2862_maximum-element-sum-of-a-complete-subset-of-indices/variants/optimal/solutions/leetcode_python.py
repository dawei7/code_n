class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        for base in range(1, n + 1):
            total = 0
            square = 1

            while base * square * square <= n:
                total += nums[base * square * square - 1]
                square += 1

            answer = max(answer, total)

        return answer
