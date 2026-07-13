from collections import defaultdict

def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n
    
    # Group indices by their values
    val_to_indices = defaultdict(list)
    for i, val in enumerate(nums):
        val_to_indices[val].append(i)
        
    # For each group, calculate the sum of distances using prefix sums
    for val in val_to_indices:
        indices = val_to_indices[val]
        m = len(indices)
        if m == 1:
            continue
            
        # Calculate prefix sums of the indices
        prefix_sums = [0] * (m + 1)
        for i in range(m):
            prefix_sums[i + 1] = prefix_sums[i] + indices[i]
            
        total_sum = prefix_sums[m]
        
        # For each index in the group, calculate the sum of distances
        # Sum = (i * current_idx - prefix_sum_before) + 
        #       ((total_sum - prefix_sum_after) - (m - 1 - i) * current_idx)
        for i in range(m):
            current_idx = indices[i]
            
            left_sum = prefix_sums[i]
            right_sum = total_sum - prefix_sums[i + 1]
            
            left_count = i
            right_count = m - 1 - i
            
            dist_left = (left_count * current_idx) - left_sum
            dist_right = right_sum - (right_count * current_idx)
            
            ans[current_idx] = dist_left + dist_right
            
    return ans
