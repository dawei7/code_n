class Solution:
    def minIncrease(self, nums: list[int]) -> int:
        def cost(index: int) -> int:
            required = max(nums[index - 1], nums[index + 1]) + 1
            return max(0, required - nums[index])

        n = len(nums)
        if n % 2 == 1:
            return sum(cost(index) for index in range(1, n - 1, 2))

        current = sum(cost(index) for index in range(2, n - 1, 2))
        answer = current

        for even_index in range(2, n - 1, 2):
            current += cost(even_index - 1) - cost(even_index)
            answer = min(answer, current)

        return answer
