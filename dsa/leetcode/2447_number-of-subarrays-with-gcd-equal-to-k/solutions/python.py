import math

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays with GCD equal to k.
    Uses the property that GCD is non-increasing as we extend the subarray.
    """
    n = len(nums)
    count = 0
    
    for i in range(n):
        current_gcd = nums[i]
        for j in range(i, n):
            current_gcd = math.gcd(current_gcd, nums[j])
            
            if current_gcd == k:
                count += 1
            elif current_gcd < k:
                # Since the GCD can only decrease or stay the same,
                # if it drops below k, it will never return to k.
                break
                
    return count
