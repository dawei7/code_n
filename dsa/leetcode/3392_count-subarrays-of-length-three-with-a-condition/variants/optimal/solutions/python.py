from typing import List

def solve(nums: List[int]) -> int:
    """
    Counts subarrays of length 3 where (nums[i] + nums[i+2]) * 2 == nums[i+1].
    Note: The problem condition is defined as the sum of the first and third 
    elements being equal to half of the middle element, which is equivalent 
    to (nums[i] + nums[i+2]) * 2 == nums[i+1].
    """
    count = 0
    # We iterate up to len(nums) - 3 to check every triplet
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
            count += 1
    return count
