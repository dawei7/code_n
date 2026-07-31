class Solution:
    def minCost(self, nums: List[int]) -> int:
        size = len(nums)
        costs = {0: 0}
        next_index = 1

        while next_index + 1 < size:
            second = nums[next_index]
            third = nums[next_index + 1]
            updated = {
                next_index: min(
                    cost + max(nums[carried], third)
                    for carried, cost in costs.items()
                ),
                next_index + 1: min(
                    cost + max(nums[carried], second)
                    for carried, cost in costs.items()
                ),
            }
            pair_cost = max(second, third)
            for carried, cost in costs.items():
                updated[carried] = cost + pair_cost
            costs = updated
            next_index += 2

        if next_index == size:
            return min(cost + nums[carried] for carried, cost in costs.items())
        return min(
            cost + max(nums[carried], nums[next_index])
            for carried, cost in costs.items()
        )
