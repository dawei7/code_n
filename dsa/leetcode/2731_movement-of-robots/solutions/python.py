from typing import List

def solve(nums: List[int], s: str, d: int) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    
    # Calculate final positions as if robots pass through each other
    final_positions = []
    for i in range(n):
        if s[i] == 'R':
            final_positions.append(nums[i] + d)
        else:
            final_positions.append(nums[i] - d)
            
    # Sort the positions to compute pairwise absolute differences efficiently
    final_positions.sort()
    
    # Compute the sum of pairwise absolute differences
    total_sum = 0
    for i in range(n):
        total_sum += final_positions[i] * (2 * i - n + 1)
        
    return total_sum % MOD
