import math

def solve(nums: list[int]) -> int:
    n = len(nums)
    ones_count = nums.count(1)
    
    if ones_count > 0:
        return n - ones_count
    
    # Find the shortest subarray with GCD == 1
    min_len = float('inf')
    
    for i in range(n):
        current_gcd = nums[i]
        for j in range(i + 1, n):
            current_gcd = math.gcd(current_gcd, nums[j])
            if current_gcd == 1:
                min_len = min(min_len, j - i + 1)
                break
                
    if min_len == float('inf'):
        return -1
    
    # Operations = (min_len - 1) to create one '1' 
    # + (n - 1) to propagate that '1' to the rest of the array
    return min_len - 1 + n - 1
