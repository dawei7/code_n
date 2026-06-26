from typing import List

def solve(nums: List[int]) -> int:
    total_sum = 0
    count = 0
    
    for num in nums:
        if num % 6 == 0:
            total_sum += num
            count += 1
            
    return total_sum // count if count > 0 else 0
