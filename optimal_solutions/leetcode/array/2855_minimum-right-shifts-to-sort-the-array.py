from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    pivot_count = 0
    pivot_index = -1
    
    # Find the number of points where the order breaks
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            pivot_count += 1
            pivot_index = i
            
    # If more than one break, it's impossible to sort via cyclic shifts
    if pivot_count > 1:
        return -1
    
    # If no breaks, the array is already sorted
    if pivot_count == 0:
        return 0
    
    # If one break, check if the last element is <= first element
    # to ensure the cyclic shift is valid
    if nums[-1] > nums[0]:
        return -1
    
    # The number of right shifts is the number of elements after the pivot
    return n - 1 - pivot_index
