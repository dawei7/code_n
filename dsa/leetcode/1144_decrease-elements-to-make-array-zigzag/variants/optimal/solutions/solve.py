"""Optimal app-local solution for LeetCode 1144."""


def solve(nums: list[int]) -> int:
    def valley_cost(parity: int) -> int:
        cost = 0
        for index in range(parity, len(nums), 2):
            left = nums[index - 1] if index > 0 else float("inf")
            right = nums[index + 1] if index + 1 < len(nums) else float("inf")
            smaller_neighbor = min(left, right)
            cost += max(0, nums[index] - smaller_neighbor + 1)
        return cost

    return min(valley_cost(0), valley_cost(1))
