import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(nums: list[int]) -> int:
    first_prime_idx = -1
    last_prime_idx = -1
    
    for i, num in enumerate(nums):
        if is_prime(num):
            if first_prime_idx == -1:
                first_prime_idx = i
            last_prime_idx = i
            
    if first_prime_idx == -1:
        return 0
        
    return last_prime_idx - first_prime_idx
