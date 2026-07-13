import math

def solve(nums: list[int], target: list[int]) -> int:
    m = len(target)
    num_masks = 1 << m

    def get_lcm(a, b):
        if a == 0 or b == 0: return 0
        return abs(a * b) // math.gcd(a, b)

    lcms = [1] * num_masks
    for mask in range(1, num_masks):
        bit = mask & -mask
        index = bit.bit_length() - 1
        lcms[mask] = get_lcm(lcms[mask ^ bit], target[index])

    # dp[mask] is the min cost to satisfy the subset of targets represented by mask
    dp = [float('inf')] * num_masks
    dp[0] = 0

    for num in nums:
        new_dp = dp[:]
        costs = [0] * num_masks
        for submask in range(1, num_masks):
            costs[submask] = (-num) % lcms[submask]

        for mask, current in enumerate(dp):
            if current == float('inf'):
                continue
            for submask in range(num_masks):
                new_mask = mask | submask
                new_dp[new_mask] = min(new_dp[new_mask], current + costs[submask])
        dp = new_dp

    return int(dp[num_masks - 1])
