import math

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subarray where product == gcd * lcm.
    """
    n = len(nums)
    max_len = 1
    
    # We iterate through all possible starting points of subarrays
    for i in range(n):
        current_prod = 1
        current_gcd = nums[i]
        current_lcm = nums[i]
        
        for j in range(i, n):
            # Update metrics for the subarray nums[i...j]
            val = nums[j]
            current_prod *= val
            
            # Update GCD and LCM
            if j == i:
                current_gcd = val
                current_lcm = val
            else:
                current_gcd = math.gcd(current_gcd, val)
                current_lcm = (current_lcm * val) // math.gcd(current_lcm, val)
            
            # Check the condition
            if current_prod == current_gcd * current_lcm:
                max_len = max(max_len, j - i + 1)
            
            # Optimization: If product exceeds a reasonable bound or 
            # becomes significantly larger than the potential LCM, 
            # we could break, but given constraints, simple check is fine.
            # Python handles large integers automatically.
            
    return max_len
