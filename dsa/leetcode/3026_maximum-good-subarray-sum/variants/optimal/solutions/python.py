def solve(nums: list[int], k: int) -> int:
    # min_prefix_sums stores the minimum prefix sum encountered for each value
    # prefix_sum[i] is the sum of nums[0...i-1]
    # The sum of subarray nums[i...j] is prefix_sum[j+1] - prefix_sum[i]
    
    min_prefix_sums = {}
    current_prefix_sum = 0
    max_sum = float('-inf')
    found = False
    
    for x in nums:
        # Check for x - k
        target1 = x - k
        if target1 in min_prefix_sums:
            found = True
            max_sum = max(max_sum, current_prefix_sum + x - min_prefix_sums[target1])
            
        # Check for x + k
        target2 = x + k
        if target2 in min_prefix_sums:
            found = True
            max_sum = max(max_sum, current_prefix_sum + x - min_prefix_sums[target2])
            
        # Update the min prefix sum for the current value x
        # We store the prefix sum *before* adding x
        if x not in min_prefix_sums or current_prefix_sum < min_prefix_sums[x]:
            min_prefix_sums[x] = current_prefix_sum
            
        current_prefix_sum += x
        
    return int(max_sum) if found else 0
