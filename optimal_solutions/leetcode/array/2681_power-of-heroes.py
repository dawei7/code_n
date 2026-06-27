def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    
    # Step 1: Sort the array
    nums.sort()
    
    total_power = 0
    
    # current_sum_of_min_terms will store sum_{j=0}^{i-1} (nums[j] * 2^(i-1-j))
    # This represents the weighted sum of previous elements that can act as minimums
    # when nums[i] is the maximum.
    current_sum_of_min_terms = 0 
    
    for num in nums:
        # Calculate the power contribution for the current 'num' as the maximum element.
        # This includes two parts:
        # 1. When 'num' is the only element in the subsequence: num^3
        # 2. When 'num' is the maximum and some nums[j] (j < current index) is the minimum:
        #    sum_{j=0}^{i-1} (num^2 * nums[j] * 2^(i-1-j))
        #    This sum can be factored as num^2 * (sum_{j=0}^{i-1} nums[j] * 2^(i-1-j))
        #    The term in parentheses is exactly current_sum_of_min_terms.
        
        # Calculate num^3 % MOD
        num_cubed = pow(num, 3, MOD)
        
        # Calculate (num^2 * current_sum_of_min_terms) % MOD
        num_squared_times_min_terms = (pow(num, 2, MOD) * current_sum_of_min_terms) % MOD
        
        # Add these two parts to get the total contribution for the current 'num' as max
        current_num_contribution = (num_cubed + num_squared_times_min_terms) % MOD
        
        # Add to the overall total power
        total_power = (total_power + current_num_contribution) % MOD
        
        # Update current_sum_of_min_terms for the next iteration (i+1).
        # The new sum will be:
        # (nums[i] * 2^0) + (nums[i-1] * 2^1) + ... + (nums[0] * 2^i)
        # This is equivalent to (current_sum_of_min_terms * 2 + nums[i])
        current_sum_of_min_terms = (current_sum_of_min_terms * 2 + num) % MOD
        
    return total_power
