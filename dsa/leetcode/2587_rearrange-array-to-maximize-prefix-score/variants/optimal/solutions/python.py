from typing import List

def solve(nums: List[int]) -> int:
    """
    Maximizes the number of positive prefix sums by sorting the array
    in descending order and calculating the prefix sums.
    """
    # Sort in descending order to maximize the prefix sum growth
    nums.sort(reverse=True)
    
    count = 0
    current_prefix_sum = 0
    
    for num in nums:
        current_prefix_sum += num
        if current_prefix_sum > 0:
            count += 1
        else:
            # Since the array is sorted descending, if the current sum 
            # is <= 0, all subsequent sums will also be <= 0.
            break
            
    return count
