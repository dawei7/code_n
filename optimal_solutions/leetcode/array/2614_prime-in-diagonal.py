import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(nums: list[list[int]]) -> int:
    n = len(nums)
    max_prime = 0
    
    for i in range(n):
        # Primary diagonal: nums[i][i]
        # Secondary diagonal: nums[i][n - 1 - i]
        val1 = nums[i][i]
        val2 = nums[i][n - 1 - i]
        
        if is_prime(val1):
            if val1 > max_prime:
                max_prime = val1
        
        if is_prime(val2):
            if val2 > max_prime:
                max_prime = val2
                
    return max_prime
