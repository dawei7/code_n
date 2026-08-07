class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        costs = [[0] * k for _ in range(2)]

        for index, value in enumerate(nums):
            remainder = value % k
            for target in range(k):
                difference = abs(remainder - target)
                costs[index % 2][target] += min(difference, k - difference)

        best_cost = float("inf")
        best_remainder = -1
        second_cost = float("inf")
        for remainder, cost in enumerate(costs[1]):
            if cost < best_cost:
                second_cost = best_cost
                best_cost = cost
                best_remainder = remainder
            elif cost < second_cost:
                second_cost = cost

        answer = float("inf")
        for remainder, cost in enumerate(costs[0]):
            odd_cost = second_cost if remainder == best_remainder else best_cost
            answer = min(answer, cost + odd_cost)

        return int(answer)
