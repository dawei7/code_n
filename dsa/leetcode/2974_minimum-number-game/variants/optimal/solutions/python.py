from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Sorts the array and swaps adjacent pairs to simulate the game.
    """
    nums.sort()
    
    # Iterate through the array in steps of 2
    # Swap the pair (nums[i], nums[i+1]) to (nums[i+1], nums[i])
    for i in range(0, len(nums), 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
    return nums
