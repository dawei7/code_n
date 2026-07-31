class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        cheapest = nums.copy()
        answer = sum(cheapest)

        for operations in range(1, n):
            for chocolate_type in range(n):
                source = (chocolate_type - operations) % n
                cheapest[chocolate_type] = min(
                    cheapest[chocolate_type], nums[source]
                )
            answer = min(answer, operations * x + sum(cheapest))

        return answer
