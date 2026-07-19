from typing import List

def solve(nums: List[int], k: int) -> List[List[int]]:
    """
    Partitions the array into triplets such that the difference between 
    the max and min in each triplet is <= k.
    """
    nums.sort()
    result = []
    
    # Iterate through the sorted array in steps of 3
    for i in range(0, len(nums), 3):
        # Check if the triplet satisfies the condition: max - min <= k
        # Since the array is sorted, nums[i+2] is max and nums[i] is min
        if nums[i + 2] - nums[i] > k:
            return []
        
        result.append([nums[i], nums[i + 1], nums[i + 2]])
        
    return result
