import math

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    count = 0
    
    for i in range(n):
        current_lcm = nums[i]
        for j in range(i, n):
            current_lcm = lcm(current_lcm, nums[j])
            
            # If current_lcm exceeds k or is not a divisor of k,
            # any further extension will not result in an LCM of k.
            if current_lcm > k or k % current_lcm != 0:
                break
            
            if current_lcm == k:
                count += 1
                
    return count
