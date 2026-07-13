def solve(nums: list[int], cost1: int, cost2: int) -> int:
    n = len(nums)
    if n <= 1:
        return 0
    
    min_val = min(nums)
    max_val = max(nums)
    total_sum = sum(nums)
    MOD = 10**9 + 7
    
    def get_cost(target):
        s = n * target - total_sum
        m = target - min_val
        
        # If we can pair up almost all increments
        if 2 * m <= s:
            # Use cost2 for s // 2 pairs, cost1 for s % 2
            return (s // 2) * min(2 * cost1, cost2) + (s % 2) * cost1
        else:
            # We are forced to use cost1 for the excess of the max element
            # The number of pairs we can form is (s - m)
            # The remaining (m - (s - m)) = 2m - s elements must be filled with cost1
            pairs = s - m
            remainder = m - pairs
            return pairs * min(2 * cost1, cost2) + remainder * cost1

    ans = float('inf')
    # The target can range from max_val to 2 * max_val
    # We check target = max_val and target = max_val + 1 separately
    # because the logic for the "bottleneck" element changes.
    for target in range(max_val, 2 * max_val + 1):
        ans = min(ans, get_cost(target))
        
    return ans % MOD
