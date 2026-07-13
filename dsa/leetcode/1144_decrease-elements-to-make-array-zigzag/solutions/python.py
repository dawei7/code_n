def solve(nums):
    n = len(nums)

    def cost_for_valleys(parity):
        total = 0
        for i, value in enumerate(nums):
            if i % 2 != parity:
                continue
            limit = float("inf")
            if i > 0:
                limit = min(limit, nums[i - 1])
            if i + 1 < n:
                limit = min(limit, nums[i + 1])
            if value >= limit:
                total += value - limit + 1
        return total

    return min(cost_for_valleys(0), cost_for_valleys(1))
