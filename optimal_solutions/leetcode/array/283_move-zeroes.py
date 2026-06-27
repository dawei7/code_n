from typing import List

def solve(nums: List[int]) -> None:
    """
    Moves all zeros in the list to the end while maintaining the relative 
    order of non-zero elements in-place.
    """
    last_non_zero_index = 0
    
    # Iterate through the array
    for current in range(len(nums)):
        # If the current element is non-zero, swap it with the element 
        # at the last_non_zero_index
        if nums[current] != 0:
            nums[last_non_zero_index], nums[current] = nums[current], nums[last_non_zero_index]
            last_non_zero_index += 1
