from typing import List

def solve(nums: List[int]) -> List[int]:
    total_sum = sum(nums)
    left_sum = 0
    result = []
    
    for x in nums:
        # right_sum is total_sum minus the current element and the left_sum
        right_sum = total_sum - left_sum - x
        result.append(abs(left_sum - right_sum))
        # Update left_sum for the next iteration
        left_sum += x
        
    return result
