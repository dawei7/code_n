import math

def solve(nums: list[int], targets: list[int]) -> int:
    m = len(targets)
    n = len(nums)
    
    def get_lcm(a, b):
        if a == 0 or b == 0: return 0
        return abs(a * b) // math.gcd(a, b)

    # Precompute cost to make nums[i] divisible by a subset of targets
    # cost[i][mask] = min increment to make nums[i] divisible by all targets in mask
    # Since m is small (up to 4), we can iterate through all masks
    num_masks = 1 << m
    costs = [[float('inf')] * num_masks for _ in range(n)]
    
    for i in range(n):
        for mask in range(num_masks):
            lcm_val = 1
            for j in range(m):
                if (mask >> j) & 1:
                    lcm_val = get_lcm(lcm_val, targets[j])
            
            remainder = nums[i] % lcm_val
            if remainder == 0:
                costs[i][mask] = 0
            else:
                costs[i][mask] = lcm_val - remainder
                
    # dp[mask] is the min cost to satisfy the subset of targets represented by mask
    dp = [float('inf')] * num_masks
    dp[0] = 0
    
    for i in range(n):
        new_dp = dp[:]
        for mask in range(num_masks):
            if dp[mask] == float('inf'):
                continue
            for submask in range(num_masks):
                new_mask = mask | submask
                new_dp[new_mask] = min(new_dp[new_mask], dp[mask] + costs[i][submask])
        dp = new_dp
        
    return int(dp[num_masks - 1])
