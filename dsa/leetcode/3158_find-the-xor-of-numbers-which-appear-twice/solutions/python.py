from typing import List

def solve(nums: List[int]) -> int:
    seen = set()
    xor_sum = 0
    
    for num in nums:
        if num in seen:
            xor_sum ^= num
        else:
            seen.add(num)
            
    return xor_sum
