class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        right = [0] * n
        left = [0] * n

        for i in range(n - 1):
            gap = nums[i + 1] - nums[i]

            right_cost = gap
            if i == 0 or gap < nums[i] - nums[i - 1]:
                right_cost = 1
            right[i + 1] = right[i] + right_cost

            left_cost = gap
            if i + 1 == n - 1 or gap <= nums[i + 2] - nums[i + 1]:
                left_cost = 1
            left[i + 1] = left[i] + left_cost

        answer = []
        for start, target in queries:
            if start < target:
                answer.append(right[target] - right[start])
            else:
                answer.append(left[start] - left[target])
        return answer
