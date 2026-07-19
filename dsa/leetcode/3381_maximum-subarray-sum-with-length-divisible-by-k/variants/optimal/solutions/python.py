from typing import List

def solve(nums: List[int], k: int) -> int:
    n = len(nums)
    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
    
    # min_prefix_at_rem[r] stores the minimum prefix_sums[i] 
    # encountered so far where i % k == r
    min_prefix_at_rem = [float('inf')] * k
    min_prefix_at_rem[0] = 0
    
    max_sum = float('-inf')
    
    for i in range(1, n + 1):
        rem = i % k
        # If we have seen a prefix sum with the same remainder,
        # the subarray between that index and i has length divisible by k.
        if min_prefix_at_rem[rem] != float('inf'):
            current_subarray_sum = prefix_sums[i] - min_prefix_at_rem[rem]
            if current_subarray_sum > max_sum:
                max_sum = current_subarray_sum
        
        # Update the minimum prefix sum for this remainder
        if prefix_sums[i] < min_prefix_at_rem[rem]:
            min_prefix_at_rem[rem] = prefix_sums[i]
            
    return int(max_sum)
