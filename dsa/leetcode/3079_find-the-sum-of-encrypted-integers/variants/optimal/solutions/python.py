from typing import List

def solve(nums: List[int]) -> int:
    def encrypt(n: int) -> int:
        s = str(n)
        max_digit = max(s)
        return int(max_digit * len(s))
    
    total_sum = 0
    for num in nums:
        total_sum += encrypt(num)
    return total_sum
