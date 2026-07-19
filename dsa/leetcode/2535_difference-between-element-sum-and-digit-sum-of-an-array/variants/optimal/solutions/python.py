from typing import List

def solve(nums: List[int]) -> int:
    element_sum = 0
    digit_sum = 0
    
    for num in nums:
        element_sum += num
        
        # Extract digits of the current number
        temp = num
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
            
    return abs(element_sum - digit_sum)
